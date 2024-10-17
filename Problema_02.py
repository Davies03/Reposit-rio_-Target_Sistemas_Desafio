def contar_letra_a(texto):
    """Conta a quantidade de vezes que a letra 'a' (maiúscula e minúscula) aparece em uma palavra."""
    return texto.lower().count('a')

# Entrada do usuário
texto = input("Escreva uma palavra: ")

# Contar a letra 'a' na palavra
quantidade_a = contar_letra_a(texto)

# Exibir os resultados
if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vez(es) na palavra.")
else:
    print("A letra 'a' não aparece na palavra.")


"""Explicação do Código:"""

"""1.Função contar_letra_a(texto):
 * Converte a Palavra para minúsculas usando lower() para garantir que tanto 'a' quanto 'A' sejam contados.
 * Utiliza o método count() para contar quantas vezes a letra 'a' aparece na Palavra."""

"""2.Entrada do Usuário:
 * O programa pede ao usuário para inserir uma Palavra."""

"""3.Exibição dos Resultados:
 * O programa exibe quantas vezes a letra 'a' aparece na Palavra, ou informa que ela não está presente."""