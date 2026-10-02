
define alien = Character("Alien", color="#ffffff")

label start:

    $ player_name = "Player"
    
    # Put quotes around the input prompt string
    $ temp_name = renpy.input("What is your name?", length=15)
    $ temp_name = temp_name.strip()
    if temp_name:
        $ player_name = temp_name

    show alien normal at Position(xalign=1.5, yalign=0.0)
    show alien at easein 1.5, Position(xalign=0.8, yalign=0.0)

   
    alien "Get up, weirdo."
    alien "I said..."

 
    show text "{size=80}{color=#ff0000}GET UP{/color}{/size}" at truecenter with dissolve

    
    pause
    
    return
