# Nomes dos integrantes do grupo:
# 1. Guilherme Alexandre Cunha Silva
# 2. Érika Mara de Morais Machado
# 3. Maria Luiza Bernardo Madeira
# 4. Verônica Rodrigues da Silva França

'''
Corrija a classe SistemaAcademico, responsável por calcular informações
acadêmicas de um aluno.

A classe deve possuir os seguintes métodos:

1. calcular_media(notas)
   - Recebe uma lista de notas.
   - Retorna a média aritmética das notas.
   - Caso a lista esteja vazia, retorna 0.

2. calcular_frequencia(total_aulas, faltas)
   - Recebe o número total de aulas e a quantidade de faltas do aluno.
   - Calcula e retorna a frequência do aluno em porcentagem.

3. verificar_aprovacao(media, frequencia)
   - Recebe a média final e a frequência do aluno.
   - Deve analisar se o aluno atende aos critérios mínimos de aprovação
     definidos pela instituição.
   - Retorna "Aprovado" quando o aluno cumpre os critérios necessários.
   - Caso contrário, retorna "Reprovado".
'''

class SistemaAcademico:
    
    def calcular_media(self, notas):
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def calcular_frequencia(self, total_aulas, faltas):
        if total_aulas == 0:
            return 0
        presenca = (total_aulas - faltas) / total_aulas
        return presenca * 100

    def verificar_aprovacao(self, media, frequencia):
        if media >= 6.0 and frequencia >= 70:
            return "Aprovado"
        return "Reprovado"