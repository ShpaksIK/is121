import os
import json
import datetime
import requests
# import asyncio

from bs4 import BeautifulSoup
import telebot
from telebot import types
# from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import pytz


# Получение данных .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

schedule_chislitel = [
    {
        "0": "",
        "1": "<u>Операционные системы и среды</u>. ДОТ. Грудкова А.Л.",
        "2": "<u>Психология общения</u>. ДОТ. Никитина А.М.",
        "3": "",
        "4": "",
    },
    {
        "0": "",
        "1": "<u>Дискретная математика с элементами алегбры логики</u>. М102. Холманова В.М.",
        "2": "<u>Психология общения</u>. Б202. Никитина А.М.",
        "3": "<u>Информационные технологии</u>. 1п/гр Б309. Кувшинова В.С. 2п/гр А407. Комиссарова О.В.",
        "4": "",
    },
    {
        "0": "<u>Основы алгоритмизации и программирования</u>. ДОТ. Королева П.Д.",
        "1": "<u>Информационные технологии</u>. ДОТ. Кувшинова В.А.",
        "2": "<u>МДК.06.01 Внедрение ИС</u>. ДОТ. Вакансия",
        "3": "",
        "4": "",
    },
    {
        "0": "<u>История</u>. А304. Свободина Н.В.",
        "1": "<u>Архитектура аппаратных средств</u>. 1п/гр Б403. Груздев В.В. 2п/гр Б204. Байдина Ю.А.",
        "2": "<u>МДК.06.01 Внедрение ИС</u>. 1п/гр, 2п/гр Б403. Пронина Л.Ю.",
        "3": "",
        "4": "",

    },
    {
        "0": "",
        "1": "<u>Основы алгоритмизации и прораммирования</u>. 1п/гр Б301. Королева П.Д. 2п/гр Б302. Неделяева Н.А.",
        "2": "<u>Физическая культура</u>. Спорт.зал. Куликова А.А.",
        "3": "<u>Основы алгоритмизации и программирования</u>. 1п/гр Б301. Королева П.Д. 2п/гр Б302. Неделяева Н.А.",
        "4": "",
    },
    {
        "0": "",
        "1": "<u>Основы финансовой грамотности</u>. М207. Белогорская Я.В.",
        "2": "<u>МДК.02.01 Технология разработки ПО</u>. 1п/гр, 2п/гр Б301. Вершинина Н.А.",
        "3": "<u>МДК.02.01 Технология разработки ПО</u>. 1п/гр, 2п/гр Б301. Вершинина Н.А.",
        "4": "",

    },
]
schedule_chislitel_copy = schedule_chislitel.copy()
schedule_znamenatel = [
    {
        "0": "<u>История</u>. ДОТ. Свободина Н.В.",
        "1": "<u>Операционные системы и среды</u>. ДОТ. Грудкова А.Л.",
        "2": "<u>Психология общения</u>. ДОТ. Никитина А.М.",
        "3": "",
        "4": "",
    },
    {
        "0": "",
        "1": "<u>Дискретная математика с элементами алегбры логики</u>. М102. Холманова В.М.",
        "2": "<u>Операционные системы и среды</u>. 1п/гр Б301. Гудкова А.Л. 2п/гр Б302. Кувшинова В.А.",
        "3": "<u>Информационные технологии</u>. 1п/гр Б309. Кувшинова В.С. 2п/гр А407. Комиссарова О.В.",
        "4": "",
    },
    {
        "0": "<u>Основы алгоритмизации и программирования</u>. ДОТ. Королева П.Д.",
        "1": "<u>Архитектура аппаратных средств</u>. ДОТ. Груздев В.В.",
        "2": "<u>МДК.06.01 Внедрение ИС</u>. ДОТ. Вакансия",
        "3": "",
        "4": "",
    },
    {
        "0": "",
        "1": "<u>Архитектура аппаратных средств</u>. 1п/гр Б403. Груздев В.В. 2п/гр Б204. Байдина Ю.А.",
        "2": "<u>МДК.06.01 Внедрение ИС</u>. 1п/гр, 2п/гр Б403. Пронина Л.Ю.",
        "3": "",
        "4": "",

    },
    {
        "0": "",
        "1": "<u>Основы алгоритмизации и прораммирования</u>. 1п/гр Б301. Королева П.Д. 2п/гр Б302. Неделяева Н.А.",
        "2": "<u>Физическая культура</u>. Спорт.зал. Куликова А.А.",
        "3": "<u>МДК.06.01 Внедрение ИС</u>. 1п/гр, 2п/гр Б302. Пронина Л.Ю.",
        "4": "",
    },
    {
        "0": "",
        "1": "<u>Основы финансовой грамотности</u>. М207. Белогорская Я.В.",
        "2": "<u>МДК.02.01 Технология разработки ПО</u>. 1п/гр, 2п/гр Б301. Вершинина Н.А.",
        "3": "<u>МДК.06.01 Внедрение ИС</u>. А403. Вакансия",
        "4": "",

    },
]
schedule_znamenatel_copy = schedule_znamenatel.copy()
dezhurstva = [
    "Пашко Д. и Мушаков М.",
    "Шахбазян Г. и Малявин Д.",
    "Баранова С. и Воронина П.",
    "Попов Д. и Рейбречук А.",
    "Третьяков А. и Клоков А.",
    "Щербатова А. и Игнашев А.",
    "Бухарева А. и Воробьёва П.",
    "Кузнецов Р. и Ножницкий Д.",
    "Тюнин М. и Муталиева К.",
    "Короткова Н. и Мартынова А.",
    "Зверева А. и Савельева Л.",
    "Панкова Д. и Калугин М.",
    "Петров С. и Осов В.",
    "Софронов М. и Неустроев М.",
    "Невиницин М. и Докторов В.",
    "Абдурозиков Р. и Пирожников Д.",
    "Иосипчук М. и Волков М."
]
days_in_numbers = {
    "Monday": [0, "понедельник"],
    "Tuesday": [1, "вторник"],
    "Wednesday": [2, "среда"],
    "Thursday": [3, "четверг"],
    "Friday": [4, "пятница"],
    "Saturday": [5, "суббота"],
    "Sunday": [6, "воскресенье"],
}

