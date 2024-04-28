import pygame


class User(pygame.sprite.Sprite):
    def __init__(self, id, username, chat_id, group, script):
        super().__init__(group)
        self.id = id
        self.username = username
        self.chat_id = chat_id
        self.action_list = [script]
        self.registered = []
        self.answers = []
        self.q = ''
        self.poll = []
        self.anws = []
