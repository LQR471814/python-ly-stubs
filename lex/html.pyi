from . import FallthroughParser as FallthroughParser, Parser as Parser, _token, lilypond as lilypond
from _typeshed import Incomplete

class Comment(_token.Comment): ...

class CommentStart(Comment, _token.BlockCommentStart):
    rx: str
    def update_state(self, state) -> None: ...

class CommentEnd(Comment, _token.Leaver, _token.BlockCommentEnd):
    rx: str

class String(_token.String): ...
class Tag(_token.Token): ...

class TagStart(Tag):
    rx: str
    def update_state(self, state) -> None: ...

class TagEnd(Tag, _token.Leaver):
    rx: str

class AttrName(_token.Token):
    rx: str

class EqualSign(_token.Token):
    rx: str
    def update_state(self, state) -> None: ...

class Value(_token.Leaver):
    rx: str

class StringDQStart(String, _token.StringStart):
    rx: str
    def update_state(self, state) -> None: ...

class StringSQStart(String, _token.StringStart):
    rx: str
    def update_state(self, state) -> None: ...

class StringDQEnd(String, _token.StringEnd, _token.Leaver):
    rx: str

class StringSQEnd(String, _token.StringEnd, _token.Leaver):
    rx: str

class EntityRef(_token.Character):
    rx: str

class LilyPondTag(Tag): ...

class LilyPondVersionTag(LilyPondTag):
    rx: str

class LilyPondFileTag(LilyPondTag):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondFileTagEnd(LilyPondTag, _token.Leaver):
    rx: str

class LilyPondInlineTag(LilyPondTag):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondCloseTag(LilyPondTag, _token.Leaver):
    rx: str

class LilyPondTagEnd(LilyPondTag):
    rx: str
    def update_state(self, state) -> None: ...

class LilyPondInlineTagEnd(LilyPondTag, _token.Leaver):
    rx: str

class SemiColon(_token.Token):
    rx: str
    def update_state(self, state) -> None: ...

class ParseHTML(Parser):
    mode: str
    items: Incomplete

class ParseAttr(Parser):
    items: Incomplete

class ParseStringDQ(Parser):
    default: Incomplete
    items: Incomplete

class ParseStringSQ(Parser):
    default: Incomplete
    items: Incomplete

class ParseComment(Parser):
    default: Incomplete
    items: Incomplete

class ParseValue(FallthroughParser):
    items: Incomplete
    def fallthrough(self, state) -> None: ...

class ParseLilyPondAttr(Parser):
    items: Incomplete

class ParseLilyPondFileOptions(Parser):
    items: Incomplete

class ParseLilyPond(lilypond.ParseGlobal):
    items: Incomplete

class ParseLilyPondInline(lilypond.ParseMusic):
    items: Incomplete
