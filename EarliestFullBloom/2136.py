class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        tempoTotal = 0
        temposPlantio = 0

        plantas = tuple(zip(plantTime, growTime)) # Guardando o par tempo de plantio e crescimento em numa tupla.

        # Interval Scheduling Modificado

        # Ordenando em ordem decresente de tempo de crescimento (tempo de termino).
        plantas = sorted([(plantio, crescimento) for (plantio, crescimento) in plantas], key=lambda x:x[1], reverse=True)

        # Pegando o par de tempos de crescimento e de plantio.
        for plantio, crescimento in plantas:
            temposPlantio += plantio
            tempoTotal = max(tempoTotal, temposPlantio+crescimento)

        return tempoTotal
