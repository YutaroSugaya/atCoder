from collections import defaultdict, deque

def main():
    n = int(input().strip())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            ans += 1
    print(ans)    

if __name__ == "__main__":
    main() 