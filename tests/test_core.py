import builtins
from pathlib import Path
import pytest
from file_converter import core


def _create_file(p: Path, name: str) -> Path:
    f = p / name
    f.write_text("x")
    return f


def test_validate_wrong_ext(tmp_path):
    """Arquivos com extensão inválida devem ser rejeitados."""
    txt = _create_file(tmp_path, "x.txt")
    if hasattr(core, "validate_input"):
        with pytest.raises(ValueError):
            core.validate_input(txt)
    else:
        # Se não houver validate_input, a conversão deve falhar cedo
        with pytest.raises(Exception):
            core.convert_docx_to_pdf(txt)


def test_convert_docx_rejects_wrong_ext(tmp_path):
    """Chamando convert_docx_to_pdf com .txt deve falhar."""
    txt = _create_file(tmp_path, "x.txt")
    with pytest.raises(Exception):
        core.convert_docx_to_pdf(txt)


def test_convert_calls_docx2pdf(monkeypatch, tmp_path):
    """Interceta import de docx2pdf e verifica src/dest normalizados."""
    called = {}

    real_import = builtins.__import__

    def fake_import(name, *a, **kw):
        if name == "docx2pdf":
            class M:
                pass
            m = M()

            def fake_convert(src, dest_dir):
                called["src"] = src
                called["dest"] = dest_dir

            m.convert = fake_convert
            return m
        return real_import(name, *a, **kw)

    builtins.__import__ = fake_import
    try:
        docx = _create_file(tmp_path, "doc.docx")
        outdir = tmp_path / "saida"
        outdir.mkdir(exist_ok=True)
        core.convert_docx_to_pdf(docx, outdir)
    finally:
        builtins.__import__ = real_import

    # Normaliza e compara caminhos de forma robusta (Windows/Unix)
    assert Path(called["src"]).name == "doc.docx"
    assert Path(called["dest"]).resolve() == outdir.resolve()


def test_build_output_custom_dir_if_available(tmp_path):
    """Se a função existir, garante que o diretório de saída é respeitado."""
    if hasattr(core, "build_output_path"):
        f = _create_file(tmp_path, "a.docx")
        outdir = tmp_path / "saida"
        out = core.build_output_path(f, outdir)
        # o caminho deve estar dentro de "saida"
        assert outdir in out.parents
    else:
        pytest.skip("build_output_path não existe no core atual")


def test_build_output_default_dir_if_available(tmp_path):
    """Se existir, verifica que cria (ou usa) diretório padrão (ex.: output/)."""
    if hasattr(core, "build_output_path"):
        f = _create_file(tmp_path, "a.docx")
        out = core.build_output_path(f, None)
        assert out.parent.exists()
    else:
        pytest.skip("build_output_path não existe no core atual")

def test_validate_empty_filename(tmp_path):
    """Arquivo sem nome deve gerar erro."""
    f = tmp_path / ""
    with pytest.raises(Exception):
        # dependendo da sua implementação pode ser FileNotFoundError ou ValueError
        core.validate_input(f)
