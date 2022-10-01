from _typeshed import Incomplete

class Transposer:
    scale: Incomplete
    octave: Incomplete
    steps: Incomplete
    alter: Incomplete
    def __init__(self, fromPitch, toPitch, scale: Incomplete | None = ...) -> None: ...
    def transpose(self, pitch) -> None: ...

class Simplifier(Transposer):
    scale: Incomplete
    def __init__(self, scale: Incomplete | None = ...) -> None: ...
    def transpose(self, pitch) -> None: ...

class ModeShifter(Transposer):
    octave: int
    modpitches: Incomplete
    steps: Incomplete
    alter: Incomplete
    def __init__(self, key, scale) -> None: ...
    def closestPitch(self, pitch): ...
    def transpose(self, pitch) -> None: ...

class ModalTransposer:
    numSteps: Incomplete
    notes: Incomplete
    alter: Incomplete
    def __init__(self, numSteps: int = ..., scaleIndex: int = ...) -> None: ...
    @staticmethod
    def getKeyIndex(text): ...
    def transpose(self, pitch) -> None: ...

def transpose(cursor, transposer, language: str = ..., relative_first_pitch_absolute: bool = ...): ...