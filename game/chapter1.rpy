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
    bp "Hey! Hey you!"

    "Who’s yelling? Hold on...{p}this doesn’t look like my bed…"
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

    show pim confused
    p "Haha what? You must have hit your head pretty hard! I’m Pim. Who are you?"
    define pN = Character("[pName]")
    default pName = "You"
    $i = 0
    label name:

        $ pName = renpy.input("What is your name?")
        $ pName = pName.strip()
        if pName.lower() == "pim" and i!=3:
            show pim upset
            p "Hold on now! That’s my name >:<"
            $i+=1
            jump name
        elif pName.lower() == "pim":
            show pim anger
            p "Fine Then >>>>>:(((((((("
        if not pName:
            $pName = "Pantheon"

    show pim
    pN "My name is [pName]!"
    p "[pName]! That sure is a funny name..!{p}That’s almost a..."
    show pim confused
    menu:
        p "Human-like name...Come to think of it...I know most Orin in the realm"
        "Say nothing":
            pN "..."
        "Laugh nervously":
            pN "he...{p}hehe...{p}he"
        "I’m not an Orin":
            pN "I’m not an Orin"

    show pim
    p "Hey it’s okay! This isn’t the first time someone has gotten stuck in the dream realm! There must be a reason why."
    show pim worried
    p "Funny that you should appear now...{p}Corruption has been running rampant and I can’t send you back till it’s fixed."

    menu:
        "Why not??":
            pN "Why not??"

    show pim worried
    p "We can’t have corruption running into your world now can we?"
    show pim
    p "Don’t worry I’ll take care of you till we can solve this corruption! You can even stay at my place!"

    # ...

    hide pim
    "On the way to Pim’s house, they shared everything about these Orins and dreams and corruption. It was way too much to learn about all at once."

    scene bg aetherroom
    p "This is my place! Or well my girlfriend’s place! Our place! It’s not much but this home! You can stay in Lulu’s twin’s room. They aren’t around anymore."
    show pim confused
    p "Why are you looking at me like that?? Aether just doesn’t live here anymore geez..."

    "This Aether sure was well kept. Everything was meticulously organized from movies to music albums. Hopefully, they wouldn’t mind you staying here too much"

    show screen ingameMenu
    p "This is home! But if you want to travel the town just click on that map of yours:"
    p "Here you can click on different locations. Different Orins live in different places so feel free to explore. But be wary of corrupted Orins! I wouldn’t want you getting infected!"
    p "If you pick up any items you can click your bag! I would kill for some sparkles if you ever pick any up!"
    p "That’s all from me! If you ever need guidance just come back home! I’m sure Lumine or I can help~"
    p "Click on the map now!"
    p "Please click on the map now"

    $L = 0
    label leave:
        $L+=1
        p "Click map"
        p "Map. Click. Go."
        if L < 100:
            jump leave
        else:
            label aLeave:
                show pim anger
                p "LEAVE"
                jump aLeave
