from edgelq_sdk.iam.proto.v1 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from edgelq_sdk.limits.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.limits.proto.v1 import plan_pb2 as _plan_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanAssignment(_message.Message):
    __slots__ = ("name", "metadata", "default_regional_plan", "service", "regional_plan_overrides", "extensions", "allowances", "applied_regions", "applied_plan_spec_generation", "source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REGIONAL_PLAN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_PLAN_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    APPLIED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_PLAN_SPEC_GENERATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    default_regional_plan: str
    service: str
    regional_plan_overrides: _containers.RepeatedCompositeFieldContainer[_common_pb2.RegionalPlanAssignment]
    extensions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
    allowances: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
    applied_regions: _containers.RepeatedScalarFieldContainer[str]
    applied_plan_spec_generation: int
    source: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., default_regional_plan: _Optional[str] = ..., service: _Optional[str] = ..., regional_plan_overrides: _Optional[_Iterable[_Union[_common_pb2.RegionalPlanAssignment, _Mapping]]] = ..., extensions: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ..., allowances: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ..., applied_regions: _Optional[_Iterable[str]] = ..., applied_plan_spec_generation: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...
