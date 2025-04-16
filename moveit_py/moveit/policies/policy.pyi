import abc
from abc import ABC, abstractmethod
from rclpy.node import Node
from typing import Any

class Policy(ABC, Node, metaclass=abc.ABCMeta):
    logger: Any
    param_listener: Any
    params: Any
    activate_policy_service: Any
    _is_active: bool
    def __init__(self, params, node_name) -> None: ...
    @property
    def is_active(self) -> Any: ...
    def activate_policy(self, request: Any, response: Any) -> Any: ...
    def get_sensor_msg_type(self, msg_type: str) -> Any: ...
    def get_command_msg_type(self, msg_type: str) -> Any: ...
    def register_sensors(self): ...
    def register_command(self): ...
    @abstractmethod
    def forward(self): ...
