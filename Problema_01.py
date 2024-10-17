def fibonacci_sequence(n):
    """Gera a sequência de Fibonacci até o número n."""
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def check_fibonacci(num):
    """Verifica se o número pertence à sequência de Fibonacci."""
    fib_sequence = fibonacci_sequence(num)
    if num in fib_sequence:
        return True
    return False

# Entrada do usuário
try:
    number = int(input("Informe um número: "))
    if check_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, informe um número inteiro válido.")


    """Explicação do Código:"""

"""1. Função fibonacci_sequence(n):
 * Cria uma lista chamada sequence que armazena os números da sequência de Fibonacci
 até que o próximo número seja maior que n.
 * Começa com 0 e 1 e usa um loop while para calcular os próximos números."""

"""2. Função check_fibonacci(num):
 * Gera a sequência de Fibonacci até o número informado e verifica se esse número está
 na lista gerada."""

"""3. Entrada do Usuário:
 * O programa pede ao usuário para inserir um número.
 * Em seguida, verifica se o número pertence à sequência de Fibonacci e exibe uma
 mensagem apropriada."""