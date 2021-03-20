import requests, threading, time
# Threading so the join is way more faster
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
            if bot_invite.status_code == 429:
                time.sleep(bot_invite.json()['retry_after'])
                self._bot_inviter(token, inv_link)
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
            elif r.status_code == 429:
                time.sleep(r.json()['retry_after'])
                self._bot_leaver(token, guild_id)
            else:
                print(f'Failed to leave {self.server_name} [{r.status_code} {r.json()}]')

        def server_join(self, inv_link):
            for x in self.tokens:
                threading.Thread(target=self._bot_inviter, args=[x, inv_link]).start()

        def server_leave(self, guild_id):
            for x in self.tokens:
                threading.Thread(target=self._bot_leaver, args=[x, guild_id]).start()
