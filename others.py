from telebot import types
token = '1037828551:AAF-qjJWdu_ZgWAx29zy1buNBaO5eRv8AYI'

bot_mems = []
adm = [891118348, 699068229, 972575928, 955037319, 914959123, 1053801273, 197234400, 358031730]

starttext = '''Salom! 
Botdan to'liq foydalanish uchun [Qo'llanma](https://telegra.ph/TGraphUz-Bot-01-20) bilan tanishib chiqing'''

telegram1 = ('[Telegram for Android](https://play.google.com/store/apps/details?id=org.telegram.messenger) - Android '
            'telefonlar uchun\n[Telegram for IOS](https://telega.one/dl/ios) - iPhone/iPad\n[Telegram Desktop]('
            'https://telegram.org/dl/desktop/win) - Windows uchun\n[Telegram Desktop](https://telegram.org/dl/macos) '
            '- macOS uchun')

qoidalar = '''1. Guruhimiz mavzusi: Telegram(TG) va Telegraph(TGraph) Messenger'dan yiroq mavzularni ochmemiz.
1.1. Nakrutka haqida gapirmaymiz.
1.2. Savdo bo'yicha maslahatlashmaymiz.
1.3. Shunchaki suhbatlashmaymiz.
1.4. Faqat TG va TGraph haqida suhbatlashamiz.

2. Reklama qilmaymiz.
2.1. O'z mahsulotimizni sotmaymiz.
2.2. Kanallardan ssilka(havola) tashlamaymiz.
2.3. Kanal/botlardan xabar forward qilmaymiz(uzatmaymiz).
2.4. Referall ssilkalar yubormaymiz.
2.5. Screnshotda yoki xabar matnida boshqa kanal/guruh/botlarga havolalarni ko‘rsatmaymiz.

3. Yolg'on xabarlar tarqatmaymiz.
3.1. Bo'lmagan narsani haqiqat qilib ko'rsatishga urinmaymiz.
3.2. Kanallar/guruhlardan kelgan "bola yo'qolib qoldi","ammamni o'g'li kasal" mazmunli xabarlarni yubormaymiz.
3.3. "Shuncha kishiga tarqatsang baxtli bo'lasan, tarqatmasang o'lasan" mazmunidagi xabarlarni yubormaymiz.
3.4. "Tekin net topdim, lichga, pullik" mazmunidagi xabarlar yubormaymiz.

4. Hurmatda bo'lamiz.
4.1. Nimadir so'rayotganda farosat bilan so'raymiz.
4.2. So'kinish mumkin emas.
4.3. Bilmagan narsangizga talashib, kelishmovchilik chiqarmaymiz.
4.4. Kelisholme qoseng srazi lichga ot, yoki nomeriga ter.

5. Javob kutamiz.
5.1. Bironta foydalanuvchi savolimizga javob bersa uni javobini qadrlaymiz.
5.2. Hamma ham sizni "bemani" savolingizga javob berishga majbur emas.
5.3. Savol berishdan oldin savolingiz to'g'riligiga amin bo'ling.
5.4. Tezroq javob olmoqchi bosez farosat bilan savol bering.

6. Bu guruh "Play Market" emas.
6.1. Guruhda faqat Telegram va Graph Messenger(Telegraph) muhokama qilinadi.
6.2. "Videoni mbsini kichraytiradigan prog qaysi", "... progni topib beringlar" kabi habarlar o'chirib tashlanadi va habar jo'natuvchisi bloklanadi.
Dastur kerak bo'lsa guruhgamas @apkdl_bot ga yozing!
6.3. Biz guruhda videodagi .mp3 ni topib bermaymiz.

7. Adminlarni belgilang.
7.1. Savolingizga aniq javob kerak bo'lsa savol oxirida biror admin usernamesini yozib yuboring.
7.2. Qoida buzilganini ko'rsangiz  biror admin usernamesini yozib o'sha qoida buzilgan habarga reply qilib yuboring.

Keyinchalik #qoidalar o'zgarishi mumkin!

Qoidalarni topish uchun #qoidalar heshtegidan foydalaning!

Adminlar: @Mr_Kasimov, @SindorbekUz, @Snake_BloG, @nqarshiboyev, @Padishakh_Murod, @NurikNazarov11, @Ilhombek_Blogg
'''