# Инициализация бота
bot = telebot.TeleBot(TOKEN)
# bot = AsyncTeleBot(TOKEN)

# Обновление состояний раз в время
# async def update_state():
#     while True:
#         await asyncio.sleep(60)
#         with open("./data.json", "r", encoding="utf-8") as jf:
#             fd = json.load(jf)
#         day_of_week = datetime.datetime.now().strftime("%A")
#         if days_in_numbers[day_of_week][0] != fd["today"]:
#             fd["today"] = days_in_numbers[day_of_week][0]
#             with open("./data.json", "w", encoding="utf-8") as jf:
#                 json.dump(fd, jf, indent=4)
#         else:
#             print("Good")

def check_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.datetime.now(moscow_tz)
    if current_time_moscow >= current_time_moscow.replace(hour=12, minute=0):
        return ">"
    return "<"

def check_week():
    url = "https://menu.sttec.yar.ru/timetable/rasp_first.html"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            page_text = soup.get_text()
            contains_znamenatel = "Знаменатель" in page_text
            contains_chislitel = "Числитель" in page_text
            if contains_znamenatel:
                return "знаменатель"
            elif contains_chislitel:
                return "числитель"
        return "не удалось выполнить запрос"
    except Exception as e:
        return e
    
def check_zameni(day="today"):
    url = "https://menu.sttec.yar.ru/timetable/rasp_first.html"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', border=1)
            rows = table.find_all('tr')[1:]
            replacements = []
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    group = cols[1].get_text(strip=True)
                    if group == "ИС1-21":
                        replacement_info = {
                            "number": cols[2].get_text(strip=True),
                            "dis_raspistanie": cols[3].get_text(strip=True),
                            "dis_zameta": cols[4].get_text(strip=True),
                            "auditory": cols[5].get_text(strip=True)
                        }
                        replacements.append(replacement_info)
            time = check_time()
            current_day = datetime.datetime.now()
            day_of_week = current_day.strftime("%A")
            check = check_week()

            if day == "today":
                if time == "<":
                    if check == "знаменатель":
                        for i in replacements:
                            schedule_znamenatel_copy[days_in_numbers.get(day_of_week)[0]][str(i["number"])] = f"<u>{i['dis_zameta']}</u>. {i['auditory']} (замена)"
                        schedule = f"<b>РАСПИСАНИЕ НА СЕГОДНЯ</b> (знаменатель, {days_in_numbers.get(day_of_week)[1]})\n\n"
                        for k, v in schedule_znamenatel_copy[days_in_numbers.get(day_of_week)[0]].items():
                            if v != "":
                                schedule += f"<b>{k} пара:</b>  {v}\n"
                    elif check == "числитель":
                        for i in replacements:
                            schedule_chislitel_copy[days_in_numbers.get(day_of_week)[0]][str(i["number"])] = f"<u>{i['dis_zameta']}</u>, {i['auditory']} (замена)"
                        schedule = f"<b>РАСПИСАНИЕ НА СЕГОДНЯ</b> (числитель, {days_in_numbers.get(day_of_week)[1]})\n\n"
                        for k, v in schedule_chislitel_copy[days_in_numbers.get(day_of_week)[0]].items():
                            if v != "":
                                schedule += f"<b>{k} пара:</b>  {v}\n"
                    else:
                        schedule = f"Ошибка получения данных:\n\n{check}"
                    with open("./data.json", "r", encoding="utf-8") as jf:
                        fd = json.load(jf)
                    fd["lastDay"] = schedule
                    with open("./data.json", "w", encoding="utf-8") as jf:
                        json.dump(fd, jf, indent=4)
                else:
                    with open("./data.json", "r", encoding="utf-8") as jf:
                        fd = json.load(jf)
                    schedule = fd["lastDay"]
                return schedule if schedule else "❌ Ошибка: нет данных ❌"
            elif day == "tomorrow":
                current_day_number = days_in_numbers[day_of_week][0]
                next_day_number = (current_day_number + 1) % 7
                next_day_name = [day for day, info in days_in_numbers.items() if info[0] == next_day_number][0]
                if check == "знаменатель":
                    if time == ">":
                        for i in replacements:
                            schedule_znamenatel[days_in_numbers[next_day_name][0]][str(i["number"])] = f"<u>{i['dis_zameta']}</u>, {i['auditory']} (замена)"
                    schedule = f"<b>РАСПИСАНИЕ НА ЗАВТРА</b> (знаменатель, {days_in_numbers[next_day_name][1]})\n\n"
                    for k, v in schedule_znamenatel[days_in_numbers[next_day_name][0]].items():
                        if v != "":
                            schedule += f"<b>{k} пара:</b>  {v}\n"
                    if time == "<":
                        schedule += "\n<i>Замен на завтра ещё нет. Обновление будет после 12:00.</i>"
                elif check == "числитель":
                    if time == ">":
                        for i in replacements:
                            schedule_chislitel[days_in_numbers[next_day_name][0]][str(i["number"])] = f"<u>{i['dis_zameta']}</u>, {i['auditory']} (замена)"
                    schedule = f"<b>РАСПИСАНИЕ НА ЗАВТРА</b> (числитель, {days_in_numbers[next_day_name][1]})\n\n"
                    for k, v in schedule_chislitel[days_in_numbers[next_day_name][0]].items():
                        if v != "":
                            schedule += f"<b>{k} пара:</b>  {v}\n"
                    if time == "<":
                        schedule += "\n<i>Замен на завтра ещё нет. Обновление будет после 12:00.</i>"
                else:
                    schedule = f"❌ Ошибка получения данных:\n\n{check}"
                return schedule
        else:
            return "❌ Ошибка получения замен ❌"
    except Exception as e:
        return f"❌ Возникла ошибка:\n{e}"
    
