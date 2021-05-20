from random import randint
import telebot

bot = telebot.TeleBot('1756397257:AAGjqG33JvOhj6AgIsrrp7KzE2cLFRyioSM')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

db_soup = [
    dict(name='Борщ', рецепт='Какой-то рецепт'),
    dict(name='Солянка', рецепт='Какой-то рецепт'),
    dict(name='Гороховый суп', рецепт='Какой-то рецепт')
]

rand_index = randint(0, 2)
print(db_soup[2]['name'] + '\n' + db_soup[2]['рецепт'])

bot.polling(none_stop=True)