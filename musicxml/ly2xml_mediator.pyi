from . import xml_objs as xml_objs
from _typeshed import Incomplete

class Mediator:
    score: Incomplete
    sections: Incomplete
    insert_into: Incomplete
    current_note: Incomplete
    current_lynote: Incomplete
    current_is_rest: bool
    current_time: Incomplete
    bar_dura: Incomplete
    action_onnext: Incomplete
    divisions: int
    dur_token: str
    dur_tokens: Incomplete
    dots: int
    tied: bool
    voice: int
    staff: int
    part: Incomplete
    group: Incomplete
    group_num: int
    current_chord: Incomplete
    q_chord: Incomplete
    prev_pitch: Incomplete
    prev_chord_pitch: Incomplete
    store_voicenr: int
    staff_id_dict: Incomplete
    store_unset_staff: bool
    staff_unset_notes: Incomplete
    lyric_sections: Incomplete
    lyric: Incomplete
    lyric_syll: bool
    lyric_nr: int
    ongoing_wedge: bool
    ongoing_dashes: bool
    octdiff: int
    prev_tremolo: int
    tupl_dur: int
    tupl_sum: int
    slur_stack: Incomplete
    multiple_rest: bool
    multiple_rest_bar: Incomplete
    current_mark: int
    bar_is_pickup: bool
    stem_dir: Incomplete
    def __init__(self) -> None: ...
    def new_header_assignment(self, name, value) -> None: ...
    bar: Incomplete
    def new_section(self, name, glob: bool = ...) -> None: ...
    def new_snippet(self, name) -> None: ...
    def new_lyric_section(self, name, voice_id) -> None: ...
    def check_name(self, name, nr: int = ...): ...
    def get_var_byname(self, name): ...
    def new_group(self) -> None: ...
    def close_group(self) -> None: ...
    def change_group_bracket(self, system_start) -> None: ...
    def new_part(self, pid: Incomplete | None = ..., to_part: Incomplete | None = ..., piano: bool = ...) -> None: ...
    def part_not_empty(self): ...
    def get_part_by_id(self, pid, partholder: Incomplete | None = ...): ...
    def set_voicenr(self, command: Incomplete | None = ..., add: bool = ..., nr: int = ..., piano: int = ...) -> None: ...
    def revert_voicenr(self) -> None: ...
    def set_staffnr(self, staffnr, staff_id: Incomplete | None = ...) -> None: ...
    def add_staff_id(self, staff_id) -> None: ...
    def add_snippet(self, snippet_name) -> None: ...
    def check_voices(self) -> None: ...
    def check_voices_by_nr(self) -> None: ...
    def check_lyrics(self, voice_id) -> None: ...
    def check_part(self) -> None: ...
    def check_simultan(self) -> None: ...
    def check_score(self) -> None: ...
    def get_first_var(self): ...
    def set_pickup(self) -> None: ...
    current_attr: Incomplete
    def new_bar(self, fill_prev: bool = ...) -> None: ...
    def add_to_bar(self, obj) -> None: ...
    def create_barline(self, bl) -> None: ...
    def new_repeat(self, rep) -> None: ...
    def new_key(self, key_name, mode) -> None: ...
    def bijective(self, n): ...
    def new_mark(self, num_mark: Incomplete | None = ...) -> None: ...
    def new_word(self, word) -> None: ...
    def new_time(self, num, den, numeric: bool = ...) -> None: ...
    clef: Incomplete
    def new_clef(self, clefname) -> None: ...
    def set_relative(self, note) -> None: ...
    def increase_bar_dura(self, duration) -> None: ...
    def new_note(self, note, rel: bool = ..., is_unpitched: bool = ...) -> None: ...
    def new_iso_dura(self, note, rel: bool = ..., is_unpitched: bool = ...) -> None: ...
    def create_unpitched(self, unpitched): ...
    def create_barnote_from_note(self, note): ...
    def copy_barnote_basics(self, bar_note): ...
    def new_duration_token(self, token, tokens) -> None: ...
    def check_current_note(self, rel: bool = ..., rest: bool = ..., is_unpitched: bool = ...) -> None: ...
    def stem_direction(self, direction) -> None: ...
    def set_octave(self, relative) -> None: ...
    def do_action_onnext(self, note) -> None: ...
    def check_duration(self, rest) -> None: ...
    def new_chord(self, note, duration: Incomplete | None = ..., rel: bool = ..., chord_base: bool = ...) -> None: ...
    def new_chordbase(self, note, duration, rel: bool = ...) -> None: ...
    def new_chordnote(self, note, rel): ...
    def copy_prev_chord(self, duration) -> None: ...
    def clear_chord(self) -> None: ...
    def chord_end(self) -> None: ...
    def new_rest(self, rest) -> None: ...
    def note2rest(self) -> None: ...
    def set_mult_rest(self) -> None: ...
    def set_mult_rest_bar(self, dur) -> None: ...
    def scale_rest(self, bs) -> None: ...
    def change_to_tuplet(self, tfraction, ttype, nr, length: Incomplete | None = ...) -> None: ...
    def change_tuplet_type(self, index, newtype) -> None: ...
    def set_tuplspan_dur(self, token: Incomplete | None = ..., tokens: Incomplete | None = ..., fraction: Incomplete | None = ...) -> None: ...
    def unset_tuplspan_dur(self) -> None: ...
    def calc_tupl_den(self, tfraction, length): ...
    def tie_to_next(self) -> None: ...
    def set_slur(self, nr, slur_type, phrasing: bool = ...) -> None: ...
    def new_articulation(self, art_token) -> None: ...
    def new_dynamics(self, dynamics) -> None: ...
    def new_grace(self, slash: int = ...) -> None: ...
    def new_chord_grace(self, slash: int = ...) -> None: ...
    def new_gliss(self, line: Incomplete | None = ...) -> None: ...
    def end_gliss(self, note, line) -> None: ...
    def set_tremolo(self, trem_type: str = ..., duration: int = ..., repeats: int = ...) -> None: ...
    def new_trill_spanner(self, end: Incomplete | None = ...) -> None: ...
    def new_ottava(self, octdiff) -> None: ...
    def set_ottava(self, note, plac, octdir, size) -> None: ...
    def new_tempo(self, unit, dur_tokens, tempo, string) -> None: ...
    def set_by_property(self, prprty, value, group: bool = ...) -> None: ...
    def set_partname(self, name) -> None: ...
    def set_partabbr(self, abbr) -> None: ...
    def set_groupname(self, name) -> None: ...
    def set_groupabbr(self, abbr) -> None: ...
    def set_partmidi(self, midi) -> None: ...
    def new_lyric_nr(self, num) -> None: ...
    def new_lyrics_text(self, txt) -> None: ...
    def new_lyrics_item(self, item) -> None: ...
    def duration_from_tokens(self, tokens): ...
    def check_divs(self) -> None: ...
    def add_break(self) -> None: ...

def getNoteName(index): ...
def get_xml_alter(alter): ...
def durval2type(durval): ...
def get_fifths(key, mode): ...
def clefname2clef(clefname): ...
def get_mult(num, den): ...
def get_voice(c): ...
def artic_token2xml_name(art_token): ...
def calc_trem_dur(repeats, base_scaling, duration): ...
def get_line_style(style): ...
def get_group_symbol(lily_sys_start): ...