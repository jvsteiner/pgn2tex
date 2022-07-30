import chess
import chess.pgn
import chess.svg

from typing import Iterator, Tuple, Dict, List, Optional
from pathlib import Path


def load_pgn(path: Path) -> Iterator[chess.pgn.Game]:
    with open(path) as fd:
        game = chess.pgn.read_game(fd)
        while game:
            yield game
            game = chess.pgn.read_game(fd)


def get_section_from_level(title, level, book=False) -> str:

    if book:
        if level == 0:
            return "\\chapter{" + title + "}"
        else:
            return get_section_from_level(title, level - 1, book=False)
    if level == 0:
        return "\\section{" + title + "}"
    if level == 1:
        return "\\subsection{" + title + "}"
    if level == 2:
        return "\\subsubsection{" + title + "}"
    else:
        return title + "."


def strip_comment(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')' and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret.strip()
