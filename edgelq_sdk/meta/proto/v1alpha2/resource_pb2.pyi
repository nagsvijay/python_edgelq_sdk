from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ("name", "plural_name", "fqn", "is_regional", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLURAL_NAME_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    IS_REGIONAL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    plural_name: str
    fqn: str
    is_regional: bool
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., plural_name: _Optional[str] = ..., fqn: _Optional[str] = ..., is_regional: bool = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
