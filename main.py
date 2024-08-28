# Crie um programa que receba do usuário um número inteiro positivo, e o programa retorne a quantidade de números informada da sequência de Fibonacci.

def fibonacci(valor):
    n = []
    i = 0
    for i in range(valor):
        if i == 0:
            n.append(0)
        elif i == 1:
            n.append(1)
        else:
            proximo_valor = n[i-1] + n[i-2]
            n.append(proximo_valor)
            i += 1 
    return n

while True:
    num = int(input('Digite um número para iniciar: '))
    sequencia = fibonacci(num)
    for x in sequencia:
        print(x)
    opcao = input('Deseja continuar (s/n)? ')
    if opcao.lower() != 'n':
        continue
    else:
        print('Programa encerrado!')
        break