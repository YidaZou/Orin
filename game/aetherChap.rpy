label aetherChap:
    scene bg aetherforest

    "You enter a clearing of misty trees. This place seems strangely familiar….Up ahead you hear the soft sounds of crying."
    window hide
    image j = "aether j.png"
    play sound "audio/Jumpscare.mp3"
    show j zorder 10
    pause 5
    hide j
    window auto

    menu:
        "Hello?":
            "At the sound of your voice, the trees seemed to tremble and shake. A cloaked figure slowly moved from the mist"
        "Oh hell nah miss me with that I’m going home":
            "At the sound of your voice, the trees seemed to giggle and sway. A shadowy figure appeared from the mist"
        "This must be the place where I meet the love of my life uwu <3":
            "At the sound of your voice, the trees seemed to blush and shiver. Love? A soft voice emerged from the mist"
