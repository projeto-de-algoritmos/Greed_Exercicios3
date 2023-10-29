# Tipo de problema: Agendamento para minimizar o atraso.

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Declarando variaveis auxiliares.
        tempoTotal = 0
        temposPlantio = 0

        # Criando uma tupla ordenada (decrescente em relacao ao crescimento) 
        # com os tempos de cresimento e plantio.
        plantas = sorted(((plantio, crescimento) for (plantio, crescimento) in zip(plantTime, growTime)), key=lambda x:x[1], reverse=True)

        # Pegando o par de tempos de crescimento e de plantio.
        for plantio, crescimento in plantas:
            temposPlantio += plantio                                # Incrementando o tempo de plantio.
            tempoTotal = max(tempoTotal, temposPlantio+crescimento) # Verificando se o tempo total eh maior que o tempos de plantio + de crescimento.

        return tempoTotal
