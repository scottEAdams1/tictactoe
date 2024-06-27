def win(cells):
    if (cells[0][0].type == cells[0][1].type
    and cells[0][1] == cells[0][2]
    and cells[0][0].type != ""):
        print(f"Winner is {cells[0][0].type}")
        return True
    if (cells[1][0].type == cells[1][1].type
    and cells[1][1] == cells[1][2]
    and cells[1][0].type != ""):
        print(f"Winner is {cells[1][0].type}")
        return True
    if (cells[2][0].type == cells[2][1].type
    and cells[2][1] == cells[2][2]
    and cells[2][0].type != ""):
        print(f"Winner is {cells[2][0].type}")
        return True
    if (cells[0][0].type == cells[1][0].type
    and cells[1][0].type == cells[2][0].type
    and cells[0][0].type != ""):
        print(f"Winner is {cells[0][0].type}")
        return True
    if (cells[0][1].type == cells[1][1].type
    and cells[1][1].type == cells[2][1].type
    and cells[0][1].type != ""):
        print(f"Winner is {cells[0][1].type}")
        return True
    if (cells[0][2].type == cells[1][2].type
    and cells[1][2].type == cells[2][2].type
    and cells[0][2].type != ""):
        print(f"Winner is {cells[0][2].type}")
        return True
    if (cells[0][0].type == cells[1][1].type
    and cells[1][1].type == cells[2][2].type
    and cells[0][0].type != ""):
        print(f"Winner is {cells[0][0].type}")
        return True
    if (cells[0][2].type == cells[1][1].type
    and cells[1][1].type == cells[2][0].type
    and cells[0][2].type != ""):
        print(f"Winner is {cells[0][2].type}")
        return True
    return False