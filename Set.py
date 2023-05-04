#Dia 07 aprendendo Python
#Exercício 01
print('EXERCÍCIO 01')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
C = len(it_companies)
print('Temos no catálogo ',C, 'empresas de TI')
it_companies.add('Twitter')
Outras_empresas = {'Samsung', 'Dell', 'Tencent'}
it_companies.update(Outras_empresas)
print(it_companies)
it_companies.discard('Apple')
print(it_companies)
#Exercício 02
print('EXERCÍCIO 02')
D = A.union(B)
print(D)
print(A.intersection(B))
print('Is A subset of B?', A.issubset(B))
print('Diferença simétrica entre conjunto e subconjunto: ', A.symmetric_difference(B))
#Exercício 03
print('EXERCÍCIO 03')
E = len(age)
c_age = set(age)
F = len(c_age)
print('Tamanho da lista', E)
print('Tamanho do conjunto', F)
G = 'I am a teacher and I love to inspire and teach people.'
print(G)
i = set(G.split())
print(i)
j = len(i)
print('Na frase dada existem ',j ,' frases únicas')