from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "description", "expression", "parameter_declarations")
    class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Condition.ParameterType]
        STRING: _ClassVar[Condition.ParameterType]
        INT64: _ClassVar[Condition.ParameterType]
        DOUBLE: _ClassVar[Condition.ParameterType]
        BOOL: _ClassVar[Condition.ParameterType]
        STRING_ARRAY: _ClassVar[Condition.ParameterType]
        INT64_ARRAY: _ClassVar[Condition.ParameterType]
        DOUBLE_ARRAY: _ClassVar[Condition.ParameterType]
        BOOL_ARRAY: _ClassVar[Condition.ParameterType]
        OBJECT: _ClassVar[Condition.ParameterType]
    TYPE_UNSPECIFIED: Condition.ParameterType
    STRING: Condition.ParameterType
    INT64: Condition.ParameterType
    DOUBLE: Condition.ParameterType
    BOOL: Condition.ParameterType
    STRING_ARRAY: Condition.ParameterType
    INT64_ARRAY: Condition.ParameterType
    DOUBLE_ARRAY: Condition.ParameterType
    BOOL_ARRAY: Condition.ParameterType
    OBJECT: Condition.ParameterType
    class ParameterDeclaration(_message.Message):
        __slots__ = ("key", "type")
        KEY_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        key: str
        type: Condition.ParameterType
        def __init__(self, key: _Optional[str] = ..., type: _Optional[_Union[Condition.ParameterType, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    description: str
    expression: str
    parameter_declarations: _containers.RepeatedCompositeFieldContainer[Condition.ParameterDeclaration]
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., expression: _Optional[str] = ..., parameter_declarations: _Optional[_Iterable[_Union[Condition.ParameterDeclaration, _Mapping]]] = ...) -> None: ...

class ExecutableCondition(_message.Message):
    __slots__ = ("condition", "params")
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    condition: str
    params: _struct_pb2.Struct
    def __init__(self, condition: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
