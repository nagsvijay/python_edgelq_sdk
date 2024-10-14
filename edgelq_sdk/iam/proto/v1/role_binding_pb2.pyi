from edgelq_sdk.iam.proto.v1 import condition_pb2 as _condition_pb2
from edgelq_sdk.iam.proto.v1 import role_pb2 as _role_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleBinding(_message.Message):
    __slots__ = ("name", "metadata", "role", "owned_objects", "member", "scope_params", "executable_conditions", "member_type", "category", "ancestry_path", "parent_by_org", "spec_generation", "has_owned_objects", "disable_for_child_scopes")
    class Parent(_message.Message):
        __slots__ = ("parent", "member")
        PARENT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        parent: str
        member: str
        def __init__(self, parent: _Optional[str] = ..., member: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    OWNED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ANCESTRY_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_BY_ORG_FIELD_NUMBER: _ClassVar[int]
    SPEC_GENERATION_FIELD_NUMBER: _ClassVar[int]
    HAS_OWNED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FOR_CHILD_SCOPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    role: str
    owned_objects: _containers.RepeatedScalarFieldContainer[str]
    member: str
    scope_params: _containers.RepeatedCompositeFieldContainer[_role_pb2.ScopeParam]
    executable_conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ExecutableCondition]
    member_type: str
    category: _role_pb2.Role.Category
    ancestry_path: _containers.RepeatedCompositeFieldContainer[RoleBinding.Parent]
    parent_by_org: str
    spec_generation: int
    has_owned_objects: bool
    disable_for_child_scopes: bool
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., role: _Optional[str] = ..., owned_objects: _Optional[_Iterable[str]] = ..., member: _Optional[str] = ..., scope_params: _Optional[_Iterable[_Union[_role_pb2.ScopeParam, _Mapping]]] = ..., executable_conditions: _Optional[_Iterable[_Union[_condition_pb2.ExecutableCondition, _Mapping]]] = ..., member_type: _Optional[str] = ..., category: _Optional[_Union[_role_pb2.Role.Category, str]] = ..., ancestry_path: _Optional[_Iterable[_Union[RoleBinding.Parent, _Mapping]]] = ..., parent_by_org: _Optional[str] = ..., spec_generation: _Optional[int] = ..., has_owned_objects: bool = ..., disable_for_child_scopes: bool = ...) -> None: ...
