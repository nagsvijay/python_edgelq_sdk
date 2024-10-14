from edgelq_sdk.iam.proto.v1alpha2 import condition_pb2 as _condition_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleBinding(_message.Message):
    __slots__ = ("name", "role", "member", "condition_binding", "ancestry_path", "metadata")
    class Parent(_message.Message):
        __slots__ = ("parent", "member")
        PARENT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        parent: str
        member: str
        def __init__(self, parent: _Optional[str] = ..., member: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    CONDITION_BINDING_FIELD_NUMBER: _ClassVar[int]
    ANCESTRY_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: str
    member: str
    condition_binding: _condition_pb2.ConditionBinding
    ancestry_path: _containers.RepeatedCompositeFieldContainer[RoleBinding.Parent]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., role: _Optional[str] = ..., member: _Optional[str] = ..., condition_binding: _Optional[_Union[_condition_pb2.ConditionBinding, _Mapping]] = ..., ancestry_path: _Optional[_Iterable[_Union[RoleBinding.Parent, _Mapping]]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
