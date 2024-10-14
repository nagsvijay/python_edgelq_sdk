from edgelq_sdk.limits.proto.v1 import limit_pb2 as _limit_pb2
from edgelq_sdk.limits.proto.v1 import limit_change_pb2 as _limit_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateLimitSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
