from PPlay.sound import *
from PPlay.sprite import *


class EfeitoExplosao:
    def __init__(self, x, y):
        self.frames = ["frames/one.png", "frames/two.png", "frames/three.png", "frames/four.png", "frames/five.png"]
        self.frame_atual = 0
        self.tempo_acumulado = 0
        self.intervalo = 0.1
        self.ativa = True
        self.som = Sound("explosao_bomba.mp3")
        self.som.play()

        #pegar primeiro frame para colocar na posicao correta
        self.sprite = Sprite(self.frames[self.frame_atual])
        self.sprite.x = x-(self.sprite.width/2) #depois colocar posicoes certinhas da nave atingida
        self.sprite.y = y-(self.sprite.height/2)

    def update(self, dt):
        self.tempo_acumulado += dt
        if self.tempo_acumulado >=self.intervalo:
            self.tempo_acumulado = 0
            self.frame_atual += 1

            if self.frame_atual <len(self.frames):
                x_atual = self.sprite.x
                y_atual = self.sprite.y
                self.sprite = Sprite(self.frames[self.frame_atual]) 
                self.sprite.x = x_atual
                self.sprite.y = y_atual
            else:
                self.ativa = False
    def draw(self):
        if self.ativa:
            self.sprite.draw()
