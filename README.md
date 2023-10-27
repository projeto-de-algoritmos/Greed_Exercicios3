# Exercicios2

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Caminhoneiro<br>

## Alunos

| Matrícula  | Aluno                       |
| ---------- | --------------------------- |
| 21/1029147 | Arthur de Melo Viana        |
| 21/1029666 | Matheus Henrique Dos Santos |

## Sobre

Exercícios do Sphere Online Judge:

- [EXPEDI](https://www.spoj.com/problems/EXPEDI/)

Exercícios do LeetCode:

## Screenshots

As seções a seguir explicitam os exercícios resolvidos e apresentam uma breve explicação das resoluções. É possível observar o status de conclusão do problema e uma descrição do algoritmo utilizado. A dificuldadade dos exercícios do SPOJ, [de acordo com o próprio site](https://www.spoj.com/tutorials/USERS/#choose), é melhor analisada pela quantidade de usuários que solucionaram e pela taxa de aceitação das submissões, a qual ficou no título de cada seção entre parênteses da seguinte forma: Users - ACC%. Já a dificuldade do leetcode é dada de forma explícita na página do problema.

### EXPEDI - Expedition (2143 - 20.40%)

Utilização do algoritmo do caminhoneiro, modificado para um cenário no qual o tanque do caminhão possui capacidade infinita e cada posto preenche parcialmente o tanque. Para a resolução de tal exercício, deve-se imprimir uma única linha com a menor quantidade de vezes que o caminhão deve ser abastecido para chegar a seu destino. Portanto, a quantidade de vezes que o caminhão foi abastecido foi feita por meio do auxílio de um vetor de visitados. Logo, desde que o tanque tenha combustível para chegar ao posto e não esteja visitado, independente de sua capacidade, o posto será colocado no heap e marcado como visitado. O heap de máximo tem como peso a quantidade de combustível do posto. O vetor de postos foi ordenado para evitar TLE pelas alterações constantes no heap, mas a solução é aceita mesmo sem a ordenação, como pode se analisar nas duas submissões abaixo do enunciado.

![Imagem EXPEDI1](assets/enunciadoEXPEDI.png)

![Imagem EXPEDI](assets/EXPEDI.png)

## Instalação

**Linguagens**: C++ e Python<br>

Para rodar os arquivos em C++, é recomendado utilizar o WSL caso esteja no Windows. Nele, execute os comandos `sudo apt update` e `sudo apt install build-essential` para instalar o g++. O código em C++ também pode ser enviado no próprio [SPOJ](https://www.spoj.com/) ou compilado e executado no [Ideone](https://ideone.com/).

Já para rodar os arquivos em Python, pode ser utilizado o interpretador online [GDB](https://www.onlinegdb.com/) ou instalar o Python na sua máquina (as instruções para instalação podem ser encontradas no [guia de instalação](https://wiki.python.org/moin/BeginnersGuide/Download)).

## Uso

Para os exercícios em C++, compile o código utilizando `g++ -o prog arquivo.cpp` e execute-o utilizando `./prog`, por fim, digite o input no terminal. Também pode ser utilizado o comando `./prog < entrada.txt` caso exista algum caso de teste válido no arquivo de texto. Os links para os problemas resolvidos estão na seção "Sobre", onde podem ser enviados para verificar se foram aceitos.

Para os exercícios em Python, basta digitar `python nome-do-arquivo.py` no terminal de preferência. Da mesma forma, a solução pode ser enviada na própria página do problema.

## Vídeo

Para acessar o vídeo explicativo sobre os exercícios, [clique aqui](https://www.youtube.com/embed/).

Para baixar o vídeo, [clique aqui](apresentacao.mp4).