r_1 = '''1. Guruhimiz mavzusi: Telegram(TG) va Telegraph(TGraph) Messenger'dan yiroq mavzularni ochmemiz.
1.1. Nakrutka haqida gapirmaymiz.
1.2. Savdo bo'yicha maslahatlashmaymiz.
1.3. Shunchaki suhbatlashmaymiz.
1.4. Faqat TG va TGraph haqida suhbatlashamiz.
@{}'''

r_2 = '''2. Reklama qilmaymiz.
2.1. O'z mahsulotimizni sotmaymiz.
2.2. Kanallardan ssilka(havola) tashlamaymiz.
2.3. Kanal/botlardan xabar forward qilmaymiz(uzatmaymiz).
2.4. Referall ssilkalar yubormaymiz.
2.5. Screnshotda yoki xabar matnida boshqa kanal/guruh/botlarga havolalarni ko‘rsatmaymiz.
@{}'''

r_3 = '''3. Yolg'on xabarlar tarqatmaymiz.
3.1. Bo'lmagan narsani haqiqat qilib ko'rsatishga urinmaymiz.
3.2. Kanallar/guruhlardan kelgan "bola yo'qolib qoldi","ammamni o'g'li kasal" mazmunli xabarlarni yubormaymiz.
3.3. "Shuncha kishiga tarqatsang baxtli bo'lasan, tarqatmasang o'lasan" mazmunidagi xabarlarni yubormaymiz.
3.4. "Tekin net topdim, lichga, pullik" mazmunidagi xabarlar yubormaymiz.
@{}'''

r_4 = '''4. Hurmatda bo'lamiz.
4.1. Nimadir so'rayotganda farosat bilan so'raymiz.
4.2. So'kinish mumkin emas.
4.3. Bilmagan narsangizga talashib, kelishmovchilik chiqarmaymiz.
4.4. Kelisholme qoseng srazi lichga ot, yoki nomeriga ter.
@{}'''

r_5 = '''5. Javob kutamiz.
5.1. Bironta foydalanuvchi savolimizga javob bersa uni javobini qadrlaymiz.
5.2. Hamma ham sizni "bemani" savolingizga javob berishga majbur emas.
5.3. Savol berishdan oldin savolingiz to'g'riligiga amin bo'ling.
5.4. Tezroq javob olmoqchi bosez farosat bilan savol bering.
@{}'''

r_6='''6. Bu guruh "Play Market" emas.
6.1. Guruhda faqat Telegram va Graph Messenger(Telegraph) muhokama qilinadi.
6.2. "Videoni mbsini kichraytiradigan prog qaysi", "... progni topib beringlar" kabi habarlar o'chirib tashlanadi va habar jo'natuvchisi bloklanadi.
Dastur kerak bo'lsa guruhgamas @apkdl_bot ga yozing!
6.3. Biz guruhda videodagi .mp3 ni topib bermaymiz.
@{}'''

r_7 = '''7. Adminlarni belgilang.
7.1. Savolingizga aniq javob kerak bo'lsa savol oxirida biror admin usernamesini yozib yuboring.
7.1. Qoida buzilganini ko'rsangiz  biror admin usernamesini yozib o'sha qoida buzilgan habarga reply qilib yuboring.
@{}'''

commands = 'Bot komandalari:' \
           '\n`!telegram` - telegram yuklash uchun URL adres olish' \
           '\n`!telegraph` - telegraph yuklash uchun URL adres olish' \
           '\n`!ghost` - Telegraph uchun Ghost Aktivator' \
           '\n`!ghost mode` - Ghost Mode haqida ma\'lumot' \
           '\n`#qoidalar` - Guruh qoidalari' \
           '\n`!uz` - Telegraph uchun o\'zbek tilini o\'rnatish qo\'llanmasi' \
           '\n`!ru` - Telegraph uchun rus tilini o\'rnatish qo\'llanmasi' \
           '\n`!proxy` - proxy haqida ma\'lumot ' \
           '\n`SPAM` - spam haqida ma\'lumot olish' \
           '\n`MODE` - telegraph mode' \
           '\n`ID` - habar yoki chat ID raqamini olish' \
           '\n`<> text` - bot o\'z nomidan text\'ni jo\'natadi'

