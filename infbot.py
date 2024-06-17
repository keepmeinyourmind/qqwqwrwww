import asyncio
import logging
from settings import BOT_TOKEN as Token

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram import F

from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


dp = Dispatcher()
link1 = f"https://obuchonok.ru/node/1160"
text1 = "Русский язык"
link2 = f"https://obuchonok.ru/node/1175"
text2 = "Обществознание"
link3 = f"https://obuchonok.ru/node/1124"
text3 = "Физика"
link4 = f"https://obuchonok.ru/node/444"
text4 = "Биология"
link5 = f"https://obuchonok.ru/node/1174"
text5 = "Психилогия"
link6 = f"https://obuchonok.ru/node/431"
text6 = "Математика"
link7 = f"https://obuchonok.ru/node/1118"
text7 = "Английский язык"
link8 = f"https://obuchonok.ru/node/1122"
text8 = "Химия"
link9 = f"https://obuchonok.ru/node/440"
text9 = "Информатика"

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text="Обрабатываю, ждите...")
    await message.answer(text=f'Здравствуйте, {message.from_user.full_name}, чем я могу Вам помочь?\n'
                            f'Чтобы узнать о моих возможностях, введите /help')


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="Обрабатываю, ждите...")
    await message.answer(text='Вот список доступных команд:\n'
                            '/presentation - Здесь я подскажу Вам, как правильно оформить презентацию к проекту\n'
                            '/themes - Здесь я предложу Вам на выбор предметы для проекта, которые я считаю самыми актуальными и интересными\n'
                            '/documentation - При отправке этой команды я скажу Вам, как требуется оформлять доклад к проекту')


@dp.message(Command("presentation"))
async def handle_presentation(message: types.Message):
    await message.answer(text="Обрабатываю, ждите...")
    await message.answer(text = 'Правила оформления презентации:\n'
                                '- Презентация не должна превышать 15 слайдов.\n'
                                '- Титульный лист должен включать:\n'
                                '   • полное наименование образовательной организации;\n'
                                '   • сведения об авторе и руководителе проекта;\n'
                                '   • год разработки проекта\n'
                                '- Текст слайдов должен быть кратким, читаемым, максимально информативным и содержать основную информацию по всем разделам проекта, расположенную в порядке представления каждого раздела.\n'
                                '- Слайды должны быть оформлены в едином стиле.\n'
                                '- Презентация может содержать иллюстрации, графики, схемы, таблицы, с лаконичным использованием анимационных и цветовых эффектов.')


@dp.message(Command("themes"))
async def handle_themes(message: types.Message):
    await message.answer(text="Обрабатываю, ждите...")
    await message.answer(text = "Вот список предметов, которые, по моему мнениию, являются самыми интересными для проекта:(При нажатии на название предмета открывается сайт с темами)\n"
                                f"• <a href=\"{link1}\">{text1}</a>\n"
                                f"• <a href=\"{link2}\">{text2}</a>\n"
                                f"• <a href=\"{link3}\">{text3}</a>\n"
                                f"• <a href=\"{link4}\">{text4}</a>\n"
                                f"• <a href=\"{link5}\">{text5}</a>\n"
                                f"• <a href=\"{link6}\">{text6}</a>\n"
                                f"• <a href=\"{link7}\">{text7}</a>\n"
                                f"• <a href=\"{link8}\">{text8}</a>\n"
                                f"• <a href=\"{link9}\">{text9}</a>\n"
                                f"Если это не помогло, введите /info", parse_mode="html")


@dp.message(Command("documentation"))
async def handle_documentation(message: types.Message):
    await message.answer(text="Обрабатываю, ждите...")
    await message.answer(text="Для правильного оформления доклада следуйте этим правилам:\n"
                            "• Текст печатается на одной стороне листа белой бумаги формата A4\n"
                            "• Междустрочный интервал может быть равен 1 или 1.15\n"
                            "• Шрифт должен быть начертания Times New Roman и выровнен по ширине\n"
                            "• Кавычки должны быть вида «кавычки-елочки»\n"
                            "• Нумерация страниц:\n"
                            "             -арабскими цифрами\n"
                            "             -сквозная, от титульного листа, при этом номер страницы на титульном листе не проставляют\n"
                            "             -проставляется со второй страницы\n"
                            "             -порядковый номер страницы ставится внизу по середине строки")


