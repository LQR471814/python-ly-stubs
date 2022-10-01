from _typeshed import Incomplete
from collections.abc import Generator
from typing import Type
from ly.node import WeakNode as WeakNode

string_types: Type[str]

class LyNode(WeakNode):
    isAtom: bool
    before: int
    after: int
    def ly(self, printer): ...
    def concat(self, other): ...

class Leaf(LyNode): ...

class Container(LyNode):
    defaultSpace: str
    @property
    def before(self): ...
    @property
    def after(self): ...
    def ly(self, printer): ...

class Printer:
    primary_quote_left: str
    primary_quote_right: str
    secondary_quote_left: str
    secondary_quote_right: str
    typographicalQuotes: bool
    language: str
    indentString: str
    def __init__(self) -> None: ...
    def quoteString(self, text): ...
    def indentGen(self, node, startIndent: int = ...) -> Generator[Incomplete, None, None]: ...
    def indent(self, node): ...

class Reference:
    name: Incomplete
    def __init__(self, name: str = ...) -> None: ...
    def __format__(self, format_spec): ...

class Named:
    name: str
    def ly(self, printer): ...

class HandleVars:
    childClass: Incomplete
    def ifbasestring(func): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, valueObj) -> None: ...
    def __contains__(self, name): ...
    def __delitem__(self, name) -> None: ...
    def importNode(self, obj): ...

class AddDuration:
    def ly(self, printer): ...

class Block(Container):
    defaultSpace: str
    before: Incomplete
    after: Incomplete

class Document(Container):
    defaultSpace: str
    after: int

