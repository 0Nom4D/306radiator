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
        tmp = int(0)

        for nb in self._args:
            try:
                tmp = int(nb)
                self._intArgs.append(tmp)
            except ValueError:
                print("ValueError at ArgChecker l.16")
                return False
        return True
