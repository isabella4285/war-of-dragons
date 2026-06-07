from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.sound import *
import random
from player import Player
from clouds import CloudManager
from enemies import Focke_Wulf
from explosao import EfeitoExplosao



soundtrack = Sound("vai/artes/Trilha.mp3")  # Carrega a trilha sonora
#soundtrack.set_volume(0.5)  # Ajusta o volume da trilha sonora
soundtrack.set_repeat(True)  # Toca a trilha sonora em loop
soundtrack.play()  # Inicia a reprodução da trilha sonora
class Game:
    def __init__(self):
        # Inicialização da janela e inputs
        self.janela = Window(1500, 1000)
        self.teclado = Window.get_keyboard()
        self.run_game = True
        
        # Cenário estático
        self.fundo = Sprite("vai/artes/Fundo.png")
        self.retangulo = Sprite("caixas/ret.png")
        self.ret_menor = Sprite("caixas/ret_menor.png")
        
        self.posicionar_cenario()

        # Instanciando as entidades do jogo
        self.player = Player(self.janela)
        self.cloud_manager = CloudManager(self.janela)
        self.enemies = Focke_Wulf(self.janela)
        
        self.lista_explosoes = [] #para gerenciar o tanto de explosoes

    def posicionar_cenario(self):
        # Lógica de posicionamento dos retângulos estáticos
        self.retangulo.x = self.janela.width / 2 - self.retangulo.width / 2
        self.retangulo.y = self.janela.height - self.retangulo.height - 10

        self.ret_menor.x = self.retangulo.width + self.retangulo.x + 70
        self.ret_menor.y = self.retangulo.y

    def explosao(self, x, y):
        nova_explosao = EfeitoExplosao(x, y)
        self.lista_explosoes.append(nova_explosao)

    def checar_colisoes(self):
        tiros_player = self.player.get_tiros()
        naves_inimigas = self.enemies.get_naves()
        tiros_inimigos = self.enemies.get_tiros()

        #TIRO PLAYER VS NAVES INIMIGAS
        for tiro in tiros_player[:]: #[:] = copia da lista
            for nave in naves_inimigas[:]:
                if Collision.collided(tiro, nave):

                    pos_x = nave.x + (nave.width/2)
                    pos_y = nave.y + (nave.height/2)

                    tiros_player.remove(tiro)
                    naves_inimigas.remove(nave)
                    
                    self.explosao(pos_x, pos_y)

                    print("Nave inimiga abatida!")
                    break

        #colisao tiro inimigo vs player
        for tiro_inimigo in tiros_inimigos[:]:
            if Collision.collided(tiro_inimigo, self.player.player):
                tiros_inimigos.remove(tiro_inimigo)
                print("Jogador leva dano!")
                self.player.vida -= 1
                print(self.player.vida)
                if self.player.vida == 0:
                    print("GAME OVER")
                    self.run_game = False
    


    def run(self):
        # Loop principal do jogo
        while self.run_game:
            dt = self.janela.delta_time()

            # 1. Entrada de dados e Atualizações (Update)
            self.player.move(self.teclado)
            self.cloud_manager.update(dt)
            self.enemies.update(dt)

            self.checar_colisoes()

            for explosao in self.lista_explosoes:
                explosao.update(dt)

            self.lista_explosoes = [exp for exp in self.lista_explosoes if exp.ativa]

            self.player.intervalo(dt)
                
            self.player.shoot(self.teclado, dt)

            self.janela.set_background_color((100, 230, 255))
            
            self.fundo.draw()
            self.cloud_manager.draw()
            self.player.draw()
            self.enemies.draw()
            
            for explosao in self.lista_explosoes:
                explosao.draw()



            self.retangulo.draw()
            self.ret_menor.draw()

            self.janela.draw_text(f"Vidas: {self.player.vida}", self.janela.width - 150, self.janela.height-140, size=20, color = (0,0,0), font_name='Arial', bold=True)

            # 3. Atualiza a tela
            self.janela.update()

# Para rodar o jogo:
if __name__ == "__main__":
    jogo = Game()
    jogo.run()