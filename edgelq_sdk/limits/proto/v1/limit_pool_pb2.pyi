from edgelq_sdk.iam.proto.v1 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LimitPool(_message.Message):
    __slots__ = ("name", "metadata", "service", "resource", "region", "configured_size", "active_size", "reserved", "source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_SIZE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    service: str
    resource: str
    region: str
    configured_size: int
    active_size: int
    reserved: int
    source: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., service: _Optional[str] = ..., resource: _Optional[str] = ..., region: _Optional[str] = ..., configured_size: _Optional[int] = ..., active_size: _Optional[int] = ..., reserved: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...
