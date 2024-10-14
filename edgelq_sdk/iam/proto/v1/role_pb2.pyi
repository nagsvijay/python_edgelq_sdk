from edgelq_sdk.iam.proto.v1 import condition_pb2 as _condition_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "description", "category", "scope_params", "grants", "owned_objects", "services", "rb_spec_generation")
    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[Role.Category]
        PUBLIC: _ClassVar[Role.Category]
        INTERNAL: _ClassVar[Role.Category]
        OWNER: _ClassVar[Role.Category]
        SERVICE: _ClassVar[Role.Category]
        AGENT: _ClassVar[Role.Category]
        USER: _ClassVar[Role.Category]
    UNDEFINED: Role.Category
    PUBLIC: Role.Category
    INTERNAL: Role.Category
    OWNER: Role.Category
    SERVICE: Role.Category
    AGENT: Role.Category
    USER: Role.Category
    class ScopeParamType(_message.Message):
        __slots__ = ("name", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[Role.ScopeParamType.Type]
            STRING: _ClassVar[Role.ScopeParamType.Type]
            ARRAY_OF_STRINGS: _ClassVar[Role.ScopeParamType.Type]
        UNDEFINED: Role.ScopeParamType.Type
        STRING: Role.ScopeParamType.Type
        ARRAY_OF_STRINGS: Role.ScopeParamType.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Role.ScopeParamType.Type
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Role.ScopeParamType.Type, str]] = ...) -> None: ...
    class Grant(_message.Message):
        __slots__ = ("sub_scope", "permissions", "resource_field_conditions", "request_field_conditions", "executable_conditions")
        class FieldCondition(_message.Message):
            __slots__ = ("path", "value")
            PATH_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            path: str
            value: str
            def __init__(self, path: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        SUB_SCOPE_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        REQUEST_FIELD_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        EXECUTABLE_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        sub_scope: str
        permissions: _containers.RepeatedScalarFieldContainer[str]
        resource_field_conditions: _containers.RepeatedCompositeFieldContainer[Role.Grant.FieldCondition]
        request_field_conditions: _containers.RepeatedCompositeFieldContainer[Role.Grant.FieldCondition]
        executable_conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ExecutableCondition]
        def __init__(self, sub_scope: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ..., resource_field_conditions: _Optional[_Iterable[_Union[Role.Grant.FieldCondition, _Mapping]]] = ..., request_field_conditions: _Optional[_Iterable[_Union[Role.Grant.FieldCondition, _Mapping]]] = ..., executable_conditions: _Optional[_Iterable[_Union[_condition_pb2.ExecutableCondition, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SCOPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    OWNED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    RB_SPEC_GENERATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    description: str
    category: Role.Category
    scope_params: _containers.RepeatedCompositeFieldContainer[Role.ScopeParamType]
    grants: _containers.RepeatedCompositeFieldContainer[Role.Grant]
    owned_objects: _containers.RepeatedScalarFieldContainer[str]
    services: _containers.RepeatedScalarFieldContainer[str]
    rb_spec_generation: int
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., category: _Optional[_Union[Role.Category, str]] = ..., scope_params: _Optional[_Iterable[_Union[Role.ScopeParamType, _Mapping]]] = ..., grants: _Optional[_Iterable[_Union[Role.Grant, _Mapping]]] = ..., owned_objects: _Optional[_Iterable[str]] = ..., services: _Optional[_Iterable[str]] = ..., rb_spec_generation: _Optional[int] = ...) -> None: ...

class ScopeParam(_message.Message):
    __slots__ = ("name", "string", "strings", "value_from")
    class StringValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class ArrayOfStringsValue(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class FromValue(_message.Message):
        __slots__ = ("source", "path")
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[ScopeParam.FromValue.Source]
            PRINCIPAL_METADATA: _ClassVar[ScopeParam.FromValue.Source]
        UNDEFINED: ScopeParam.FromValue.Source
        PRINCIPAL_METADATA: ScopeParam.FromValue.Source
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        source: ScopeParam.FromValue.Source
        path: str
        def __init__(self, source: _Optional[_Union[ScopeParam.FromValue.Source, str]] = ..., path: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FROM_FIELD_NUMBER: _ClassVar[int]
    name: str
    string: ScopeParam.StringValue
    strings: ScopeParam.ArrayOfStringsValue
    value_from: ScopeParam.FromValue
    def __init__(self, name: _Optional[str] = ..., string: _Optional[_Union[ScopeParam.StringValue, _Mapping]] = ..., strings: _Optional[_Union[ScopeParam.ArrayOfStringsValue, _Mapping]] = ..., value_from: _Optional[_Union[ScopeParam.FromValue, _Mapping]] = ...) -> None: ...
