from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_pb2 as _metric_descriptor_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDescriptorChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("metric_descriptor", "view_index")
        METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        metric_descriptor: _metric_descriptor_pb2.MetricDescriptor
        view_index: int
        def __init__(self, metric_descriptor: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "metric_descriptor", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        metric_descriptor: _metric_descriptor_pb2.MetricDescriptor
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., metric_descriptor: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("metric_descriptor",)
        METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        metric_descriptor: _metric_descriptor_pb2.MetricDescriptor
        def __init__(self, metric_descriptor: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ...) -> None: ...
    class Removed(_message.Message):
        __slots__ = ("name", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        view_index: int
        def __init__(self, name: _Optional[str] = ..., view_index: _Optional[int] = ...) -> None: ...
    ADDED_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    added: MetricDescriptorChange.Added
    modified: MetricDescriptorChange.Modified
    current: MetricDescriptorChange.Current
    removed: MetricDescriptorChange.Removed
    def __init__(self, added: _Optional[_Union[MetricDescriptorChange.Added, _Mapping]] = ..., modified: _Optional[_Union[MetricDescriptorChange.Modified, _Mapping]] = ..., current: _Optional[_Union[MetricDescriptorChange.Current, _Mapping]] = ..., removed: _Optional[_Union[MetricDescriptorChange.Removed, _Mapping]] = ...) -> None: ...
