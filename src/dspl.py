# Display level


def init(lvl, lvl_new=[]):
    for i in range(len(lvl)):
        lvl_new.append(4)
        for o in lvl[i]:
            if o == 'X':
                lvl_new.append(1)
            if o == 'P':
                lvl_new.append(2)
            if o == 'F':
                lvl_new.append(0)
            if o == ' ':
                lvl_new.append(3)
    return lvl_new


def display_lvl(lvl, lvl_print=''):
    for i in range(len(lvl)):
        if lvl[i] == 1:
            lvl_print += 'X'
        if lvl[i] == 2:
            lvl_print += '+'
        if lvl[i] == 3:
            lvl_print += ' '
        if lvl[i] == 0:
            lvl_print += ':'
        if lvl[i] == 4:
            lvl_print += '\n'

    print(lvl_print)
