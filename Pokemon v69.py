import pygame
import os
import random

class ataque:
    name = None
    dmg = 0
    acc = 0
    pp = 0
    maxpp = 0

    def __init__(self, name, dmg, acc, maxpp):
        self.name = name
        self.dmg = dmg
        self.acc = acc
        self.pp = maxpp
        self.maxpp = maxpp

    def useon(self, seupkm, pkmadversario):
        super_efetivo = 'no'
        if seupkm.type == 'Water' and pkmadversario.type == 'Fire':
            super_efetivo = 'yes'
        elif seupkm.type == 'Fire' and pkmadversario.type == 'Grass':
            super_efetivo == 'yes'
        elif seupkm.type == 'Electric' and pkmadversario.type == 'Water' or seupkm.type == 'Electric' and \
                pkmadversario.type == 'Flying':
            super_efetivo = 'yes'
        elif seupkm.type == 'Flying' and pkmadversario.type == 'Grass':
            super_efetivo = 'yes'
        elif seupkm.type == 'Grass' and pkmadversario.type == 'Water':
            super_efetivo = 'yes'

        not_very_effective = 'no'
        if pkmadversario.type == 'Water' and seupkm.type == 'Fire' or pkmadversario.type == seupkm.type:
            not_very_effective = 'yes'
        elif pkmadversario.type == 'Fire' and seupkm.type == 'Grass' or pkmadversario.type == seupkm.type:
            not_very_effective = 'yes'
        elif pkmadversario.type == 'Electric' and seupkm.type == 'Flying' or pkmadversario.type == seupkm.type:
            not_very_effective = 'yes'
        elif pkmadversario.type == 'Flying' and seupkm.type == 'Grass' or pkmadversario.type == seupkm.type:
            not_very_effective = 'yes'
        elif pkmadversario.type == 'Grass' and seupkm.type == 'Water' or pkmadversario.type == 'Grass' and \
                seupkm.type == 'Electric' or pkmadversario.type == seupkm.type:
            not_very_effective = 'yes'

        if self.pp > 0 and self.acc >= random.randrange(0, 100):
            if super_efetivo == 'yes':
                pkmadversario.hp -= 2 * int(self.dmg)
                self.pp -= 1
                return ('super')
            elif super_efetivo == 'no':
                if not_very_effective == 'yes':
                    pkmadversario.hp -= int(self.dmg) / 2
                    self.pp -= 1
                    return ('dumb')
                elif not_very_effective == 'no':
                    pkmadversario.hp -= int(self.dmg)
                    self.pp -= 1
                    return ('normal')

        else:
            #print(seupkm.nome + "'s" + ' attack missed!')
            return ('miss')


#Ataques Blastoise        (acc padrão-30, para ficar mais interessante, ter mais reviravoltas e coisa do tipo)
Bubble = ataque('Bubble', 40, 100-30, 30)
Water_Gun = ataque('Water Gun', 40, 100-30, 25)
Hydro_Pump = ataque('Hydro Pump', 110, 80-30, 5)
Skull_Bash = ataque('Skull Bash', 130, 100-30, 10)
Blastoise_atks = (Bubble, Water_Gun, Hydro_Pump, Skull_Bash)

#Ataques Blastoise2
Bubble2 = ataque('Bubble', 40, 100-30, 30)
Water_Gun2 = ataque('Water Gun', 40, 100-30, 25)
Hydro_Pump2 = ataque('Hydro Pump', 110, 80-30, 5)
Skull_Bash2 = ataque('Skull Bash', 130, 100-30, 10)
Blastoise_atks2 = (Bubble2, Water_Gun2, Hydro_Pump2, Skull_Bash2)

#Ataques Charizard
Ember = ataque('Ember', 40, 100-30, 25)
Heat_Wave = ataque('Heat Wave', 95, 90-30, 10)
Flamethrower = ataque('Flamethrower', 130, 90-30, 5)
Overheat = ataque('Overheat', 130, 90-30, 5)
Charizard_atks = (Ember, Heat_Wave, Flamethrower, Overheat)

