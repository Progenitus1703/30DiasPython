#Dia 06 aprendendo Python
#Exercício 01
Tupla_Vazia = ()
Irmãos = ('Davi', 'Saulo')
Irmãs = ('Marianita', 'Mariana')
Siblings = Irmãos + Irmãs
print(Siblings)
a = len(Irmãos)
b = len(Irmãs)
c = len(Siblings)
print('Você tem', a, 'irmãos homens', b, ',irmãs mulheres e', c, 'irmãos no total')
Parentes = ('\nRenê', 'Vládia')
Família = Parentes + Siblings
List = list(Família)
Fam = '\n'.join(List)
print('Sua família é composta pelos seguintes membros: ', Fam)
#Exercício 02
print('EXERCÍCIO 02')
d1 = str(Família[0])
d2 = str(Família[2])
d3 = str(Família[3]) 
Homens = (d1,d2,d3)
e1 = str(Família[1])
e2 = str(Família[4])
e3 = str(Família[5])
Mulheres = (e1,e2,e3)
Man = '\n'.join(Homens)
Woman = '\n'.join(Mulheres)
print('Homens da sua família: ', Man)
print('Mulheres da sua família: ', Woman)
#2.2
print('PARTE 2.2')
Frutas = ('Tomate','Pepino','Caju')
Vegetais = ('Alface', 'Rabanete', 'Couve')
Animais = ('Vaca', 'Galinha', 'Porco')
Fazendários = Frutas + Vegetais + Animais
FZD = list(Fazendários)
print(FZD)
Meio = len(FZD)//2
FZD1 = FZD[0:Meio] + FZD[Meio+1:]
print('Fazendários sem o elemento central', FZD1)
fzd3 = FZD[3:-3]
print('Fazendários sem os 3 primeiros e últimos elementos', fzd3)
print('Existem porquinhos em sua fazenda? ', 'Porco' in FZD)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estônia é um país nórdico? ', 'Estonia' in nordic_countries)
print('Iceland é um país nórdico? ', 'Iceland' in nordic_countries)