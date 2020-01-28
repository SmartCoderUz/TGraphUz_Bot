import random
import string
import time
from time import sleep
from a1 import init_db
import telebot
from telebot import types

from a1 import add_member
from a1 import count_login
from a1 import id_chat
from a1 import id_msg
from a1 import login
from others import *
from a1 import id_user

url = 'https://telegram.me/{0}?start={1}_{2}'

tokenn = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))

bot = telebot.TeleBot(token)
logo = open('logo.jpg', 'rb')

rules = open('Umumiy_qoidalar.pdf', 'rb')


@bot.message_handler(commands=['activate'])
def send_start(start):
    try:
        for i in start_list:
            bot.delete_message(start.chat.id, message_id=i)
            start_list.clear()
    except IndexError:
        return
    bot_mems.append(start.from_user)
    keystart = types.InlineKeyboardMarkup(row_width=1)
    start1 = types.InlineKeyboardButton(text='Bot qo\'llanmasi', url='https://telegra.ph/TGraphUz-Bot-01-20')
    rulesk = types.InlineKeyboardButton(text='Umumiy qoidalar', url='https://drive.google.com/open?id'
                                                                    '=1UCOF8lu6D0BvvQHl50Kc50WeF-yiEsUd')
    keystart.add(start1, rulesk)
    msg = bot.send_message(start.chat.id, text=starttext, reply_markup=keystart, parse_mode="Markdown")
    msg
    start_list.append(msg.message_id)


@bot.message_handler(commands=['help'])
def any_msg(message):
    try:
        for i in help_list:
            bot.delete_message(message.chat.id, message_id=i)
            help_list.clear()
    except (IndexError):
        return
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Qo\'shimcha", callback_data="other")
    second_button = types.InlineKeyboardButton(text="Bot haqida", callback_data="about")
    keyboardmain.add(first_button, second_button)
    msg = bot.send_message(message.chat.id, text=commands, parse_mode='Markdown', reply_markup=keyboardmain)
    msg
    help_list.append(msg.message_id)


@bot.message_handler(content_types=['new_chat_members'])
def new_member(a):
    bot_name = bot.get_me().username
    key = types.InlineKeyboardMarkup(row_width=2)
    k1 = types.InlineKeyboardButton('Qo\'llanma', 'https://telegra.ph/TGraphUz-Bot-01-20')
    k2 = types.InlineKeyboardButton('Umumiy qoidalar',
                                    'https://drive.google.com/open?id=1UCOF8lu6D0BvvQHl50Kc50WeF-yiEsUd')
    accept = types.InlineKeyboardButton('Roziman', url.format(bot_name, a.new_chat_member.id, ''.join(login)))
    key.add(k1, k2)
    key.add(accept)
    msg = bot.send_message(a.chat.id, newtext.format(a.new_chat_member.first_name, a.new_chat_member.id),
                           reply_markup=key, parse_mode='Markdown')
    msg
    add_member(user_id=a.new_chat_member.id, text=tokenn, mes_id=msg.message_id, chat_id=a.chat.id)



@bot.message_handler(commands=['start'], func=lambda m: login in m.text.split())
def accept(m):
    if m.from_user.id == id_user:

        bot.restrict_chat_member(id_chat, m.from_user.id, can_send_media_messages=True,
                                 can_send_other_messages=True, can_add_web_page_previews=True,
                                 can_send_messages=True)
        bot.send_message(m.from_user.id,
                         'Juda soz! \nEndi bemalol guruhda yozishingiz mumkin.\n\nLekin qoidalarni unutmang!')
        bot.delete_message(id_chat, id_msg)
    elif count_login == 2:
        bot.send_message(m.from_user.id, 'Siz allaqachon qoidalarga rozilik bildirgansiz!')
    else:
        bot.send_message(m.from_user.id,
                         'Knopka bor ekan deb bosuvradimi?\nShoshilmang, hali siz uchun ham knopka jo\'natamiz, '
                         'o\'shanda bosasz!')


@bot.message_handler(
    content_types=['new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
                   'pinned_message'])
