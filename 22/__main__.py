from functools import partial


def deal_into_new_stack(deck):
    new_deck = deck.copy()
    new_deck.reverse()
    return new_deck


def cut_n_cards(deck, n):
    if n == 0:
        return deck.copy()

    if n > 0:
        cut_point = n
    else:
        cut_point = len(deck) + n

    cut_cards = deck[:cut_point]
    rest_of_cards = deck[cut_point:]
    return rest_of_cards + cut_cards


def deal_with_increment_n(deck, n):
    length = len(deck)
    new_deck = length * [None]
    position = 0
    for card in deck:
        assert new_deck[position] is None
        new_deck[position] = card
        position = (position + n) % length
    return new_deck


def parse_shuffles(string):
    parts = string.split(" ")
    first = parts[0]
    last = parts[-1]

    if first == "cut":
        return partial(cut_n_cards, n = int(last))

    assert first == "deal"

    if last == "stack":
        return deal_into_new_stack
    else:
        return partial(deal_with_increment_n, n = int(last))


with open("22/input.txt") as f:
    shuffles = list(map(parse_shuffles, f.read().splitlines()))

deck = [i for i in range(10007)]
for shuffle in shuffles:
    deck = shuffle(deck)

for i, card in enumerate(deck):
    if card == 2019:
        print("The answer to Part 1 is {}.".format(i))
