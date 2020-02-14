import random
import string
import time
from time import sleep
from test import *

import telebot
from telebot import types

from others import *

url = 'https://telegram.me/{0}?start={1}_{2}'

tokenn = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))

bot = telebot.TeleBot(token)
#golos = open('golos.jpg', 'rb')
#text_1 = open('text_1.jpg', 'rb')
#rulesf = open('rules.jpg', 'rb')
#rules_adm = open('rules_adm.jpg', 'rb')

fon = open('main.jpg', 'rb')
a1 = open('(1).png', 'rb')
a2 = open('(2).png', 'rb')
a3 = open('(3).png', 'rb')
a4 = open('(4).png', 'rb')
a5 = open('(5).png', 'rb')
a6 = open('(6).png', 'rb')
a7 = open('(7).png', 'rb')

rules = open('Umumiy_qoidalar.pdf', 'rb')

accept_key = types.InlineKeyboardMarkup(row_width=3)
key1 = types.InlineKeyboardButton('So\'zboshi', callback_data='gap1')
key2 = types.InlineKeyboardButton('Qoidalar', callback_data='qoida')
key3 = types.InlineKeyboardButton('Vazifalar', callback_data='vazifa')
accept1 = types.InlineKeyboardButton('Roziman', callback_data='roziman')
accept_key.add(key1, key2, key3)
accept_key.add(accept1)



@bot.message_handler(content_types=['new_chat_members'])
def new_member(a):
    bot.restrict_chat_member(a.chat.id, a.new_chat_member.id, can_send_messages=False, can_send_media_messages=False,
                             can_send_other_messages=False, can_add_web_page_previews=False)
    bot.delete_message(a.chat.id, a.message_id)
    key_list = types.InlineKeyboardMarkup()
    key_accept = types.InlineKeyboardButton(text='Roziman', callback_data='roziman')
    key_rules = types.InlineKeyboardButton(text='Qoidalar', url='https://t.me/uzb_telegraph/167531')
    key_list.add(key_accept)
    key_list.add(key_rules)
    welcome = '111.png'
    if a.new_chat_member.username == None:
        watermark_text(welcome, 'logo.jpg',
                       text=a.new_chat_member.first_name,
                       pos=(440, 240))
    else:
        watermark_text(welcome, 'logo.jpg',
                       text='@{}'.format(a.new_chat_member.username),
                       pos=(440, 240))
    logo = open('logo.jpg', 'rb')
    bot.send_photo(a.chat.id, logo, caption=newtext.format(a.new_chat_member.first_name, a.new_chat_member.id),
                   reply_markup=key_list, parse_mode='Markdown')




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
    return


'''
@bot.message_handler(commands=['start'], func=lambda m: m.text.split()[1] == 'rules')
def send_rules(a):
    try:
        bot.send_photo(a.chat.id, text_1)
        bot.send_photo(a.chat.id, rulesf)
        bot.send_photo(a.chat.id, rules_adm)
    except IndexError:
        return

@bot.message_handler(commands=['start'], func=lambda m: m.text.split()[1] == 'background')
def back(tg):
    bot.send_photo(tg.chat.id, photo=fon, caption=fon_text, reply_markup=keyboard_b)
'''

@bot.message_handler(commands=['test'])
def send_test(test):
    msg = bot.send_message(test.chat.id, 'BOT ISHLAYABDI ({})'.format(' / '), reply_to_message_id=test.message_id)
    msg
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' — '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' \ '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' | '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.edit_message_text('BOT ISHLAYABDI ({})'.format(' / '), msg.chat.id, message_id=msg.message_id)
    sleep(0.05)
    bot.delete_message(msg.chat.id, msg.message_id)
    bot.delete_message(test.chat.id, test.message_id)
''''
@bot.message_handler(commands=['captchaon'])
def captcha_on(a):
    captcha.update(status='on')
    msg = bot.send_message(a.chat.id, 'Captcha was successfully activated!')
    msg
    sleep(30)
    bot.delete_message(a.chat.id, msg.message_id)
@bot.message_handler(commands=['captchaoff'])
def captcha_on(a):
    captcha.update(status='off')
    msg = bot.send_message(a.chat.id, 'Captcha was successfully disabled!')
    msg
    sleep(30)
    bot.delete_message(a.chat.id, msg.message_id)


isstart = True
@bot.message_handler(commands=['captchaon'])  # ДИРЕКТОРИЯ
def st(command):
    global isstart
    isstart = True
    if isstart == True:
        bot.send_message(command.chat.id, 'Captcha was successfully activated!', reply_to_message_id=command.message_id)

@bot.message_handler(commands=['captchaoff'])  # ДИРЕКТОРИЯ
def br(command):
    global isstart
    isstart = False
    if isstart == False:
        bot.send_message(command.chat.id, 'Captcha was successfully disabled!', reply_to_message_id=command.message_id)
'''


