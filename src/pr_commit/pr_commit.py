"""The pr-commit hook."""

import re
import argparse
from typing import Sequence

E_LIST = re.compile("[eèéêëěẽēėęEÈÉÊËĚẼĒĖĘ]")


def has_fifth_glyph(filename: str, log: bool) -> bool:
    """
    Function that returns whether a file contains the letter E in its title or contents.

    Parameters
    ----------
    filename : str
        The file name.
    log : bool
        Whether or not to log the invalid lines to the output.

    Returns
    -------
    bool
        Whether or not the file contains the letter E in its title or contents.
    """
    if E_LIST.search(filename):
        if log:
            print(f"Invalid naming: {filename}")
        return True
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            if E_LIST.search(line):
                if log:
                    print(f"Invalid string: {line}")
                return True
    return False


def main(argv: Sequence[str] = None) -> int:
    """
    The command line interface for pr-commit.

    Parameters
    ----------
    argv : Sequence[str] | None, optional
        The command line arguments, by default None.

    Returns
    -------
    int
        1 if there is a pr-commit error, or 0 if there is not.
    """
    parser = argparse.ArgumentParser(prog="pr-commit")
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames to process.",
    )
    parser.add_argument(
        "--log",
        default=False,
        action="store_true",
    )

    args = parser.parse_args(argv)

    return (
        1
        if any([has_fifth_glyph(filename, args.log) for filename in args.filenames])
        else 0
    )
