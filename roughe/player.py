import colourCodes as colours


s_Name = "Aughustus IV"
s_Face = f"{colours.b_GREEN}\u2588"

#a_facecolours[f"{colours.b_GREEN}", f"{colours.b_RED}", f"{colours.b_YELLOW}"]

i_Start_x = 5
i_Start_y = 5

i_Player_x = 1
i_Player_y = 1

i_Life   = 100    # default health
i_Armour =  25   # default armour, will drin this first before health
i_Rubies = 100   # 100 Rubies = $1




i_MaxInt = 999999999
i_MinInt = 0


def DrawPlayer(i_Player_y, i_Player_x):
    return f"\x1b[{i_Player_y};{i_Player_x}H"
