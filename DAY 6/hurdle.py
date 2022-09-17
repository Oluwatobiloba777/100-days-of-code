def turnRight():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turnRight()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
while front_is_clear():
    move()
turn_left()
    