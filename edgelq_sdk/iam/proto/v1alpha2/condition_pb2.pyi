from edgelq_sdk.iam.proto.v1alpha2 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1alpha2 import project_pb2 as _project_pb2
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
    __slots__ = ("name", "display_name", "description", "expression", "parameter_declarations", "metadata")
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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    expression: str
    parameter_declarations: _containers.RepeatedCompositeFieldContainer[Condition.ParameterDeclaration]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., expression: _Optional[str] = ..., parameter_declarations: _Optional[_Iterable[_Union[Condition.ParameterDeclaration, _Mapping]]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...

class ConditionBinding(_message.Message):
    __slots__ = ("condition", "parameters", "params")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    condition: str
    parameters: _containers.ScalarMap[str, str]
    params: _struct_pb2.Struct
    def __init__(self, condition: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