#Ataques Charizard2
Ember2 = ataque('Ember', 40, 100-30, 25)
Heat_Wave2 = ataque('Heat Wave', 95, 90-30, 10)
Flamethrower2 = ataque('Flamethrower', 130, 90-30, 5)
Overheat2 = ataque('Overheat', 130, 90-30, 5)
Charizard_atks2 = (Ember2, Heat_Wave2, Flamethrower2, Overheat2)

#Ataques Jolteon
Thunder_Shock = ataque('Thunder Shock', 50, 100-30, 30)
Thunder = ataque('Thunder', 130, 70-30, 10)
Shock_Wave = ataque('Shock Wave', 80, 100-30, 20)
Hyper_Beam = ataque('Hyper Beam', 170, 90-30, 5)
Jolteon_atks = (Thunder_Shock, Thunder, Shock_Wave, Hyper_Beam)

#Ataques Jolteon2
Thunder_Shock2 = ataque('Thunder Shock', 40, 100-30, 30)
Thunder2 = ataque('Thunder', 110, 70-30, 10)
Shock_Wave2 = ataque('Shock Wave', 60, 100-30, 20)
Hyper_Beam2 = ataque('Hyper Beam', 150, 90-30, 5)
Jolteon_atks2 = (Thunder_Shock2, Thunder2, Shock_Wave2, Hyper_Beam2)

#Ataques Pidgeot
Gust = ataque('Gust', 40, 100-30, 35)
Wing_Attack = ataque('Wing Attack', 60, 100-30, 35)
Air_Cutter = ataque('Air Cutter', 60, 95-30, 25)
Fly = ataque('Fly', 90, 95-30, 15)
Pidgeot_atks = (Gust, Wing_Attack, Air_Cutter, Fly)

#Ataques Pidgeot
Gust2 = ataque('Gust', 40, 100-30, 35)
Wing_Attack2 = ataque('Wing Attack', 60, 100-30, 35)
Air_Cutter2 = ataque('Air Cutter', 60, 95-30, 25)
Fly2 = ataque('Fly', 90, 95-30, 15)
Pidgeot_atks2 = (Gust2, Wing_Attack2, Air_Cutter2, Fly2)

#Ataques Venussaur
Vine_Whip = ataque('Vine Whip', 45, 100-30, 25)
Razor_Leaf = ataque('Razor Leaf', 55, 95-30, 25)
Solar_Beam = ataque('Solar Beam', 120, 100-30, 10)
Magical_Leaf = ataque('Magical Leaf', 60, 100-30, 20)
Venusaur_atks = (Vine_Whip, Razor_Leaf, Solar_Beam, Magical_Leaf)

#Ataques Venussaur
Vine_Whip2 = ataque('Vine Whip', 45, 100-30, 25)
Razor_Leaf2 = ataque('Razor Leaf', 55, 95-30, 25)
Solar_Beam2 = ataque('Solar Beam', 120, 100-30, 10)
Magical_Leaf2 = ataque('Magical Leaf', 60, 100-30, 20)
Venusaur_atks2 = (Vine_Whip2, Razor_Leaf2, Solar_Beam2, Magical_Leaf2)

#Ataques Jorge
Jorge = ataque('Jorge', 9001, 10000000, 4242)
Jorge_atks = (Jorge, Jorge, Jorge, Jorge)
Jorge_atks2 = (Jorge, Jorge, Jorge, Jorge)

class Pokemon:
    nome = None
    maxhp = 0
    hp = 0
    atks = None
    type = None

    def __init__(self, name, maxhp, atks, type):
        self.nome = name
        self.maxhp = int(maxhp)
        self.hp = int(maxhp)
        #atks -> list(atk1, atk2, ...)
        self.atks = atks
        self.type = type

    def faintcheck(self):
        if self.hp <= 0:
            print(self.nome + ' has fainted!')
            return(True)

