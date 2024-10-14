from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from edgelq_sdk.limits.proto.v1 import limit_pool_pb2 as _limit_pool_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Limit(_message.Message):
    __slots__ = ("name", "metadata", "service", "resource", "region", "configured_limit", "active_limit", "usage", "sources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    service: str
    resource: str
    region: str
    configured_limit: int
    active_limit: int
    usage: int
    sources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., service: _Optional[str] = ..., resource: _Optional[str] = ..., region: _Optional[str] = ..., configured_limit: _Optional[int] = ..., active_limit: _Optional[int] = ..., usage: _Optional[int] = ..., sources: _Optional[_Iterable[str]] = ...) -> None: ...
