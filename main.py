import telebot, random
from telebot import types
api_key = "5250140838:AAESlhD0oNVmUzpfJVY_pceJ8oqevRxWVOM"
bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=["start"])
def start(m, res=False):
  bot.send_message(m.chat.id, 'Hi! My name is Eglishik and I will help you learn English quickly and easily! Where do you want to start?')
  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1=types.KeyboardButton("Vocabulary practice")
  item2=types.KeyboardButton("Grammar practice")
  item3=types.KeyboardButton("Theory")
  item4=types.KeyboardButton("Help")
  markup.add(item1)
  markup.add(item2)
  markup.add(item3)
  markup.add(item4)
  bot.send_message(m.chat.id, 'Pick a category and let’s go! ?? ',  reply_markup=markup)

vocabulary_list = ['Food??', 'Clothes??', 'Sport???????', 'Hobbies??', 'Verbs????', 'School??', 'Animals??', 'Emothions??', 'Appereance????????', 'House and Decor??']
theory_list =  ['Tenses', 'Modal verbs', 'Irregular verbs']
grammar_list = ['Present Simple', 'Past Simple', 'Future Simple' ]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Vocabulary practice":
    keyboard = types.InlineKeyboardMarkup()
    for vocabulary in vocabulary_list:
      key = types.InlineKeyboardButton(text= vocabulary, callback_data = vocabulary)
      keyboard.add(key)
    bot.send_message(message.from_user.id, text ="Choose the category of words you want to learn!", reply_markup=keyboard)

  if message.text == "Grammar practice":
    keyboard = types.InlineKeyboardMarkup()
    for grammar in grammar_list:
      key = types.InlineKeyboardButton(text=grammar, callback_data='Grammar practice' + grammar)
      keyboard.add(key)
    bot.send_message(message.from_user.id, text ="Choose the grammar category in which you want to practice! We advise you to study the theory first! (For now, you can only practice these tenses)", reply_markup=keyboard)

  if message.text == "Help":
    bot.send_message(message.from_user.id, text ="How are you doing? Is everything working out for you? \n \nWith me you can increase your English vocabulary , practice grammar and learn a lot! ??\n \nIf you have any questions, suggestions or if anything doesn't work, contact us at englishik.bot@mail.ru")

  if message.text == "Theory":
    keyboard = types.InlineKeyboardMarkup()
    for theory in theory_list:
      key = types.InlineKeyboardButton(text= theory, callback_data = theory)
      keyboard.add(key)
    bot.send_message(message.from_user.id, text ="What theory do you want to know? ??", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if "Irregular verbs" in call.data.strip():
      bot.send_message(call.message.chat.id, text="This is a table for repeating irregular verbs!")
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/bot/0v.jpeg', 'rb'))
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/bot/1v.jpeg', 'rb'))
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/bot/2v.jpeg', 'rb'))
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/bot/3v.jpeg', 'rb'))
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/bot/4v.jpeg', 'rb'))
    if "Modal verbs" in call.data.strip():
      bot.send_message(call.message.chat.id, text="This is a table of modal verbs!")
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/1600.jpg', 'rb'))
    if call.data == "Tenses" :
      keyboard = types.InlineKeyboardMarkup()
      key1 = types.InlineKeyboardButton(text='Table of English Tenses', callback_data='Table of English Tenses')
      key2 = types.InlineKeyboardButton(text='Uses of Tenses', callback_data='Uses of Tenses')
      keyboard.add(key1)
      keyboard.add(key2)
      bot.send_message(call.message.chat.id, text= "What exactly do you want to know?", reply_markup=keyboard)
    if call.data == "Table of English Tenses":
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/10.png', 'rb'))
    if call.data == "Uses of Tenses":
      bot.send_photo(chat_id=call.message.chat.id, photo=open('/content/drive/MyDrive/11.jpg', 'rb'))

    if "Present Simple" in call.data.strip():
      bot.send_message(call.message.chat.id, text="Put the verbs in the following sentences in the affirmative, question, and negative forms of Present Simple")
      # bot.send_message(call.message.chat.id, text="1. I (to do) morning exercises.")
      # while message.text != "do" or 'Do':
      #   bot.send_message(call.message.chat.id, text="Try again!")
      
            # if message.text == "works" or 'Works':
            #   bot.send_message(call.message.chat.id, text="2. He (to work) at a factory.")



    # if "Food" in call.data.strip():
    #   @bot.message_handler(content_types=['text'])
    #   @bot.poll_answer_handler(func=lambda message: True)
    #   async def handle_poll_answer(quiz_answer: PollAnswer):
    #     my_quiz = await bot.send_poll(message.chat.id, '??????????, ????? ???????? ????? ?????', ['Telegram', 'Viber', 'WhatsApp', 'Messenger'], type='quiz', correct_option_id=0, is_anonymous=False)
    #     if my_quiz.poll.correct_option_id == quiz_answer.option_ids[0]:
    #       await bot.send_message(quiz_answer.user.id, '?????????! ???? ??????')
    #     else:
    #       await bot.sned_message(quiz_answer.user.id, '????, ?? ??? ???????????? ?????. ????????? ?????? - ????? ????? ???????')

    #       await bot.send_poll(message.chat.id, '??????????, ????? ???????? ????? ?????', ['Telegram', 'Viber', 'WhatsApp', 'Messenger'], type='quiz', correct_option_id=0, is_anonymous=False)

    # keyboard = types.InlineKeyboardMarkup()
    
      
      # key1 = types.InlineKeyboardButton(text='??', callback_data='yes_delete')
      # key2 = types.InlineKeyboardButton(text='???', callback_data='no_delete')
      
      # keyboard.add(key1)
      # keyboard.add(key2)
      # bot.send_message(call.message.chat.id, text="You chose the food category ??! Let's begin our training")
      # bot.send_message(call.message.chat.id, text="Choose the correct translation of this word", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)