# Tipo de problema: Algoritmo de agendamento de intervalo.

def maxRunTime(n: int, batteries: list[int]) -> int:

    # Variavel tempo das bateriaa
    tempoBaterias = sum(batteries)

    # Ordenando as baterias em ordem crescente
    batteries.sort()

    # Calculando a media de tempo gasto pelos computadores
    media = (tempoBaterias // n)
        
    # Verificando se a ultima bateria, a maior de todas, 
    # eh maior que o consumo medio
    while batteries[-1] > media:   
        tempoBaterias -= batteries.pop()    # Atualizando o tempo total restante para conter somente as baterias limitantes
        n -= 1                              # Atualizando o numero de baterrias
        media = (tempoBaterias // n)        # Atualiza a media de tempo gasto pelos computadores

    return (tempoBaterias // n)


print('Caso de Teste 1 - Input: n = 2, batteries = [3,3,3]')
print('Resultado Esperado: 4')
print(f'Resultado Calculado: {maxRunTime(2, [3,3,3])}')
print('')
print('Caso de Teste 2 - Input: n = 2, batteries = [1,1,1,1]')
print('Resultado Esperado: 2')
print(f'Resultado Calculado: {maxRunTime(2, [1,1,1,1])}')
print('')
