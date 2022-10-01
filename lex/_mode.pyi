from typing import Callable, Literal
from ly.lex import Parser

Modes = Literal["lilypond", "html", "scheme",
                "latex", "texinfo", "docbook", "mup"]
modes: dict[Modes, Callable[[], Parser]]
extensions: dict[Modes, str]


def guessMode(text): ...
