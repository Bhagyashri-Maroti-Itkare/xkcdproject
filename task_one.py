"""
CLI tool to feach data from "https://xkcd.com/"

python task_one.py --max 87  --any 15
"""
import argparse
from random import randrange
from typing import List

def rand_gen(start: int = 1, stop: int = 87, limit: int = 15) ->List[int]:
    """

    Args:
        start (int): first numeric value of the range
        stop (int): last numeric value of the range
        limit (int): number of result to yield

    Returns:
        list [int]: random values in range(start:stop) with count limited to 'limit'

    """
    result  = [randrange(start,stop+1) for i in range(limit)]
    return result
if __name__ == "__main__":
    example = """example:
    python task_one.py --max 87 --any 15
    """
    parser = argparse.ArgumentParser(
        description="CLI tool to feach resource(s) from API",
        epilog=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be feach"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunk of resources to be feached"
    )

    args = parser.parse_args()
    print(args.any)
    print(args.max)

    print(parser.print_help())
    comic_number_set = rand_gen(1,87,15) #comic_number_set = rand_gen(1,args.max,args.any)
    print(comic_number_set)