@dp.message(Command("info", prefix="!/"))
async def buttons(message: types.Message):
    button1 = InlineKeyboardButton(text = "Посмотреть интересные проекты",
                                url="https://obuchonok.ru/klass/proekt/10",)
    button2 = InlineKeyboardButton(text = "Сайт с алгоритмом выбора темы",
                                url="https://workproekt.ru/temy-proektov/kak-vyibrat-temu-proektnoy-rabotyi/",)
    button3 = InlineKeyboardButton(text = "Я так и не смог выбрать😥", callback_data="unluck")
    row1 = [button1]
    row2 = [button2]
    row3 = [button3]
    rows = [row1,
            row2,
            row3,]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text = "В таком случае могу предложить такие варианты",
        reply_markup = markup,
    )


@dp.callback_query(F.data == "unluck")
async def call(callback: CallbackQuery):
    await callback.message.answer("Если уж все так сложно, то попробуйте поспрашивать у других ребят, как они подходили к выбору предмета и темы, может быть они Вам подскажут")
    await callback.message.answer(f"Спасибо за то, что обратились ко мне! Если возникнут еще вопросы, напишите \"Помоги мне!\"")


@dp.message()
async def messaging(message: types.Message):
    btn1 = InlineKeyboardButton(text = "Я не могу определиться с предметом", callback_data="theme")
    btn2 = InlineKeyboardButton(text = "Какие требования к докладу?", callback_data="doklad")
    btn3 = InlineKeyboardButton(text = "Какие требования к презентации?", callback_data="preza")
    rw1 = [btn1]
    rw2 = [btn2]
    rw3 = [btn3]
    rws = [rw1,
        rw2,
        rw3]
    mrkp = InlineKeyboardMarkup(inline_keyboard=rws)
    if message.text.lower() == 'помоги мне!':
        await message.answer(text="Чем я могу вам помочь?", reply_markup=mrkp)


@dp.callback_query(F.data == "theme")
async def theme(callback: CallbackQuery):
    bt2 = InlineKeyboardButton(text = "Да, давайте", callback_data="yes")
    r2 = [bt2]
    rs = [r2]
    mrkup = InlineKeyboardMarkup(inline_keyboard=rs)
    await callback.message.answer("Чтож, давайте проведем небольшой тест, и мы поймем какой предмет Вам подходит", reply_markup=mrkup)


@dp.callback_query(F.data == "doklad")
async def document(callback: CallbackQuery):
    b1 = InlineKeyboardButton(text = "Я не могу определиться с предметом", callback_data="theme")
    b3 = InlineKeyboardButton(text = "Какие требования к презентации?", callback_data="preza")
    ro1 = [b1]
    ro3 = [b3]
    ros = [ro1,
        ro3]
    mrk = InlineKeyboardMarkup(inline_keyboard=ros)
    await callback.message.answer("Введиие команду /documentation, и я подскажу Вам как правильно оформить доклад", reply_markup=mrk)


@dp.callback_query(F.data == "preza")
async def preza(callback: CallbackQuery):
    btt1 = InlineKeyboardButton(text = "Я не могу определиться с предметом", callback_data="theme")
    btt2 = InlineKeyboardButton(text = "Какие требования к докладу?", callback_data="doklad")
    rs1 = [btt1]
    rs2 = [btt2]
    rss = [rs1,
        rs2]
    mrp = InlineKeyboardMarkup(inline_keyboard=rss)  
    await callback.message.answer("Введите /presentation, и я подскажу Вам, что нужно сделать, чтобы правильно оформить Вашу презентацию", reply_markup=mrp)