class Text(Leaf):
    text: Incomplete
    def __init__(self, text: str = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class TextDur(AddDuration, Text): ...

class Line(Text):
    before: Incomplete
    after: Incomplete

class Comment(Text):
    after: int
    def ly(self, printer): ...

class LineComment(Comment):
    before: int

class BlockComment(Comment):
    @property
    def before(self): ...
    @property
    def after(self): ...
    def ly(self, printer): ...

class QuotedString(Text):
    isAtom: bool
    def ly(self, printer): ...

class Newline(LyNode):
    after: int

class BlankLine(Newline):
    before: int

class Scheme(Text):
    isAtom: bool
    def ly(self, printer): ...

class Version(Line):
    def ly(self, printer): ...

class Include(Line):
    def ly(self, printer): ...

class Assignment(Container):
    before: Incomplete
    after: Incomplete
    name: Incomplete
    def __init__(self, name: Incomplete | None = ..., parent: Incomplete | None = ..., valueObj: Incomplete | None = ...) -> None: ...
    def setValue(self, obj) -> None: ...
    def value(self): ...
    def ly(self, printer): ...

class Identifier(Leaf):
    isAtom: bool
    name: Incomplete
    def __init__(self, name: Incomplete | None = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Statement(Named, Container):
    before: int
    isAtom: bool

class Command(Statement):
    name: Incomplete
    def __init__(self, name, parent: Incomplete | None = ...) -> None: ...

class Enclosed(Container):
    may_remove_brackets: bool
    pre: Incomplete
    post: Incomplete
    before: Incomplete
    after: Incomplete
    isAtom: bool
    def ly(self, printer): ...

class Seq(Enclosed):
    pre: Incomplete
    post: Incomplete

class Sim(Enclosed):
    pre: Incomplete
    post: Incomplete

class Seqr(Seq):
    may_remove_brackets: bool

class Simr(Sim):
    may_remove_brackets: bool

class SchemeLily(Enclosed):
    pre: Incomplete
    post: Incomplete

class SchemeList(Enclosed):
    pre: Incomplete
    post: Incomplete
    def ly(self, printer): ...

class StatementEnclosed(Named, Enclosed):
    may_remove_brackets: bool

class CommandEnclosed(StatementEnclosed):
    name: Incomplete
    def __init__(self, name, parent: Incomplete | None = ...) -> None: ...

class Section(StatementEnclosed):
    may_remove_brackets: bool
    before: Incomplete
    after: Incomplete

class Book(Section):
    name: str

class BookPart(Section):
    name: str

class Score(Section):
    name: str

class Paper(HandleVars, Section):
    name: str

class Layout(HandleVars, Section):
    name: str

class Midi(HandleVars, Section):
    name: str

class Header(HandleVars, Section):
    name: str

class With(HandleVars, Section):
    name: str
    before: Incomplete
    after: Incomplete
    def ly(self, printer): ...

class ContextName(Text):
    def ly(self, printer): ...

class Context(HandleVars, Section):
    name: str
    def __init__(self, contextName: str = ..., parent: Incomplete | None = ...) -> None: ...

class ContextType(Container):
    before: Incomplete
    after: Incomplete
    isAtom: bool
    ctype: Incomplete
    new: Incomplete
    cid: Incomplete
    def __init__(self, cid: Incomplete | None = ..., new: bool = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...
    def getWith(self): ...
    def addInstrumentNameEngraverIfNecessary(self) -> None: ...

class ChoirStaff(ContextType): ...
class ChordNames(ContextType): ...
class CueVoice(ContextType): ...
class Devnull(ContextType): ...
class DrumStaff(ContextType): ...
class DrumVoice(ContextType): ...
class Dynamics(ContextType): ...
class FiguredBass(ContextType): ...
class FretBoards(ContextType): ...
class Global(ContextType): ...
class GrandStaff(ContextType): ...
class GregorianTranscriptionStaff(ContextType): ...
class GregorianTranscriptionVoice(ContextType): ...
class InnerChoirStaff(ContextType): ...
class InnerStaffGroup(ContextType): ...
class Lyrics(ContextType): ...
class MensuralStaff(ContextType): ...
class MensuralVoice(ContextType): ...
class NoteNames(ContextType): ...
class PianoStaff(ContextType): ...
class RhythmicStaff(ContextType): ...

class ScoreContext(ContextType):
    ctype: str

class Staff(ContextType): ...
class StaffGroup(ContextType): ...
class TabStaff(ContextType): ...
class TabVoice(ContextType): ...
class VaticanaStaff(ContextType): ...
class VaticanaVoice(ContextType): ...
class Voice(ContextType): ...

class UserContext(ContextType):
    ctype: Incomplete
    def __init__(self, ctype, cid: Incomplete | None = ..., new: bool = ..., parent: Incomplete | None = ...) -> None: ...

class ContextProperty(Leaf):
    prop: Incomplete
    context: Incomplete
    def __init__(self, prop, context: Incomplete | None = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class InputMode(StatementEnclosed): ...

class ChordMode(InputMode):
    name: str

class InputChords(ChordMode):
    name: str

class LyricMode(InputMode):
    name: str

class InputLyrics(LyricMode):
    name: str

class NoteMode(InputMode):
    name: str

class InputNotes(NoteMode):
    name: str

class FigureMode(InputMode):
    name: str

class InputFigures(FigureMode):
    name: str

class DrumMode(InputMode):
    name: str

class InputDrums(DrumMode):
    name: str

class AddLyrics(InputLyrics):
    name: str
    may_remove_brackets: bool
    before: Incomplete
    after: Incomplete

class LyricsTo(LyricMode):
    name: str
    cid: Incomplete
    def __init__(self, cid, parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Pitch(Leaf):
    octave: Incomplete
    note: Incomplete
    alter: Incomplete
    def __init__(self, octave: int = ..., note: int = ..., alter: int = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Duration(Leaf):
    dur: Incomplete
    dots: Incomplete
    factor: Incomplete
    def __init__(self, dur, dots: int = ..., factor: int = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Chord(Container):
    def ly(self, printer): ...

class Relative(Statement):
    name: str

class Transposition(Statement):
    name: str

class KeySignature(Leaf):
    note: Incomplete
    alter: Incomplete
    mode: Incomplete
    def __init__(self, note: int = ..., alter: int = ..., mode: str = ..., parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class TimeSignature(Leaf):
    num: Incomplete
    beat: Incomplete
    def __init__(self, num, beat, parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Partial(Named, Duration):
    name: str
    before: Incomplete
    after: Incomplete

class Tempo(Container):
    before: Incomplete
    after: Incomplete
    duration: Incomplete
    value: Incomplete
    def __init__(self, duration, value, parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class Clef(Leaf):
    clef: Incomplete
    def __init__(self, clef, parent: Incomplete | None = ...) -> None: ...
    def ly(self, printer): ...

class VoiceSeparator(Leaf):
    def ly(self, printer): ...

class Mark(Statement):
    name: str

class Markup(StatementEnclosed):
    name: str

class MarkupEnclosed(CommandEnclosed): ...
class MarkupCommand(Command): ...