#Criando os pokemons (2 de cada, caso o player 2 seja o mesmo pokemon do player 1)

Blastoise = Pokemon('Blastoise', 362, Blastoise_atks, 'Water')
Charizard = Pokemon('Charizard', 360, Charizard_atks, 'Fire')
Jolteon = Pokemon('Jolteon', 334, Jolteon_atks, 'Electric')
Pidgeot = Pokemon('Pidgeot', 370, Pidgeot_atks, 'Flying')
Venusaur = Pokemon('Venusaur', 364, Venusaur_atks, 'Grass')

Blastoise2 = Pokemon('Blastoise', 362, Blastoise_atks2, 'Water')
Charizard2 = Pokemon('Charizard', 360, Charizard_atks2, 'Fire')
Jolteon2 = Pokemon('Jolteon', 334, Jolteon_atks2, 'Electric')
Pidgeot2 = Pokemon('Pidgeot', 370, Pidgeot_atks2, 'Flying')
Venusaur2 = Pokemon('Venusaur', 364, Venusaur_atks2, 'Grass')

Jorge = Pokemon('Jorge', 1000000, Jorge_atks, 'Fire')
Jorge2 = Pokemon('Jorge', 1000000, Jorge_atks2, 'Fire')

y=0
pygame.init()
pygame.mixer.init()

def goodbye(win):
    # Programa ativado ao fechar a pagina
    fon = win.get_rect()
    fundo = pygame.image.load(os.path.join(".\\imagens", "goodbye.jpg")).convert_alpha()
    fundo = pygame.transform.scale(fundo, (fon[2], fon[3]))
    win.blit(fundo, (0,0))
    pygame.display.update()
    a = pygame.mixer.Sound(os.path.join(".\\Audios", "GoodbyeJoJo.wav"))
    a.play()
    pygame.time.wait(2500)


c = {"amarelo":(255, 255, 0), "azul":(0,0,255), "branco": (255,255,255), "cinza": (200,200,200), "preto": (0,0,0),
     "verde": (0,255,0), "vermelho":(255,0,0), 140:"azul", "fundo": (100, 100, 100), 230: "vermelho", 320: "amarelo",
     410: "cinza", 500: "verde"} #dicionario cores
p = {590: "Jorge",140:"Blastoise", 230: "Charizard", 320: "Jolteon", 410: "Pidgeot", 500: "Venusaur"} #dicionario pokemon
u = {"FigBag": 415, "PokRun" : 470, "FigPok" : 430, "BagRun" : 610, "Fight" : [430, 415], "Bag" : [610, 415],
     "Pokemon" : [430, 470], "Run" : [610, 470]} # Dicionario opcoes

class Window:
    __width = 0 #largura
    __height = 0 #altura
    __color = (0, 0, 0) #cor
    def __init__(self, largura, altura): #construtor
        self.__width = largura
        self.__height = altura
    def returnWinSize(self): #retorna tamanho da tela
        return (self.__width, self.__height)
    def returnColor(self): #retorna a cor da janela
        return self.__color

class Picture:
    __imagem = 0
    __width = 0
    __heigh = 0
    def __init__(self, str):
        imagem = pygame.image.load(os.path.join(".\\imagens", str)).convert_alpha()
        x = imagem.get_rect()
        self.__imagem = imagem
        self.__width = x[2]
        self.__heigh = x[3]
    def ajuste_hor(self, x):
        # pega e corrige a escala do y para o x dado
        b = ((int(x), round((self.__heigh * x / self.__width))))
        fundo = pygame.transform.scale(self.__imagem, b)
        self.__imagem = fundo
    def ajuste_ver(self, y):
        # pega e corrige a escala do x para o y dado
        b = ((round((self.__width * y / self.__heigh)), int(y)))
        fundo = pygame.transform.scale(self.__imagem, b)
        self.__imagem = fundo
    def get_rect(self):
        a = self.__imagem.get_rect()
        return(a)
    def tela(self, win, x):
        win.blit(self.__imagem, x)

