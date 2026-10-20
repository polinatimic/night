import telebot
from telebot import types

TOKEN = '8771077414:AAGW9BE1Xb3bZUSbcUqvPSNFemJW33TWGpI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "🌸 Привет, любимый! 🌸\n\n"
        "Добро пожаловать в твоё личное *Меню на ночь*.\n"
        "Валюта здесь — поцелуи 💋\n\n"
        "Твой баланс: *БЕЗЛИМИТ* ♾️\n\n"
        "Выбирай, что тебе хочется, и я всё устрою:"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('🍕 Вкусная еда — 3 поцелуя', callback_data='order_food'))
    markup.add(types.InlineKeyboardButton('💆‍♀️ Массаж спины (10 мин) — 5 поцелуев', callback_data='order_massage'))
    markup.add(types.InlineKeyboardButton('💅 Массаж рук (5 мин) — 5 поцелуев', callback_data='order_hands'))
    markup.add(types.InlineKeyboardButton('🚿 Совместный душ — 5 поцелуев', callback_data='order_shower'))
    markup.add(types.InlineKeyboardButton('🎬 Фильм (выбираешь ты) — 5 поцелуев', callback_data='order_movie_he'))
    markup.add(types.InlineKeyboardButton('🍿 Фильм (выбираю я) — 2 поцелуя', callback_data='order_movie_she'))
    markup.add(types.InlineKeyboardButton('✨ Исполнить одно желание — 5 поцелуев', callback_data='order_wish'))
    markup.add(types.InlineKeyboardButton('🤚 Чесание головы — 3 поцелуя', callback_data='order_head'))
    markup.add(types.InlineKeyboardButton('🤭 Щекочу тебя 15 секунд — 20 поцелуев', callback_data='order_tickle'))
    
    markup.add(types.InlineKeyboardButton('💌 Сказать комплимент (и получить поцелуй)', callback_data='compliment'))
    
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')

# --- НАЧАЛО ЧАСТИ 2 ---
@bot.callback_query_handler(func=lambda call: call.data.startswith('order_'))
def handle_order(call):
    bot.answer_callback_query(call.id, text="Заказано! Жду оплату поцелуями 💋")
    
    item_names = {
        'order_food': 'Еду',
        'order_massage': 'Массаж спины',
        'order_hands': 'Массаж рук',
        'order_shower': 'Совместный душ',
        'order_movie_he': 'Фильм (твой выбор)',
        'order_movie_she': 'Фильм (мой выбор)',
        'order_wish': 'Исполнение желания',
        'order_head': 'Чесание головы',
        'order_tickle': 'Щекотку 15 секунд'
    }
    
    item_name = item_names.get(call.data, 'Пункт')
    text = f"✅ *Заказано!* {item_name}.\n\nЯ уже готовлюсь. Жду оплату поцелуями! 💋"
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'compliment')
def handle_compliment(call):
    bot.answer_callback_query(call.id)
    msg = bot.send_message(call.message.chat.id, "Напиши мне комплимент, и я дам тебе поцелуй в подарок 💌:")
    bot.register_next_step_handler(msg, process_compliment)

def process_compliment(message):
    kiss = "💋"
    text = (
        f"✨ *Комплимент принят!* ✨\n\n"
        f"«{message.text}»\n\n"
        f"+1 поцелуй тебе в подарок! {kiss}\n"
        f"*Твой баланс всё ещё БЕЗЛИМИТ ♾️*"
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

print("Бот 'Меню на ночь' запущен...")
bot.infinity_polling()
