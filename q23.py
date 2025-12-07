# Haunted House Game

print("Welcome to the Haunted House")
direction = input("Go upstairs or downstairs? ").lower()

if direction == "downstairs":
    print("Game Over")
else:
    move = input("enter the room or stay outside? ").lower()
    if move == "enter the room":
        print("Game Over")
    else:
        monster = input("ghost, vampire, or werewolf? ").lower()
        if monster == "werewolf":
            print("You Win")
        else:
            print("Game Over")