class Vid:
    __imagem = 0
    __width = 0
    __heigh = 0
    def __init__(self, str):
        imagem = pygame.image.load(os.path.join(".\\Video", str)).convert_alpha()
        x = imagem.get_rect()
        self.__imagem = imagem
        self.__width = x[2]
        self.__heigh = x[3]
    def ajuste_hor(self, x):
        # pega e corrige a escala do y para o x dado
        b = ((int(x), round((self.__heigh * x / self.__width))))
        fundo = pygame.transform.scale(self.__imagem, b)
        self.__imagem = fundo
    def ajuste_ver(self, y):
        # pega e corrige a escala do x para o y dado
        b = ((round((self.__width * y / self.__heigh)), int(y)))
        fundo = pygame.transform.scale(self.__imagem, b)
        self.__imagem = fundo
    def get_rect(self):
        a = self.__imagem.get_rect()
        return(a)
    def tela(self, win, x):
        win.blit(self.__imagem, x)

def video():
    w = Window(800, 533)
    win = pygame.display.set_mode(w.returnWinSize())
    pygame.display.set_caption('Introdução')
    pygame.mixer.music.load(os.path.join(".\\Audios", "PLGIE.wav"))
    pygame.mixer.music.play(0)
    vi = h = 1
    run = d = True
    while run:
        clock = pygame.time.Clock()
        clock.tick(10)
        if vi<10:
            vid = Vid("Pok0000" + str(vi) + ".png")
            vid.ajuste_hor(800)
            vid.tela(win, (0, 0))
            pygame.display.update()
        elif vi<100:
            vid = Vid("Pok000"+str(vi)+".png")
            vid.ajuste_hor(800)
            vid.tela(win,(0,0))
            pygame.display.update()
        elif h and vi > 431:
            pygame.mixer.music.load(os.path.join(".\\audios", "Title Theme.wav"))
            pygame.mixer.music.play(-1)
            h = 0
        elif vi >= 100:
            vid = Vid("Pok00"+str(vi)+".png")
            vid.ajuste_hor(800)
            vid.tela(win, (0, 0))
            pygame.display.update()
            if vi == 601:
                vi = 551
        vi += 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = d = False
                pygame.mixer.music.stop()
                goodbye(win)
                return d
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    som()
                    if vi < 431:
                        vi = 431
                    else:
                        run = False
                        return(d)
                elif event.key == pygame.K_ESCAPE:
                    run = d = False
                    pygame.mixer.music.stop()
                    goodbye(win)
                    return (d)

def centro_texto(text, altura, color, menuFont, l, win):
    superf = menuFont.render(text, True, color)
    f = l - superf.get_width() / 2
    win.blit(superf, [f, altura])  # funcao de centralizar texto
    return f

def centro_texto2(text, altura, color, menuFont, l, win):
    superf = menuFont.render(text, True, color)
    f = l - superf.get_width() / 2
    win.blit(superf, [f, altura - superf.get_height() / 4]) #funcao de centralizar texto
    return f

def som():
    a = pygame.mixer.Sound(os.path.join(".\\audios", "Troca.wav"))
    a.play()

def menu_permanente():
    w = Window(800, 600) #cria objeto janela com dimensões 800x600
    pygame.display.set_caption('Menu')
    win = pygame.display.set_mode(w.returnWinSize()) #cria a janela do jogo
    pygame.draw.rect(win, c["branco"], ((200,90), (400,475)))
    pygame.draw.rect(win, c["preto"], ((210, 100), (380, 455)))
    menuFont= pygame.font.Font(os.path.join(".\\fontes","joystix monospace.ttf"), 30)
    centro_texto('Choose your pokemon', 5, c["branco"],menuFont, w.returnWinSize()[0] / 2, win)
    centro_texto('Blastoise', 120, c["azul"], menuFont, w.returnWinSize()[0] / 2, win)
    centro_texto('Charizard', 210, c["vermelho"], menuFont, w.returnWinSize()[0] / 2, win)
    centro_texto('Jolteon', 300, c["amarelo"], menuFont, w.returnWinSize()[0] / 2, win)
    centro_texto('Pidgeot', 390, c["cinza"], menuFont, w.returnWinSize()[0] / 2, win)
    centro_texto('Venusaur', 480, c["verde"], menuFont, w.returnWinSize()[0] / 2, win)
    pygame.display.update()
    return win

