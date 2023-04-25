'''
Solicite a quantidade de alunos de uma turma e a quantidade de notas. 
Para cada aluno, solicite as suas notas e exiba a sua respectiva média
(a média deve ser arredondada para duas casas decimais).
'''


alunos = int(input('Insira o número de alunos: '))
notas = int(input('Insira a quantidade de notas: '))

for i in range (alunos):
    soma = 0
    for n in range(notas):
        a = float(input('informe a nota: '))
        soma += a 
    media = soma / notas
    print(f'Média: {round(media, 2)}')


