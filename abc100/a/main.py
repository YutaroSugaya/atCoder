import math
from collections import defaultdict


def main():
    a,b=map(int,input().split())
    print(":(" if a>8 or b>8 else "Yay!")

if __name__ == "__main__":
    main()