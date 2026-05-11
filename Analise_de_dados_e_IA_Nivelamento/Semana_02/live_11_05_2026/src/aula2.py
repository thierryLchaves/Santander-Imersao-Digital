nome = input("Me diga seu nome: ")
idade = input("Me diga sua idade")
print(f"olá {nome}! Você ten {idade} anos!")


primeiro_numero = int(input("Diga o primeiro número: "))
segundo_numero = int(input("Diga o segundo número: "))
print(f"A soma é {primeiro_numero + segundo_numero}")

a = 2
b = 3
print(f"{a} > {b} dá {a>b}")
print(f"{a} < {b} dá {a<b}")
print(f"{a} >= {b} dá {a>=b}")
print(f"{a} <= {b} dá {a<=b}")
print(f"{a} == {b} dá {a==b}")
print(f"{a} =! {b} dá {a<b}")

idade = int(input("Diga a sua idade: "))
if idade < 18:
    print("Você não pode comprar bebidas alcoólicas!!! 😡🤬")
else:
    print("Você pode comprar bebidas alcoólicas!")


idoso = input("Você é idose ? (sim/não): ")
deficiente = input("Você é deficiente ? (sim/não): ")

if idoso == "sim" or deficiente == "sim":
    print("Pode estacionar!")
else:
    print("Procure outra vaga")


idosos = input("Você é idose ? (sim/não): ")
cartao = input("Você possui cartão de idoso? (sim/não): ")

if idosos == "sim" and cartao == "sim":
    print("Pode estacionar!")
else:
    print("Procure outra vaga")

letra = input("Digite uma letra:")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("É vogal!")
else:
    print("Não é vogal!")
