from typing import Literal
import ly.lex.lilypond
from _typeshed import Incomplete
from collections.abc import Generator

Note = Literal[0, 1, 2, 3, 4, 5, 6]
Alter = float
Octave = Literal[-2, 2]
Accidental = Literal["", "?", "!"]

Language = Literal["nederlands", "english", "deutsch", "svenska",
                   "italiano", "espanol", "portugues", "vlaams",
                   "norsk", "suomi", "catalan"]

pitchInfo: dict[Language, tuple[
    tuple[str, str, str, str, str, str],
    tuple[str, str, str, str, str, str, str],
    tuple[tuple[str, str], ...] | None
]]


class PitchNameNotAvailable(Exception):
    language: Language
    def __init__(self, language: Language) -> None: ...


class Pitch:
    note: Note
    alter: Alter
    octave: Octave
    accidental: Accidental
    octavecheck: bool
    def __init__(self, note: Note = ..., alter: Alter = ..., octave: Octave = ...,
                 accidental: Accidental = ..., octavecheck: bool | None = ...) -> None: ...

    def output(self, language: Language = ...) -> str: ...
    @classmethod
    def c1(cls) -> Pitch: ...
    @classmethod
    def c0(cls) -> Pitch: ...
    @classmethod
    def f0(cls) -> Pitch: ...
    def copy(self) -> Pitch: ...
    def makeAbsolute(self, lastPitch: Pitch) -> None: ...
    def makeRelative(self, lastPitch: Pitch) -> None: ...


class PitchWriter:
    language: Language
    names: Incomplete
    accs: Incomplete
    replacements: Incomplete
    def __init__(self, names, accs, replacements=...) -> None: ...
    def __call__(self, note, alter: int = ...): ...


class PitchReader:
    names: Incomplete
    accs: Incomplete
    replacements: Incomplete
    rx: Incomplete
    def __init__(self, names, accs, replacements=...) -> None: ...
    def __call__(self, text): ...


def octaveToString(octave) -> str: ...
def octaveToNum(octave): ...
def pitchReader(language): ...
def pitchWriter(language): ...


class PitchIterator:
    source: Incomplete
    def __init__(self, source, language: Language = ...) -> None: ...
    language: Language
    def setLanguage(self, lang): ...
    def tokens(self) -> Generator[Incomplete, None, None]: ...
    def read(self, token): ...
    def pitches(self) -> Generator[Incomplete, None, None]: ...
    def position(self, t): ...
    def write(self, pitch, language: Incomplete | None = ...) -> None: ...


class LanguageName(ly.lex.Token):
    ...
