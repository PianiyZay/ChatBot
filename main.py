from random import randint
import telebot

db_soup = [
    dict(name='Борщ', рецепт='Какой-то рецепт'),
    dict(name='Солянка', рецепт='Какой-то рецепт'),
    dict(name='Гороховый суп', рецепт='Какой-то рецепт')
]

rand_index = randint(0, 2)
print(db_soup[2]['name'] + '\n' + db_soup[2]['рецепт'])
