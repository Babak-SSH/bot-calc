#!/.local/lib/python3.6
# -*- coding: utf-8 -*-
import telepot
import time
import urllib3
import telebot
import time
from calculator_logic import calculate


#this part is for server settings 
proxy_url = "SERVER:PORT" #your proxy server
telepot.api._pools = {'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))



def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            print(m.text) # prints the sent message to the console


bot = telebot.TeleBot('<TOKEN>') #your <TOKEN> goes here
bot.set_update_listener(listener)  # register listener


@bot.message_handler(commands=['help']) #Discribes how to use and what it is doing
def help_command(m):
	bot.send_message(m.chat.id, '''
    it is  calcroid you can start by typing /calculate and get out with /exit command
    ''')


@bot.message_handler(commands=['calculate'])#turn on the calculation function
def calc_start(m):
    bot.reply_to(m, "ok")
    bot.send_message(m.chat.id, "what you want me to do?")
    global comm
    comm = 1
    return


@bot.message_handler(commands=['exit'])#turn off the functions
def exit_command(m) :
    global comm
    comm = 0
    bot.send_message(m.chat.id, "thanks for using my bot")
    return


def error_type(m) :
    bot.send_message(m.chat.id, "error :(")#any other kind of not defined texts will lead to error (temporary)
    return


@bot.message_handler(func=lambda message: True, content_types = ['text']) #the main calculation function
def calc_msg(m):  
        try :
            if comm == 1 :
                s = str(m.text)
                group = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','(',')','!'] #all acceptble characters for calculating
                for ele in range(0,len(s)) :
                    if s[ele] in group :
                        b = True
                    else :
                        b = False
                        break
                if b == True :
                    anw = calculate(m.text)#logic
                    bot.reply_to(m, anw)
                elif b == False :
                    error_type(m)
            else:
                error_type(m)
        except NameError :
            bot.send_message(m.chat.id, "use /help")
            error_type(m)


print ('Listening ...')#just to see if it connects

bot.polling()#starting bot


# Keep the program running.
while 1:
    time.sleep(10)