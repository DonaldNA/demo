import math
import sys
import argparse

def main():

    parser = argparse.ArgumentParser(description='Process some numbers.')
    parser.add_argument('numbers', metavar='N', type=float, nargs=2,
                    help='an number for the accumulator')
    parser.add_argument('--hypotenus', dest='hypotenus', action='store_const',
                    const=calc_hypotenus, default=calc_hypotenus,
                    help='calculate hypotenus')

    args = parser.parse_args()
    print(args.hypotenus(args.numbers))



def calc_hypotenus(float_lst) -> float:
    a, b = float_lst
    c = math.sqrt((a**2)+ (b**2))
    return c
    

if __name__ == "__main__":
    main()