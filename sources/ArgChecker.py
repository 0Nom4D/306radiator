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
        for i in [1, 2]:
            if self._intArgs[i] < 1 or self._intArgs[i] >= self._intArgs[0] - 2:
                return False
        if len(self._intArgs) == 5:
            for i in [3, 4]:
                if not 0 <= self._intArgs[i] < self._intArgs[0]:
                    return False
        return True

    def getArgsList(self) -> list:
        return self._intArgs
