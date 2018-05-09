import PIL.Image
import PIL.ImageTk


def render_image(src):
    im = PIL.Image.open("./pict/"+src)
    photo = PIL.ImageTk.PhotoImage(im)
    return photo


# client items
logo = render_image("logo.png")
halloffame = render_image("halloffame.png")
score = render_image("score.png")
play = render_image("play.png")
back = render_image("back.png")

# client buttons
gamemodeimages = [(render_image("gm ("+str(i)+").png"),
                   render_image("sgm ("+str(i)+").png")) for i in [0, 1, 2]]
gameoppimages = [(render_image("vs ("+str(i)+").png"),
                  render_image("svs ("+str(i)+").png")) for i in [1, 2]]

# score items
headplayername = render_image("playernamelabel.png")
scoregamemodeslabels = [render_image("scgm"+str(i)+".png") for i in [0, 1, 2]]
playernameimage = render_image("playername.png")
playerscoreimage = render_image("playerscore.png")

#game items
xvict=render_image("vict (1).png")
ovict=render_image("vict (2).png")
xselect=render_image("game (1).png")
oselect=render_image("game (2).png")
empty=render_image("empty.png")
again=render_image("again.png")