#Dia 09 aprendendo Python, Tarefa bastante difícil
idade = float(input('Qual a sua idade? '))

if idade >= 18:
    print('Você já tem idade para dirigir')
else:
    print(f"Ainda faltam {18 - idade} anos para você poder dirigir")

print("Eu tenho 25 anos")
age = 25
id = int(idade)

if id == age:
    print('Nós temos a mesma idade')
elif id > age:
    print(f'Você é mais velho do que eu por {id - age} anos')
else:
    print(f'Eu sou mais velho do que você por {age - id} anos')

nota = int(input('De 0 a 100, qual foi a nota obtida? '))

if nota > 80:
    print('Parabéns, você tirou nota A')
elif nota > 70:
    print('Você tirou um B, nada mal')
elif nota > 60:
    print('Você tirou nota C, aproveite a oportunidade para estudar mais')
elif nota > 50:
    print('Você tirou nota D, talvez você não tenha entendido bem a matéria e deva falar com seu professor')
else:
    print('Você tirou nota E, talvez você não tenha entendido bem a matéria e deva falar com seu professor')

month = input('Em qual mês nós estamos? "Por favor escreva a primeira letra do mês em maiúscula" ')

if month in ['Janeiro', 'Fevereiro']:
    print('Nós estamos no Verão!')
elif month == 'Março':
    print('Podemos estar no fim do Verão ou no início do Outono')
elif month in ['Abril', 'Maio']:
    print('Nós estamos no Outono!')
elif month == 'Junho':
    print('Podemos estar no fim do Outono ou no início do Inverno')
elif month in ['Julho', 'Agosto']:
    print('Nós estamos no Inverno!')
elif month == 'Setembro':
    print('Podemos estar no fim do Inverno ou no início da Primavera')
elif month in ['Outubro', 'Novembro']:
    print('Nós estamos na Primavera!')
elif month == 'Dezembro':
    print('Podemos estar no fim da Primavera ou no início do Verão')
else:
    print('Você digitou o mês erroneamente, por favor tente novamente')

frutas = ['banana', 'maçã', 'laranja', 'limão']
print('Essa é a nossa lista de frutas para comprar:', ', '.join(frutas))

el = input("Que outra fruta você gostaria de adicionar? ")

if el in frutas:
    print('Essa fruta já está na lista, amigo')
else:
    frutas.append(el)
    print('Okay! Nossa nova lista de compras será:')
    print(', '.join(frutas))

#Nível 03, o mais impossível até agora
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

a = 'skills' in person

if a:
    b = len(person['skills']) // 2
    c = person['skills'][b]
    d = len(person['skills'])
    print(f'Essa pessoa tem {d} habilidades em seu repertório, aquela que está na mediana é {c}')
    if 'Python' in person['skills']:
        print('Essa pessoa é foda, sabe python')
    else:
        print('Essa pessoa é uma qualquer, não sabe python')
else:
    print('Essa pessoa não tem habilidades em seu repertório')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

skills = person['skills']
if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('Titulagem desconhecida')

h = person['is_marred']
i = person['country']
j = person['first_name']
k = person['last_name']

if h and i == 'Finland' :
    print(f'{j} {k} lives in {i}. He is married')

input("Pressione Enter para sair...")
