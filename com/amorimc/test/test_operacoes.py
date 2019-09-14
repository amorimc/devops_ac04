from unittest import TestCase
from com.amorimc.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_multiplicacao(self):
		self.assertEqual(self.operacoes.multiplicacao([2,8]), 16, "A multiplicacao é 16")