from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from goten_sdk.types import multi_region_policy_pb2 as _multi_region_policy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ("name", "title", "metadata", "multi_region_policy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    metadata: _meta_pb2.Meta
    multi_region_policy: _multi_region_policy_pb2.MultiRegionPolicy
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., multi_region_policy: _Optional[_Union[_multi_region_policy_pb2.MultiRegionPolicy, _Mapping]] = ...) -> None: ...
