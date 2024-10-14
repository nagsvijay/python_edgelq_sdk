from edgelq_sdk.iam.proto.v1alpha2 import condition_pb2 as _condition_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(_message.Message):
    __slots__ = ("name", "display_name", "included_permissions", "default_condition_binding", "included_condition_bindings", "required_conditions", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONDITION_BINDING_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_CONDITION_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    included_permissions: _containers.RepeatedScalarFieldContainer[str]
    default_condition_binding: _condition_pb2.ConditionBinding
    included_condition_bindings: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ConditionBinding]
    required_conditions: _containers.RepeatedScalarFieldContainer[str]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., included_permissions: _Optional[_Iterable[str]] = ..., default_condition_binding: _Optional[_Union[_condition_pb2.ConditionBinding, _Mapping]] = ..., included_condition_bindings: _Optional[_Iterable[_Union[_condition_pb2.ConditionBinding, _Mapping]]] = ..., required_conditions: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
