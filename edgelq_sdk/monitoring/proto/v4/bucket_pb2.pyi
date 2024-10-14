from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bucket(_message.Message):
    __slots__ = ("name", "metadata", "metrics", "resources", "required_alt_kvs")
    class ResolvedValues(_message.Message):
        __slots__ = ("key", "values")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        key: int
        values: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, key: _Optional[int] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...
    class ResolvedKeysWithValues(_message.Message):
        __slots__ = ("resolved_kvs",)
        RESOLVED_KVS_FIELD_NUMBER: _ClassVar[int]
        resolved_kvs: _containers.RepeatedCompositeFieldContainer[Bucket.ResolvedValues]
        def __init__(self, resolved_kvs: _Optional[_Iterable[_Union[Bucket.ResolvedValues, _Mapping]]] = ...) -> None: ...
    class RequiredTypedLabels(_message.Message):
        __slots__ = ("types", "labels")
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Bucket.RequiredTypedLabels.Strings
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Bucket.RequiredTypedLabels.Strings, _Mapping]] = ...) -> None: ...
        class Strings(_message.Message):
            __slots__ = ("strings",)
            STRINGS_FIELD_NUMBER: _ClassVar[int]
            strings: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, strings: _Optional[_Iterable[str]] = ...) -> None: ...
        TYPES_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        types: _containers.RepeatedScalarFieldContainer[str]
        labels: _containers.MessageMap[str, Bucket.RequiredTypedLabels.Strings]
        def __init__(self, types: _Optional[_Iterable[str]] = ..., labels: _Optional[_Mapping[str, Bucket.RequiredTypedLabels.Strings]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ALT_KVS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    metrics: _containers.RepeatedCompositeFieldContainer[Bucket.RequiredTypedLabels]
    resources: _containers.RepeatedCompositeFieldContainer[Bucket.RequiredTypedLabels]
    required_alt_kvs: _containers.RepeatedCompositeFieldContainer[Bucket.ResolvedKeysWithValues]
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[Bucket.RequiredTypedLabels, _Mapping]]] = ..., resources: _Optional[_Iterable[_Union[Bucket.RequiredTypedLabels, _Mapping]]] = ..., required_alt_kvs: _Optional[_Iterable[_Union[Bucket.ResolvedKeysWithValues, _Mapping]]] = ...) -> None: ...
