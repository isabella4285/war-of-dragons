from PPlay.sprite import *
from PPlay.sound import *

class Player:
    def __init__(self, window):
        self.window = window
        self.player = Sprite("vai/Player.png")
        # Centraliza o player na base da tela
        self.player.x = window.width // 2 - self.player.width // 2
        self.player.y = window.height - self.player.height - 10
        self.speed_x = 2
        self.speed_y = 5
        self.vida = 10

        #sobre o tiro
        self.tiro = Sprite("vai/artes/tiro.png")
        self.fire_sound = Sound("vai/artes/dragon_fire.mp3")  # Carrega o som do tiro
        self.lista_tiros = []
        self.lista_rastro = []
        self.time_intervalo = 0
        self.cooldown_tiro = 0.3 # delay de 0.3 segundos entre os tiros
    
    def intervalo(self, dt):
        self.time_intervalo += dt  # Controla o tempo entre um tiro e outro
        
    
    def move(self, keyboard):
        if keyboard.key_pressed("UP") and self.player.y > 0:
            self.player.y -= self.speed_y
        if keyboard.key_pressed("DOWN") and self.player.y < self.window.height - self.player.height:
            self.player.y += self.speed_y
        if keyboard.key_pressed("LEFT") and self.player.x > 0:
            self.player.x -= self.speed_x
        if keyboard.key_pressed("RIGHT") and self.player.x < self.window.width - self.player.width:
            self.player.x += self.speed_x
    def shoot(self, keyboard, dt):
            # 1. CRIAÇÃO DO TIRO: Só acontece quando aperta ESPAÇO e o cooldown resetou
            if keyboard.key_pressed("SPACE") and self.time_intervalo >= self.cooldown_tiro:
                # IMPORTANTE: Criar um NOVO Sprite para cada tiro, senão você moverá o mesmo objeto sempre
                novo_tiro = Sprite("vai/artes/tiro.png")
                novo_tiro.x = self.player.x + (self.player.width // 2) - (novo_tiro.width // 2)
                novo_tiro.y = self.player.y - novo_tiro.height
                
                self.lista_tiros.append(novo_tiro)
                self.fire_sound.play()  # Toca o som do tiro
                self.time_intervalo = 0 # Reseta o cooldown

            # 2. MOVIMENTAÇÃO E LIMPEZA: Roda SEMPRE (fora do 'if' do teclado)
            for tiro in self.lista_tiros:
                tiro.y -= 400 * dt  # Move todos os tiros existentes para cima

            # Remove da lista os tiros que já sumiram pelo topo da tela
            self.lista_tiros = [tiro for tiro in self.lista_tiros if tiro.y > -tiro.height]

    def get_tiros(self):
        return self.lista_tiros

    def draw(self):
        self.player.draw()
        for tiro in self.lista_tiros:
            tiro.draw()