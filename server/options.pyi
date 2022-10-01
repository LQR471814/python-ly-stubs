from _typeshed import Incomplete
from ly.cli import setvar as setvar

class ServerOptions:
    port: int
    timeout: int
    def __init__(self) -> None: ...

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
