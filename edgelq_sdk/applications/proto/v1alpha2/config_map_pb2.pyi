from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigMap(_message.Message):
    __slots__ = ("name", "display_name", "metadata", "data", "binary_data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BinaryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metadata: _meta_pb2.Meta
    data: _containers.ScalarMap[str, str]
    binary_data: _containers.ScalarMap[str, bytes]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., data: _Optional[_Mapping[str, str]] = ..., binary_data: _Optional[_Mapping[str, bytes]] = ...) -> None: ...
