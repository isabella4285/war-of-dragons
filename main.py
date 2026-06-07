from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.scenemanager import Scene, SceneManager
from PPlay.parallax import ParallaxSystem

janela = Window(400, 700)

teclado = Window.get_keyboard()

player = Sprite("vai/Player.png")
capa = Sprite("vai/Capa.png")

player.x = janela.width//2 - player.width//2
player.y = janela .height - player.height - 10

fundo = ParallaxSystem()
fundo.add_layer("vai/artes/Fundo.png", 0.0)
fundo.add_layer("vai/artes/Nuvens.png", 0.4)

player.set_position((janela.width//2 - player.width//2), (janela.height - player.height - 10))

class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.fundo = (0, 0, 0)

    def loop(self):
        if self.teclado.key_down("ENTER"):
            #SceneManager.change_scene(MenuJog())
            pass

    def draw(self):
        self.janela.set_background_color(self.fundo)
        capa.draw()

class MenuJog(Scene):
    def __init__(self):
        super().__init__()

    def loop(self):
        if self.teclado.key_down("ESC"):
            SceneManager.change_scene(Menu())


    def draw(self):
        self.janela.set_background_color(0)
        fundo.draw()
        player.draw()

SceneManager.change_scene(Menu())

while True:
    SceneManager.run()
    janela.update()