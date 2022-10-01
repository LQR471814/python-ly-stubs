from _typeshed import Incomplete

class _command:
    def __init__(self) -> None: ...
    def run(self, opts, cursor, output) -> None: ...
    @staticmethod
    def get_absolute(opts, cursor): ...

class set_variable(_command):
    def __init__(self, arg) -> None: ...
    def run(self, opts, cursor, output) -> None: ...

class _info_command(_command):
    def run(self, opts, cursor, output) -> None: ...
    def get_info(self, info) -> None: ...

class mode(_info_command):
    def get_info(self, info): ...

class version(_info_command):
    def get_info(self, info): ...

class language(_info_command):
    def get_info(self, info): ...

class _edit_command(_command): ...

class indent(_edit_command):
    def indenter(self, opts): ...
    def run(self, opts, cursor, output) -> None: ...

class reformat(indent):
    def run(self, opts, cursor, output) -> None: ...

class translate(_edit_command):
    language: Incomplete
    def __init__(self, language) -> None: ...
    def run(self, opts, cursor, output) -> None: ...

class transpose(_edit_command):
    def __init__(self, arg) -> None: ...
    def run(self, opts, cursor, output) -> None: ...

class rel2abs(_edit_command):
    def run(self, opts, cursor, output) -> None: ...

class abs2rel(_edit_command):
    def run(self, opts, cursor, output) -> None: ...

class simplify_accidentals(_edit_command):
    def run(self, opts, cursor, output) -> None: ...

class _export_command(_command):
    output: Incomplete
    def __init__(self, output: Incomplete | None = ...) -> None: ...

class musicxml(_export_command):
    def run(self, opts, cursor, output) -> None: ...

class write(_command):
    output: Incomplete
    def __init__(self, output: Incomplete | None = ...) -> None: ...
    def run(self, opts, cursor, output) -> None: ...

class highlight(_export_command):
    def run(self, opts, cursor, output) -> None: ...
hl = highlight