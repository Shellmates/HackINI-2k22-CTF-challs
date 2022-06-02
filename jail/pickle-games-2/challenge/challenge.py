#!/usr/bin/env python3

import pickle
import pickletools

from flag import FLAG


def check(data):
    return len(data) <= 400 and all(
        opcode.code.encode() != pickle.REDUCE
        for opcode, _, _ in pickletools.genops(data)
    )


if __name__ == "__main__":
    print("Welcome to the pickle games! (Level 1)")
    data = bytes.fromhex(input("Enter your hex-encoded pickle data: "))
    if check(data):
        result = pickle.loads(data)
        print(f"Result: {result}")
    else:
        print("Check failed :(")
