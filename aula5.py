
nome=input("Digite seu nome: ")
altura=float(input("Digite sua altura em metros: "))
peso=float(input("Digite seu peso: "))
imc= peso/ (altura*altura)

print("Nome: ",nome)
print("Altura: ",altura)
print("Peso: ",peso)
print("Seu IMC é de: ",round((imc),2))