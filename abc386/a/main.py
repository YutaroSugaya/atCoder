def is_full_house(cards):
    from collections import Counter
    count = Counter(cards)
    if len(count) == 2 and set(count.values()) == {3,2}:
        return True
    return False

def main():
    A, B, C, D = map(int, input().split())

    for x in range(1,14):
        cards = [A, B, C, D, x]
        if is_full_house(cards):
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()
