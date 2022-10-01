from . import FallthroughParser as FallthroughParser, Parser as Parser, _token
from _typeshed import Incomplete

class Comment(_token.Comment): ...

class LineComment(Comment):
    rx: str

class String(_token.String): ...

class StringQuotedStart(String, _token.StringStart):
    rx: str
    def update_state(self, state) -> None: ...

class StringQuotedEnd(String, _token.StringEnd):
    rx: str
    def update_state(self, state) -> None: ...

class StringQuoteEscape(_token.Character):
    rx: str

class Macro(_token.Token):
    rx: str

class Preprocessor(_token.Token):
    rx: str

class ParseMup(Parser):
    mode: str
    items: Incomplete

class ParseString(Parser):
    default: Incomplete
    items: Incomplete