def ss(s):
    bot.delete_message(s.chat.id, s.message_id)


@bot.message_handler(content_types=['text'])
def send_telegraph(tg):
    if tg.text == '!telegram':
        bot.send_message(tg.chat.id, text=telegram1, parse_mode='Markdown', disable_web_page_preview=True,
                         reply_to_message_id=tg.message_id)
    elif tg.text == '!telegraph':
        bot.send_message(tg.chat.id,
                         text='[Telegraph](https://play.google.com/store/apps/details?id=ir.ilmili.telegraph) - '
                              'Android uchun',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif tg.text == '!ghost':
        bot.send_message(tg.chat.id,
                         text='[Ghost Activator](https://t.me/TGraphUz/53) - Telegraph uchun ghost aktivator',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif tg.text == '!ghost mode':
        bot.send_message(tg.chat.id, '[Ghost Mode](https://telegra.ph/Telegraph-Ghost-Mode-01-20) - Ghost Mode nima?',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif '#qoidalar' in tg.text:
        try:
            for i in qoidalar_list:
                bot.delete_message(tg.chat.id, message_id=i)
                qoidalar_list.clear()
        except IndexError:
            return
        if tg.chat.type in ['group', 'supergroup']:
            msg = bot.send_message(tg.chat.id, '✅ Guruh qoidalari bilan tanishib chiqing: [QOIDALAR]('
                                               'https://t.me/uzb_telegraph/167531)', reply_to_message_id=tg.message_id,
                                   parse_mode='Markdown')
            msg
            qoidalar_list.append(msg.message_id)
        else:
            bot.send_chat_action(tg.chat.id, action='typing')
            sleep(random * 2 + 3)
            bot.send_message(tg.chat.id, qoidalar, reply_to_message_id=tg.message_id)
    elif tg.text == '!uz':
        bot.send_message(tg.chat.id,
                         text='[O\'zbek tili](https://t.me/TGraphUz/764) - Telegraph uchun o\'zbek tilini o\'rnatish',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif tg.text == '!ru':
        bot.send_message(tg.chat.id, text='[Rus tili](https://t.me/TGraphUz_Bot_files/522) - Telegraph uchun rus '
                                          'tilini o\'rnatish',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif tg.text == '!proxy':
        bot.send_message(tg.chat.id, '[Proxy](http://bit.ly/38ltSiz) - Proxy haqida ma\'lumot',
                         reply_to_message_id=tg.message_id, parse_mode='Markdown', disable_web_page_preview=True)
    elif '!ro' in tg.text:
        try:
            for i in ro_list:
                bot.delete_message(tg.chat.id, message_id=i)
                ro_list.clear()
        except (IndexError):
            return

        usertg = bot.get_chat_member(tg.chat.id, tg.from_user.id)
        if usertg.status in ['administrator', 'creator']:
            a1 = str(tg.text).split(' ')
            user = '[{0}](tg://user?id={1})'.format(tg.reply_to_message.from_user.first_name,
                                                    tg.reply_to_message.from_user.id)
            text = '''{0} siz {1}ga read-only rejimiga tushirildingiz.
Sabab: *{2}* | ▪️▪️▪️▪️▪️⏰*5(soat)*'''
            text2 = '''{0} siz {1}ga read-only rejimiga tushirildingiz.
Sabab: *{2}* | ▫️▪️▪️▪️▪️⏰*4(soat)*'''
            text3 = '''{0} siz {1}ga read-only rejimiga tushirildingiz.
Sabab: *{2}* | ▫️▫️▪️▪️▪️⏰*3(soat)*'''
            text4 = '''{0} siz {1}ga read-only rejimiga tushirildingiz.
Sabab: *{2}* | ▫️▫️▫️▪️▪️⏰*2(s)*'''
            text5 = '''{0} siz {1}ga read-only rejimiga tushirildingiz.
Sabab: *{2}* | ▫️▫️▫️▫️▪️⏰*1(soat)*'''
            time1 = a1[1]
            if '#' in a1:
                a2 = a1[a1.index('#') + 1:]
                if 'm' in time1:
                    time1 = int(a1[1].split('m')[0])
                    TIME = '{} minut'.format(time1)
                    msg = bot.send_message(tg.chat.id, text.format(user, TIME, " ".join(a2)),
                                           disable_web_page_preview=True, parse_mode='Markdown')
                    msg
                    bot.restrict_chat_member(chat_id=tg.chat.id, user_id=tg.reply_to_message.from_user.id,
                                             until_date=time.time() + time1 * 60)
                    bot.delete_message(tg.chat.id, tg.message_id)
                    sleep(60 * 60)
                    bot.edit_message_text(text2.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text3.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text4.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text5.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.delete_message(tg.chat.id, msg.message_id)
                elif 'h' in time1:
                    time1 = int(a1[1].split('h')[0])
                    TIME = '{} soat'.format(time1)
                    msg = bot.send_message(tg.chat.id, text.format(user, TIME, " ".join(a2)),
                                           disable_web_page_preview=True, parse_mode='Markdown')
                    msg
                    bot.restrict_chat_member(chat_id=tg.chat.id, user_id=tg.reply_to_message.from_user.id,
                                             until_date=time.time() + time1 * 60 * 60, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False,
                                             can_add_web_page_previews=False)
                    bot.delete_message(tg.chat.id, tg.message_id)
                    sleep(60 * 60)
                    bot.edit_message_text(text2.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text3.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text4.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text5.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.delete_message(tg.chat.id, msg.message_id)
                elif 'd' in time1:
                    time1 = int(a1[1].split('d')[0])
                    TIME = '{} kun'.format(time1)
                    msg = bot.send_message(tg.chat.id, text.format(user, TIME, " ".join(a2)), parse_mode='Markdown')
                    msg
                    bot.restrict_chat_member(chat_id=tg.chat.id, user_id=tg.reply_to_message.from_user.id,
                                             until_date=time.time() + time1 * 60 * 60 * 24, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False,
                                             can_add_web_page_previews=False)
                    bot.delete_message(tg.chat.id, tg.message_id)
                    sleep(60 * 60)
                    bot.edit_message_text(text2.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text3.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text4.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.edit_message_text(text5.format(user, TIME, " ".join(a2)), tg.chat.id, msg.message_id,
                                          disable_web_page_preview=True, parse_mode='Markdown')
                    sleep(60 * 60)
                    bot.delete_message(tg.chat.id, msg.message_id)
    elif tg.text == '!unro':
        bot.restrict_chat_member(tg.chat.id, tg.reply_to_message.from_user.id, can_send_media_messages=True,
                                 can_send_messages=True, can_send_other_messages=True,
                                 can_add_web_page_previews=True)
    elif tg.text == '!kick':
        user = bot.get_chat_member(tg.chat.id, tg.from_user.id)
        if user.status in ['administrator', 'creator']:
            bot.kick_chat_member(tg.chat.id, tg.reply_to_message.from_user.id)
        else:
            return
    elif '#1' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_1.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#2' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_2.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#3' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_3.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#4' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_4.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#5' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_5.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#6' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_6.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#7' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_7.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif 'odamgarchilik' in tg.text:
        try:
            for i in message_list:
                bot.delete_message(tg.chat.id, message_id=i)
                message_list.clear()
        except (IndexError):
            return
        bot.send_chat_action(tg.chat.id, action='typing')
        sleep(random() * 2 + 3)
        user = tg.reply_to_message.from_user.username
        msg = bot.reply_to(tg, odamgarchilik.format(user),
                           parse_mode='Markdown')
        msg
        message_list.append(msg.message_id)
    elif 'SPAM' in tg.text:
        bot.reply_to(message=tg.reply_to_message,
                     text='Spam nima? Undan qanday saqlanish mumkin? [Batafsil...]('
                          'https://telegra.ph/Telegramda-spam-Bu-nima-Undan-qanday-himoyalanish-mumkin-Spamga'
                          '-tushmaslik-uchun-nima-qilish-kerak-01-20)',
                     parse_mode='Markdown')
        bot.delete_message(tg.chat.id, tg.message_id)
    elif '<>' in tg.text:
        a1 = str(tg.text).split(' ')
        a2 = a1[a1.index('<>') + 1:]
        bot.reply_to(tg.reply_to_message, text=" ".join(a2), parse_mode='Markdown')
        bot.delete_message(tg.chat.id, tg.message_id)

    elif 'MODE' in tg.text:
        bot.reply_to(tg.reply_to_message, text='https://t.me/uzb_telegraph/189540')
        bot.delete_message(tg.chat.id, tg.message_id)
    elif tg.text == 'NEW':
        bot.reply_to(tg.message, text='Botning eng so\'ngi versiyasi uchun [Qo\'llanma]('
                                      'https://telegra.ph/TGraphUz-Bot-01-20)', parse_mode='Markdown')
    elif tg.text == '!report':
        bot.delete_message(tg.chat.id, tg.message_id)
        for i in adm:
            bot.send_message(chat_id=i, text='[{0}](t.me/{1}) ushbu [habar](t.me/{2}/{3})ga shikoyat qildi!'.format(
                tg.from_user.first_name, tg.from_user.username, tg.chat.username, tg.reply_to_message.message_id),
                             disable_web_page_preview=True, parse_mode='Markdown')
    elif '!d' in tg.text:
        try:
            usertg = bot.get_chat_member(tg.chat.id, tg.from_user.id)
            if usertg.status in ['administrator', 'creator']:
                a1 = str(tg.text).split(' ')
                time1 = a1[1]
                if '!d' in a1:
                    if 'm' in time1:
                        time1 = int(a1[1].split('m')[0])
                        sleep(time1 * 60)
                        bot.delete_message(tg.chat.id, tg.reply_to_message.message_id)
                        bot.delete_message(tg.chat.id, tg.message_id)
                    elif 'h' in time1:
                        time1 = int(a1[1].split('h')[0])
                        sleep(time1 * 60 * 60)
                        bot.delete_message(tg.chat.id, tg.reply_to_message.message_id)
                        bot.delete_message(tg.chat.id, tg.message_id)
                    elif 'd' in time1:
                        time1 = int(a1[1].split('d')[0])
                        sleep(time1 * 60 * 60 * 24)
                        bot.delete_message(tg.chat.id, tg.reply_to_message.message_id)
                        bot.delete_message(tg.chat.id, tg.message_id)
        except IndexError:
            bot.delete_message(tg.chat.id, tg.reply_to_message.message_id)
            bot.delete_message(tg.chat.id, tg.message_id)
    elif tg.text == '!reload_admins':
        admins = bot.get_chat_administrators(tg.chat.id)
        bot.send_message(tg.chat.id, 'Reloaded!', reply_to_message_id=tg.message_id)
        bot.send_message(tg.from_user.id, admins)
    elif tg.text == 'ID':
        try:
            ID = tg.reply_to_message.message_id
            bot.send_message(tg.chat.id, ID, reply_to_message_id=tg.message_id)
        except AttributeError:
            bot.send_message(tg.chat.id, '{}'.format(tg.chat.id), reply_to_message_id=tg.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":

        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        first_button = types.InlineKeyboardButton(text="Qo\'shimcha", callback_data="other")
        second_button = types.InlineKeyboardButton(text="Bot haqida", callback_data="about")
        keyboardmain.add(first_button, second_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=commands,
                              parse_mode='Markdown', reply_markup=keyboardmain)

    elif call.data == "other":
        keyboard = types.InlineKeyboardMarkup()
        commandsb = types.InlineKeyboardButton('Admin\'s commands', callback_data='commands')
        backbutton = types.InlineKeyboardButton(text="◀️ortga", callback_data="mainmenu")
        keyboard.add(commandsb)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Guruh sozlamalari!", reply_markup=keyboard)
    elif call.data == 'about':
        kword = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="◀️ortga", callback_data="mainmenu")
        kword.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=abouttext,
                              reply_markup=kword)

    elif call.data == 'commands':
        bot.send_message(call.from_user.id, text=adm_commands, parse_mode='Markdown')


if __name__ == "__main__":
    bot.polling(none_stop=True)
