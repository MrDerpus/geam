################################################################################
#   This game is just for fun, a simple t4est of skills
#   and a learning exprience for me.  Enjoy?
#
#   Author: Matthew. Klatt
################################################################################

import includes as inc


inc.os.system("color")

# main game loop
# game loop waits for player movement and then will update poitions
while(inc.window.b_Running == True):


    # draw player . . .
    print(f"{inc.player.DrawPlayer(inc.player.i_Player_y , inc.player.i_Player_x)}{inc.player.s_Face}")



    # player logic . . .



    # Get player input . . .
    if(inc.keys.is_pressed('w')):
        inc.player.i_Player_y -= 1 # Move Up
    elif(inc.keys.is_pressed('s')):
        inc.player.i_Player_y += 1 # Move Down
    elif(inc.keys.is_pressed('a')):
        inc.player.i_Player_x -= 1 # Move Left
    elif(inc.keys.is_pressed('d')):
        inc.player.i_Player_x += 1 # Move Right
    elif(inc.keys.is_pressed('r')):
        inc.os.system("cls") # clear console



    inc.time.sleep(0.1)
    #inc.os.system("cls")