@dp.callback_query(F.data == "yes")
async def test(callback: CallbackQuery):
    btn11 = InlineKeyboardButton(text = "Гуманитарные", callback_data="gum")
    btn12 = InlineKeyboardButton(text = "Технические", callback_data="tech")
    btn13 = InlineKeyboardButton(text = "Хим-Био", callback_data = "bio")
    ryad1 = [btn11]
    ryad2 = [btn12]
    ryad3 = [btn13]
    ryadi = [ryad1,
            ryad2,
            ryad3]
    mrkp1 = InlineKeyboardMarkup(inline_keyboard=ryadi)
    await callback.message.answer(f"Давай начнем.\n"
                                "Какая область предметов Вам нравится больше?", reply_markup=mrkp1)
    
@dp.callback_query(F.data == "gum")
async def gumanitariy(callback: CallbackQuery):
    button11 = InlineKeyboardButton(text = "Языковые", callback_data="lang")
    button12 = InlineKeyboardButton(text = "Социологические", callback_data="social")
    rd1 = [button11]
    rd2 = [button12]
    rds = [rd1, 
        rd2]
    mrkp2 = InlineKeyboardMarkup(inline_keyboard=rds)
    await callback.message.answer("Теперь нужно выбрать, какая сфера гуманитарных предметов Вас больше интересует", reply_markup=mrkp2)


@dp.callback_query(F.data == "lang")
async def languages(callback: CallbackQuery):
    bttn1 = InlineKeyboardButton(text = "Родной", callback_data="rodnoy")
    bttn2 = InlineKeyboardButton(text = "Иностранный", callback_data="foreign")
    ryd1 = [bttn1]
    ryd2 = [bttn2]
    rydi = [ryd1,
            ryd2]
    mrkp3 = InlineKeyboardMarkup(inline_keyboard=rydi)
    await callback.message.answer("А сейчас скажите мне, какой язык Вам больше нравится?", reply_markup=mrkp3)


@dp.callback_query(F.data == "rodnoy")
async def rodnoy(callback: CallbackQuery):
    bn1 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l1 = [bn1]
    t1 = [l1]
    mrkp_R = InlineKeyboardMarkup(inline_keyboard=t1)
    await callback.message.answer(f"Вам точно подойдет Русский язык! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link1}\">{text1}</a>", reply_markup=mrkp_R, parse_mode="html")

@dp.callback_query(F.data == "foreign")
async def foreign(callback: CallbackQuery):
    knopka1 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l2 = [knopka1]    
    t2 = [l2]
    mrkp_F = InlineKeyboardMarkup(inline_keyboard=t2)
    await callback.message.answer(f"Вам точно подойдет Английский язык! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link7}\">{text7}</a>", reply_markup=mrkp_F, parse_mode="html")


@dp.callback_query(F.data == "social")
async def social(callback: CallbackQuery):
    knopka11 = InlineKeyboardButton(text="Психическая деятельность человека", callback_data="psycho")
    knopka12 = InlineKeyboardButton(text="Жизнь общества", callback_data="obsch")
    l31 = [knopka11]
    l32 = [knopka12]
    t3 = [l31, 
        l32]
    mrkpp = InlineKeyboardMarkup(inline_keyboard=t3)
    await callback.message.answer("Что Вам больше нравится изучать?", reply_markup=mrkpp)


@dp.callback_query(F.data == "psycho")
async def psycho(callback: CallbackQuery):
    knopka111 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l311 = [knopka111]
    t31 = [l311]
    mrkp_P = InlineKeyboardMarkup(inline_keyboard=t31)
    await callback.message.answer(f"Вам точно подойдет Психология! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link5}\">{text5}</a>", reply_markup=mrkp_P, parse_mode="html")


@dp.callback_query(F.data == "obsch")
async def obsch(callback: CallbackQuery):
    knopka112 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l321 = [knopka112]
    t32 = [l321]
    mrkp_O = InlineKeyboardMarkup(inline_keyboard=t32)
    await callback.message.answer(f"Вам точно подойдет Обществознание! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link2}\">{text2}</a>", reply_markup=mrkp_O, parse_mode="html")