def menu_variavel(win):
    x=int(140)
    ll = False
    run = True
    pygame.draw.rect(win, c["preto"], ((210, 100), (60, 455)))
    pygame.draw.circle(win, c[c[x]], (260, x), 10)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = x = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x -= 90
                    if x<140:
                        x=140
                    else:
                        som()
                        pygame.draw.rect(win, c["preto"], ((210, 100), (60, 455)))
                        pygame.draw.circle(win, c[c[x]], (260, x), 10)
                        pygame.display.update()
                elif event.key == pygame.K_RIGHT:
                    if ll:
                        x = 590
                        pygame.draw.rect(win, c["preto"], ((210, 100), (60, 455)))
                        pygame.display.update()
                    else:
                        ll = True
                elif event.key == pygame.K_DOWN:
                    x += 90
                    if x > 500:
                        x = 500
                    else:
                        som()
                        pygame.draw.rect(win, c["preto"], ((210, 100), (60, 455)))
                        pygame.draw.circle(win, c[c[x]], (260, x), 10)
                        pygame.display.update()
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    som()
                    return(x)
                    break
                elif event.key == pygame.K_ESCAPE:
                    run = x = False

def jogo_permanente():
    w = Window(800, 533)  # cria objeto janela com dimensões 800x533
    pygame.display.set_caption('Menu')
    win = pygame.display.set_mode(w.returnWinSize())  # cria a janela do jogo
    pygame.mixer.music.load(os.path.join(".\\audios", "Trainer Battle.wav"))
    pygame.mixer.music.play(-1)
    return win

def impressao_lenta(win, texto, gameFont):
    # Escreverá lentamente os textos na tela
    k = ""
    for a in texto:
        pygame.time.wait(50)
        k+= a
        superf = gameFont.render(k, True, c["branco"])
        win.blit(superf, (35, 400))  # funcao de centralizar texto
        pygame.display.update()

def game_bar(win, k, p):
    # Programa que fará regulação da barra de vida dos pokemons
    a = p.hp/p.maxhp
    j = (162, 16)
    pygame.draw.rect(win, c["fundo"], (k, j))
    if a >= 0.5:
        l = "verde"
    elif a >= 0.2:
        l = "amarelo"
    else:
        l= "vermelho"
    pygame.draw.rect(win, c[l], (k, (j[0] * a, j[1])))
    pygame.display.update()

def Jorge(ac, f, g, h, i):
    if ac[1] == u["FigBag"]:
        if ac[0] == h:
            ac[0] = f
        elif ac[0] == i:
            ac[0] = g
    if ac[1] == u["PokRun"]:
        if ac[0] == f:
            ac[0] = h
        elif ac[0] == g:
            ac[0] = i
    return(ac)

