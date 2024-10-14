from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from goten_sdk.types import multi_region_policy_pb2 as _multi_region_policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ("name", "title", "parent_organization", "root_organization", "ancestry_path", "metadata", "multi_region_policy", "allowed_services", "business_tier", "service_tiers", "service_errors")
    class ServiceErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.ServiceErrors
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.ServiceErrors, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ROOT_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ANCESTRY_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TIER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TIERS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    parent_organization: str
    root_organization: str
    ancestry_path: _containers.RepeatedScalarFieldContainer[str]
    metadata: _meta_pb2.Meta
    multi_region_policy: _multi_region_policy_pb2.MultiRegionPolicy
    allowed_services: _containers.RepeatedScalarFieldContainer[str]
    business_tier: _common_pb2.BusinessTier
    service_tiers: _containers.RepeatedCompositeFieldContainer[_common_pb2.ServiceBusinessTier]
    service_errors: _containers.MessageMap[str, _common_pb2.ServiceErrors]
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., parent_organization: _Optional[str] = ..., root_organization: _Optional[str] = ..., ancestry_path: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., multi_region_policy: _Optional[_Union[_multi_region_policy_pb2.MultiRegionPolicy, _Mapping]] = ..., allowed_services: _Optional[_Iterable[str]] = ..., business_tier: _Optional[_Union[_common_pb2.BusinessTier, str]] = ..., service_tiers: _Optional[_Iterable[_Union[_common_pb2.ServiceBusinessTier, _Mapping]]] = ..., service_errors: _Optional[_Mapping[str, _common_pb2.ServiceErrors]] = ...) -> None: ...
