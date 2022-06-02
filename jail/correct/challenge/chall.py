#!/usr/bin/env python3

import base64

WELCOME = "Welcome to the Wonderland of PYTHON"


def bad_inp(arg):
    return any(ord(char) >= 128 for char in arg) 


def check(password):
    if password == base64.b64decode(
        "".join(
            (
                chr((c - 84734) % 383)
                for c in [
                    180,
                    201,
                    195,
                    207,
                    190,
                    141,
                    169,
                    140,
                    189,
                    200,
                    165,
                    141,
                    192,
                    178,
                    144,
                    199,
                    170,
                    175,
                    168,
                    142,
                    192,
                    162,
                    144,
                    207,
                    181,
                    162,
                    210,
                    213,
                    170,
                    178,
                    173,
                    202,
                    174,
                    139,
                    194,
                    200,
                    179,
                    212,
                    168,
                    201,
                    190,
                    213,
                    139,
                    213,
                    169,
                    161,
                    140,
                    169,
                    178,
                    162,
                    198,
                    194,
                    190,
                    163,
                    169,
                    198,
                    181,
                    201,
                    164,
                    148,
                    164,
                    158,
                    191,
                    205,
                    191,
                    141,
                    177,
                    212,
                    189,
                    142,
                    211,
                    199,
                    191,
                    142,
                    165,
                    198,
                    191,
                    196,
                    164,
                    152,
                ]
            )
        )
    ):
        return print(
            base64.b64decode(
                "".join(
                    (
                        chr((c - 68874) % 764)
                        for c in [
                            213,
                            164,
                            218,
                            222,
                            212,
                            185,
                            234,
                            230,
                            203,
                            202,
                            196,
                            222,
                            213,
                            165,
                            230,
                            198,
                            212,
                            220,
                            196,
                            228,
                            191,
                            163,
                            171,
                            232,
                            203,
                            223,
                            226,
                            222,
                            203,
                            165,
                            196,
                            236,
                            202,
                            164,
                            217,
                            162,
                            213,
                            163,
                            171,
                            219,
                            191,
                            236,
                            192,
                            231,
                            202,
                            164,
                            192,
                            232,
                            213,
                            224,
                            188,
                            163,
                            213,
                            186,
                            196,
                            222,
                            204,
                            186,
                            162,
                            175,
                        ]
                    )
                )
            )
        )
    return print("Wrong password")


def main():
    scope = {"__builtins__": {func.__name__: func for func in safe_builtins}}
    print(WELCOME)
    while True:
        inp = input("Command : ")
        if not bad_inp(inp):
            try:
                eval(inp, scope)
            except:
                print("Yes it's jail, but don't break it")
        else:
            print("Imagine all the hours you were gonna save if it was allowed")


if __name__ == "__main__":
    safe_builtins = [
        abs,
        aiter,
        all,
        any,
        anext,
        ascii,
        bin,
        bool,
        bytearray,
        bytes,
        callable,
        chr,
        classmethod,
        compile,
        complex,
        delattr,
        dict,
        dir,
        divmod,
        enumerate,
        filter,
        float,
        format,
        frozenset,
        globals,
        hasattr,
        hash,
        hex,
        id,
        int,
        isinstance,
        issubclass,
        iter,
        len,
        list,
        locals,
        map,
        max,
        memoryview,
        min,
        oct,
        ord,
        pow,
        print,
        property,
        range,
        repr,
        reversed,
        round,
        set,
        setattr,
        slice,
        sorted,
        staticmethod,
        str,
        sum,
        super,
        tuple,
        type,
        vars,
        zip,
        bad_inp,
        check,
    ]
    main()
