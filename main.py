import logging
import sys
import time

from pyperclip import PyperclipTimeoutException, copy, waitForNewPaste


def init_clipboard():
    """clear clipboard"""
    copy("")


def update_clipboard(s: str):
    """update clipboard by specified string"""
    copy(s)


def format(s: str) -> str:
    """extract \r and \n"""
    return s.replace("\r", "").strip().replace("\n", " ")


def run(waiting_seconds: int = 60, sleep_seconds: int = 1):
    init_clipboard()

    while True:
        try:
            logging.info("🤔 waiting for new copy to clipboard...")
            text = waitForNewPaste(waiting_seconds)
        except PyperclipTimeoutException:
            logging.info("👋 timeout! bye~~")
            sys.exit(0)
        except KeyboardInterrupt:
            logging.info("👋 see ya!")
            sys.exit(0)

        if text == "":
            logging.info("🖼️ you might take a screenshot. skip it.\n")
            continue

        logging.info("🌀 BEFORE")
        logging.info(f"{text}\n")

        formatted_text = format(text)

        logging.info("✨ AFTER")
        logging.info(f"{formatted_text}\n")

        update_clipboard(formatted_text)

        time.sleep(sleep_seconds)


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    run()
