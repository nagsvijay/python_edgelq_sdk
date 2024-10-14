from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoKey(_message.Message):
    __slots__ = ("name", "metadata", "key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    key: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...
