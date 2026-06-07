import random
from PPlay.sprite import *
from PPlay.sound import *

# focke wulf = mais rapidoAeronaves inimigas:
'''Unidades de diferentes tipos que aparecem de forma constante pelas bordas
superior e inferior da tela. Por ordem de velocidade:
- Focke Wulf: o avião mais rápido.

- Messerschmitt BF 109 F: segundo mais rápido.

- He 111: avião bombardeiro que não atira, mas tem mais vida que os demais.
Caso o jogador falhe em derrubá-lo em certo intervalo de tempo, recebe
dano. É o avião mais lento.

Dragão Gigante (the Final Boss):
O grande objetivo da missão. Um dragão de espécie rara, maior, mais rápido e mais
ameaçador que o do jogador.


4. Interface de Usuário
Contador de Pontuação:
Display numérico para o score do jogador.
Indicador de Vidas/Multiplicador:
Ícones indicando o estado atual do jogador.
Cronômetro/Tempo de Jogo:
Relógio para marcar o progresso da missão
Caixa de diálogo/Texto:
Espaço para informaçẽos constantes de batalhas e desenvolvimento da história.'''


"""fazer uma lista e no main, escolher aleatoriamente o inimigo que vai aparecer. de acordo com a selecao, vai ser a classe que sera chamada aqui"""


lista_enemies = ["Focke_Wulf", ]

class Focke_Wulf:
    def __init__(self, window):
        self.window = window
        self.spawn_rate = 1.5 # intervalo para criacao deles 
        self.time = 0
        
        self.vida = 1


        self.speed_y = 250
        self.cooldown_tiro = 0.8 # delay de 0.3 segundos entre os tiros
        self.time_intervalo = 0
      

        self.lista_tiros = []
        self.naves_passadas = []
    
    def update(self, dt):
        self.time += dt
        self.time_intervalo += dt  # Controla o tempo entre um tiro e outro

        # Criação de novas naves
        if self.time >= self.spawn_rate:
            nova_nave = Sprite("vai/avioes/fw.png")
            nova_nave.x = random.randint(0, int(self.window.width - nova_nave.width))
            nova_nave.y = -nova_nave.height#random.randint(self.window.height, -self.enemy.height)
            self.naves_passadas.append(nova_nave)
            self.time = 0

        # Atualiza posições
        for nave in self.naves_passadas:
            nave.y += self.speed_y*dt
        
        self.shoot(dt)

        # Filtra apenas as nuvens que ainda estão na tela
        self.naves_passadas = [n for n in self.naves_passadas if n.y <= self.window.height]
        self.lista_tiros = [tiro for tiro in self.lista_tiros if tiro.y < self.window.height+tiro.height]
        
    def shoot(self, dt):
            if self.time_intervalo >= self.cooldown_tiro:
                # IMPORTANTE: Criar um NOVO Sprite para cada tiro, senão você moverá o mesmo objeto sempre
                for nave in self.naves_passadas:
                    novo_tiro = Sprite("vai/artes/fogo.png")
                    novo_tiro.x = nave.x + (nave.width // 2) - (novo_tiro.width // 2)
                    novo_tiro.y = nave.y+nave.height
                    self.lista_tiros.append(novo_tiro)
                #self.fire_sound.play()  # Toca o som do tiro
                self.time_intervalo = 0 # Reseta o cooldown

            # 2. MOVIMENTAÇÃO E LIMPEZA: Roda SEMPRE (fora do 'if' do teclado)
            for tiro in self.lista_tiros:
                tiro.y += 450 * dt  # Move todos os tiros existentes para baixo

            # Remove da lista os tiros que já sumiram pelo topo da tela
            
    def get_naves(self):
        return self.naves_passadas
    
    def get_tiros(self):
        return self.lista_tiros

    def draw(self):
        for nave in self.naves_passadas:
            nave.draw()
        for tiro in self.lista_tiros:
            tiro.draw()