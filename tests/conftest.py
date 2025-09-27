import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def app():
    """Cria uma instância única de QApplication para todos os testes Qt."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app
