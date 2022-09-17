import config
import logging
import DateTime
import numpy as np
import markups as nav
import glob, os, os.path
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types.message import ContentType, ContentTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql_1 import Databasee
from aiogram.types import ReplyKeyboardRemove
from main import pie, all_bar_all, koment_bar


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
db = Databasee('db_astrum (3).db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Yonalshingizni tanlang', reply_markup=nav.direction)
    else:
        await bot.send_message(message.from_user.id, "Salom :)", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='ds')
async def ds(message: types.CallbackQuery):
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'ds')
        db.set_signup(message.from_user.id, 'done')
        user_id = message.message.from_user.id
        await message.message.delete()
        await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                               reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='fs')
async def fs(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.mainMenu)
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'fs')
        db.set_signup(message.from_user.id, 'done')


@dp.callback_query_handler(text='se')
async def se(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.mainMenu)
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'se')
        db.set_signup(message.from_user.id, 'done')

# =========================================== MENTORS ==================================================================


@dp.callback_query_handler(text='m1')
async def m1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, 'Azodov Sarvar')
    bir = 1
    if db.get_limit(message.from_user.id) >= bir:
        await bot.send_message(message.from_user.id, 'Bugun cheklovdan oshib ketdi')
    else:
        await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)
        db.add_lim(message.from_user.id, 1)


@dp.callback_query_handler(text='m2')
async def m2(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Olloyorov Sirojiddin")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m3')
async def m3(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, 'Rasulov Rahmatulloh')
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m4')
async def m4(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Shomurodov Sarvarbek")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m5')
async def m5(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Shukurov Jasur")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m6')
async def m6(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Azizova Aziza")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m7')
async def m7(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Arslanova Nodira")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m8')
async def m8(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor("Alimbayeva Asalbonu")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m9')
async def m9(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, "Orifjonov Abdulaziz")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)

# ====================================----COMENT----======================================================


@dp.callback_query_handler(text='bad')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.bad_comment)


@dp.callback_query_handler(text='good')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.good_comment)


@dp.callback_query_handler(text='great')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.great_comment)

# ====================================================================================================================


@dp.callback_query_handler(text='bc1')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    time = datetime.now()
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.date_time(message.from_user.id, time)
    db.add_qoniqarsiz(message.from_user.id, "Mentor o'z vaqtida ish joyida yo'q")
    # db.add_users(message.from_user.id, time)
    # db.add_users(message.from_user.id, "Mentor o'z vaqtida ish joyida yo'q")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='bc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor umuman yordam bera olmadi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='bc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor yordam berishdan bosh tortdi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc1')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor ish joyiga kech keldi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor savolimga toliq jovob berolmadi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor javob berdi ammo muomilasizlik blan")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc1')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor o'z vaqtida ish joyida")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor barcha savoimga javob berdi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor juda ham yaxshi tushuntirdi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc4')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_users(message.from_user.id)
    db.add_qoniqarsiz(message.from_user.id, "Mentor yangicha va qiziqarli usulda taqdimot qilib tushuntirdi")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)

# ========================================== ADMIN ===================================================================

@dp.message_handler(commands=['admin'])
async def admin_system(message: types.Message):
    await bot.send_message(message.from_user.id, 'Please enter password')


@dp.callback_query_handler(text='adm_m')
async def admin_system(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    all_bar_all()
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/all_plots.png', 'rb')
    await message.message.delete()
    await bot.send_photo(message.from_user.id, img, 'Barcha mentorlarni analitikasi', reply_markup=nav.adm_menu)
    #await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.amentors)
    pass


@dp.callback_query_handler(text='adm_ds_m')
async def admin_ds_system(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.adsmentors)


@dp.callback_query_handler(text='adm_fs_m')
async def admin_ds_system(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.adm_fs_m)


@dp.callback_query_handler(text='adm_se_m')
async def admin_ds_system(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.adm_se_m)

@dp.callback_query_handler(text='am1')
async def admin_nodira(message: types.CallbackQuery):
    pie("Azodov Sarvar")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azodov Sarvar', reply_markup=nav.adm_nodira)

@dp.callback_query_handler(text='admm1')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Arslanova Nodira")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Arslanova Nodira qoyilgan kamentariyalar')



@dp.callback_query_handler(text='am2')
async def admin_nodira(message: types.CallbackQuery):
    pie("Olloyorov Sirojiddin")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Olloyorov Sirojiddin')
@dp.callback_query_handler(text='am3')
async def admin_nodira(message: types.CallbackQuery):
    pie("Rasulov Rahmatulloh")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Rasulov Rahmatulloh')
@dp.callback_query_handler(text='am4')
async def admin_nodira(message: types.CallbackQuery):
    pie("Shomurodov Sarvarbek")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shomurodov Sarvarbek')
@dp.callback_query_handler(text='am5')
async def admin_nodira(message: types.CallbackQuery):
    pie("Shukurov Jasur")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shukurov Jasur')
@dp.callback_query_handler(text='am6')
async def admin_nodira(message: types.CallbackQuery):
    pie("Azizova Aziza")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azizova Aziza')
@dp.callback_query_handler(text='am7')
async def admin_nodira(message: types.CallbackQuery):
    pie("Arslanova Nodira")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Arslanova Nodira umumiy analitikasi', reply_markup=nav.adm_nodira)

@dp.callback_query_handler(text='admm1')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Arslanova Nodira")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Arslanova Nodira qoyilgan kamentariyalar')


@dp.callback_query_handler(text='am8')
async def admin_nodira(message: types.CallbackQuery):
    pie("Alimbayeva Asalbonu")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Alimbayeva Asalbonu')
@dp.callback_query_handler(text='am9')
async def admin_nodira(message: types.CallbackQuery):
    pie("Orifjonov Abdulaziz")
    img = open('/Users/student/PycharmProjects/bot/MentorFeedbackAnalysisBot/Analysis/imag/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Orifjonov Abdulaziz')




"""_____________________________________________________________________________________________________________________________________________________________________________________________________"""
# ==========================================+++++++===================================================================

@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Reaktsiya qoldirish':
            await bot.send_message(message.from_user.id, 'Assalomu aleykum 😊', reply_markup=types.ReplyKeyboardRemove())
            if db.get_directions(message.from_user.id) == 'ds':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.ds_mentors)
            elif db.get_directions(message.from_user.id) == 'fs':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.fs_mentors)
            elif db.get_directions(message.from_user.id) == 'se':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.se_mentors)

        if message.text == 'asd':
            await bot.send_message(message.from_user.id, 'Welcome to admin system :)')
            await bot.send_message(message.from_user.id, 'Analysis', reply_markup=nav.adm_analysis)

        if message.text == 'Back':
            await bot.send_message(message.from_user.id, 'Bosh Menu', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, 'Analysis', reply_markup=nav.adm_analysis)


while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
