from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("🔙Назад")
btnMenu = KeyboardButton("Главная страница")

#----- Main menu ---
btnAll = KeyboardButton("Показать все скидки")
btnSettings = KeyboardButton("⚙Настройки")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAll, btnSettings)

#---settings ---

btnBrand = KeyboardButton("Выбрать бренд")
btnHigh_price = KeyboardButton("Макс. цена")
btnHigh_sale = KeyboardButton("Мин. скидка")
btnCards = KeyboardButton("Макс. кол-во карточек")
settingsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBrand, btnHigh_price, btnHigh_sale, btnCards, btnMenu)

#---brand ---
btnAdidas = KeyboardButton("Adidas")
btnAsosDsgn = KeyboardButton("Asos")
btnNike = KeyboardButton("Nike")
btnAdidasOrgn = KeyboardButton("Adidas Originals")
brandMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAdidas, btnAdidasOrgn,
                                                          btnNike, btnAsosDsgn, btnMain)

#---max price ---
first_price = KeyboardButton("4000")
second_price = KeyboardButton("7000")
third_price = KeyboardButton("12000")
any_price = KeyboardButton("Без ограничения")
priceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(first_price, second_price, third_price, any_price, btnMain)

#---min sale---
first_sale = KeyboardButton("10%")
second_sale = KeyboardButton("30%")
third_sale = KeyboardButton("50%")
saleMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(first_sale, second_sale, third_sale, btnMain)

#---max--cards
first_cards = KeyboardButton("5")
second_cards = KeyboardButton("15")
third_cards = KeyboardButton("30")
cardsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(first_cards, second_cards, third_cards, btnMain)