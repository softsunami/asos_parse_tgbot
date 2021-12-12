from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
import markup as mp
from casos_parse import collect_data
import json
import time
import config as cfg

token = "5068744934:AAFdFDTtcCOG_dmxE6x7seLmSK6pad3T-Sw"
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
whois_list = []


@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, я бот, который отслеживает скидки на кроссовки."
                                                 "Перед запуском бота в настройках необходимо "
                                                 "указать параметры\n\nПараметры по умолчанию:\n"
                                                 "Максимальная цена - 30000 рублей\n"
                                                 "Поиск по бренду - Adidas\n"
                                                 "Минимальная скидка - 10%\n"
                                                 "Максимальное количество карточек - 15 штук",
                           reply_markup=mp.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    try:

        print(
            message.from_user.last_name,
            message.from_user.first_name,
            message.from_user.username,
            "\n"
        )
    finally:
        pass
    if message.text == "Показать все скидки":
        await message.answer("Ищу выгодные предложения...")
        collect_data(cfg.max_price, cfg.id_dict[cfg.brand])

        with open("result.json", encoding="utf-8") as file:
            data = json.load(file)
        count = 0
        for index, item in enumerate(data):
            if item.get("sale") >= cfg.min_sale:
                card = f'{hlink(item.get("full_name"), item.get("url"))}\n' \
                       f'{hbold("🔥Скидка: ")}{str(item.get("sale")) + "%"}\n' \
                       f'{hbold("💲Стоимость со скидкой: ")} {item.get("current_price")}'
                count += 1
                if index % 10 == 0:
                    time.sleep(3)
                if count <= cfg.max_cards and card is not None:
                    await message.answer(card)
        if count == 0:
            await message.answer("Скидок по таким критериям нет")

    elif message.text == "🔙Назад":  # Ready
        await bot.send_message(message.from_user.id, "Назад", reply_markup=mp.settingsMenu)
    # Settings -----------------------------------------------------------
    elif message.text == "⚙Настройки":
        await bot.send_message(message.from_user.id, "⚙Настройки", reply_markup=mp.settingsMenu)
    # Settings_Brand -----------------------------------------------------------
    elif message.text == "Выбрать бренд":
        await bot.send_message(message.from_user.id, "🔎Выброр бренда", reply_markup=mp.brandMenu)

    elif message.text == "Adidas":
        await bot.send_message(message.from_user.id, "✔Выбрано")
        cfg.brand = "adidas"

    elif message.text == "Nike":
        await bot.send_message(message.from_user.id, "✔Выбрано")
        cfg.brand = "Nike"

    elif message.text == "Adidas Originals":
        await bot.send_message(message.from_user.id, "✔Выбрано")
        cfg.brand = "adidas Originals"

    elif message.text == "New balance":
        await bot.send_message(message.from_user.id, "✔Выбрано")
        cfg.brand = "New Balance"
    # Settings_Price -----------------------------------------------------------
    elif message.text == "Макс. цена":
        await bot.send_message(message.from_user.id, "Выберите максимальную цену", reply_markup=mp.priceMenu)

    elif message.text == "4000":
        cfg.max_price = int(message.text)
        await bot.send_message(message.from_user.id, "Установлена максимальная цена - 4000")
    elif message.text == "7000":
        cfg.max_price = int(message.text)
        await bot.send_message(message.from_user.id, "Установлена максимальная цена - 7000")
    elif message.text == "12000":
        cfg.max_price = int(message.text)
        await bot.send_message(message.from_user.id, "Установлена максимальная цена - 12000")
    elif message.text == "Без ограничения":
        cfg.max_price = 30000
        await bot.send_message(message.from_user.id, "Нет ограничения по цене")
    # Settings_Sale -----------------------------------------------------------
    elif message.text == "Мин. скидка":
        await bot.send_message(message.from_user.id, "Выберите минимальную скидка", reply_markup=mp.saleMenu)
    elif message.text == "10%":
        await bot.send_message(message.from_user.id, "✔Выбрано", reply_markup=mp.saleMenu)
        cfg.min_sale = 10
    elif message.text == "30%":
        await bot.send_message(message.from_user.id, "✔Выбрано", reply_markup=mp.saleMenu)
        cfg.min_sale = 30
    elif message.text == "50%":
        await bot.send_message(message.from_user.id, "✔Выбрано", reply_markup=mp.saleMenu)
        cfg.min_sale = 50
    # Settings_maxcards
    elif message.text == "Макс. кол-во карточек":
        await bot.send_message(message.from_user.id, "Выберите максимальное количество карточек",
                               reply_markup=mp.cardsMenu)
    elif message.text == "5":
        cfg.max_cards = 5
    elif message.text == "15":
        cfg.max_cards = 15
    elif message.text == "30":
        cfg.max_cards = 30
    # Home page
    elif message.text == "Главная страница":
        await bot.send_message(message.from_user.id, "Главная страница", reply_markup=mp.mainMenu)
    else:
        await message.reply("Неизвестная команда")


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    print("Бот запущен...")
    main()
