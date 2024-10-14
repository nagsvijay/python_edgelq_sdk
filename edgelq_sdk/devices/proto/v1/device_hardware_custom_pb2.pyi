from edgelq_sdk.devices.proto.v1 import device_hardware_pb2 as _device_hardware_pb2
from edgelq_sdk.devices.proto.v1 import device_hardware_change_pb2 as _device_hardware_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeregisterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeregisterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
