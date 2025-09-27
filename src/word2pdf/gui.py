import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QFileDialog, QMessageBox, QLabel
)
from PySide6.QtGui import QIcon, QFont, QAction, QColor, QPalette
from PySide6.QtCore import Qt

from .core import convert_docx_to_pdf, convert_csv_to_pdf, convert_pptx_to_pdf


class ConversorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Arquivos → PDF")
        self.setFixedSize(600, 340)
        self.setWindowIcon(QIcon.fromTheme("document-save"))

        # Fonte padrão
        font = QFont("Segoe UI", 10)
        self.setFont(font)

        # Central widget
        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.setSpacing(15)

        # Título
        title = QLabel("📄 Conversor de Arquivos para PDF")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Input + botão selecionar
        hbox = QHBoxLayout()
        self.input_path = QLineEdit()
        self.input_path.setPlaceholderText("Selecione um arquivo .docx, .csv ou .pptx")
        self.btn_select = QPushButton("📂 Procurar")
        hbox.addWidget(self.input_path)
        hbox.addWidget(self.btn_select)
        layout.addLayout(hbox)

        # Botões de conversão
        self.btn_word = QPushButton("📝 Word → PDF")
        self.btn_csv = QPushButton("📊 CSV → PDF")
        self.btn_pptx = QPushButton("🎤 PowerPoint → PDF")

        for btn, color in [
            (self.btn_word, "#4CAF50"),
            (self.btn_csv, "#FF9800"),
            (self.btn_pptx, "#9C27B0"),
        ]:
            btn.setMinimumHeight(40)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border-radius: 8px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: #555;
                }}
            """)
            layout.addWidget(btn)

        # Label com autoria + link para GitHub
        link = QLabel(
            '<a href="https://github.com/DonattoPieve">'
            '🔧 Desenvolvido por <b>Donatto Pieve</b>  </a>'
        )
        link.setAlignment(Qt.AlignCenter)
        link.setOpenExternalLinks(True)  # permite clicar
        link.setStyleSheet("color: #64B5F6; font-size: 9pt; font-style: italic; margin-top: 15px;")
        layout.addWidget(link)

        self.setCentralWidget(central)

        # Conectar ações
        self.btn_select.clicked.connect(self._selecionar_arquivo)
        self.btn_word.clicked.connect(lambda: self._converter(convert_docx_to_pdf))
        self.btn_csv.clicked.connect(lambda: self._converter(convert_csv_to_pdf))
        self.btn_pptx.clicked.connect(lambda: self._converter(convert_pptx_to_pdf))

        # Menu superior
        self._create_menu()

    def _create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("Arquivo")

        abrir = QAction("Abrir arquivo...", self)
        abrir.triggered.connect(self._selecionar_arquivo)
        sair = QAction("Sair", self)
        sair.triggered.connect(self.close)

        file_menu.addAction(abrir)
        file_menu.addSeparator()
        file_menu.addAction(sair)

    def _selecionar_arquivo(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Escolher arquivo", str(Path.home()),
            "Arquivos suportados (*.docx *.csv *.pptx)"
        )
        if path:
            self.input_path.setText(path)

    def _converter(self, func):
        caminho = self.input_path.text().strip()
        if not caminho:
            QMessageBox.critical(self, "Erro", "Nenhum arquivo selecionado.")
            return
        try:
            out = func(caminho)
            QMessageBox.information(self, "Sucesso", f"✅ PDF gerado em:\n{out}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha na conversão:\n{e}")


def aplicar_dark_mode(app: QApplication):
    """Aplica tema escuro global no Qt."""
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    app.setPalette(dark_palette)
    app.setStyle("Fusion")


def main():
    app = QApplication(sys.argv)
    aplicar_dark_mode(app)
    w = ConversorWindow()
    w.show()
    sys.exit(app.exec())
