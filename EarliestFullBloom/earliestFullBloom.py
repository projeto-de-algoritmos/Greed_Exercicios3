def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:

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


print('Caso de Teste 1 - Input: plantTime = [1,4,3], growTime = [2,3,1]')
print(f'Resultado: {earliestFullBloom([1,4,3], [2,3,1])}')
print('')
print('Caso de Teste 2 - Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]')
print(f'Resultado: {earliestFullBloom([1,2,3,2], [2,1,2,1])}')
print('')
print('Caso de Teste 3 - Input: plantTime = [1], growTime = [1]')
print(f'Resultado: {earliestFullBloom([1], [1])}')
print('')