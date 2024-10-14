from edgelq_sdk.iam.proto.v1alpha2 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1alpha2 import project_pb2 as _project_pb2
from edgelq_sdk.limits.proto.v1alpha2 import common_pb2 as _common_pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_pb2 as _plan_pb2
from edgelq_sdk.meta.proto.v1alpha2 import service_pb2 as _service_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanAssignment(_message.Message):
    __slots__ = ("name", "plan", "service", "extensions", "regional_distributions", "source", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_DISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    plan: str
    service: str
    extensions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
    regional_distributions: _containers.RepeatedCompositeFieldContainer[_common_pb2.RegionalDistribution]
    source: str
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., plan: _Optional[str] = ..., service: _Optional[str] = ..., extensions: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ..., regional_distributions: _Optional[_Iterable[_Union[_common_pb2.RegionalDistribution, _Mapping]]] = ..., source: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
