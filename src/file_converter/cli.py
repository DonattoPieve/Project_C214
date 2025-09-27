import pytest
from file_converter import cli

def test_cli_parse_args_docx():
    args = cli.parse_args(["input.docx", "--outdir", "saida"])
    assert args.input == "input.docx"
    assert args.outdir == "saida"

def test_cli_parse_args_csv():
    args = cli.parse_args(["input.csv"])
    assert args.input == "input.csv"

def test_cli_rejects_format(capsys):
    rc = cli.main(["input.txt"])
    out = capsys.readouterr()
    assert rc == 1
    assert "Formato não suportado" in out.err

def test_cli_no_args():
    with pytest.raises(SystemExit):
        cli.parse_args([])
