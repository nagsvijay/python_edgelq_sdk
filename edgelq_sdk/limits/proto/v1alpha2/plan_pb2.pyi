from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from edgelq_sdk.limits.proto.v1alpha2 import common_pb2 as _common_pb2_1
from edgelq_sdk.meta.proto.v1alpha2 import service_pb2 as _service_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ("name", "display_name", "service", "resource_limits", "plan_level", "business_tier", "metadata")
    class PlanLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[Plan.PlanLevel]
        SYSTEM: _ClassVar[Plan.PlanLevel]
        ORGANIZATION: _ClassVar[Plan.PlanLevel]
        PROJECT: _ClassVar[Plan.PlanLevel]
    UNDEFINED: Plan.PlanLevel
    SYSTEM: Plan.PlanLevel
    ORGANIZATION: Plan.PlanLevel
    PROJECT: Plan.PlanLevel
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    PLAN_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TIER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    service: str
    resource_limits: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.Allowance]
    plan_level: Plan.PlanLevel
    business_tier: _common_pb2.BusinessTier
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., service: _Optional[str] = ..., resource_limits: _Optional[_Iterable[_Union[_common_pb2_1.Allowance, _Mapping]]] = ..., plan_level: _Optional[_Union[Plan.PlanLevel, str]] = ..., business_tier: _Optional[_Union[_common_pb2.BusinessTier, str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
