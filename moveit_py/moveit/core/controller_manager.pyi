from typing import Any

class ExecutionStatus:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def status(self) -> Any: ...
    def __bool__(self) -> Any: ...
