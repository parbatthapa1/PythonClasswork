# 22. Magic Forest Game

print("Welcome to the Magic Forest")
direction = input("Go north or south? ").lower()

if direction == "south":
    print("Game Over")
else:
    move = input("cross the river or follow the path? ").lower()
    if move == "cross the river":
        print("Game Over")
    else:
        choice = input("fairy, ogre, or elf? ").lower()
        if choice == "elf":
            print("You Win")
        else:
            print("Game Over")