def AtkTxt(gameFont, win, ac, p1):
    f = int(centro_texto2(p1.atks[0].name, u["FigBag"], c["preto"], gameFont, 150, win) - 25)
    g = int(centro_texto2(p1.atks[1].name, u["FigBag"], c["preto"], gameFont, 140 + 250, win) - 25)
    h = int(centro_texto2(p1.atks[2].name, u["PokRun"], c["preto"], gameFont, 150, win) - 25)
    i = int(centro_texto2(p1.atks[3].name, u["PokRun"], c["preto"], gameFont, 140 + 250, win) - 25)
    if ac == [f, u["FigBag"]]:
        centro_texto2(str(p1.atks[0].pp), u["FigBag"], c["preto"], gameFont, 700, win)
        centro_texto2(str(p1.atks[0].maxpp), u["FigBag"], c["preto"], gameFont, 750, win)
        a = 0
        return(a)
    elif ac == [g, u["FigBag"]]:
        centro_texto2(str(p1.atks[1].pp), u["FigBag"], c["preto"], gameFont, 700, win)
        centro_texto2(str(p1.atks[1].maxpp), u["FigBag"], c["preto"], gameFont, 750, win)
        a = 1
        return (a)
    elif ac == [h, u["PokRun"]]:
        centro_texto2(str(p1.atks[2].pp), u["FigBag"], c["preto"], gameFont, 700, win)
        centro_texto2(str(p1.atks[2].maxpp), u["FigBag"], c["preto"], gameFont, 750, win)
        a = 2
        return (a)
    elif ac == [i, u["PokRun"]]:
        centro_texto2(str(p1.atks[3].pp), u["FigBag"], c["preto"], gameFont, 700, win)
        centro_texto2(str(p1.atks[3].maxpp), u["FigBag"], c["preto"], gameFont, 750, win)
        a = 3
        return (a)
    else:
        centro_texto2(str(p1.atks[0].pp), u["FigBag"], c["preto"], gameFont, 700, win)
        centro_texto2(str(p1.atks[0].maxpp), u["FigBag"], c["preto"], gameFont, 750, win)
        return(f, g, h, i)

