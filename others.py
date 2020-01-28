
token = '<token>'

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



newtext = '''[{0}](tg://user?id={1}) *safimizga hush kelibsiz!*

Guruhda yozish imkoniga ega bo'lish uchun:
`- Bot qo'llanmasi bilan tanishib chiqing!`
`- Umumiy qoidalar bilan tanishib chiqqach "Roziman" knopkasi orqali botga start bosing!`
Shundan so'nggina guruhda yoza olasiz.
Bular guruhda tartibni saqlash maqsadida qilingan! Bizni to'g'ri tushunasiz degan umiddamiz.


*TGraphUz*
'''

grs = 358031730


login = []
id_user = []
id_msg = []
id_chat = []


token_list =[0]
qoidalar_list = []
ro_list = []
start_list = []
help_list = []
message_list = []
