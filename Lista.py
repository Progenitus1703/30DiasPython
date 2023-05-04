#Dia 05 aprendendo Python
a = []
Sabores = ['Marguerita', 'Palmito', 'Brocolis', '4 Queijos', 'Vegetariano']
c = len(Sabores)
First = Sabores[0]
Last = Sabores[-1]
Middle = Sabores[c//2]
print("Sua lista vazia: ", a, "\n Sabores que um vegetariano pode pedir no Kalzone: ", Sabores, "\n Quantos opções são: ", c)
print("Primeiro sabor listado: ", First)
print("Último sabor listado: ", Last, "\n Sabor listado no meio da lista: ", Middle)
#06
Empresas = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print (Empresas)
Guardar = Empresas[3]
Empresas[3] = 'Samsung'
print(Empresas)
Empresas.append(Guardar)
Meio = len(Empresas)//2
Empresas.insert(Meio,'Tencent')
f = Empresas[-1]
Empresas.pop(-1)
g = f.upper()
Empresas.append(g)
print( Empresas)
#14
h = '#'.join(Empresas)
print(h)
print("Amazon faz partes das empresas de tecnologia? ", 'Amazon' in Empresas)
Empresas.sort()
print(Empresas)
Sem3P = Empresas[3:]
Sem3U = Empresas[:-3]
Meio = len(Empresas)//2
Empresas.pop(Meio)
print(Sem3P)
print(Sem3U)
print(Empresas)
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Full_Stack = front_end + back_end + ['python'] + ['SQL']
print(Full_Stack)
#Nível 02
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
k = ages[0]
l = ages[-1]
print("Idade mínima: ", ages[0], "\n Idade máxima: ", ages[-1])
ages.append(k)
ages.append(l)
ages.sort()
print(ages)
Meio = len(ages)//2
Quantidade = len(ages)
def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

Somatorio = somalista(ages)
Média = float(Somatorio/Quantidade)
range = l - k
print("Quantidade de alunos é: ", Quantidade, "\nMediana das idades é: ", ages[Meio], "\nMédia das idades é: ", Média)
print("O alcance das idades é: ", range)

print('FINALIZANDO')
Países = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
m = len(Países)
Meio = len(Países)//2 + 1
Primeira_metade = Países[:Meio]
Segunda_Metade = Países[Meio:]
print(Primeira_metade)
print(Segunda_Metade)
n,o,p, *rest = Países
P3 = [n,o,p]
Escandinavos = [rest]
print(P3)
print(Escandinavos)