def jogo_recursivo(win, x, y, p1, p2):
    # Pegando as imagens e fontes e definindo seus tamanhos.
    # Fontes
    gameFont = pygame.font.Font(os.path.join(".\\fontes", "pokemon_fire_red.ttf"), 50)
    lvlFont = pygame.font.Font(os.path.join(".\\fontes", "pokemon_fire_red.ttf"), 35)
    # Imagens
    fundo = Picture("Background.png")
    fundo.ajuste_hor(800)
    caixa_t = Picture("text_bar.png")
    caixa_t.ajuste_hor(800)
    base1 = Picture("Base1.png")
    base1.ajuste_hor(475)
    base2 = Picture("Base2.png")
    base2.ajuste_hor(465)
    Pokemon = Picture(p[x]+".png")
    Pokemon.ajuste_hor(200)
    PokemonB = Picture(p[y] + "B.png")
    PokemonB.ajuste_hor(200)
    Barra = Picture("barra_1.png")
    Barra.ajuste_hor(325)
    BarraB = Picture("barra_2.png")
    BarraB.ajuste_hor(325)
    setinha = Picture("setinha.png")
    setinha.ajuste_hor(20)
    f0 = caixa_t.get_rect()
    Und_Bar1 = Picture("fgt_options.png")
    Und_Bar1.ajuste_ver(round(f0[3]))
    battaglia = Picture("pp_bar.png")
    battaglia.ajuste_hor(800)
    # Tamanhos
    f0 = Und_Bar1.get_rect()
    f1 = base1.get_rect()
    f2 = base2.get_rect()
    f3 = PokemonB.get_rect()
    f4 = BarraB.get_rect()
    f5 = caixa_t.get_rect()
    h = 800
    ab = [430, 415]
    ac = [125, 415]
    nyan = 0
    # Aqui a brincadeira começa a ficar séria!
    run = d = True
    l = False
    while run:
        clock = pygame.time.Clock()
        clock.tick(50)
        if h>=0:
            h -= 9
            # Movimentação das bases na tela
            fundo.tela(win, (0, 0))
            caixa_t.tela(win, (0, 373))
            base1.tela(win, (h, round(373 - f1[3])))
            base2.tela(win, (round(800- h -f2[2]), 150))
            Pokemon.tela(win, (round(475- h), 175 - f2[3]))
            PokemonB.tela(win, (125 + h, round(373 - f3[3])))
            pygame.display.update()
        elif h>-10: #depois
            h -= 10
            Barra.tela(win, (0, 75))
            BarraB.tela(win, (800 - f4[2], 373 - f4[3]))
            Und_Bar1.tela(win, (800 - f0[2], 373))
            setinha.tela(win, ab)
            superf = gameFont.render(p[y], True, c["preto"])
            win.blit(superf, (522, 260))
            superg = lvlFont.render("42", True, c["preto"])
            win.blit(superg, (758, 266))
            superh = gameFont.render(p[x], True, c["preto"])
            win.blit(superh, (20, 75))
            superi = lvlFont.render("42", True, c["preto"])
            win.blit(superi, (267, 82))
            superj = gameFont.render("What will " + p[y] + " do?", True, c["branco"])
            win.blit(superj, (35, 400))
            game_bar(win, (621, 308), p1)   #barra de vida player 1
            game_bar(win, (126, 124), p2)   #barra de vida player 2
            pygame.display.update()
        else:
            for event in pygame.event.get(): #parte de comando da tela
                if event.type == pygame.QUIT:
                    run = d = False
                    pygame.mixer.music.stop()
                    goodbye(win)
                    return(d)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if l:
                            if ac[1] != u["FigBag"]:
                                som()
                                battaglia.tela(win, (800 - f5[2], 373))
                                ac[1] = u["FigBag"]
                                ac = Jorge(ac, f, g, ha, i)
                                nyan = AtkTxt(gameFont, win, ac, p1) #Escreve os nomes dos ataques
                                setinha.tela(win, ac)
                                pygame.display.update()
                        else:
                            if ab[1] != u["FigBag"]:
                                som()
                                ab[1] = u["FigBag"]
                                Und_Bar1.tela(win, (800 - f0[2], 373))
                                setinha.tela(win, ab)
                                pygame.display.update()
                    elif event.key == pygame.K_DOWN:
                        if l:
                            if ac[1] != u["PokRun"]:
                                som()
                                battaglia.tela(win, (800 - f5[2], 373))
                                ac[1] = u["PokRun"]
                                ac = Jorge(ac, f, g, ha, i)
                                nyan = AtkTxt(gameFont, win, ac, p1)  # Escreve os nomes dos ataques
                                setinha.tela(win, ac)
                                pygame.display.update()
                        else:
                            if ab[1] != u["PokRun"]:
                                som()
                                ab[1] = u["PokRun"]
                                Und_Bar1.tela(win, (800 - f0[2], 373))
                                setinha.tela(win, ab)
                                pygame.display.update()
                    elif event.key == pygame.K_LEFT:
                        if l:
                            if ac[0] != f and ac[0] != h:
                                som()
                                battaglia.tela(win, (800 - f5[2], 373))
                                ac[0] = f
                                ac = Jorge(ac, f, g, ha, i)
                                nyan = AtkTxt(gameFont, win, ac, p1)  # Escreve os nomes dos ataques
                                setinha.tela(win, ac)
                                pygame.display.update()
                        else:
                            if ab[0] != u["FigPok"]:
                                som()
                                ab[0] = u["FigPok"]
                                Und_Bar1.tela(win, (800 - f0[2], 373))
                                setinha.tela(win, ab)
                                pygame.display.update()
                    elif event.key == pygame.K_RIGHT:
                        if l:
                            if ac[0] != g and ac[0] != i:
                                som()
                                battaglia.tela(win, (800 - f5[2], 373))
                                ac[0] = g
                                ac = Jorge(ac, f, g, ha, i)
                                nyan = AtkTxt(gameFont, win, ac, p1)  # Escreve os nomes dos ataques
                                setinha.tela(win, ac)
                                pygame.display.update()
                        else:
                            if ab[0] != u["BagRun"]:
                                som()
                                ab[0] = u["BagRun"]
                                Und_Bar1.tela(win, (800 - f0[2], 373))
                                setinha.tela(win, ab)
                                pygame.display.update()
                    elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        som()
                        if l:
                            # Programa de dano
                            run = False
                            caixa_t.tela(win, (0, 373))
                            if p1.atks[nyan].pp > 0:
                                nyan2 = p1.atks[nyan].useon(p1, p2)
                                if nyan2 == 'super':
                                    impressao_lenta(win, p1.nome + "'s " + p1.atks[nyan].name + " is super effective!",
                                                    gameFont)
                                elif nyan2 == 'dumb':
                                    impressao_lenta(win, p1.nome + "'s " + p1.atks[nyan].name +
                                                    " is not very effective...", gameFont)
                                elif nyan2 == 'normal':
                                    impressao_lenta(win, p1.nome + " used " + p1.atks[nyan].name + "!", gameFont)
                                elif nyan2 == 'miss':
                                    impressao_lenta(win, p1.nome + "'s " + p1.atks[nyan].name + " missed!", gameFont)


                            elif p1.atks[nyan].pp == 0:
                                impressao_lenta(win, p1.nome + " is tired of using this!", gameFont)
                            print(str(p2.nome) + ' ' + str(p2.hp) + '/' + str(p2.maxhp))
                            p2_faint = p2.faintcheck()
                            p1_faint = p1.faintcheck()
                            if p1_faint == True:
                                caixa_t.tela(win, (0, 373))
                                impressao_lenta(win, p1.nome + " has fainted!", gameFont)
                                pygame.time.wait(1000)
                                pygame.mixer.music.stop()
                                goodbye(win)
                            elif p2_faint == True:
                                caixa_t.tela(win, (0, 373))
                                impressao_lenta(win, p2.nome + " has fainted!", gameFont)
                                pygame.time.wait(1000)
                                pygame.mixer.music.stop()
                                goodbye(win)
                                run = d = False
                            pygame.time.wait(200)
                            return(d)
                        else:
                            if ab == u["Fight"]:
                                pj = ac[0]
                                battaglia.tela(win, (800 - f5[2], 373))
                                e = AtkTxt(gameFont, win, ac, p1)
                                f = e[0]
                                g = e[1]
                                ha = e[2]
                                i = e[3]
                                ac[0] = f  # Escreve os nomes dos ataques
                                setinha.tela(win, ac)
                                pygame.display.update()
                                l = True
                            elif ab == u["Pokemon"]:
                                continue
                            elif ab == u["Bag"]:
                                continue
                            elif ab == u["Run"]:
                                pygame.mixer.music.stop()
                                goodbye(win)
                                run = False
                    elif event.key == pygame.K_b:
                        h = l = e = a = 0
                        ac[0] = pj
                    elif event.key == pygame.K_ESCAPE:
                        run = d = False
                        pygame.mixer.music.stop()
                        goodbye(win)
                        return(d)

