import math
from collections import defaultdict

def main():
    n,m=map(int,input().split())
    a = 0
    a += sum(map(int, input().split()))
    if a <= m:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
