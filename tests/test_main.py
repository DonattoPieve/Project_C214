import pytest
from PySide6.QtWidgets import QApplication
from main import *


# Instância única da aplicação Qt
app = QApplication([])

@pytest.fixture
def janela():
    return ConversorWordPDF()

# --------------------------
# TESTES POSITIVOS (10)
# --------------------------

def test_titulo_janela(janela):
    assert janela.windowTitle() == "Conversor Word → PDF"

def test_label_texto(janela):
    assert "Selecione um arquivo Word" in janela.label.text()

def test_botao_converter_existe(janela):
    assert janela.btn_convert.text() == "Converter para PDF"

def test_botao_selecionar_existe(janela):
    assert janela.btn_select.text() == "Selecionar Arquivo"

def test_input_path_vazio(janela):
    assert janela.input_path.text() == ""

def test_input_path_define_texto(janela):
    janela.input_path.setText("meu_arquivo.docx")
    assert janela.input_path.text() == "meu_arquivo.docx"

def test_input_extensao_correta(janela):
    janela.input_path.setText("arquivo.docx")
    assert janela.input_path.text().endswith(".docx")

def test_input_numero(janela):
    janela.input_path.setText("123")
    assert janela.input_path.text() == "123"

def test_input_caracteres_especiais(janela):
    janela.input_path.setText("@#$%")
    assert janela.input_path.text() == "@#$%"

def test_label_nao_vazio(janela):
    assert janela.label.text() != ""
# ---------------------------
# TESTES NEGATIVOS (10)
# ---------------------------

def test_input_none(janela):
    janela.input_path.setText("")
    assert janela.input_path.text() == ""

def test_input_espacos(janela):
    janela.input_path.setText("   ")
    assert janela.input_path.text().strip() == ""

def test_input_sem_extensao(janela):
    janela.input_path.setText("arquivo")
    assert "." not in janela.input_path.text()

def test_input_extensao_errada(janela):
    janela.input_path.setText("arquivo.txt")
    assert janela.input_path.text().endswith(".txt")

def test_input_caminho_invalido(janela):
    janela.input_path.setText("C:/<>:?*.docx")
    assert any(c in janela.input_path.text() for c in "<>:?*")

def test_input_extensao_maiuscula(janela):
    janela.input_path.setText("arquivo.DOC")
    assert janela.input_path.text().endswith(".DOC")

def test_input_multiplas_extensoes(janela):
    janela.input_path.setText("arquivo.docx.exe")
    assert janela.input_path.text().endswith(".exe")

def test_input_caminho_longo(janela):
    caminho = "a" * 260 + ".docx"
    janela.input_path.setText(caminho)
    assert len(janela.input_path.text()) > 255

def test_input_somente_simbolos(janela):
    janela.input_path.setText("!!!!!!!")
    assert janela.input_path.text() == "!!!!!!!"

def test_input_nome_vazio_com_extensao(janela):
    janela.input_path.setText(".docx")
    assert janela.input_path.text().startswith(".")
