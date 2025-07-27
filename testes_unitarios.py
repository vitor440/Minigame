from pacote.calculo import Calculo
import unittest


class TestCalculo(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculo(2)

    def test_verifica_resultado(self):
        self.assertEqual()