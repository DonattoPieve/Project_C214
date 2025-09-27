from file_converter.core import convert_csv_to_pdf
import pandas as pd


def test_csv_to_pdf(tmp_path):
    f = tmp_path / "data.csv"
    f.write_text("a,b\n1,2\n3,4")
    out = convert_csv_to_pdf(f, tmp_path)
    assert out.exists()
