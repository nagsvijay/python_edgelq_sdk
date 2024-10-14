from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_pb2 as _limit_pool_pb2
from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_change_pb2 as _limit_pool_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateLimitPoolSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
