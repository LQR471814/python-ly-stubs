from . import setvar as setvar
from _typeshed import Incomplete
from collections.abc import Generator

def usage() -> None: ...
def usage_short() -> None: ...
def version() -> None: ...
def die(message) -> None: ...

class Options:
    mode: Incomplete
    in_place: bool
    encoding: str
    output_encoding: Incomplete
    output: Incomplete
    replace_pattern: bool
    backup_suffix: str
    with_filename: Incomplete
    default_language: str
    rel_startpitch: bool
    rel_absolute: Incomplete
    indent_width: int
    indent_tabs: bool
    tab_width: int
    full_html: bool
    inline_style: bool
    stylesheet: Incomplete
    number_lines: bool
    wrapper_tag: str
    wrapper_attribute: str
    document_id: str
    linenumbers_id: str
    def __init__(self) -> None: ...
    def set_variable(self, name, value) -> None: ...

class Output:
    def __init__(self) -> None: ...
    def get_filename(self, opts, filename): ...
    def file(self, opts, filename, encoding) -> Generator[Incomplete, None, None]: ...

def parse_command_line(): ...
def parse_command(arg): ...
def load(filename, encoding, mode): ...
def main(): ...
