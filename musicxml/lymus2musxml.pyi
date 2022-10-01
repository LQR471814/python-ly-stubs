from . import create_musicxml as create_musicxml, ly2xml_mediator as ly2xml_mediator, xml_objs as xml_objs
from _typeshed import Incomplete
from collections.abc import Generator

excl_list: Incomplete
group_contexts: Incomplete
pno_contexts: Incomplete
staff_contexts: Incomplete
part_contexts: Incomplete

class End:
    node: Incomplete
    def __init__(self, node) -> None: ...

class ParseSource:
    musxml: Incomplete
    mediator: Incomplete
    relative: bool
    tuplet: Incomplete
    scale: str
    grace_seq: bool
    trem_rep: int
    piano_staff: int
    numericTime: bool
    voice_sep: bool
    sims_and_seqs: Incomplete
    override_dict: Incomplete
    ottava: bool
    with_contxt: Incomplete
    schm_assignm: Incomplete
    tempo: Incomplete
    tremolo: bool
    tupl_span: bool
    unset_tuplspan: bool
    alt_mode: Incomplete
    rel_pitch_isset: bool
    slurcount: int
    slurnr: int
    phrslurnr: int
    mark: bool
    pickup: bool
    def __init__(self) -> None: ...
    def parse_text(self, ly_text, filename: Incomplete | None = ...) -> None: ...
    def parse_document(self, ly_doc, relative_first_pitch_absolute: bool = ...) -> None: ...
    def parse_tree(self, mustree) -> None: ...
    def parse_nodes(self, nodes) -> None: ...
    def musicxml(self, prettyprint: bool = ...): ...
    def Assignment(self, a) -> None: ...
    def MusicList(self, musicList) -> None: ...
    def Chord(self, chord) -> None: ...
    def Q(self, q) -> None: ...
    in_context: bool
    def Context(self, context) -> None: ...
    def check_context(self, context, context_id: Incomplete | None = ..., token: str = ...) -> None: ...
    def VoiceSeparator(self, voice_sep) -> None: ...
    def Change(self, change) -> None: ...
    def PipeSymbol(self, barcheck) -> None: ...
    def Clef(self, clef) -> None: ...
    def KeySignature(self, key) -> None: ...
    def Relative(self, relative) -> None: ...
    def Partial(self, partial) -> None: ...
    def Note(self, note) -> None: ...
    def Unpitched(self, unpitched) -> None: ...
    def DrumNote(self, drumnote) -> None: ...
    def check_note(self, note) -> None: ...
    def check_tuplet(self) -> None: ...
    def Duration(self, duration) -> None: ...
    def Tempo(self, tempo) -> None: ...
    def Tie(self, tie) -> None: ...
    def Rest(self, rest) -> None: ...
    def Skip(self, skip) -> None: ...
    def Scaler(self, scaler) -> None: ...
    def Number(self, number) -> None: ...
    def Articulation(self, art) -> None: ...
    def Postfix(self, postfix) -> None: ...
    def Beam(self, beam) -> None: ...
    def Slur(self, slur) -> None: ...
    def PhrasingSlur(self, phrslur) -> None: ...
    def Dynamic(self, dynamic) -> None: ...
    def Grace(self, grace) -> None: ...
    def TimeSignature(self, timeSign) -> None: ...
    def Repeat(self, repeat) -> None: ...
    def Tremolo(self, tremolo) -> None: ...
    def With(self, cont_with) -> None: ...
    def Set(self, cont_set) -> None: ...
    def Command(self, command) -> None: ...
    def UserCommand(self, usercommand) -> None: ...
    def Markup(self, markup) -> None: ...
    def MarkupWord(self, markupWord) -> None: ...
    def MarkupList(self, markuplist) -> None: ...
    def String(self, string) -> None: ...
    def LyricsTo(self, lyrics_to) -> None: ...
    def LyricText(self, lyrics_text) -> None: ...
    def LyricItem(self, lyrics_item) -> None: ...
    def NoteMode(self, notemode) -> None: ...
    def ChordMode(self, chordmode) -> None: ...
    def DrumMode(self, drummode) -> None: ...
    def FigureMode(self, figmode) -> None: ...
    def LyricMode(self, lyricmode) -> None: ...
    override_key: str
    def Override(self, override) -> None: ...
    def PathItem(self, item) -> None: ...
    def Scheme(self, scheme) -> None: ...
    def SchemeItem(self, item) -> None: ...
    def SchemeQuote(self, quote) -> None: ...
    fraction: Incomplete
    def End(self, end) -> None: ...
    def get_previous_node(self, node): ...
    def simple_node_gen(self, node) -> Generator[Incomplete, None, None]: ...
    def iter_header(self, tree): ...
    def get_score(self, node): ...
    def iter_score(self, scorenode, doc) -> Generator[Incomplete, None, None]: ...
    def unfold_repeat(self, repeat_node, repeat_count, doc) -> Generator[Incomplete, None, None]: ...
    def find_score_sub(self, doc): ...
    def look_ahead(self, node, find_node): ...
    def look_behind(self, node, find_node): ...
    def gen_med_caller(self, func_name, *args) -> None: ...