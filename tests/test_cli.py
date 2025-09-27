import pytest
from file_converter import cli


def test_cli_success_docx(monkeypatch, tmp_path, capsys):
    fake_pdf = tmp_path / "saida.pdf"

    def fake_convert(i, o=None):
        fake_pdf.write_text("ok")
        return fake_pdf

    monkeypatch.setattr("file_converter.cli.convert_docx_to_pdf", fake_convert)

    docx = tmp_path / "arquivo.docx"
    docx.write_text("conteudo")

    rc = cli.main([str(docx), "--outdir", str(tmp_path)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "saida.pdf" in out


def test_cli_success_csv(monkeypatch, tmp_path, capsys):
    fake_pdf = tmp_path / "saida.pdf"

    def fake_convert(i, o=None):
        fake_pdf.write_text("ok")
        return fake_pdf

    monkeypatch.setattr("file_converter.cli.convert_csv_to_pdf", fake_convert)

    csv = tmp_path / "dados.csv"
    csv.write_text("a,b\n1,2")

    rc = cli.main([str(csv), "--outdir", str(tmp_path)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "saida.pdf" in out


def test_cli_success_pptx(monkeypatch, tmp_path, capsys):
    fake_pdf = tmp_path / "saida.pdf"

    def fake_convert(i, o=None):
        fake_pdf.write_text("ok")
        return fake_pdf

    monkeypatch.setattr("file_converter.cli.convert_pptx_to_pdf", fake_convert)

    pptx = tmp_path / "slides.pptx"
    pptx.write_text("fakepptx")

    rc = cli.main([str(pptx), "--outdir", str(tmp_path)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "saida.pdf" in out


def test_cli_rejects_format(capsys, tmp_path):
    txt = tmp_path / "arq.txt"
    txt.write_text("x")

    rc = cli.main([str(txt)])
    out = capsys.readouterr()
    assert rc == 1
    assert "Formato não suportado" in out.err


def test_cli_error_docx(monkeypatch, tmp_path):
    def boom(i, o=None):
        raise RuntimeError("boom")

    monkeypatch.setattr("file_converter.cli.convert_docx_to_pdf", boom)

    docx = tmp_path / "falha.docx"
    docx.write_text("conteudo")

    rc = cli.main([str(docx)])
    assert rc == 1


def test_cli_no_args():
    with pytest.raises(SystemExit):
        cli.parse_args([])
