# Tipo de problema: Algoritmo de agendamento de intervalo.

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

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
    