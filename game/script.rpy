﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bp = Character("???",color="FFFFFF") #unseen characters

define p = Character("Pim",color="#FCE59D")
define l = Character("Lulu",color="#B9FFFF")
define a = Character("Aether",color="#FCE59D")

# The game starts here.

screen ingameMenu:
    zorder 9
    hbox:
        imagebutton auto "Map %s.png" focus_mask True action Show("mapscreen")

screen mapscreen:
    zorder 10
    add "Mapchonk.png"
    imagebutton auto "Mapaether %s.png" focus_mask True action Call("aetherChap")
    hbox:
        imagebutton auto "Map %s.png" focus_mask True action Hide("mapscreen")


label start:


    call chapter1



    # This ends the game.
