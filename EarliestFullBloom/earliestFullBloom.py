# Tipo de problema: Agendamento para minimizar o atraso.

def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:

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


print('Caso de Teste 1 - Input: plantTime = [1,4,3], growTime = [2,3,1]')
print(f'Resultado: {earliestFullBloom([1,4,3], [2,3,1])}')
print('')
print('Caso de Teste 2 - Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]')
print(f'Resultado: {earliestFullBloom([1,2,3,2], [2,1,2,1])}')
print('')
print('Caso de Teste 3 - Input: plantTime = [1], growTime = [1]')
print(f'Resultado: {earliestFullBloom([1], [1])}')
print('')