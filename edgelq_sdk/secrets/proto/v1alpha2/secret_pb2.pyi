from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Secret(_message.Message):
    __slots__ = ("name", "enc_data", "data", "metadata")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENC_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    enc_data: bytes
    data: _containers.ScalarMap[str, str]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., enc_data: _Optional[bytes] = ..., data: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
