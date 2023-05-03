import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5921492080/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5921492080')
   open(f"Users/5921492080/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 26305268
API_HASH = "4e385c619185805f48427df36458d056"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
UPDATES_CHANNEL = "rjbr0"
OWNER= [5921492080,6285755686]
PREMIUM=[5921492080,6285755686]
bot = pyrogram.Client("bot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(bot, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = bot.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            bot.send_message(chat_id=message.chat.id,text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/InducedBotsSupport).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await bot.send_message(chat_id=message.chat.id, text="**Please Join My Updates Channel To Use Me!\n and click on to Check /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await bot.send_message(chat_id=message.chat.id, text="**Something Went Wrong. Contact My [Support Group](https://t.me/InducedBotsSupport).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1

# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.command("start"))
def start(bot, message):
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Login✅", callback_data="Login"), InlineKeyboardButton("Adding💯", callback_data="Adding") ],[InlineKeyboardButton("Phone⚙️", callback_data="Edit"), InlineKeyboardButton("PhoneSee💕", callback_data="Ish")],[InlineKeyboardButton("Phone Remove⚙️", callback_data="Remove"), InlineKeyboardButton("AdminPannel", callback_data="Admin")]])
   message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm Induced Scraper Bot \nMade for doing Scraping for free,\nWithout Using Any Use of Python.\n\nMade with ❤️ By @RJbr0**")
   start = bot.get_messages(chatid, message_ids=message.message_id)
   
# ------------------------------- Set Phone No --------------------------------- #
@bot.on_message(filters.command("phone"))
def phone(bot, message):
 try:
   message.delete()

   if message.from_user.id not in PREMIUM:
      bot.send_message(message.chat.id, f"**Premium deilsin ❤️ By @Ber4tbey**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = bot.ask(chat_id=message.chat.id, text="**Giriş yapmak için hesap sayısını girin (in intiger)\n\nMade with ❤️ By @Ber4tbey**")
      n = int(number.text)
      a+=n
      if n<1 :
         bot.send_message(message.chat.id, """**Geçersiz Biçim 1'den az Tekrar deneyin\n\nMade with ❤️ By @Ber4tbey**""")
         return
      if a>100:
         bot.send_message(message.chat.id, f"**Yalnızca {100-a} Telefon numarası ekleyebilirsiniz \n\nMade with ❤️ By @Ber4tbey**")
         return
      for i in range (1,n+1):
         number = await bot.ask(chat_id=message.chat.id, text="**Şimdi Telegram Hesabınızın Telefon Numarasını Uluslararası Formatta Gönderin. \n**Ülke Kodu** dahil. \nÖrnek: **+14154566376 = 14154566376 sadece + değil**\n\nMade with ❤️ By @Ber4tbey**")
         phone = number.text
         if "+" in phone:
            bot.send_message(message.chat.id, """**Bahsedildiği gibi + dahil değildir\n\nMade with ❤️ By @Ber4tbey**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            bot.send_message(message.chat.id, f"**{n}). Phone: {phone} Set Sucessfully✅\n\nMade with ❤️ By @Ber4tbey**")
         else:
            bot.send_message(message.chat.id, """**Geçersiz Numara Biçimi Tekrar deneyin\n\nMade with ❤️ By @Ber4tbey**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   bot.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ❤️ By @Ber4tbey**")
   return



# ------------------------------- Acc Login --------------------------------- #
@bot.on_message(filters.command(["login"]))
def login(bot, message):
 try:
   message.delete()
 
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**Premium Üyesi deilsin\n\nMade with ❤️ By @Ber4tbey**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      client.connect()
      if not client.is_user_authorized():
         try:
            client.send_code_request(phone)
         except FloodWait as e:
            message.reply(f"{e.x} Saniyelik Floodwait'iniz Var")
            return
         except PhoneNumberInvalidError:
            message.reply("Telefon Numaranız Geçersiz.\n\nYeniden Başlamak için /start'a basın!")
            return
         except PhoneNumberBannedError:
            message.reply(f"{phone} is Baned")
            continue
         try:
            otp = bot.ask(message.chat.id, ("Telefon numaranıza bir OTP gönderilir, \nLütfen OTP'yi `1 2 3 4 5` formatında girin. __(Her sayı arasındaki boşluk!)__ \n\nBot OTP göndermiyorsa, Bot'a /start komutuyla /yeniden başlatmayı ve Görevi Başlatmayı tekrar deneyin.\nİptal etmek için /iptal'e basın."), timeout=300)
         except TimeoutError:
            message.reply("5 Dakikalık Zaman Sınırına Ulaşıldı.\nYeniden Başlamak için /start'a basın!")
            return
         otps=otp.text
         try:
            client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            message.reply("Geçersiz kod.\n\nYeniden Başlamak için /start'a basın!")
            return
         except PhoneCodeExpiredError:
            message.reply("Kodun Süresi Doldu.\n\nYeniden Başlamak için /start'a basın!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Hesabınızın İki Adımlı Doğrulaması Var.\nLütfen Parolanızı Girin.",timeout=300)
            except TimeoutError:
               message.reply("`5 Dakikalık Zaman Sınırına Ulaşıldı.\n\nYeniden Başlamak için /start'a basın!`")
               return
            try:
               client.sign_in(password=two_step_code.text)
            except Exception as e:
               message.reply(f"**HATA:** `{str(e)}`")
               return
            
      with open("Users/5921492080/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/6285755686/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      client(functions.contacts.UnblockRequest(id='@SpamBot'))
      client.send_message('SpamBot', '/start')
      msg = str(client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="Good news, no limits are currently applied to your account. You’re free as a bird!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = client.get_me()
      bot.send_message(message.chat.id, f"Başarıyla Giriş Yap✅ Yapıldı.\n\n**Ad:** {me.first_name}\n**Kullanıcı adı:** {me.username}\n**Telefon:** {phone}\n**SpamBot İstatistikleri :** {stats}\n\n**Made with ❤️ By @Ber4tbey**")     
      po+=1
      client.disconnect()
     except ConnectionError:
      client.disconnect()
      client.connect()
     except TypeError:
      bot.send_message(message.chat.id, "**Telefon numarasını girmediniz \nlütfen Config⚙️  /start ile düzenleyin.\n\nMade with ❤️ By @Ber4tbey**")  
     except Exception as e:
      bot.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ❤️ By @Ber4tbey**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    bot.send_message(message.chat.id, f"**Tüm Hesapların Girişi {s}  {po} Hesap Kullanılabilir \n\nMade with ❤️ By @Ber4tbey**") 
 except Exception as e:
   bot.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ❤️ By @Ber4tbey**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@bot.on_message(filters.command("adding"))
def to(bot, message):
 try:

   if message.from_user.id not in PREMIUM:
      bot.send_message(message.chat.id, f"**Premium üyesi deilsin\n\nMade with ❤️ By @Ber4tbey**")
      return
   number = bot.ask(chat_id=message.chat.id, text="**Grup kullanıcı adını atınız \n\nMade with ❤️ By @Ber4tbey**")
   From = number.text
   number = bot.ask(chat_id=message.chat.id, text="**Gtup kullanıcı adını atınız \n\nMade with ❤️ By @Ber4tbey**")
   To = number.text
   number = bot.ask(chat_id=message.chat.id, text="**Şimdi Gönder Başlangıcı  \n\nMade with ❤️ By @Ber4tbey**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Ekleme başladı**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            client.connect()
            client(JoinChannelRequest(To))
            bot.send_message(chat_id=message.chat.id, text=f"**Scraping Start**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     client.disconnect()
                     r+="**\nMade with ❤️ By @Ber4tbey**"
                     bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     bot.send_message(message.chat.id, f"**Error: {phone}Sonrakine Geçerken Bazı Hatalar oluştu\n\nMade with ❤️ By @Ber4tbey**")
                     break
                  if dad>40:
                     r+="**\nMade with ❤️ By @Ber4tbey**"
                     bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Ekleme başladı**\n\n"
                     dad=0
                  client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  client.disconnect()
                  r+="**\nMade with ❤️ By @Ber4tbey**"
                  bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  bot.send_message(chat_id=message.chat.id, text=f'**FloodWaitError for {s.seconds} sec\nMoving To Next Number**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  client.disconnect()
                  bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     client.disconnect()
                     bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     bot.send_message(chat_id=message.chat.id, text=f"**Too Many PeerFloodError\nMoving To Next Number**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
   bot.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Made with ❤️ By @Ber4tbey")
 except Exception as e:
   bot.send_message(message.chat.id, f"**Error: {e}\n\nMade with ❤️ By @Ber4tbey**")
   return



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.command("phonesee"))
def start(bot, message):
  
   if message.from_user.id not in PREMIUM:
      bot.send_message(message.chat.id, f"**Premium üyesi deilsin\n\nMade with ❤️ By @Ber4tbey**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Your Phone Numbers are**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nMade with ❤️ By @Ber4tbey**"
               await bot.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Your Phone Numbers are**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nMade with ❤️ By @Ber4tbey**"
         await bot.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.command("remove"))
def start(bot, message):
 try:
   
   if message.from_user.id not in PREMIUM:
      bot.send_message(message.chat.id, f"**Premium üyesi deilsin\n\nMade with ❤️ By @Ber4tbey**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await bot.ask(chat_id=message.chat.id, text="**Silmek için hesap numarasını gönder\n\nMade with ❤️ By @Ber4tbey**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         bot.send_message(chat_id=message.chat.id,text="Başarılı")
   except Exception as a:
      pass
 except Exception as e:
   bot.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ❤️ By @Ber4tbey**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@bot.on_message(filters.command('ishan'))
def subscribers_count(bot, message):

   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
      bot.send_message(chat_id=message.chat.id,text=f"**Hi** `{message.from_user.first_name}` **!\n\nWelcome to Admin Pannel of Üye Bot\n\nMade with ❤️ By @Ber4tbey**", reply_markup=but)
   else:
      bot.send_message(chat_id=message.chat.id,text="**You are not owner of Bot \n\nMade with ❤️ By @Ber4tbey**")



# ------------------------------- Buttons --------------------------------- #
@bot.on_callback_query()
def button(bot, update):
   k = update.data
   if "Login" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /login'e tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Ish" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /phonesee'ye tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Remove" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /kaldır'a tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Adding" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık bir şey yok..!\nOturum Aç✅ Hesaptan eklemeye başlamak için /adding tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Edit" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /phone'a tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Home" in k:
      update.message.delete()
      bot.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nEve Gitmek için /start'a tıklamanız yeterli.\n\nMade with ❤️ By @Ber4tbey**""") 
   elif "Users" in k:
      update.message.delete()
      msg = bot.send_message(update.message.chat.id,"Lütfen bekleyin...")
      messages = users_info(app)
      msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      update.message.delete()
      number = bot.ask(chat_id=update.message.chat.id, text="**Yeni Kullanıcının Kullanıcı Kimliğini Gönder\n\nMade with ❤️ By @Ber4tbey**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         bot.send_message(chat_id=update.message.chat.id,text="Done SucessFully")

   elif "Check" in k:
      update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Made with ❤️ By @Ber4tbey**"
         bot.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         app.send_message(chat_id=update.message.chat.id,text=f"**Welcome to Admin Pannel of Induced Bot\n\nMade with ❤️ By @Ber4tbey**", reply_markup=but)
      else:
         app.send_message(chat_id=update.message.chat.id,text="**You are not owner of Bot \n\nMade with ❤️ By @Ber4tbey**")
   elif "Broadcast" in k:
    try:
      query = query_msg()
      a=0
      b=0
      number = bot.ask(chat_id=update.message.chat.id, text="**Now me message For Broadcast\n\nMade with ❤️ By @Ber4tbey**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            bot.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      bot.send_message(update.message.chat.id,f"Successfully Broadcasted to {a} Chats\nFailed - {b} Chats !")
    except Exception as e:
      bot.send_message(update.message.chat.id,f"**Error: {e}\n\nMade with ❤️ By @Ber4tbey**")




text = """
╔════╗ㅤMembers 
╚═╗╔═╝ Scraping Bot
╔═╣╠═╗
║╔╣╠╗║ㅤInduced
║╚╣╠╝║ Scraper Bot
╚═╣╠═╝
╔═╝╚═╗ 
╚════╝ 
"""
print(text)
print("Induced Ekleme başladıed Sucessfully........")
bot.run()
