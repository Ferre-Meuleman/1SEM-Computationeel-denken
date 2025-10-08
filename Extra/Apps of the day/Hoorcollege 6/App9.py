films = [
    {'name': "Monty Python and the Holy Grail",             'score': [ 9, 10, 9.5, 8.5, 3, 7.5 ,8 ] },
    {'name': "Monty Python ' s Life of Brian",              'score': [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]},
    {'name': "Monty Python ' s Meaning of Life",            'score': [ 7, 6, 5 ] },
    {'name': "And Now For Something Completely Different",  'score': [ 6, 5, 6, 6 ]}
]

for film in films:
    name = film['name']
    score = sum(film['score'])/len(film['score'])
    
    print(f"The film: {name} scored: {score:.1f}/10")