from edgelq_sdk.audit.proto.v1 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditedResourceDescriptor(_message.Message):
    __slots__ = ("name", "display_name", "description", "labels", "promoted_label_key_sets", "versions", "spec_fields", "state_fields", "meta_fields", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_LABEL_KEY_SETS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    META_FIELDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.LabelDescriptor]
    promoted_label_key_sets: _containers.RepeatedCompositeFieldContainer[_common_pb2.LabelKeySet]
    versions: _containers.RepeatedScalarFieldContainer[str]
    spec_fields: _containers.RepeatedScalarFieldContainer[str]
    state_fields: _containers.RepeatedScalarFieldContainer[str]
    meta_fields: _containers.RepeatedScalarFieldContainer[str]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.LabelDescriptor, _Mapping]]] = ..., promoted_label_key_sets: _Optional[_Iterable[_Union[_common_pb2.LabelKeySet, _Mapping]]] = ..., versions: _Optional[_Iterable[str]] = ..., spec_fields: _Optional[_Iterable[str]] = ..., state_fields: _Optional[_Iterable[str]] = ..., meta_fields: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
