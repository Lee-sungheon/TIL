# king

king, stone, N = input().split()
king_alp = king[0:1]
king_num = int(king[1:2])
stone_alp = stone[0:1]
stone_num = int(stone[1:2])

for index in range(int(N)):
    move = input()

    if move == 'R' and king_alp < 'H':
        king_alp = str(chr(ord(king_alp) + 1))
        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp < 'H':
                stone_alp = str(chr(ord(stone_alp) + 1))
            else:
                king_alp = str(chr(ord(king_alp) - 1))

    elif move == 'L' and king_alp > 'A':
        king_alp = str(chr(ord(king_alp) - 1))
        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp > 'A':
                stone_alp = str(chr(ord(stone_alp) - 1))
            else:
                king_alp = str(chr(ord(king_alp) + 1))

    elif move == 'B' and king_num > 1:
        king_num -= 1
        if king_alp == stone_alp and king_num == stone_num:
            if stone_num > 1:
                stone_num -= 1
            else:
                king_num += 1

    elif move == 'T' and king_num < 8:
        king_num += 1
        if king_alp == stone_alp and king_num == stone_num:
            if stone_num < 8:
                stone_num += 1
            else:
                king_num -= 1

    elif move == 'RT' and king_alp < 'H' and king_num < 8:
        king_num += 1
        king_alp = str(chr(ord(king_alp) + 1))

        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp < 'H' and stone_num < 8:
                stone_num += 1
                stone_alp = str(chr(ord(stone_alp) + 1))
            else:
                king_num -= 1
                king_alp = str(chr(ord(king_alp) - 1))

    elif move == 'LT' and king_alp > 'A' and king_num < 8:
        king_num += 1
        king_alp = str(chr(ord(king_alp) - 1))

        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp > 'A' and stone_num < 8:
                stone_num += 1
                stone_alp = str(chr(ord(stone_alp) - 1))
            else:
                king_num -= 1
                king_alp = str(chr(ord(king_alp) + 1))

    elif move == 'RB' and king_alp < 'H' and king_num > 1:
        king_num -= 1
        king_alp = str(chr(ord(king_alp) + 1))

        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp < 'H' and stone_num > 1:
                stone_num -= 1
                stone_alp = str(chr(ord(stone_alp) + 1))
            else:
                king_num += 1
                king_alp = str(chr(ord(king_alp) - 1))

    elif move == 'LB' and king_alp > 'A' and king_num > 1:
        king_num -= 1
        king_alp = str(chr(ord(king_alp) - 1))

        if king_alp == stone_alp and king_num == stone_num:
            if stone_alp > 'A' and stone_num > 1:
                stone_num -= 1
                stone_alp = str(chr(ord(stone_alp) - 1))
            else:
                king_num += 1
                king_alp = str(chr(ord(king_alp) + 1))
        
print((king_alp + str(king_num)))
print((stone_alp + str(stone_num)))