d = video()
if d:
    win = menu_permanente()
    y = menu_variavel(win)
    if y:
        x = menu_variavel(win)
    else:
        pygame.mixer.music.stop()
        goodbye(win)
    pygame.mixer.music.stop()

    if y and x: # Pula se o jogo for fechado
        win = jogo_permanente()
    if y:
        if x:
            run = True
            ky = 0

            # atribuindo os Pokemons dos players
            p1list = [Blastoise, Charizard, Jolteon, Pidgeot, Venusaur]
            p2list = [Blastoise2, Charizard2, Jolteon2, Pidgeot2, Venusaur2]
            p1 = None
            p2 = None
            if y:
                for j1 in range(len(p1list)):
                    # print(j2, p[y], p1list[j1])
                    if p[y] == str(p1list[j1].nome):
                        p1 = p1list[j1]
            if x:
                for j2 in range(len(p2list)):
                    # print(j2, p[x], p2list[j2])
                    if p[x] == str(p2list[j2].nome):
                        p2 = p2list[j2]
            while run:
                if ky == 0:
                    w = jogo_recursivo(win, x, y, p1, p2)
                    ky = 1
                elif ky == 1:
                    w = jogo_recursivo(win, x, y, p2, p1)
                    ky = 0
                a = x
                x = y
                y = a
                run = w
        else:
            goodbye(win)