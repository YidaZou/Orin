# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bp = Character("???",color="FFFFFF") #unseen characters

define p = Character("Pim",color="#FCE59D")
define l = Character("Lumine",color="#B9FFFF")
define a = Character("Aether",color="#DA2119")
define al = Character("Alatus",color="#1164B4")

# The game starts here.

screen ingameMenu:
    hbox:
        imagebutton auto "Map/Map %s.png" focus_mask True action Show("mapscreen")

screen mapscreen:
    add "Map/Mapchonk.png"
    #Aether
    imagebutton auto "Map/Mapaether %s.png" focus_mask True action [Hide("mapscreen"), Jump("aetherChap")]


    #Alatus
    imagebutton auto "Map/Mapalatus %s.png" focus_mask True action [Hide("mapscreen"), Jump("alatusChap")]
    hbox:
        imagebutton auto "Map/Map %s.png" focus_mask True action Hide("mapscreen")


label start:

    show screen ingameMenu
    call chapter1



    # This ends the game.