lists = []

botid = [1043844849]

adm_commands = 'Commands for admins:(with reply)' \
               '\n`!ro vaqt # sabab` -  belgilan vaqtga read only rejimiga tushirish, Sabab ko\'rsatilishi shart' \
               '\n`!unro` - read only rejimidan chiqarish' \
               '\n`!kick` - kick user from group' \
               '\n`!d` - tezkor o\'chirish' \
               '\n`!d vaqt` - belgilangan vaqtdan keyin o\'chirish' \
               '\n`#1` - qoidalarning 1-bo\'limi' \
               '\n`#2` - qoidalarning 2-bo\'limi' \
               '\n`#3` - qoidalarning 3-bo\'limi' \
               '\n`#4` - qoidalarning 4-bo\'limi' \
               '\n`#5` - qoidalarning 5-bo\'limi' \
               '\n`#6` - qoidalarning 6-bo\'limi' \
               '\n`#7` - qoidalarning 7-bo\'limi'

abouttext = '\nUshbu bot @uzb_telegraph va @TGraphUz guruhlarida foydalanuvchilarga tezkor javob berish va tartibni ' \
            'saqlash maqsadida yaratilgan.' \
            '\nBot maxsus komandalar orqali boshqariladi, foydalanuvchi komandalari bilan tanishish uchun /help ' \
            'buyrug\'ini jo\'nating.' \
            '\nBotda qo\'shimcha, guruhni nazorat qilish komandalariyam mavjud bo\'lib, ular faqat adminlar ' \
            'ro\'yxatiga kiritilganlarga ko\'rinadi' \
            '\nAdmin komandalari bilan tanishish uchun /help buyrug\'i jo\'natiladi va bot menusida Boshqa tugmasi ' \
            'bosiladi.' \
            '\nBOT TUZUVCHISI -  @NurikNazarov11'
ro_text = '[{0}](t.me/{1}) siz qoidani buzganingiz uchun {2}ga read-only rejimiga tushirildingiz!'

odamgarchilik = '''*Natija:*
`Nurik Nazarovdan @uzb_telegraph guruhi uchun 'The Zen' maslahatlar to'plami
(Tim Peters'ning 'The Zen of Python' qoidalar to'plamidan ilhomlanib yozilgan)

- O'zingiz haqingizdagi qisqa tanishtiruv 'salom' dan yaxshi.
- Oldin berilgan javobni ko'rsatish savolga qayta javob yozishdan yaxshi.
- Bitta uzun xabar bo'laklab jo'natilgan xabarlardan yaxshi.
- Xabarni tuzatish uchun tahrirlab qo'yish yana boshqa bir xabar jo'natishdan yaxshiroq.
- Mavzu haqida gaplashish undan chetlashishdan yaxshi.
- Lekin yaxshi mavzuda gaplashish bu vaqt ajratishga arziydigan hol.
- Faqat u nakrutka botga link berish bilan boshlanmagan bo'lsa.
- Xushmuomalalik ahamiyatga ega.
- Kayfiyatning yomonligi qoidalarni buzishga arzirli sabab bo'lolmaydi.
- So'rash uchun so'ramang, shunchaki savolning o'zini yozing.
- Matnli xabar ovozlisidan yaxshi.
- Faqat agar bu ovozli konferensiya bo'lmasa.
- Botlar, soat qo'yish, spamdan chiqish haqida alohida guruhlarda gaplashish ularni shu guruhda muhokama qilishdan yaxshiroq.
- Savolni avval Googlega yozish uni o'sha zahoti guruhga jo'natishdan yaxshi.
- Qoidalarga amal qilish adminlarning (ayniqsa @NurikNazarov11) nazariga tushishdan yaxshiroq.
- Uxlashdan oldin tishni yuvib yotish sog'liqqa foydali.`

@{0} uchun jo'natildi!'''

