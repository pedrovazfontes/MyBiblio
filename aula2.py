# Aula 2 - Conversões

# Aqui acontece uma conversão implicita
idade = input("Digite sua idade: ")


if type(idade) == str:
    # Aqui acontece uma conversão explicita
    idade=int(idade)

    #
    if idade >= 18:
        print("Pode entrar")
    else:
        
        print("Não pode entrar")
else:
    print("Exceção")

