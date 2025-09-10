# -*- coding: utf-8 -*-
import argparse
import sys
import os

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from ThirdQ import ThirdQ
from JsonDataReader import JsonDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    extension = os.path.splitext(path)[1]
    if extension == ".txt":
        reader = TextDataReader()
    elif extension == ".json":
        reader = JsonDataReader()
    else:
        raise Exception("Format {} not supported.".format(extension))
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    ThirdQ(students).print_3q()


if __name__ == "__main__":
    main()
