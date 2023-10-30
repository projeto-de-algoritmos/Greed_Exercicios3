# Tipo de problema: Agendamento para minimizar o atraso

import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Declarando o valor que serah usado para calcular o modulo.
        modulo = (10 ** 9) + 7

        # Veriaveis para guardadar a performace total e velocidade total
        performaceTotal = 0
        velocidadeTotal = 0

        # Agregando os valores de performace dos engenheiros em uma unica variavel
        engenheiros = sorted([(eficiencia, velocidade) for (eficiencia, velocidade) in zip(efficiency, speed)], reverse=True)

        # Criando uma heap de minimo para guardar o par efi/vel
        minheap = []

        # Verificando a performace com cada um dos engenheiros
        for efi, vel in engenheiros:
            # Verificando se a qtd de engenheiro eh maior que k
            if len(minheap) == k:
                aux = heapq.heappop(minheap)                                # Retirando o engenheiro da heap
                velocidadeTotal -= aux                                      # Retirando a vel do engenheiro da velocidade total
            velocidadeTotal += vel                                          # Adicionando a velocidade do engenheiro na velocidade total
            heapq.heappush(minheap, vel)                                    # Adicionando o engenheiro (velocidade dele) na heap
            performaceTotal = max(performaceTotal, efi*velocidadeTotal)     # Calculando a performace com esse engenheiro

        return performaceTotal % modulo
