from . import FallthroughParser as FallthroughParser, Parser as Parser, _token, lilypond as lilypond
from _typeshed import Incomplete

class Scheme(_token.Token): ...
class String(_token.String): ...

class StringQuotedStart(String, _token.StringStart):
    rx: str
    def update_state(self, state) -> None: ...

class StringQuotedEnd(String, _token.StringEnd):
    rx: str
    def update_state(self, state) -> None: ...

class StringQuoteEscape(_token.Character):
    rx: str

class Comment(_token.Comment): ...

class LineComment(Comment, _token.LineComment):
    rx: str

class BlockCommentStart(Comment, _token.BlockCommentStart):
    rx: str
    def update_state(self, state) -> None: ...

class BlockCommentEnd(Comment, _token.BlockCommentEnd, _token.Leaver):
    rx: str

class BlockComment(Comment, _token.BlockComment): ...

class OpenParen(Scheme, _token.MatchStart, _token.Indent):
    rx: str
    matchname: str
    def update_state(self, state) -> None: ...

class CloseParen(Scheme, _token.MatchEnd, _token.Dedent):
    rx: str
    matchname: str
    def update_state(self, state) -> None: ...

class Quote(Scheme):
    rx: str

class Dot(Scheme):
    rx: str

class Bool(Scheme, _token.Item):
    rx: str

class Char(Scheme, _token.Item):
    rx: str

class Word(Scheme, _token.Item):
    rx: str

class Keyword(Word):
    @classmethod
    def test_match(cls, match): ...

class Function(Word):
    @classmethod
    def test_match(cls, match): ...

class Variable(Word):
    @classmethod
    def test_match(cls, match): ...

class Constant(Word):
    @classmethod
    def test_match(cls, match): ...

class Number(_token.Item, _token.Numeric):
    rx: str

class Fraction(Number):
    rx: str

class Float(Number):
    rx: str

class VectorStart(OpenParen):
    rx: str

class LilyPond(_token.Token): ...

class LilyPondStart(LilyPond, _token.MatchStart, _token.Indent):
    rx: str
    matchname: str
    def update_state(self, state) -> None: ...

class LilyPondEnd(LilyPond, _token.Leaver, _token.MatchEnd, _token.Dedent):
    rx: str
    matchname: str

class ParseScheme(Parser):
    mode: str
    items: Incomplete

class ParseString(Parser):
    default: Incomplete
    items: Incomplete

class ParseBlockComment(Parser):
    default: Incomplete
    items: Incomplete

class ParseLilyPond(lilypond.ParseMusic):
    items: Incomplete
