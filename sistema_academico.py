# Nomes dos integrantes do grupo:
# 1. Guto
# 2. Ruan
# 3. Samuel

class SistemaAcademico:
    def calcular_media(self, notas):
        if not notas:
            return 0
        return sum(notas) / (len(notas)) 

    def verificar_aprovacao(self, media, frequencia):
        if media >= 6.0 and frequencia >= 75:
            return "Aprovado"
        return "Reprovado"

    # DICA: A frequência geralmente é representada em uma escala percentual
    def calcular_frequencia(self, total_aulas, faltas):
        presenca = (total_aulas - faltas) / total_aulas
        return presenca * 10