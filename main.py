import pygame
import random
import time
import sys
import os

clock = pygame.time.Clock()
def load_image(name, color_key=None):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print("Cannot load image:", name)
        raise SystemExit(message)

    image = image.convert_alpha()
    if color_key != None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

def drawline(screen, size):
    for i in range(0, size[1]+ 1, 50):
        pygame.draw.line(screen, pygame.Color('white'), [0, i], [size[0], i], width=1)
    for i in range(0, size[0] + 1, 50):
        pygame.draw.line(screen, pygame.Color('white'), [i, 0], [i, size[1]], width=1)
    
def drawzmei(screen, size, list):
    for i in range(h // 50):
        for j in range(w // 50):
            if list[i][j] == 0:
                pygame.draw.polygon(screen, pygame.Color("black"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
            if list[i][j] == 1:
                pygame.draw.polygon(screen, pygame.Color("green"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
            if list[i][j] == 2:
                pygame.draw.polygon(screen, pygame.Color("green"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
                pygame.draw.polygon(screen, pygame.Color("black"),
                                    [(j * 50 + 20, i * 50 + 20), (j * 50 + 20, i * 50 + 30)
                                        , (j * 50 + 30, i * 50 + 30) , (j * 50 + 30, i * 50 + 20)]
                                    , 0)
            if list[i][j] == 3:
                pygame.draw.circle(screen, pygame.Color("red"), (j * 50 + 25, i * 50 + 25), 24)

def tab(screen, size, records, score, name):
    font = pygame.font.Font('Arcade.txt', 60)
    fontt = pygame.font.Font('Arcade.txt', 48)
    nm = fontt.render("Player:" + name, True, (255, 255, 255))
    sct = font.render("Score:" + str(score).zfill(4), True, (255, 255, 255))
    screen.blit(nm, (size[0] + 20, 50))
    screen.blit(sct, (size[0] + 20, 0))
    for i in range(10):
        rnt = fontt.render(str(i + 1) + "." + records[i][0] + ":" + records[i][1].zfill(4), True, (255, 255, 255))
        screen.blit(rnt, (size[0] + 20, 105 + i * 50))

def start_screen(size):
    fon = pygame.transform.scale(load_image('start screen.png'), (size[0] + 350, size[1]))
    font = pygame.font.Font("Arcade.txt", 50)
    string_rendered = font.render("PRESS ANY KEY", True, (255, 255, 255))
    start = True
    b = True
    cl = time.time()
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                start = False
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        if time.time() - cl >= 1:
            cl = time.time()
            if b:
                b = False
            else:
                b = True
        if b:
            screen.blit(string_rendered, (290, 310))
        pygame.display.flip()
    start = True
    cl = time.time()
    s = ""
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and s != "":
                    return s
                elif keys[pygame.K_BACKSPACE]:
                    s = s[:-1]
                else:
                    if pygame.key.name(event.key) in ".-_abcdefghijklmnopqrstuvwxyz1234567890" and len(s) < 9:
                        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                            s += pygame.key.name(event.key).upper()
                        else:
                            s += pygame.key.name(event.key)
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        string_rendered = font.render(s, True, (255, 255, 255))
        if s == "":
            wn = font.render("WRITE YOUR NICKNAME", True, (255, 255, 255))
            wn2 = font.render("AND PRESS SPACE", True, (255, 255, 255))
            screen.blit(wn, (290, 260))
            screen.blit(wn2, (290, 310))
        screen.blit(string_rendered, (290, 310))
        pygame.display.flip()
                
if __name__=='__main__':
    file = open("records.txt", "r")
    opens = file.readline().split("/--/")
    records = []
    for i in opens:
        records.append(i.split("; "))
    file.close()
    score = 0
    pygame.init()
    w, h = 600, 600 #map(int, input().split())
    size = w, h
    list = []
    for i in range(h // 50):
        list.append([0] * (w // 50))
    g = [0, 2]
    list[0][0] = 1
    list[0][1] = 1
    list[0][2] = 2
    i1, j1 = 0, 0
    while list[i1][j1] == 1 or list[i1][j1] == 2:
        i1, j1 = random.randint(0, h // 50 - 1), random.randint(0, w // 50 - 1)
    list[i1][j1] = 3
    lis_z = [[0, 2], [0, 1], [0, 0]]
    screen = pygame.display.set_mode([size[0] + 400, size[1]])
    name = start_screen(size)
    running = True
    x = 1
    y = 0
    drawline(screen, size)
    drawzmei(screen, size, list)
    tab(screen, size, records, score, name)
    ti = time.time()
    nr = False
    win = False
    while running:
        t = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and y != 1:
                    x = 0
                    y = -1
                    t = True
                elif keys[pygame.K_s] and y != -1:
                    x = 0
                    y = 1
                    t = True
                elif keys[pygame.K_a] and x != 1:
                    x = -1
                    y = 0
                    t = True
                elif keys[pygame.K_d] and x != -1:
                    x = 1
                    y = 0
                    t = True
        if t or time.time() - ti >= 0.75:
            ti = time.time()
            t = False
            if list[(g[0] + y) % (h // 50)][(g[1] + x) % (w // 50)] == 3:
                score += 1
                f = True
                for i in list:
                    f *= all(i)
                if f:
                    print("Победа!")
                    win = True
                    running = False
                list[g[0] % (h // 50)][g[1] % (w // 50)] = 1
                list[(g[0] + y) % (h // 50)][(g[1] + x) % (w // 50)] = 2
                while list[i1][j1] == 1 or list[i1][j1] == 2:
                    i1, j1 = random.randint(0, h // 50 - 1), random.randint(0, w // 50 - 1)
                list[i1][j1] = 3
            elif list[(g[0] + y) % (h // 50)][(g[1] + x) % (w // 50)] == 1:
                print("Поражение")
                tr = True
                nr = False
                for i in records:
                    if i[0] == name:
                        if score > int(i[1]):
                            nr = True
                            pl = records.index(i)
                            i[1] = str(score)
                        tr = False
                        break
                if tr:
                    records.append([name, str(score)])
                records.sort(key=lambda x: int(x[1]), reverse=True)
                save = []
                for i in records:
                    save.append("; ".join(i))
                file = open("records.txt", "w")
                file.write("/--/".join(save))
                file.close()
                running = False
            else:
                list[g[0] % (h // 50)][g[1] % (w // 50)] = 1
                list[(g[0] + y) % (h // 50)][(g[1] + x) % (w // 50)] = 2
                k = lis_z.pop()
                list[k[0] % (h // 50)][k[1] % (w // 50)] = 0
            g[0], g[1] = g[0] + y, g[1] + x
            lis_z = [[g[0] % (h // 50), g[1] % (w // 50)]] + lis_z
        screen.fill((0, 0, 0))
        drawline(screen, size)
        drawzmei(screen, size, list)
        tab(screen, size, records, score, name)
        pygame.display.flip()
    font = pygame.font.Font("Arcade.txt", 50)
    if nr:
        st = font.render("GOOD JOB!!! YOU'VE GOT NEW RECORD", True, (255, 255, 255))
        nd = font.render("NOW YOUR SPOT ON TAB IS: " + str(pl) + "!!!", True, (255, 255, 255))
        trd = font.render("WELL DONE!!!", True, (255, 255, 255))
        x = 100
    elif win:
        st = font.render("OOOOH MYYY GOOOOD!!!", True, (255, 255, 255))
        nd = font.render("HOW, JST HOW?!?!?!", True, (255, 255, 255))
        trd = font.render("YOU ARE CHAMPION", True, (255, 255, 255))
        x = 300
    else:
        st = font.render("", True, (255, 255, 255))
        nd = font.render("YOU LOSE, TRY AGAIN", True, (255, 255, 255))
        trd = font.render("", True, (255, 255, 255))
        x = 200
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
        screen.blit(st, (x, 200))
        screen.blit(nd, (x, 300))
        screen.blit(trd, (x, 400))
        pygame.display.flip()
    pygame.quit()
    