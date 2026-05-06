import unittest
from sistema_academico import SistemaAcademico

class TestSistemaAcademico(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaAcademico()

    def test_calcular_media(self):
        self.assertEqual(self.sistema.calcular_media([8, 8, 8]), 8.0)

    def test_verificar_aprovacao_limite(self):
        self.assertEqual(self.sistema.verificar_aprovacao(6.0, 75), "Aprovado")
        
    def test_verificar_reprovacao_frequencia(self):
        self.assertEqual(self.sistema.verificar_aprovacao(10.0, 74), "Reprovado")

    def test_calcular_frequencia(self):
        # Se um aluno teve 40 aulas e 10 faltas, a frequência deve ser 75.0%
        self.assertEqual(self.sistema.calcular_frequencia(40, 10), 75.0)

if __name__ == '__main__':
    unittest.main()