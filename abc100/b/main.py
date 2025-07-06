import math
from collections import defaultdict


def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    print(a[k-1])

if __name__ == "__main__":
    main()