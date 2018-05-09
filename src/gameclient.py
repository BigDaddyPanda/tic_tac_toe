from tkinter import *
import PIL.Image
import PIL.ImageTk

root = Tk()
import gamescore as gs
import gameboard as gb
import resources as r
# player name
player = ""
player2=""
#[boardsize,opponent] 3X3 and 4X4 are 3 points winning
gamerule = [0, 0]


root.geometry("550x650+400+30")
root.title("Smart Boi-42")


def render_image(src):
    im = PIL.Image.open("./pict/buttons/"+src)
    photo = PIL.ImageTk.PhotoImage(im)
    return photo


def load_scoreboard():
    rootscore = Toplevel(root)
    rootscore.title("Smart Boi-ScoreBoard")
    gs.create_scoreboard(root, rootscore)


def start_game():
    global player,player2, gamerule
    player = playername.get()
    player2 = player2name.get() if len(player2name.get())>0 else ""
    rootgame = Toplevel(root)
    rootgame.title("Smart Boi - Game")

    if(gamerule[0] < 2):
        gb.create_gameboard(player,player2, root, rootgame,
                            gamerule[1], 3, gamerule[0]+3)
    else:
        gb.create_gameboard(player,player2, root, rootgame,
                            gamerule[1], 4, gamerule[0]+3)
    #root.withdraw()


def on_closing(root, rootgame):
    rootgame.destroy()
    root.deiconify()


logolabel = Label(root, image=r.logo)


def setgamemode(i):
    global gamerule
    gamerule[0] = i
    gamemodebuttons[i].configure(image=r.gamemodeimages[i][1])
    gamemodebuttons[(i+1) % 3].configure(image=r.gamemodeimages[(i+1) % 3][0])
    gamemodebuttons[(i+2) % 3].configure(image=r.gamemodeimages[(i+2) % 3][0])


def setgameopp(i):
    global gamerule,player2
    player2=player2*i
    gamerule[1] = i
    if(i==1):
        playernamelabel.pack(side=LEFT,padx=10)
        playername.pack(side=LEFT,padx=10)
        player2namelabel.pack(side=RIGHT,padx=10)
        player2name.pack(side=RIGHT,padx=10)
    else:
        player2namelabel.pack_forget()
        player2name.pack_forget()
    gameopponentbuttons[i].configure(image=r.gameoppimages[i][1])
    gameopponentbuttons[(i+1) %
                        2].configure(image=r.gameoppimages[(i+1) % 2][0])


gamemodebuttonslabel = PanedWindow(root)
gamemodebuttons = [Button(gamemodebuttonslabel, image=r.gamemodeimages[i][0],
                          command=lambda i=i:setgamemode(i), relief=FLAT)
                   for i in range(len(r.gamemodeimages))]
for x in gamemodebuttons:
    x.pack(padx=5, pady=10, side=LEFT)

gameopponentbuttonslabel = PanedWindow(root)
gameopponentbuttons = [Button(gameopponentbuttonslabel, image=r.gameoppimages[i][0],
                              command=lambda i=i:setgameopp(i), relief=FLAT) for i in range(len(r.gameoppimages))]
for x in gameopponentbuttons:
    x.pack(padx=5, pady=10, side=LEFT)
playernameslabel = PanedWindow(root)
playernames = PanedWindow(root)

playernamelabel = Label(playernameslabel, font=("videophreak", 25),
                        justify=CENTER, foreground="#31363e", text="Name")
playername = Entry(playernames, font=("videophreak", 25), width=8,
                   justify=CENTER, foreground="#ffff93", bg="#31363e", relief=FLAT)
player2namelabel = Label(playernameslabel, font=("videophreak", 25),
                         justify=CENTER, foreground="#31363e", text="Guest")
player2name = Entry(playernames, font=("videophreak", 25), width=8,
                    justify=CENTER, foreground="#ffff93", bg="#31363e", relief=FLAT)

gamemodelabel = Label(root, font=("videophreak", 30),
                      justify=CENTER, foreground="#31363e", text="Game Rule")
playbutton = Button(root, image=r.play, command=start_game, relief=FLAT)
scorebutton = Button(root, image=r.score, command=load_scoreboard, relief=FLAT)
cpr = Label(root, text="© Big Daddy Panda")


logolabel.pack(pady=20)
playernameslabel.pack()
playernames.pack()
playernamelabel.pack()
playername.pack()

gamemodelabel.pack()
gamemodebuttonslabel.pack()
gameopponentbuttonslabel.pack()
playbutton.pack()
scorebutton.pack()
cpr.pack(side=BOTTOM)
setgamemode(1)
setgameopp(0)

root.mainloop()
