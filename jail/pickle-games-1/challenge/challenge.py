#!/usr/bin/env python3

import pickle


def check(data):
    return len(data) <= 400


if __name__ == "__main__":
    print("Welcome to the pickle games! (Level 0)")
    data = bytes.fromhex(input("Enter your hex-encoded pickle data: "))
    if check(data):
        result = pickle.loads(data)
        print(f"Result: {result}")
    else:
        print("Check failed :(")
