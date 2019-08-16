# Get player position


def get_player_pos(lvl):
    for i in range(len(lvl)):
        if lvl[i] == 2:
            return i
