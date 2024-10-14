from edgelq_sdk.iam.proto.v1alpha2 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1alpha2 import project_pb2 as _project_pb2
from edgelq_sdk.limits.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptedPlan(_message.Message):
    __slots__ = ("name", "plan", "service", "extensions", "regional_distributions", "assignee", "metadata")
    class Assignee(_message.Message):
        __slots__ = ("project_assignee", "organization_assignee", "system_assignee")
        PROJECT_ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
        project_assignee: str
        organization_assignee: str
        system_assignee: bool
        def __init__(self, project_assignee: _Optional[str] = ..., organization_assignee: _Optional[str] = ..., system_assignee: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_DISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    plan: str
    service: str
    extensions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
    regional_distributions: _containers.RepeatedCompositeFieldContainer[_common_pb2.RegionalDistribution]
    assignee: AcceptedPlan.Assignee
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., plan: _Optional[str] = ..., service: _Optional[str] = ..., extensions: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ..., regional_distributions: _Optional[_Iterable[_Union[_common_pb2.RegionalDistribution, _Mapping]]] = ..., assignee: _Optional[_Union[AcceptedPlan.Assignee, _Mapping]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
