##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## ArgChecker
##

class ArgumentsChecker:
    def __init__(self, args: list) -> None:
        self._intArgs = list()
        self._args = args
        pass

    def checkArgsTypes(self) -> bool:
        for nb in self._args:
            try:
                tmp = int(nb)
                self._intArgs.append(tmp)
            except ValueError:
                print("ValueError at ArgChecker l.16")
                return False
        if (1 > self._intArgs[1] or self._intArgs[2] > self._intArgs[0] - 2) or \
                self._intArgs[1] == (self._intArgs[0] - 1):
            return False
        if len(self._intArgs) == 5:
            if 1 > self._intArgs[3] or self._intArgs[4] > (self._intArgs[0] - 2):
                return False
        return True

    def getArgsList(self) -> list:
        return self._intArgs
