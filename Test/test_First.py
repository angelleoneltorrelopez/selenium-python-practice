import time
import pytest
from Test.test_base import BaseTest
from Pom.page import Page


def suma(x, y):
    return x + y


class Test_First(BaseTest):
    def test_link(self):
        self.page = Page(self.driver)
        print("Prueba print")
        assert self.page.click_link()

    def test_link_js(self):
        self.page = Page(self.driver)
        assert self.page.click_link_js()

    def test_alert_get_text(self):
        self.page = Page(self.driver)
        self.page.click_button()
        message = self.page.get_text_alert()
        assert message == "Hello world!", "Reporte de regresion: El texto de la alerta en la pagina es: "+message

    def test_move_to_element(self):
        self.page = Page(self.driver)
        assert self.page.moveto_element()
        time.sleep(5)

    @pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (2, 3, 5),
            (2, 8, 10),
            (suma(2, 5), 5, 13),
            (4, suma(3, 6), 12)
        ]
    )
    def test_suma(self, input_x, input_y, expected):
        assert suma(input_x, input_y) == expected, "La suma fue incorrecta"