@dp.callback_query(F.data == "tech")
async def techo(callback: CallbackQuery):
    knopka21 = InlineKeyboardButton(text = "Логические, с работой с компьютером", callback_data="logical")
    knopka22 = InlineKeyboardButton(text = "C формулами и расчётами", callback_data="sum")
    l4_1 = [knopka21]
    l4_2 = [knopka22]
    t4 = [l4_1,
        l4_2]
    mrkp_4 = InlineKeyboardMarkup(inline_keyboard=t4)
    await callback.message.answer("Теперь надо определиться со сферой", reply_markup=mrkp_4)


@dp.callback_query(F.data == "logical")
async def logical(callback: CallbackQuery):
    knopka211 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l4_11 = [knopka211]
    t41 = [l4_11]
    mrkp_inf = InlineKeyboardMarkup(inline_keyboard=t41)
    await callback.message.answer(f"Вам точно подойдет Информатика! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link9}\">{text9}</a>", reply_markup=mrkp_inf, parse_mode="html")


@dp.callback_query(F.data == "sum")
async def sum(callback: CallbackQuery):
    knopka221 = InlineKeyboardButton(text = "С математическими формулами и расчётами", callback_data="math")
    knopka222 = InlineKeyboardButton(text = "С физическими формулами и расчётами", callback_data="physics")
    l5_1 = [knopka221]
    l5_2 = [knopka222]
    t5 = [l5_1,
        l5_2]
    mrkp_sum = InlineKeyboardMarkup(inline_keyboard=t5)
    await callback.message.answer("Выберите, какой вид расчётов вам нравится больше", reply_markup=mrkp_sum)


@dp.callback_query(F.data == "math")
async def math(callback: CallbackQuery):
    knopka231 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l5_11 = [knopka231]
    t5_1 = [l5_11]
    mrkp_M = InlineKeyboardMarkup(inline_keyboard=t5_1)
    await callback.message.answer(f"Вам точно подойдет Математика! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link6}\">{text6}</a>", reply_markup=mrkp_M, parse_mode="html")


@dp.callback_query(F.data == "physics")
async def physics(callback: CallbackQuery):
    knopka232 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l5_12 = [knopka232]
    t5_2 = [l5_12]
    mrkp_Phys = InlineKeyboardMarkup(inline_keyboard=t5_2)
    await callback.message.answer(f"Вам точно подойдет Физика! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link3}\">{text3}</a>", reply_markup=mrkp_Phys, parse_mode="html")


@dp.callback_query(F.data == "bio")
async def bio(callback: CallbackQuery):
    knopka61 = InlineKeyboardButton(text = "Химическое строение организмов", callback_data="chemistry")
    knopka62 = InlineKeyboardButton(text = "Аспекты жизни организмов", callback_data="biology")
    l6_1 = [knopka61]
    l6_2 = [knopka62]
    t6_1 = [l6_1,
            l6_2]
    mrkp_CB = InlineKeyboardMarkup(inline_keyboard=t6_1)
    await callback.message.answer("Давайте определимся, что вам интереснее изучать", reply_markup=mrkp_CB)


@dp.callback_query(F.data == "chemistry")
async def chemistry(callback: CallbackQuery):
    knopka611 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l6_11 = [knopka611]
    t6_11 = [l6_11]
    mrkp_Chem = InlineKeyboardMarkup(inline_keyboard=t6_11)
    await callback.message.answer(f"Вам точно подойдет Химия! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link8}\">{text8}</a>", reply_markup=mrkp_Chem, parse_mode="html")        


@dp.callback_query(F.data == "biology")
async def chemistry(callback: CallbackQuery):
    knopka612 = InlineKeyboardButton(text = "Спасибо!!", callback_data="thanks")
    l6_12 = [knopka612]
    t6_12 = [l6_12]
    mrkp_Chem = InlineKeyboardMarkup(inline_keyboard=t6_12)
    await callback.message.answer(f"Вам точно подойдет Биология! Вот некоторые темы, которые могут быть Вам интересны: <a href=\"{link4}\">{text4}</a>", reply_markup=mrkp_Chem, parse_mode="html")


@dp.callback_query(F.data == "thanks")
async def thanks(callback: CallbackQuery):
    await callback.message.answer("Всегда рад Вам помочь!🤗")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())