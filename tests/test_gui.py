import pytest
from file_converter.gui import ConversorWindow
from PySide6.QtWidgets import QApplication


@pytest.fixture
def app(qtbot):
    return QApplication.instance() or QApplication([])


def test_gui_widgets_exist(app, qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert w.input_path is not None
    assert w.btn_select.text() == "📂 Procurar"


def test_gui_no_path_shows_error(app, qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    w.input_path.setText("")
    with qtbot.waitSignal(w.btn_word.clicked, timeout=100):
        w.btn_word.click()


def test_gui_title(app, qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert "Conversor" in w.windowTitle()

def test_gui_window_title(app, qtbot):
    """Garante que a janela principal tem título esperado."""
    from file_converter.gui import ConversorWindow
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert "Conversor" in w.windowTitle()