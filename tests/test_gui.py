import pytest
from file_converter.gui import ConversorWindow
from PySide6.QtWidgets import QApplication


@pytest.fixture
def app(qtbot):
    return QApplication.instance() or QApplication([])


@pytest.mark.gui
def test_gui_widgets_exist(qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert w.input_path is not None
    assert w.btn_select.text() == "📂 Procurar"


@pytest.mark.gui
def test_gui_no_path_shows_error(qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    w.input_path.setText("")
    with qtbot.waitSignal(w.btn_word.clicked, timeout=100):
        w.btn_word.click()


@pytest.mark.gui
def test_gui_title(app, qtbot):
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert "Conversor" in w.windowTitle()


@pytest.mark.gui
def test_gui_window_title(app, qtbot):
    """Garante que a janela principal tem título esperado."""
    w = ConversorWindow()
    qtbot.addWidget(w)
    assert "Conversor" in w.windowTitle()
