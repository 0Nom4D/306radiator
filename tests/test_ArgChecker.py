##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_ArgChecker
##

from sources.ArgChecker import ArgumentsChecker
from sources.exitCode import exitCode


class TestExitCodes:
    def test_okCode(self):
        assert not exitCode.OK

    def test_errorCode(self):
        assert exitCode.ERROR == 84


class TestArgChecker:
    def test_BadArgumentType(self):
        tChecker = ArgumentsChecker(["a", "a", "a", "a", "a"])
        assert not tChecker.checkArgsTypes()

    def test_BadArgumentTypePrints(self, capsys):
        tChecker = ArgumentsChecker(["a", "a", "a", "a", "a"])
        tChecker.checkArgsTypes()
        stdout = capsys.readouterr()[0]
        assert stdout == "ValueError at ArgChecker l.16\n"

    def test_CasualArguments(self):
        tChecker = ArgumentsChecker(["1", "1", "1", "1", "1"])
        assert tChecker.checkArgsTypes()
