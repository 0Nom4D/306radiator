#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## main
##

from sources.ArgChecker import ArgumentsChecker
from sources.exitCode import exitCode
from sources.Radiator import Radiator
from sys import argv


def printUsage() -> int:
    print("USAGE")
    print("\t./306radiator n ir jr [i j]", end='\n\n')
    print("DESCRIPTION")
    print("\tn\t\tsize of the room")
    print("\t(ir, jr)\tcoordinates of the radiator")
    print("\t(i, j)\t\tcoordinates of a point in the room")
    return exitCode.OK


def main() -> int:
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == "--help"):
        return printUsage()
    elif len(argv) not in [4, 6]:
        return exitCode.ERROR
    ArgChecker = ArgumentsChecker(argv[1:])
    if not ArgChecker.checkArgsTypes():
        return exitCode.ERROR
    Radiator(ArgChecker.getArgsList())
    return exitCode.OK


if __name__ == "__main__":
    exit(main())