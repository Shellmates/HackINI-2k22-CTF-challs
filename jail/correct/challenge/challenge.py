#!/usr/bin/env python3

# REDACTED

WELCOME = "Welcome to the Wonderland of PYTHON"


def bad_inp(arg):
    return any(ord(char) >= 128 for char in arg) 


def check(password):
    if password == #REDACTED:
        return # print the flag
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
