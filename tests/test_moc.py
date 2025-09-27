import builtins
from pathlib import Path
from file_converter import core

def test_convert_docx_mock(tmp_path):
    """Testa se convert_docx_to_pdf chama internamente docx2pdf.convert."""
    called = {}

    # guarda referência real do import
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
        return real_import(name, *a, **kw)  # chama o import original

    builtins.__import__ = fake_import
    try:
        doc = tmp_path / "a.docx"
        doc.write_text("x")

        outdir = tmp_path / "saida"
        outdir.mkdir()

        core.convert_docx_to_pdf(str(doc), str(outdir))
    finally:
        builtins.__import__ = real_import  # restaura o import original

    # verificações
    assert "src" in called
    assert "dest" in called
    assert Path(called["src"]).name == "a.docx"
    assert Path(called["dest"]).name == "saida"

def test_cli_with_mock(monkeypatch, tmp_path, capsys):
    from file_converter import cli

    def fake_convert(i, o=None):
        return tmp_path / "mocked.pdf"

    # ⚠️ Mock aplicado no namespace certo
    monkeypatch.setattr("file_converter.cli.convert_docx_to_pdf", fake_convert)

    # Criar arquivo de entrada fake
    docx = tmp_path / "input.docx"
    docx.write_text("conteudo")

    cli.main([str(docx), "--outdir", str(tmp_path)])
    captured = capsys.readouterr()
    assert "mocked.pdf" in captured.out
