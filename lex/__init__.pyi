import enum
from ._token import *
from .. import slexer
from ._mode import extensions as extensions, guessMode as guessMode, modes as modes
from _typeshed import Incomplete

class Parser(slexer.Parser):
    re_flags: enum.IntFlag
    argcount: int
    default: Incomplete
    mode: Incomplete
    def __init__(self, argcount: Incomplete | None = ...) -> None: ...
    def freeze(self): ...

class FallthroughParser(Parser, slexer.FallthroughParser): ...

class State(slexer.State):
    def endArgument(self) -> None: ...
    def mode(self): ...

class Fridge(slexer.Fridge):
    def __init__(self, stateClass=...) -> None: ...

def state(mode): ...
def guessState(text): ...

# Names in __all__ with no definition:
#   BlockComment
#   BlockCommentEnd
#   BlockCommentStart
#   Character
#   Comment
#   Dedent
#   Error
#   Indent
#   LineComment
#   MatchEnd
#   MatchStart
#   Newline
#   Numeric
#   Space
#   String
#   StringEnd
#   StringStart
#   Token
#   Unparsed
