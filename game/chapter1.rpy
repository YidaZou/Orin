label chapter1:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #test



    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.
    "...Is that the wind?..."
    "...No..."
    "...That’s the sound of waves..."
    "...You can smell the salty breeze and hear the crash of waves..."
    "...Laughter..."
    "...Wait...Where’s it going?..."
    "...Come back-..."

    show pim bworried
    define bp = Character("???",color="FFFFFF")
    bp "Hey! Hey you!"

    "Who’s yelling? Hold on...this doesn’t look like my bed…"
    "There’s a strange ghostly white deer standing over you. They seem worried? Can deer be worried? Is this even a deer??"
    show pim worried
    menu:
        bp "Hey um. I saw you fall from the tree- Are you ok?"
        "Are you an angel? You look like an angel.":
            pN "Are you an angel? You look like an angel."
        "Did you toss me out of the tree? You seem like that type.":
            pN "Did you toss me out of the tree? You seem like that type."
        "Kiss me and we’ll find out~":
            pN "Kiss me and we’ll find out~"

    define p = Character("Pim",color="#FCE59D")
    show pim confused
    p "Haha what? You must have hit your head pretty hard! I’m Pim. Who are you?"
    define pN = Character("[pName]")
    default pName = "You"

    $ pName = renpy.input("What is your name?")
    $ pName = pName.strip()

    if not pName:
         $pName = "Pantheon"

    pN "My name is [pName]!"
    show pim
    p "*laugh* [pName]! That sure is a funny name..! That’s almost a..."
    show pim confused
    menu:
        p "Human-like name…..Come to think of it...I know most Orin in the realm"
        "Say nothing":
            pN "..."
        "Laugh nervously":
            pN "he...hehe...he"
        "I’m not an Orin":
            pN "I’m not an Orin"

    show pim
    p "*Hey it’s okay! This isn’t the first time someone has gotten stuck in the dream realm! There must be a reason why."
    show pim worried
    p "Funny that you should appear now...Corruption has been running rampant and I can’t send you back till it’s fixed."

    menu:
        "Why not??":
            pN "Why not??"

    show pim worried
    p "We can’t have corruption running into your world now can we?"
    show pim
    p "*happy* Don’t worry I’ll take care of you till we can solve this corruption! You can even stay at my place!"

    # This ends the game.
    return
