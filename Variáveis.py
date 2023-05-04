#Dia 02 aprendendo Python
name = input("Qual o seu nome? ")
sobrenome = input("Qual seu sobrenome? ")
país = input("Onde você mora? ")
idade = input("Qual a sua idade? ")
Ano = input("Em que ano estamos? ")
Marriage = input("Você é casado? ")
nome_completo = name + " " + sobrenome
Nascimento = int(Ano) - int(idade) - 1
print("Seu nome é: ", nome_completo)
print("Seu país é:", país)
print("Sua idade é:", idade)
print("Estamos no ano", Ano, "e você nasceu em", Nascimento)
if (Marriage == "Sim"):
    print("Você é uma pessoa casada")
else:
     print ("Você é uma pessoa solteira")
a = len(name)
b = len(sobrenome)
print("O seu primeiro nome tem ", a, " letras e o seu sobrenome tem ", b," letras")
if a>b:
     print("Portanto, seu nome é maior do que o seu sobrenome")
elif a==b:
     print("Portanto seu nome e sobrenome têm o mesmo tamanho")
else :
     print("Portanto seu sobrenome é maior do que seu nome")
print("Faremos agora um pequeno exercício de matemática")
Raio = input("Escolha um número para ser o raio do círculo, em metros ")
print("Qual a área e a circunferência de um círculo com esse raio?")
Area = int(3.1415926*float(Raio)*float(Raio))
Circum = int(2*3.1415926*float(Raio))
print("A área da circunferência é de ", Area, " m e seu comprimento é de ", Circum, " m")

