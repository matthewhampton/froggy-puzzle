BUM = "BUM"
HEAD = "HEAD"

PURPLE = "PURPLE"
ORANGE = "ORANGE"
BLUE = "BLUE"
GREEN = "GREEN"
PINK = "PINK"
RED = "RED"

FROGGY_CARDS = [ 
    ((BLUE, HEAD), (PURPLE, HEAD), (ORANGE, BUM), (GREEN, BUM)),
    ((BLUE, BUM), (ORANGE, HEAD), (BLUE, HEAD), (GREEN, BUM)),
    ((PURPLE, BUM), (BLUE, HEAD), (GREEN, HEAD), (ORANGE, BUM)),
    ((GREEN, BUM), (BLUE, HEAD), (PURPLE, HEAD), (BLUE, BUM)),
    ((BLUE, BUM), (BLUE, HEAD), (ORANGE, HEAD), (GREEN, BUM)),
    ((PURPLE, BUM), (ORANGE, HEAD), (GREEN, HEAD), (BLUE, BUM)),
    ((PURPLE, BUM), (ORANGE, HEAD), (GREEN, HEAD), (ORANGE, BUM)),
    ((GREEN, BUM), (ORANGE, HEAD), (BLUE, HEAD), (PURPLE, BUM)),
    ((PURPLE, BUM), (ORANGE, HEAD), (GREEN, HEAD), (BLUE, BUM)),
]

CARDS = FROGGY_CARDS

def is_winner(cards):

    for i in range(3):
        for j in range(3):
            card = cards[i][j]
            if card is None:
                continue
            if j<2:
                right_card = cards[i][j+1]
                if right_card:
                    if card[1][0] != right_card[3][0]:
                        return False
                    if card[1][1] == right_card[3][1]:
                        return False
            if j>0:
                left_card = cards[i][j-1]
                if left_card:
                    if card[3][0] != left_card[1][0]:
                        return False
                    if card[3][1] == left_card[1][1]:
                        return False
            if i<2:
                bottom_card = cards[i+1][j]
                if bottom_card:
                    if card[2][0] != bottom_card[0][0]:
                        return False
                    if card[2][1] == bottom_card[0][1]:
                        return False
            if i>0:    
                top_card = cards[i-1][j]
                if top_card:
                    if card[0][0] != top_card[2][0]:
                        return False
                    if card[0][1] == top_card[2][1]:
                        return False
    return True

def main():
    cards = [[None, None, None],[None, None, None],[None, None, None]]
    cards_left = CARDS
    fill_combinations(cards, cards_left)

def rotate_card_clockwise(card):
    return tuple(card[(p-1)%4] for p in range(4))

def rotate_solution_clockwise(cards):
    return (
        (rotate_card_clockwise(cards[2][0]), rotate_card_clockwise(cards[1][0]), rotate_card_clockwise(cards[0][0])),
        (rotate_card_clockwise(cards[2][1]), rotate_card_clockwise(cards[1][1]), rotate_card_clockwise(cards[0][1])),
        (rotate_card_clockwise(cards[2][2]), rotate_card_clockwise(cards[1][2]), rotate_card_clockwise(cards[0][2])),
    )

combinations_checked = 0
solutions = []

def fill_combinations(cards, cards_left):
    global combinations_checked, solutions
    for i in range(3):
        for j in range(3):
            if cards[i][j] is None:
                # print("Combinations for (%s, %s) - %s" % (i,j,len(cards_left)))
                for card in cards_left:

                    new_cards_left = list(cards_left)
                    new_cards_left.remove(card)

                    for rotation in range(4):
                        cards[i][j] = tuple(card[(rotation+p)%4] for p in range(4))

                        if is_winner(cards):
                            combinations_checked += 1
                            # if combinations_checked % 10 == 0:
                            # print(str(combinations_checked) + " checked")

                            if new_cards_left:
                                new_cards = [list(r) for r in cards]
                                fill_combinations(new_cards, new_cards_left)
                            else:
                                s_tuples = tuple(tuple(r) for r in cards)
                                dup = False
                                for s in solutions:
                                    if s == s_tuples:
                                        dup = True
                                        break
                                    for rc in range(4):
                                        pres = s
                                        s = rotate_solution_clockwise(s)
                                        if s == s_tuples:
                                            dup = True
                                            break
                                    if dup:
                                        break
                                if not dup:
                                    solutions.append(s_tuples)                                    
                                    print()
                                    print()
                                    print("WINNER %s!"%len(solutions))
                                    print("-------")
                                    print()
                                    for i2 in range(3):
                                        for j2 in range(3):
                                            print((i2, j2))
                                            print(cards[i2][j2])
                                    
                
                return


                    

if __name__ == "__main__":
    main()
    # print(str(combinations_checked) + " checked")