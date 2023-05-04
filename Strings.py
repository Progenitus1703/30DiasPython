#Dia 04 aprendendo python
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
nome = "Stéfano"
sobrenome = "Sobreira"
Linguagem = "Python"
string_formada = "Eu me chamo {} {} e estou aprendendo {}" .format(nome, sobrenome, Linguagem)
print(string_formada)
a = ['30', 'Dias', 'De', 'Python']
comp = ' ' .join(a)
print(comp)
company = input("Qual será o nome da sua empresa? ")

h = len(company)
print("A sua empresa se chamará" , company, "\nA sua empresa têm", h , "letras")
b = company.upper()
c = company.lower()
print("Aqui está o nome da sua empresa com as letras maiúsculas e minúsculas: \n", b, "\n", c)
#9 Questão mais difícil até então - Remover a primeira palavra de uma frase dada
def remove_primeira_palavra(frase):
    palavras = frase.split()
    return " ".join(palavras[1:])

frase = company
nova_frase = remove_primeira_palavra(frase)
print("Nome da sua empresa sem a primeira palavra:", nova_frase)
#10
e = "Coding for all"
d = "Coding" in e
print("Existe Coding em Coding for all:", True)
print(e.replace('Coding', 'Python'))
NC = company.title()
company = NC
f = company.split()
#17
Primeira_Letra = company[0]
Ultima_Letra = company[-1]
Decima = company[9]
Tamanho = len(f)
print("A primeira letra da sua empresa é:", Primeira_Letra, "\nA última letra da sua empresa é: ", Ultima_Letra, "\nA décima letra da sua empresa é", Decima)
print("A sua empresa tem ", Tamanho, " palavras")
i,j,k = f
i0 = i[0]
j0 = j[0]
k0 = k[0]
ACR = [i0, j0, k0]
ACR = "".join(ACR)

print("Uma boa abreviação para a sua empresa seria ", ACR)
e = e.title()
print("A letra C é a ", 1 + e.find('C'), "ª letra da frase ", e)
print("A letra F é a ", 1 + e.find('F'), "ª letra da frase ", e)
people = 'as pessoas'
space = ' '
l = company + space + people
l = l.title()
print("Novo nome da empresa será: ", l)
print("A última vez que a letra s aparece no nome da sua empresa é na posição: ", l.rfind('s'))
m = 'You cannot end a sentence with because because because is a conjunction'
n = len(m)
r = len('because')
o = m.find('because')
p = m.rfind('because')
print(n, o, p)
o -= 1
p = p + r
q = m[0:o] + m[p:n]
print(q)
#28
e = "Coding for all"
space = " "
s = space + e + space
t = e.startswith('Coding')
print(e, "Starts with 'Coding': ", t )
u = e.endswith('all')
print(e, "Ends with 'all': ", u )
v = s.find('C')
x = s.rfind('l')
v -= 1
Deu_certo = e[v:x]
print("Deu certo?", Deu_certo is e)
print(Deu_certo)
#34
Nome = input("Qual o seu nome? ")
Idade = input("Qual a sua idade? ")
Ps = input("Em que país você reside? ")
Cidade = input("Em que cidade você reside? ")
Tab = " \t"
String = Nome + space + Idade + Tab + Ps + Tab + Cidade
print("Nome \tIdade \tPaís \tCidade")
print(String)