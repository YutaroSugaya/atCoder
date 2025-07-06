import math
from collections import defaultdict


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    total = sum(a)
    
    if total <= m:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

