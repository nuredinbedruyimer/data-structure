red, blue = list(map(int, input().split()))

same_palyer = 0
diff_player = 0

turn = 0

colors = []
last = -1



while red and blue:
    #  patya
    if turn == 0:
        if last == 0 and red:
            colors.append(0)
            red -= 1
            last = 0
        elif last == 1 and blue:
            colors.append(1)
            blue -=1
            last = 1
        else:
            if red < blue and red:
                colors.append(0)
                red -= 1
                last = 0
            else:
                colors.append(1)
                blue -= 1
                last = 1
        turn = 1
    elif turn == 1:
        if last == 0 and blue:
            colors.append(1)
            red -= 1
            last = 1
        elif last == 1 and red:
            colors.append(0)
            blue -=1
            last = 0
        turn = 0

            
while red:
    colors.append(0)
    red -= 1
while blue:
    colors.append(1)
    blue -= 1

print(colors)

        
    