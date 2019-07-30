#one.py


def func():
	print("Func in one.py")

print("Top level in one.py")


"""Python esta atribuindo a variavel build-in
__name__ a string de mesmo nome no background.
Assim, checamos se ele fez isso e o programa
inicia executando todos codigos com identação
zero (level 0).
Ou seja,  se a variavel name for igual a string
name, entao vou rodar este codigo diretamente
"""
if __name__ == "_main__":
	print("One.py is being run directly.")

else:
	print("One.py has been imported.")