@bot.message_handler(commands=['help'])
def any_msg(message):
    try:
        for i in help_list:
            bot.delete_message(message.chat.id, message_id=i)
            help_list.clear()
    except IndexError:
        return
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Qo\'shimcha", callback_data="other")
    second_button = types.InlineKeyboardButton(text="Bot haqida", callback_data="about")
    keyboardmain.add(first_button, second_button)
    msg = bot.send_message(message.chat.id, text=commands, parse_mode='Markdown', reply_markup=keyboardmain)
    msg
    help_list.append(msg.message_id)



@bot.message_handler(
    content_types=['left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
                   'pinned_message'])
def abd(a):
    bot.delete_message(a.chat.id, a.message_id)


@bot.message_handler(content_types=['text'])
def send_telegraph(tg):
    if tg.text == 'photo':
        photo = open('logo.jpg', 'rb')
        bot.send_photo(tg.chat.id, photo, 'It is your logo!')
    elif tg.text == 'rules':
        rule = open('Umumiy_qoidalar.pdf', 'rb')
        bot.send_document(tg.chat.id, rule, caption='Umumiy qoidalar!')
    elif tg.text == '!telegram':
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
    elif 'raxmat' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'Raxmat' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'raxmad' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'Raxmad' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'rahmat' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'Rahmat' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'rahmad' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)
    elif 'Rahmad' in tg.text:
        bot.send_message(tg.chat.id, text=thanks, disable_web_page_preview=True, reply_to_message_id=tg.message_id)


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
            sleep(5)
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
        except IndexError:
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
            bot.delete_message(tg.chat.id, tg.message_id)
        else:
            return

    elif '#1' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_1.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#2' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_2.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#3' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_3.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#4' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_4.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#5' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_5.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#6' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_6.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif '#7' in tg.text:
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(tg.chat.id, r_7.format(user), reply_to_message_id=tg.message_id)
        msg
        sleep(60*60)
        bot.delete_message(tg.chat.id, msg.message_id)
    elif 'odamgarchilik' in tg.text:
        try:
            for i in message_list:
                bot.delete_message(tg.chat.id, message_id=i)
                message_list.clear()
        except IndexError:
            return
        bot.send_chat_action(tg.chat.id, action='typing')
        sleep(5)
        user = tg.reply_to_message.from_user.username
        msg = bot.send_message(chat_id=tg.chat.id, text=odamgarchilik.format(user), reply_to_message_id=tg.message_id,
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
        try:
            a1 = str(tg.text).split(' ')
            a2 = a1[a1.index('<>') + 1:]
            bot.send_message(tg.chat.id, text=' '.join(a2), disable_web_page_preview=True, parse_mode='Markdown')
            bot.delete_message(tg.chat.id, tg.message_id)
        except IndexError:
            bot.send_message(tg.chat.id, text=' '.join(a2), disable_web_page_preview=True, parse_mode='Markdown')

    elif 'golos' in tg.text:
        key = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton('Sozlash', url='https://t.me/GraphSettings/368')
        key.add(key1)
        bot.send_message(tg.chat.id, text='''*Ovozli habar jo'natayotganda musiqani qanday o'chmaydigan qilish:*
        -> Telegraph sozlamalari
            ->Chat
                ->Ovoz yozayotganda musiqni to'xtatish = `OFF`
                
Yoki SOZLASH knopkasi orqali sozlash oynasiga o'tib ham o'chirib qo'yishingiz mumkin!''', reply_to_message_id=tg.message_id,
                         reply_markup=key, parse_mode='Markdown')

    elif 'MODE' in tg.text:
        bot.reply_to(tg.reply_to_message, text='https://t.me/uzb_telegraph/189540')
        bot.delete_message(tg.chat.id, tg.message_id)
    elif tg.text == 'NEW':
        bot.reply_to(tg.message, text='Botning eng so\'ngi versiyasi uchun [Qo\'llanma]('
                                      'https://telegra.ph/TGraphUz-Bot-01-20)', parse_mode='Markdown')
    elif tg.text == '!report':
        bot.delete_message(tg.chat.id, tg.message_id)
        for i in adm:
            bot.send_message(chat_id=i, text='[{0}](tg://user?id={1}) ushbu [habar](t.me/{2}/{3})ga shikoyat qildi!'.format(
                tg.from_user.first_name, tg.from_user.id, tg.chat.username, tg.reply_to_message.message_id),
                             disable_web_page_preview=True, parse_mode='Markdown')
            bot.forward_message(chat_id=i, from_chat_id=tg.chat.id, message_id=tg.reply_to_message.message_id)

    elif '#savol' in tg.text:
        for i in adm:
            bot.send_message(chat_id=i, text='[{0}](t.me/{1}) guruhda ushbu [savol](t.me/{2}/{3})ni jo\'natdi!'.format(
                tg.from_user.first_name, tg.from_user.username, tg.chat.username, tg.message_id),
                             disable_web_page_preview=True, parse_mode='Markdown')
            bot.forward_message(chat_id=i, from_chat_id=tg.chat.id, message_id=tg.message_id)

    elif '#ID' in tg.text:
        user_ID = str(tg.text).split('#ID ')[1]
        bot.send_message(tg.chat.id, text='Siz izlagan [USER](tg://user?id={})'.format(user_ID),
                         reply_to_message_id=tg.message_id, parse_mode='Markdown')
    elif '#support' in tg.text:
        try:
            bot.send_message(tg.chat.id, 'Telegram hizmat ko\'rsatish markaziga habar jo\'natish. [Batafsil...](https://t.me/uzb_telegraph/208602)',
                             reply_to_message_id=tg.reply_to_message.message_id, disable_web_page_preview=True, parse_mode='Markdown')
            bot.delete_message(tg.chat.id, tg.message_id)
        except AttributeError:
            bot.send_message(tg.chat.id, 'Telegram hizmat ko\'rsatish markaziga habar jo\'natish. [Batafsil...](https://t.me/uzb_telegraph/208602)',
                             reply_to_message_id=tg.message_id, disable_web_page_preview=True, parse_mode='Markdown')
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

    elif '!chat back' in tg.text:
        keyboard = types.InlineKeyboardMarkup()
        go = types.InlineKeyboardButton('Batafsil...', url='https://t.me/uzb_telegraph/211187')
        keyboard.add(go)
        bot.send_message(tg.chat.id, 'Chatlar orqa foniga rasm qo\'yishni o\rganish uchun *Batafsil* tugmasini bosing!',
                         reply_markup=keyboard, reply_to_message_id=tg.reply_to_message.message_id, parse_mode='Markdown')
    elif 'pul' in tg.text:
        bot.send_message(tg.chat.id, 'Yolg\'on', reply_to_message_id=tg.message_id)
    elif 'Pul' in tg.text:
        bot.send_message(tg.chat.id, 'Yolg\'on', reply_to_message_id=tg.message_id)
    '''
    elif tg.text == '!vote':

        poll_key = types.InlineKeyboardMarkup(row_width=2)
        yes = types.InlineKeyboardButton('Ha', callback_data='yes')
        no = types.InlineKeyboardButton('Yo\'q', callback_data='no')
        poll_key.add(yes, no)
        bot.send_message(tg.chat.id, text='[{0}](tg://user?id={1})ni guruhdan ban qilaymi?
        
        Ha - {2}
        
        Yo'q - {3}'.format(tg.reply_to_message.from_user.first_name, tg.reply_to_message.from_user.id, ha, yoq),
                         reply_markup=poll_key, reply_to_message_id=tg.reply_to_message.message_id,
                         parse_mode='Markdown')
'''




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

    elif call.data == 'roziman':
        user = bot.get_chat_member(call.message.chat.id, call.from_user.id)
        if user.status == 'restricted':
            bot.restrict_chat_member(call.message.chat.id, call.from_user.id, can_add_web_page_previews=True,
                                     can_send_other_messages=True, can_send_media_messages=True, can_send_messages=True)
            bot.answer_callback_query(call.id, text='Juda soz! Endi guruhda yozishingiz mumkin!', show_alert=True)
            bot.delete_message(call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, 'Bu knopka siz uchun emas!', show_alert=True)

    elif call.data == 'first':
        bot.send_photo(call.message.chat.id, a1, caption=a1_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'second':
        bot.send_photo(call.message.chat.id, a2, caption=a2_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'third':
        bot.send_photo(call.message.chat.id, a3, caption=a3_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'fourth':
        bot.send_photo(call.message.chat.id, a4, caption=a4_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'fifth':
        bot.send_photo(call.message.chat.id, a5, caption=a5_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'sixth':
        bot.send_photo(call.message.chat.id, a6, caption=a6_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'seventh':
        bot.send_photo(call.message.chat.id, a7, caption=a7_text, reply_markup=keyboard_b)
        bot.delete_message(call.message.chat.id, call.message.message_id)


    '''
    elif call.data == 'yes':
        from others import ha
        from others import yoq
        ha += 1
        bot.edit_message_text(text='[{0}](tg://user?id={1})ni guruhdan ban qilaymi?

        Ha - {2}

        Yo'q - {3}'.format(call.message.reply_to_message.from_user.first_name,
                             call.message.reply_to_message.from_user.first_name, ha, yoq))
    elif call.data == 'no':
        from others import ha
        from others import yoq
        yoq += 1
        bot.edit_message_text(text='[{0}](tg://user?id={1})ni guruhdan ban qilaymi?

        Ha - {2}

        Yo'q - {3}'.format(call.message.reply_to_message.from_user.first_name,
                             call.message.reply_to_message.from_user.first_name, ha, yoq))
    '''
if __name__ == "__main__":
    bot.polling(none_stop=True)
