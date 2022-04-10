import math
import sys

def main():
    _, a, b = sys.argv
    a = float(a)
    b = float(b)
    c = calc_hypotenus(a,b)
    print(c)


def calc_hypotenus(a: float, b: float) -> float:
    c = math.sqrt((a**2)+ (b**2))
    return c
    

if __name__ == "__main__":
    main()