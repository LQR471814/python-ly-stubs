from . import FallthroughParser as FallthroughParser, Parser as Parser, _token
from _typeshed import Incomplete

re_articulation: str
re_dynamic: str
re_duration: str
re_dot: str
re_scaling: str
re_identifier: str
re_identifier_end: str

class Identifier(_token.Token):
    rx: Incomplete

class IdentifierRef(_token.Token):
    rx: Incomplete

class Variable(Identifier): ...
class UserVariable(Identifier): ...
class Value(_token.Item, _token.Numeric): ...

class DecimalValue(Value):
    rx: str

class IntegerValue(DecimalValue):
    rx: str

class Fraction(Value):
    rx: str

class Delimiter(_token.Token): ...

class DotPath(Delimiter):
    rx: str

class Error(_token.Error): ...
class Comment(_token.Comment): ...

class BlockCommentStart(Comment, _token.BlockCommentStart):
    rx: str
    def update_state(self, state) -> None: ...

class BlockCommentEnd(Comment, _token.BlockCommentEnd, _token.Leaver):
    rx: str

class BlockComment(Comment, _token.BlockComment): ...

class LineComment(Comment, _token.LineComment):
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

class MusicItem(_token.Token): ...

class Skip(MusicItem):
    rx: Incomplete

class Spacer(MusicItem):
    rx: str

class Rest(MusicItem):
    rx: str

class Note(MusicItem):
    rx: str

class Q(MusicItem):
    rx: str

class DrumNote(MusicItem):
    rx: str

class Octave(_token.Token):
    rx: str

class OctaveCheck(_token.Token):
    rx: str

class Accidental(_token.Token): ...

class AccidentalReminder(Accidental):
    rx: str

class AccidentalCautionary(Accidental):
    rx: str

class Duration(_token.Token): ...

class Length(Duration):
    rx: Incomplete
    def update_state(self, state) -> None: ...

class Dot(Duration):
    rx: Incomplete

class Scaling(Duration):
    rx: Incomplete

class OpenBracket(Delimiter, _token.MatchStart, _token.Indent):
    rx: str
    matchname: str

class CloseBracket(Delimiter, _token.MatchEnd, _token.Dedent):
    rx: str
    matchname: str
    def update_state(self, state) -> None: ...

class OpenSimultaneous(Delimiter, _token.MatchStart, _token.Indent):
    rx: str
    matchname: str

class CloseSimultaneous(Delimiter, _token.MatchEnd, _token.Dedent):
    rx: str
    matchname: str
    def update_state(self, state) -> None: ...

class SequentialStart(OpenBracket):
    def update_state(self, state) -> None: ...

class SequentialEnd(CloseBracket): ...

class SimultaneousStart(OpenSimultaneous):
    def update_state(self, state) -> None: ...

class SimultaneousEnd(CloseSimultaneous): ...

class PipeSymbol(Delimiter):
    rx: str

class Articulation(_token.Token): ...

class ArticulationCommand(Articulation, IdentifierRef):
    @classmethod
    def test_match(cls, match): ...

class Direction(_token.Token):
    rx: str
    def update_state(self, state) -> None: ...

class ScriptAbbreviation(Articulation, _token.Leaver):
    rx: str

class Fingering(Articulation, _token.Leaver):
    rx: str

class StringNumber(Articulation):
    rx: str

class Slur(_token.Token): ...

class SlurStart(Slur, _token.MatchStart):
    rx: str
    matchname: str

class SlurEnd(Slur, _token.MatchEnd):
    rx: str
    matchname: str

class PhrasingSlurStart(SlurStart):
    rx: str
    matchname: str

class PhrasingSlurEnd(SlurEnd):
    rx: str
    matchname: str

class Tie(Slur):
    rx: str

class Beam(_token.Token): ...

class BeamStart(Beam, _token.MatchStart):
    rx: str
    matchname: str

class BeamEnd(Beam, _token.MatchEnd):
    rx: str
    matchname: str

class Ligature(_token.Token): ...

class LigatureStart(Ligature, _token.MatchStart):
    rx: str
    matchname: str

class LigatureEnd(Ligature, _token.MatchEnd):
    rx: str
    matchname: str

class Tremolo(_token.Token): ...

class TremoloColon(Tremolo):
    rx: str
    def update_state(self, state) -> None: ...

class TremoloDuration(Tremolo, _token.Leaver):
    rx: str

class ChordItem(_token.Token): ...

class ChordModifier(ChordItem):
    rx: str

class ChordSeparator(ChordItem):
    rx: str

class ChordStepNumber(ChordItem):
    rx: str

class DotChord(ChordItem):
    rx: str

class VoiceSeparator(Delimiter):
    rx: str

class Dynamic(_token.Token):
    rx: Incomplete

