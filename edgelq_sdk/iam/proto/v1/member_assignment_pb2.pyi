from edgelq_sdk.iam.proto.v1 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemberAssignment(_message.Message):
    __slots__ = ("name", "metadata", "scope", "scope_title", "parent_organization", "scope_metadata", "multi_region_control_region", "multi_region_enabled_regions", "scope_services", "business_tier", "member", "member_region", "ctrl_status")
    class WorkStatus(_message.Message):
        __slots__ = ("pending", "pending_deletion")
        PENDING_FIELD_NUMBER: _ClassVar[int]
        PENDING_DELETION_FIELD_NUMBER: _ClassVar[int]
        pending: bool
        pending_deletion: bool
        def __init__(self, pending: bool = ..., pending_deletion: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TITLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_METADATA_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_CONTROL_REGION_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_ENABLED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SERVICES_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TIER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_REGION_FIELD_NUMBER: _ClassVar[int]
    CTRL_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    scope: str
    scope_title: str
    parent_organization: str
    scope_metadata: _meta_pb2.Meta
    multi_region_control_region: str
    multi_region_enabled_regions: _containers.RepeatedScalarFieldContainer[str]
    scope_services: _containers.RepeatedScalarFieldContainer[str]
    business_tier: _common_pb2.BusinessTier
    member: str
    member_region: str
    ctrl_status: MemberAssignment.WorkStatus
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., scope: _Optional[str] = ..., scope_title: _Optional[str] = ..., parent_organization: _Optional[str] = ..., scope_metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., multi_region_control_region: _Optional[str] = ..., multi_region_enabled_regions: _Optional[_Iterable[str]] = ..., scope_services: _Optional[_Iterable[str]] = ..., business_tier: _Optional[_Union[_common_pb2.BusinessTier, str]] = ..., member: _Optional[str] = ..., member_region: _Optional[str] = ..., ctrl_status: _Optional[_Union[MemberAssignment.WorkStatus, _Mapping]] = ...) -> None: ...
