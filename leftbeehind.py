sweet, sour = map(int, input().split())
while sour+sweet>0:
    if sour+sweet == 13:
        print("Never speak again.")
    else:
        if sweet>sour: print("To the convention.")
        elif sweet<sour: print("Left beehind.")
        else: print("Undecided.")
    sweet, sour = map(int, input().split())