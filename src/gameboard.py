from tkinter import *
from PIL import Image, ImageTk
import finalboss as gamelogic
import gamescore as score
import resources as r
import json
import time
import geometrix as go
from math import sqrt
from random import choice
from multiprocessing import Process

# from gameclient import root,rootgame
PLAYER = ""
PLAYER2 = ""
SIZE = 9
WIN = 3
OPPTYPE = 0
OPPTAGS = ["AI", "Player"]
OPPTAG="AI"
OPPNAMES = ["Rick", "Morty", "Penguin", "TeeSpoon",
            "Faker", "Grandma", "Kaspaarov", "Turing", "Snail"]
GRID = [0 for i in range(SIZE)]
# 1 == x == ai || -1 == o == you
turn_to_play = choice([-1, 1])


def did_anyone_win():
    global GRID, WIN, SIZE, PLAYER, PLAYER2
    size = int(sqrt(SIZE))
    # if GRID.count(0) > 4:
    #     return -10
    if gamelogic.win_check(1, GRID, WIN) != False:
        score.update_score(PLAYER2, size)
        return 1
    if gamelogic.win_check(-1, GRID, WIN) != False:
        score.update_score(PLAYER, size)
        return -1
    if GRID.count(0) == 0:
        return 0
    return -10


def close_popup(root, rootgame):
    rootgame.destroy()
    root.deiconify()


def announce_winner(i, gametiles, gamecomment):
    global WIN, GRID, PLAYER, PLAYER2
    todisable = [x for x in GRID if GRID[x] == 0]
    for d in todisable:
        gametiles[d].config(command='')

    text = PLAYER if i == -1 else PLAYER2
    im = r.xvict if i == -1 else r.ovict
    winz = gamelogic.extract_win_condition(GRID, WIN)
    for w in winz:
        gametiles[w].config(image=im)
    gamecomment.config(text=text+" won so easily")


def denounce_tie(gamecomment):
    gamecomment.config(text="Well Fought Young " +
                       PLAYER+".\nYou may give him 20",height=2)


def select_tile(i, gametiles, gamecomment):
    global GRID, WIN, turn_to_play,OPPTYPE
    im=[r.oselect,r.xselect][(turn_to_play%3)//2]
    gametiles[i].config(command='', image=im)
    GRID[i] = turn_to_play
    turn_to_play*=-1
    #print( OPPTYPE == 0)
    if OPPTYPE == 0:
        next_move = gamelogic.minimax(turn_to_play, GRID, win=WIN)
        index = next_move["index"]
        if index != None:
            GRID[index] = turn_to_play
            gametiles[index].config(command='', image=[r.oselect,r.xselect][(turn_to_play%3)//2])
        turn_to_play*=-1
        
    dwa = did_anyone_win()
    #print(dwa)
    if dwa == -10:
        return
    if dwa == 0:
        denounce_tie(gamecomment)
    else:
        announce_winner(did_anyone_win(), gametiles, gamecomment)


def playagain(gametiles, gameboard, gamecomment):
    global GRID, SIZE
    size = int(sqrt(SIZE))
    GRID = [0 for i in range(SIZE)]
    gametiles = [Button(gameboard, image=r.empty, relief=FLAT, command=lambda i=i:select_tile(
        i, gametiles, gamecomment)) for i in range(SIZE)]
    for i in range(len(gametiles)):
        gametiles[i].grid(row=i//size, column=i %
                          size, padx=10//size, pady=10//size)
    gamecomment.config(height=1,text="Game is on")

def create_gameboard(player, player2, root, rootgame, ishuman, win, size):
    # print(player, player2, root, rootgame, ishuman, win, size)
    global SIZE, WIN, PLAYER, PLAYER2, OPPTAG, GRID, turn_to_play,OPPTYPE
    SIZE = size**2
    WIN = win
    PLAYER = player
    PLAYER2 = choice(OPPNAMES) if len(player2) == 0 else player2
    OPPTYPE=ishuman
    OPPTAG = OPPTAGS[ishuman]
    GRID = [0 for i in range(SIZE)]
    #print(OPPTYPE, turn_to_play)

    # 0 ai// 1 you
    turn_to_play = choice([-1,1])

    rootgame.geometry("400x"+str(500+90*(size-3))+"+470+75")

    gameheader = PanedWindow(rootgame)
    gameheader.pack(fill=BOTH, padx=5, side=TOP)
    gamesubheader = PanedWindow(rootgame)
    gamesubheader.pack(fill=BOTH, padx=25, pady=0, side=TOP)

    opponent1label = Label(gameheader, text=player, font=(
        "videophreak", 25), fg="#ffff93", width=8, height=1, bg="#31363e", relief="solid")
    opponent2label = Label(gameheader, text=PLAYER2, font=(
        "videophreak", 25), fg="#ffff93", width=8, height=1, bg="#31363e", relief="solid")
    opponenttag1label = Label(gamesubheader, text="Player", font=(
        "videophreak", 10), fg="#ffff93", width=8, height=2, bg="#31363e", relief="solid")
    opponenttag2label = Label(gamesubheader, text=OPPTAG, font=(
        "videophreak", 10), fg="#ffff93", width=8, height=2, bg="#31363e", relief="solid")
    gamecomment = Label(rootgame, text="Game is on", font=("videophreak", 18),
                        fg="#ffff93", height=1, bg="#31363e")

    opponent1label.pack(side=LEFT)
    opponent2label.pack(side=RIGHT)
    opponenttag1label.pack(side=LEFT, pady=0)
    opponenttag2label.pack(side=RIGHT, pady=0)

    gameboard = PanedWindow(rootgame)
    gameboard.pack(padx=5, pady=30)
    gametiles = [Button(gameboard, image=r.empty, relief=FLAT, command=lambda i=i:select_tile(
        i, gametiles, gamecomment)) for i in range(SIZE)]
    for i in range(len(gametiles)):
        gametiles[i].grid(row=i//size, column=i %
                          size, padx=10//SIZE, pady=10//SIZE)

    gamecomment.pack(padx=5, pady=5, fill=BOTH)

    gamefooter = PanedWindow(rootgame)
    gamefooter.pack(padx=5, pady=10)

    again = Button(gamefooter, image=r.again, relief=FLAT,
                   command=lambda: playagain(gametiles, gameboard, gamecomment))
    back = Button(gamefooter, image=r.back, relief=FLAT,
                  command=lambda: close_popup(root, rootgame))
    again.pack(side=LEFT)
    back.pack(side=RIGHT)
