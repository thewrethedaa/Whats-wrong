from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
trainer = ListTrainer(ChatBot)

for files in os.listdir('C:\Users\andre\gunthercox-chatterbot-corpus-071ebf2\chatterbot_corpus\data\english'):
    data = open('C:\Users\andre\gunthercox-chatterbot-corpus-071ebf2\chatterbot_corpus\data\english' + files , 'r').readlines()
    bot.train(data)

while True:
    message = input ('You: ')
    if message.strip() != 'Bye ':
        reply = bot.get_response(message)
        print('ChatBot :', reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')