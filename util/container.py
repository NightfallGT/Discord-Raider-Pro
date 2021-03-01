class Container:
    def __init__(self):
        print('Discord Raider Pro v0.1 by Nightfall#2512')
        print('github.com/NightfallGT | discord.gg/e8Qy8JKbUK')
        self.file_path = None
        self.tokens = None

    def add_file_path(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path

    def add_tokens(self, tokens):
        self.tokens =tokens

    def get_tokens(self):
        return self.tokens

