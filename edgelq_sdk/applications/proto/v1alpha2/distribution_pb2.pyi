from edgelq_sdk.applications.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Distribution(_message.Message):
    __slots__ = ("name", "display_name", "metadata", "spec", "status")
    class Spec(_message.Message):
        __slots__ = ("selector", "template")
        class Template(_message.Message):
            __slots__ = ("metadata", "spec")
            METADATA_FIELD_NUMBER: _ClassVar[int]
            SPEC_FIELD_NUMBER: _ClassVar[int]
            metadata: _meta_pb2.Meta
            spec: _common_pb2.PodSpec
            def __init__(self, metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[_common_pb2.PodSpec, _Mapping]] = ...) -> None: ...
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        selector: LabelSelector
        template: Distribution.Spec.Template
        def __init__(self, selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., template: _Optional[_Union[Distribution.Spec.Template, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metadata: _meta_pb2.Meta
    spec: Distribution.Spec
    status: Distribution.Status
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[Distribution.Spec, _Mapping]] = ..., status: _Optional[_Union[Distribution.Status, _Mapping]] = ...) -> None: ...

class LabelSelector(_message.Message):
    __slots__ = ("match_labels", "match_expressions")
    class MatchLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    MATCH_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.ScalarMap[str, str]
    match_expressions: _containers.RepeatedCompositeFieldContainer[LabelSelectorRequirement]
    def __init__(self, match_labels: _Optional[_Mapping[str, str]] = ..., match_expressions: _Optional[_Iterable[_Union[LabelSelectorRequirement, _Mapping]]] = ...) -> None: ...

class LabelSelectorRequirement(_message.Message):
    __slots__ = ("key", "operator", "values")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
