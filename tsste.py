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
