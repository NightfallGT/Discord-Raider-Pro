import requests

class Setup:
    def __init__(self, tokens):
        self.tokens = tokens
        self.server_name = 'server'

    def _bot_inviter(self, token, inv_link):
        if len(inv_link) > 6:
                inv_link = inv_link[19:]

        headers = {'Authorization': token}
        api_link = "https://discordapp.com/api/v6/invite/" + inv_link

        bot_invite = requests.post(api_link, headers=headers)

        if 'message' in bot_invite.text:
            message = bot_invite.json()['message']
            print(f'Message: {message}')

        if 'guild' in bot_invite.text:
            server_name = bot_invite.json()['guild']['name']
            self.server_name = server_name
            print(f'Succesfully joined {server_name}')
        
        print(bot_invite.text)

    def _bot_leaver(self, token, guild_id):
        headers = {'Authorization': token}
        api_link = "https://discord.com/api/v8/users/@me/guilds/" + guild_id
        r = requests.delete(api_link, headers=headers)
        
        if r.status_code == 204:
            print(f'Succesfully left {self.server_name}')
        else:
            print(f'Tried to leave {self.server_name}')

    def server_join(self, inv_link):
        for x in self.tokens:
            self._bot_inviter(x, inv_link)

    def server_leave(self, guild_id):
        for x in self.tokens:
            self._bot_leaver(x, guild_id)