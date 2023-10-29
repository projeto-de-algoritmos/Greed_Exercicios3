# Tipo de problema: Agendamento para minimizar o atraso.

import heapq

def maxPerformance(n, speed: list[int], efficiency: list[int], k: int) -> int:
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


print('Caso de Teste 1 - Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2')
print('Resultado Esperado: 60')
print(f'Resultado Calculado: {maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)}')
print('')
print('Caso de Teste 2 - Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3')
print('Resultado Esperado: 68')
print(f'Resultado Calculado: {maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3)}')
print('')
print('Caso de Teste 3 - Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4')
print('Resultado Esperado: 72')
print(f'Resultado Calculado: {maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4)}')
print('')