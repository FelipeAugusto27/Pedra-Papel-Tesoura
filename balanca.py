'''Uma balança de mercado informa o valor de um produto usando seu peso. Crie uma balança que possa pesar:
-Cebola (R$8,99/Kg)
-Alface (R$5,99/Kg)
-Tomate (R$2,00/Kg)
'''

# Input

produto = float(input("Informe o produto: \n .1 = Cebola \n .2 = Alface \n .3 Tomate \n"))

peso = float(input("Peso do produto (Kg): "))

# Processamento de Dados e Saída

if produto == 1:
    valorfinal = 7.99 * peso
    print(f"Cebola ({peso} Kg) -> R${valorfinal:.2f}")

elif produto == 2:
    valorfinal =  5.99 * peso
    print(f"Alface ({peso} Kg) -> R${valorfinal:.2f}")

elif produto == 3:
    valorfinal = 2 * peso
    print(f"Tomate ({peso} Kg) -> R${valorfinal:.2f}")