class Command(_token.Item, IdentifierRef):
    @classmethod
    def test_match(cls, match): ...

class Keyword(_token.Item, IdentifierRef):
    @classmethod
    def test_match(cls, match): ...

class Specifier(_token.Token): ...

class Score(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Book(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class BookPart(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Paper(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Header(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Layout(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Midi(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class With(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class LayoutContext(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Markup(_token.Item): ...

class MarkupStart(Markup, Command):
    rx: Incomplete
    def update_state(self, state) -> None: ...

class MarkupLines(Markup):
    rx: Incomplete
    def update_state(self, state) -> None: ...

class MarkupList(Markup):
    rx: Incomplete
    def update_state(self, state) -> None: ...

class MarkupCommand(Markup, IdentifierRef):
    @classmethod
    def test_match(cls, match): ...
    def update_state(self, state) -> None: ...

class MarkupScore(Markup):
    rx: str
    def update_state(self, state) -> None: ...

class MarkupUserCommand(Markup, IdentifierRef):
    def update_state(self, state) -> None: ...

class MarkupWord(_token.Item):
    rx: str

class OpenBracketMarkup(OpenBracket):
    def update_state(self, state) -> None: ...

class CloseBracketMarkup(CloseBracket):
    def update_state(self, state) -> None: ...

class Repeat(Command):
    rx: str
    def update_state(self, state) -> None: ...

class RepeatSpecifier(Specifier):
    def rx(): ...

class RepeatCount(IntegerValue, _token.Leaver): ...

class Tempo(Command):
    rx: str
    def update_state(self, state) -> None: ...

class TempoSeparator(Delimiter):
    rx: str

class Partial(Command):
    rx: str

class Override(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Set(Override):
    rx: str
    def update_state(self, state) -> None: ...

class Revert(Override):
    rx: str
    def update_state(self, state) -> None: ...

class Unset(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Tweak(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Translator(Command):
    def update_state(self, state) -> None: ...

class New(Translator):
    rx: str

class Context(Translator):
    rx: str

class Change(Translator):
    rx: str

class AccidentalStyle(Command):
    rx: str
    def update_state(self, state) -> None: ...

class AccidentalStyleSpecifier(Specifier):
    def rx(): ...

class AlterBroken(Command):
    rx: str
    def update_state(self, state) -> None: ...

class Clef(Command):
    rx: str
    def update_state(self, state) -> None: ...

class ClefSpecifier(Specifier):
    def rx(): ...
    def update_state(self, state) -> None: ...

class PitchCommand(Command):
    rx: str
    def update_state(self, state) -> None: ...

class KeySignatureMode(Command):
    def rx(): ...

class Hide(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Omit(Keyword):
    rx: str
    def update_state(self, state) -> None: ...

class Unit(Command):
    rx: str

class InputMode(Command): ...

class LyricMode(InputMode):
    rx: str
    def update_state(self, state) -> None: ...

class Lyric(_token.Item): ...

class LyricText(Lyric):
    rx: str

class LyricHyphen(Lyric):
    rx: str

class LyricExtender(Lyric):
    rx: str

class LyricSkip(Lyric):
    rx: str

class Figure(_token.Token): ...

class FigureStart(Figure):
    rx: str
    def update_state(self, state) -> None: ...

class FigureEnd(Figure, _token.Leaver):
    rx: str

class FigureBracket(Figure):
    rx: str

class FigureStep(Figure):
    rx: str

class FigureAccidental(Figure):
    rx: str

class FigureModifier(Figure):
    rx: str

class NoteMode(InputMode):
    rx: str
    def update_state(self, state) -> None: ...

class ChordMode(InputMode):
    rx: str
    def update_state(self, state) -> None: ...

class DrumMode(InputMode):
    rx: str
    def update_state(self, state) -> None: ...

class FigureMode(InputMode):
    rx: str
    def update_state(self, state) -> None: ...

class UserCommand(IdentifierRef): ...

class SimultaneousOrSequentialCommand(Keyword):
    rx: str

class SchemeStart(_token.Item):
    rx: str
    def update_state(self, state) -> None: ...

class ContextName(_token.Token):
    def rx(): ...

class BackSlashedContextName(ContextName):
    def rx(): ...

class GrobName(_token.Token):
    def rx(): ...

class GrobProperty(Variable):
    rx: str

class ContextProperty(Variable):
    def rx(): ...

class PaperVariable(Variable):
    @classmethod
    def test_match(cls, match): ...

class HeaderVariable(Variable):
    @classmethod
    def test_match(cls, match): ...

class LayoutVariable(Variable):
    @classmethod
    def test_match(cls, match): ...

class Chord(_token.Token): ...

class ChordStart(Chord):
    rx: str
    def update_state(self, state) -> None: ...

class ChordEnd(Chord, _token.Leaver):
    rx: str

class DrumChordStart(ChordStart):
    def update_state(self, state) -> None: ...

class DrumChordEnd(ChordEnd): ...

class ErrorInChord(Error):
    rx: Incomplete

class Name(UserVariable): ...

class EqualSign(_token.Token):
    rx: str

class ParseLilyPond(Parser):
    mode: str

space_items: Incomplete
base_items: Incomplete
command_items: Incomplete
toplevel_base_items: Incomplete
music_items: Incomplete
music_chord_items: Incomplete

class ParseGlobal(ParseLilyPond):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseGlobalAssignment(FallthroughParser, ParseLilyPond):
    items: Incomplete

class ExpectOpenBracket(FallthroughParser, ParseLilyPond):
    default: Incomplete
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ExpectMusicList(FallthroughParser, ParseLilyPond):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseScore(ParseLilyPond):
    items: Incomplete

class ExpectScore(ExpectOpenBracket):
    replace: Incomplete

class ParseBook(ParseLilyPond):
    items: Incomplete

class ExpectBook(ExpectOpenBracket):
    replace: Incomplete

class ParseBookPart(ParseLilyPond):
    items: Incomplete

class ExpectBookPart(ExpectOpenBracket):
    replace: Incomplete

class ParsePaper(ParseLilyPond):
    items: Incomplete

class ExpectPaper(ExpectOpenBracket):
    replace: Incomplete

class ParseHeader(ParseLilyPond):
    items: Incomplete

class ExpectHeader(ExpectOpenBracket):
    replace: Incomplete

class ParseLayout(ParseLilyPond):
    items: Incomplete

class ExpectLayout(ExpectOpenBracket):
    replace: Incomplete

class ParseMidi(ParseLilyPond):
    items: Incomplete

class ExpectMidi(ExpectOpenBracket):
    replace: Incomplete

class ParseWith(ParseLilyPond):
    items: Incomplete

class ExpectWith(ExpectOpenBracket):
    replace: Incomplete

class ParseContext(ParseLilyPond):
    items: Incomplete

class ExpectContext(ExpectOpenBracket):
    replace: Incomplete

class ParseMusic(ParseLilyPond):
    items: Incomplete

class ParseChord(ParseMusic):
    items: Incomplete

class ParseString(Parser):
    default: Incomplete
    items: Incomplete

class ParseBlockComment(Parser):
    default: Incomplete
    items: Incomplete

class ParseMarkup(Parser):
    items: Incomplete

class ParseRepeat(FallthroughParser):
    items: Incomplete

class ParseTempo(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTempoAfterEqualSign(FallthroughParser):
    items: Incomplete

class ParseDuration(FallthroughParser):
    items: Incomplete
    def fallthrough(self, state) -> None: ...

class ParseDurationScaling(ParseDuration):
    items: Incomplete
    def fallthrough(self, state) -> None: ...

class ParseOverride(ParseLilyPond):
    argcount: int
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseRevert(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseGrobPropertyPath(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ExpectGrobProperty(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseSet(ParseLilyPond):
    argcount: int
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseUnset(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTweak(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTweakGrobProperty(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTranslator(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ExpectTranslatorId(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTranslatorId(FallthroughParser):
    argcount: int
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseClef(FallthroughParser):
    argcount: int
    items: Incomplete

class ParseHideOmit(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseAccidentalStyle(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseAlterBroken(FallthroughParser):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseScriptAbbreviationOrFingering(FallthroughParser):
    argcount: int
    items: Incomplete

class ParseInputMode(ParseLilyPond):
    @classmethod
    def update_state(cls, state, token) -> None: ...

class ParseLyricMode(ParseInputMode):
    items: Incomplete

class ExpectLyricMode(ExpectMusicList):
    replace: Incomplete
    items: Incomplete

class ParseChordMode(ParseInputMode, ParseMusic):
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ExpectChordMode(ExpectMusicList):
    replace: Incomplete

class ParseNoteMode(ParseMusic): ...

class ExpectNoteMode(ExpectMusicList):
    replace: Incomplete

class ParseDrumChord(ParseMusic):
    items: Incomplete

class ParseDrumMode(ParseInputMode, ParseMusic):
    items: Incomplete

class ExpectDrumMode(ExpectMusicList):
    replace: Incomplete

class ParseFigureMode(ParseInputMode, ParseMusic):
    items: Incomplete

class ParseFigure(Parser):
    items: Incomplete

class ExpectFigureMode(ExpectMusicList):
    replace: Incomplete

class ParsePitchCommand(FallthroughParser):
    argcount: int
    items: Incomplete
    def update_state(self, state, token) -> None: ...

class ParseTremolo(FallthroughParser):
    items: Incomplete

class ParseChordItems(FallthroughParser):
    items: Incomplete

class ParseDecimalValue(FallthroughParser):
    items: Incomplete
