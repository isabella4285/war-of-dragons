from PPlay.sprite import *
import random


class CloudManager:
    def __init__(self, window):
        self.window = window
        self.nuvens_passadas = []
        self.nuvens_arquivos = [
            "vai/Clouds/cloud1.png", 
            "vai/Clouds/cloud2.png", 
            "vai/Clouds/cloud3.png", 
            "vai/Clouds/cloud4.png", 
            "vai/Clouds/cloud5.png"
        ]
        self.time_fundo = 0
        self.spawn_rate = 1.0 # Tempo em segundos para nascer uma nova nuvem
        self.speed = 150 # Velocidade das nuvens

    def update(self, dt):
        self.time_fundo += dt
        
        # Criação de nuvens
        if self.time_fundo >= self.spawn_rate:
            nuvem = Sprite(random.choice(self.nuvens_arquivos))
            nuvem.x = random.randint(0, int(self.window.width - nuvem.width))
            nuvem.y = -nuvem.height
            self.nuvens_passadas.append(nuvem)
            self.time_fundo = 0

        # Atualiza posições
        for nuvem in self.nuvens_passadas:
            nuvem.y += self.speed * dt

        # Filtra apenas as nuvens que ainda estão na tela
        self.nuvens_passadas = [n for n in self.nuvens_passadas if n.y <= self.window.height]

    def draw(self):
        for nuvem in self.nuvens_passadas:
            nuvem.draw()