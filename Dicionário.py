#Dia 08 aprendendo Python
Ally = {}
Ally['Cor'] = 'Caramelo'
Ally['Raça'] = 'SRD'
Ally['Patas'] = 4
Ally['Idade'] = 10
print(Ally)
Eu = {
    'first_name':'Stéfano',
    'last_name':'Rocha',
    'age':25,
    'gênero': 'Masculino',
    'country':'Brasil',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'Bairro':'Cidade 2000',
        'zipcode':'60192125'
    }
    }
print(Eu)
print(len(Eu))
print(type(Eu['skills']))
print('Q06')
Eu['skills'].append('Civil')
Eu['skills'].append('Aprender')
print(Eu['skills'])
Chaves = Eu.keys()
Valores = Eu.values()
print(Chaves)
print(Valores)
Tupla_de_Eu = Eu.items()
print(type(Tupla_de_Eu))
print(Tupla_de_Eu)
del Eu['first_name']
print(Eu)