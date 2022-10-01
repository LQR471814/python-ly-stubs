from . import FallthroughParser as FallthroughParser, Parser as Parser, _token, lilypond as lilypond
from _typeshed import Incomplete

class Comment(_token.Comment): ...

class LineComment(Comment, _token.LineComment):
    rx: str

class BlockCommentStart(Comment, _token.BlockCommentStart):
    rx: str
    def update_state(self, state) -> None: ...

class BlockCommentEnd(Comment, _token.Leaver, _token.BlockCommentEnd):
    rx: str

class Attribute(_token.Token): ...

class Keyword(_token.Token):
    rx: str

class Block(_token.Token): ...

class BlockStart(Block):
    rx: str
    def update_state(self, state) -> None: ...

class BlockEnd(Block, _token.Leaver):
    rx: str

class EscapeChar(_token.Character):
    rx: str

class Accent(EscapeChar):
    rx: str

class Verbatim(_token.Token): ...

class VerbatimStart(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class VerbatimEnd(Keyword, _token.Leaver):
    rx: str

class LilyPondBlockStart(Block):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondBlockStartBrace(Block):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondBlockEnd(Block, _token.Leaver):
    rx: str

class LilyPondEnvStart(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondEnvEnd(Keyword, _token.Leaver):
    rx: str

class LilyPondFileStart(Block):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondFileStartBrace(Block):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondAttrStart(Attribute):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondAttrEnd(Attribute, _token.Leaver):
    rx: str

class ParseTexinfo(Parser):
    mode: str
    items: Incomplete

class ParseComment(Parser):
    default: Incomplete
    items: Incomplete

class ParseBlock(Parser):
    items: Incomplete

class ParseVerbatim(Parser):
    default: Incomplete
    items: Incomplete

class ParseLilyPondBlockAttr(Parser):
    items: Incomplete

class ParseLilyPondEnvAttr(FallthroughParser):
    items: Incomplete
    def fallthrough(self, state) -> None: ...

class ParseLilyPondAttr(Parser):
    default: Incomplete
    items: Incomplete

class ParseLilyPondFile(Parser):
    items: Incomplete

class ParseLilyPondBlock(lilypond.ParseGlobal):
    items: Incomplete

class ParseLilyPondEnv(lilypond.ParseGlobal):
    items: Incomplete
