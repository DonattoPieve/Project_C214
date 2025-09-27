import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QFileDialog, QMessageBox, QLabel,
    QDialog, QDialogButtonBox, QStyle
)
from PySide6.QtGui import QIcon, QFont, QAction, QColor, QPalette
from PySide6.QtCore import Qt

from .core import convert_docx_to_pdf, convert_csv_to_pdf, convert_pptx_to_pdf
from . import __version__   # <<< importa a versão centralizada no __init__.py


class SobreDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sobre")
        self.setFixedSize(420, 230)

        layout = QVBoxLayout(self)

        # Ícone de informação (padrão do sistema)
        icon_label = QLabel()
        icon = self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        icon_label.setPixmap(icon.pixmap(48, 48))
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        # Título + versão
        title = QLabel(
        f"📄 Conversor de Arquivos → PDF<br>"
        f"<span style='font-size:9pt; color:gray;'>Versão {__version__}</span>"
        )
        title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Autor
        autor = QLabel("🔧 Desenvolvido por <b>Donatto Pieve</b>")
        autor.setAlignment(Qt.AlignCenter)
        layout.addWidget(autor)

        # Link clicável
        link = QLabel(
            '<a href="https://github.com/DonattoPieve">'
            '🌐 github.com/DonattoPieve</a>'
        )
        link.setAlignment(Qt.AlignCenter)
        link.setOpenExternalLinks(True)
        layout.addWidget(link)

        # Botão fechar
        botoes = QDialogButtonBox(QDialogButtonBox.Ok)
        botoes.accepted.connect(self.accept)
        layout.addWidget(botoes)


class ConversorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Arquivos → PDF")
        self.setFixedSize(600, 320)
        self.setWindowIcon(QIcon.fromTheme("document-save"))

        font = QFont("Segoe UI", 10)
        self.setFont(font)

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

        # Menu Arquivo
        file_menu = menu.addMenu("Arquivo")
        abrir = QAction("Abrir arquivo...", self)
        abrir.triggered.connect(self._selecionar_arquivo)
        sair = QAction("Sair", self)
        sair.triggered.connect(self.close)
        file_menu.addAction(abrir)
        file_menu.addSeparator()
        file_menu.addAction(sair)

        # Menu Ajuda
        ajuda_menu = menu.addMenu("Ajuda")
        sobre = QAction("Sobre", self)
        sobre.triggered.connect(self._mostrar_sobre)
        ajuda_menu.addAction(sobre)

    def _mostrar_sobre(self):
        dialog = SobreDialog(self)
        dialog.exec()

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
