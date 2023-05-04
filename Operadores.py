#Dia 03 de Python
print("adição", 1+2)
print("multiplicação de complexos", (1 + 2j)*(1-2j)) #multiplicação de complexos
print(3>2) #checa se True ou se False
print ("1 is 1", 1 is 1) #função is == "=="
print("1 is not 2", 1 is not 2) #função is not == "!="
print("S in Stéfano", "S" in "Stéfano")
print("T in Stéfano", "T" in "Stéfano")
print(True and False)
print(True or False)
a = not(True)
print(a)

#12
a = len("python")
b = len("dragon")
c = a is b
print("python and dragon have the same length", c)
d = "on" in "python"
e = "on" in "dragon"
print("on is found in both 'python' and 'dragon'", d is True and e is True)
print("jargon is in 'I hope this course is not full of jargon.'", "jargon" in "I hope this course is not full of jargon.")
f = str(len("python"))
print(f)
#17 checking if a number is even
g = int(input("Digite um número: "))
print("Você digitou o número", g)
h = g%2
if h == 0:
    print("O número digitado é par")
else :
    print("O número digitado é ímpar")
i = int(9.8)

print("o inteiro de 9,8 é igual a 10", i is 10)
print("O inteiro de i é igual a ", i)
#23 Questão difícil fodase
x = int(input("Digite um número: "))
y = 1
x += 1
while y < x :
    print(y, 1, y, y**2, y**3)
    y += 1
print("Suas informações foram prontamente salvas para o nosso posterior uso")
pergunta = input("Já podemos fechar o arquivo?")
exit()