# Обработчик кнопки, команды "/start"
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='ПОМОЩЬ', callback_data='help')
    keyboard.add(key_yes)
    bot.send_message(message.chat.id, text=f"👋 Привет, {message.from_user.first_name}! 👋\n\nЯ бот группы ИС1-21/22 Ярославского Градостроительного Колледжа ⭐️\nСмотри замены и график дежурства здесь! 💥\nНажми \"/help\" для помощи 📗\n\nПо вопросам: @Shpaks2 или @kuertov666", reply_markup=keyboard)

# Обработчик кнопки, команды "/help"
@bot.message_handler(func=lambda message: message.text == '/help')
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/today")
    btn3 = types.KeyboardButton("/tomorrow")
    btn4 = types.KeyboardButton("/d")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Доступные команды:\n\n/today - расписание на текущий день с учетом замен.\n/tomorrow - расписание на завтрашний день с учетом замен.\n/d - график дежурства на вчера, сегодня и завтра", reply_markup=markup)

# Обработчик кнопки, команды "/today"
@bot.message_handler(func=lambda message: message.text == '/today')
def today_command(message):
    schedule = check_zameni(day="today")
    bot.send_message(message.chat.id, text=f"{schedule}", parse_mode="HTML")

# Обработчик кнопки, команды "/tomorrow"
@bot.message_handler(func=lambda message: message.text == '/tomorrow')
def tomorrow_command(message):
    schedule = check_zameni(day="tomorrow")
    bot.send_message(message.chat.id, text=f"{schedule}", parse_mode="HTML")
    
# Обработчик кнопки, команды "/d"
@bot.message_handler(func=lambda message: message.text == '/d')
def work_command(message):
    with open("./data.json", "r", encoding="utf-8") as jf:
        fd = json.load(jf)
    day_of_week = days_in_numbers[datetime.datetime.now().strftime("%A")]
    if day_of_week[0] != fd["today"]:
        fd["today"] = day_of_week[0]
        with open("./data.json", "w", encoding="utf-8") as jf:
            json.dump(fd, jf, indent=4)
    current_d = dezhurstva[fd["dezh"]-1]
    if days_in_numbers[datetime.datetime.now().strftime("%A")][0] != 6:
        bot.send_message(message.chat.id, text=f"<b>ГРАФИК ДЕЖУРСТВА</b> (сегодня, {day_of_week[1]})\n\n{current_d}", parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, text=f"<b>ГРАФИК ДЕЖУРСТВА НА ЗАВТРА</b> (понедельник)\n\n{current_d}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/help")
        btn2 = types.KeyboardButton("/today")
        btn3 = types.KeyboardButton("/tomorrow")
        btn4 = types.KeyboardButton("/d")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(call.message.chat.id, text="Доступные команды:\n\n/today - расписание на текущий день с учетом замен.\n/tomorrow - расписание на завтрашний день с учетом замен.\n/d - график дежурства на вчера, сегодня и завтра", reply_markup=markup)


# Запуск бота
bot.polling(none_stop=True, interval=0)
# async def main():
#     asyncio.create_task(update_state())
#     await bot.polling(none_stop=True, interval=0)

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
