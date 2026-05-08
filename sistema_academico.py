# Nomes dos integrantes do grupo:
# 1. Luiz Carlos de Paiva Silva
# 2. Kaique Inácio Salvador
# 3. Sandy Karolina Maciel

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