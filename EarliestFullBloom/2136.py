class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        n = len(plantTime) # Pegando a quantidade de plantas.

        tempoTotal = 0
        temposCrescimento = 0

        plantas= {} # Dicionario para guardar a relacao de tempo de plantio e crescimento.
        # Prenchedo o dicionario.
        for i in range(n):
            plantas[f'{plantTime[i]}'] = growTime[i]

        # Ordenando o dicionario em ordem decresente de tempo de crescimento.
        dict(sorted(plantas.items(), key=lambda x:x[1], reverse=True))

        for planta in plantas.keys():
            temposCrescimento += int(planta)
            tempoTotal = max(tempoTotal, temposCrescimento+planta+int(plantas[f'{planta}']))

        return tempoTotal

