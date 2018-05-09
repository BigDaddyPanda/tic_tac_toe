from tkinter import *
from PIL import Image, ImageTk
import resources as r
import json
# from gameclient import root,rootscore
data = {}


def init():
    global data
    if data == {}:
        load_scores()


def close_popup(root, rootscore):
    rootscore.destroy()
    root.deiconify()


def update_score(playername, gamemode=3):
    global data
    init()
    if data.get(playername) == None:
        data[playername] = [0, 0, 0]
    # print(data)
    data[playername][gamemode-3] += 1
    save_scores()


def load_scores():
    global data
    with open('./content/score.json', 'r') as f:
        data = json.load(f)
        f.close()


def save_scores():
    global data
    init()
    with open('./content/score.json', 'w') as f:
        json.dump(data, f)
        f.close()


def create_scoreboard(root, rootscore):
    global data
    rootscore.geometry("400x600+470+50")
    load_scores()
    data = dict(
        sorted(data.items(), key=lambda i: i[1][0]+2*i[1][1]+3*i[1][2], reverse=True))
    logolabel = Label(rootscore, image=r.halloffame)
    scorelabel = Label(rootscore, image=r.score)
    logolabel.pack(padx=5, pady=10)
    scorelabel.pack(padx=5, pady=10)

    scoreheader = PanedWindow(rootscore, bg="#31363e")
    scoreheader.pack(padx=5, pady=5)

    hpnl = Label(scoreheader, text="PlayerName", font=(
        "videophreak", 10), fg="#ffff93", width=20, height=2, bg="#31363e")
    hpnl.pack(side=LEFT)
    hpn3 = Label(scoreheader, text="3x3", font=("videophreak", 10),
                 fg="#ffff93", width=8, height=2, bg="#31363e")
    hpn4 = Label(scoreheader, text="4x4", font=("videophreak", 10),
                 fg="#ffff93", width=8, height=2, bg="#31363e")
    hpn5 = Label(scoreheader, text="5x5", font=("videophreak", 10),
                 fg="#ffff93", width=8, height=2, bg="#31363e")
    hpn3.pack(side=LEFT)
    hpn4.pack(side=LEFT)
    hpn5.pack(side=LEFT)

    scoreboard = PanedWindow(rootscore)
    scoreboard.pack(padx=5, pady=10)

    playersname = [Label(scoreboard, font=("videophreak", 10), fg="#ffff93", width=20, height=2,
                         bg="#31363e", text=x[0]) for x in data.items()][0:5]
    playersscore = [[Label(scoreboard, font=("videophreak", 10), fg="#ffff93", width=8, height=2, bg="#31363e", text=str(y)) for y in x[1]]
                    for x in data.items()][0:5]
    # print(playersscoress)
    for i in range(5):
        playersname[i].grid(row=i, pady=3, column=0)
        playersscore[i][0].grid(row=i, pady=3, column=1)
        playersscore[i][1].grid(row=i, pady=3, column=2)
        playersscore[i][2].grid(row=i, pady=3, column=3)

    back = Button(rootscore, image=r.back, relief=FLAT,
                  command=lambda: close_popup(root, rootscore))
    back.pack(padx=5, pady=5)
