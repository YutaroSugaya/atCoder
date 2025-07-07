import itertools

def main():
    n = int(input())    
    strings = [input().strip() for _ in range(n)]
    car = []
    ans = 0
    for perm in itertools.permutations(range(n), 2):
        i, j = perm
        result = strings[i] + strings[j]
        if result not in car:
            ans += 1
            car.append(result)
    print(ans)

if __name__ == "__main__":
    main()

