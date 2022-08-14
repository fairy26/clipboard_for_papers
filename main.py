import sys
import time

from pyperclip import copy, waitForNewPaste, PyperclipTimeoutException


def init_clipboard():
    """clear clipboard"""
    copy("")


def format(s: str) -> str:
    """extract \r and \n"""
    return s.replace("\r", "").strip().replace("\n", " ")


def debug(string: str, before: bool = False, after: bool = False):
    """print strings with prefix"""
    if before:
        print("--- FORMAT ---")
        print(repr(string))
    elif after:
        print("  -  vvvv  -")
        print(repr(string))
        print("--------------\n")
    else:
        print(string)


def run():
    init_clipboard()
    during = 60  # [s]

    while True:
        try:
            string = waitForNewPaste(during)
        except PyperclipTimeoutException:
            debug("exit")
            sys.exit(0)
        except KeyboardInterrupt:
            debug("exit")
            sys.exit(0)

        if string == "":
            continue

        debug(string, before=True)
        string = format(string)
        debug(string, after=True)

        copy(string)

        time.sleep(1)


if __name__ == "__main__":
    run()