newtext = '''[{0}](tg://user?id={1}) *safimizga hush kelibsiz!*

So'ngi paytlarda guruhda tartibsizlik biroz kuchaygani sababli, biz har bir yangi guruh a'zosi [QOIDLAR](https://t.me/uzb_telegraph/167531)ga rozilik bildirishini talab qilamiz!
*Guruhda yozish huquqiga ega bo'lish uchun *[QOIDALAR](https://t.me/uzb_telegraph/167531)* bilan to'liq tanishib chiqing!*
Shundan keyingina *ROZIMAN* tugmasini bosing.

*DIQQAT!*
Siz qoidalarga rozilik bildirgach guruhda yozish huquqiga ega bo'lasiz. Shu ondan boshlab qoidalarni buzsangiz hech qanday ogohlantirishsiz jazolanasiz!
Shu sababli [QOIDALAR](https://t.me/uzb_telegraph/167531)ni diqqat bilan o'qib chiqing va guruhda odob-ahloq qoidalariga rioya qiling!

_Hurmat bilan:_
                         *TGraphUz*
'''

keyboard_b = types.InlineKeyboardMarkup(row_width=7)
A1 = types.InlineKeyboardButton('1', callback_data='first')
A2 = types.InlineKeyboardButton('2', callback_data='second')
A3 = types.InlineKeyboardButton('3', callback_data='third')
A4 = types.InlineKeyboardButton('4', callback_data='fourth')
A5 = types.InlineKeyboardButton('5', callback_data='fifth')
A6 = types.InlineKeyboardButton('6', callback_data='sixth')
A7 = types.InlineKeyboardButton('7', callback_data='seventh')

keyboard_b.add(A1, A2, A3, A4, A5, A6, A7)

a1_text = '''1-bosqich
#themeTutorial
yangi tema yaratamiz

Keyingi bosqichga o'tish uchun 2 ni bosing'''
a2_text = '''2-bosqich
#themetutorial
Yaratish jarayonida ushbu funksiyani yoqib qo'yamiz.

Keyingi bosqichga o'tish uchun 3 ni bosing'''
a3_text = '''3-bosqich
#themetutorial
Quyida biz yaratgan tema. Unda esa "pro theme" ekanligini anglatuvchi belgi(kok strelka)
endi tema burchagidagi 3 ta nuqta(options)ni bosamiz(qizil strelka)

Keyingi bosqichga o'tish uchun 4 ni bosing'''
a4_text = '''4-bosqich
#themetutorial
endi esa "edit" ni tanlaymiz.

Keyingi bosqichga o'tish uchun 5 ni bosing'''
a5_text = '''5-bosqich
#themetutorial
demak bizning pro temamiz sozlama bo'limi ochildi. bu yerdan juda kop narsani ozimizga moslab olsak bo'ladi.

hozir bizga keraklisi esa "Main screen"

Keyingi bosqichga o'tish uchun 6 ni bosing'''
a6_text = '''6-bosqich
#themetutorial
demak bizga kerakli joyga yetib keldik.
"Chat list" to'plamida birinchida turgan funksiyani tanlaymiz

Keyingi bosqichga o'tish uchun 7 ni bosing'''
a7_text = '''7-bosqich
#themetutorial
shuni tanlaymiz. gallereya ochiladi va rasm tanlaymiz. tanlabo'lganimidsn so'ng dasturdan butunlay chiqib ketamiz(oxirgilar royhatidan tozalaymiz ya'ni surib tashlaymiz)
endi dasturga(telegraph) qaytadan kiramiz.
Manzaraga esa o'zingiz guvoh bo'ling ;)

@TGraphUz kanaliga obuna bo'ling!'''

fon_text = '''
Chatlar ro'yhati orqa foniga Gallereyadan rasm qo'yish!

Guruhda eng ko'p berilayotgan savolga javob screenshotlar bilan @UZB_TELEGRAPH guruhiga #themetutorial heshtegi bilan yuborildi.
https://t.me/uzb_telegraph/206709

#theme #attheme #tutorial
@TGraphUz

Boshlash uchun 1 ni bosing'''

grs = 358031730

'''
ha = {
    'count':, 'members':
}
yoq = 0
'''
thanks = '''Arzimaydi 😉
Lekin raxmatni o'rniga tanishlaringizni @tgraphuz va @uzb_telegraph larga taklif qilsangiz yanada yaxshi bo'lardi😉'''

raxmat = str('raxmat Raxmat Raxmad tashakkur спасиба спвсибо').split()
token_list =[0]
qoidalar_list = []
ro_list = []
start_list = []
help_list = []
message_list = []

captcha = {'status':'off'}
