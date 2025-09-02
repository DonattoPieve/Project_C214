import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QFileDialog, QMessageBox, QLabel
)
from docx2pdf import convert


class ConversorWordPDF(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor Word → PDF")
        self.setFixedSize(500, 200)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Label
        self.label = QLabel("Selecione um arquivo Word (.docx):")
        layout.addWidget(self.label)

        # Campo de texto
        self.input_path = QLineEdit()
        layout.addWidget(self.input_path)

        # Botão selecionar
        self.btn_select = QPushButton("Selecionar Arquivo")
        self.btn_select.clicked.connect(self.selecionar_arquivo)
        layout.addWidget(self.btn_select)

        # Botão converter
        self.btn_convert = QPushButton("Converter para PDF")
        self.btn_convert.clicked.connect(self.converter_pdf)
        layout.addWidget(self.btn_convert)

    def selecionar_arquivo(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione um arquivo Word",
            "",
            "Documentos Word (*.docx)"
        )
        if caminho:
            self.input_path.setText(caminho)

    def converter_pdf(self):
        caminho_word = self.input_path.text().strip()

        if not caminho_word:
            QMessageBox.critical(self, "Erro", "Nenhum arquivo selecionado.")
            return

        try:
            pasta_destino = os.path.dirname(caminho_word)
            convert(caminho_word, pasta_destino)

            QMessageBox.information(
                self,
                "Sucesso",
                f"Arquivo convertido para PDF em:\n{pasta_destino}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha na conversão:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ConversorWordPDF()
    janela.show()
    sys.exit(app.exec())