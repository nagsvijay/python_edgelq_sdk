from edgelq_sdk.meta.proto.v1alpha2 import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Allowance(_message.Message):
    __slots__ = ("resource", "value")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    value: int
    def __init__(self, resource: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class RegionalDistribution(_message.Message):
    __slots__ = ("resource", "limits_by_region")
    class LimitsByRegionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    LIMITS_BY_REGION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    limits_by_region: _containers.ScalarMap[str, int]
    def __init__(self, resource: _Optional[str] = ..., limits_by_region: _Optional[_Mapping[str, int]] = ...) -> None: ...
