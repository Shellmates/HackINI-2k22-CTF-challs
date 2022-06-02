#!/usr/bin/env python3

import pickle
import io

from flag import FLAG


class Flag:
    def __init__(self, flag):
        self.flag = flag

    def __getattribute__(self, item):
        return "lol"


class Empty:
    pass


flagObj = Flag(FLAG)


class MyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if (
            module == "__main__"
            and (
                name.startswith("Flag")
                or name.startswith("Empty")
                or name.startswith("flagObj")
            )
            and not "class" in name
            and not "global" in name
        ):
            return super().find_class(module, name)
        else:
            raise pickle.UnpicklingError("No :(")


def check(data):
    return len(data) <= 80


if __name__ == "__main__":
    print("Welcome to the pickle games! (Level 2)")
    data = bytes.fromhex(input("Enter your hex-encoded pickle data: "))
    if check(data):
        result = MyUnpickler(io.BytesIO(data)).load()
        print(f"Result: {result}")
    else:
        print("Check failed :(")
