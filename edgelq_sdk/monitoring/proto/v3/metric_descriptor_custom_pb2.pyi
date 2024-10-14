from edgelq_sdk.monitoring.proto.v3 import metric_descriptor_pb2 as _metric_descriptor_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMetricDescriptorsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by", "field_mask", "view", "include_paging_info")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAGING_INFO_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    include_paging_info: bool
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., include_paging_info: bool = ...) -> None: ...

class ListMetricDescriptorsResponse(_message.Message):
    __slots__ = ("metric_descriptors", "next_page_token", "prev_page_token", "current_offset", "total_results_count")
    METRIC_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    metric_descriptors: _containers.RepeatedCompositeFieldContainer[_metric_descriptor_pb2.MetricDescriptor]
    next_page_token: str
    prev_page_token: str
    current_offset: int
    total_results_count: int
    def __init__(self, metric_descriptors: _Optional[_Iterable[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ..., current_offset: _Optional[int] = ..., total_results_count: _Optional[int] = ...) -> None: ...

class GetMetricDescriptorRequest(_message.Message):
    __slots__ = ("name", "field_mask", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class CreateMetricDescriptorRequest(_message.Message):
    __slots__ = ("parent", "metric_descriptor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metric_descriptor: _metric_descriptor_pb2.MetricDescriptor
    def __init__(self, parent: _Optional[str] = ..., metric_descriptor: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ...) -> None: ...

class UpdateMetricDescriptorRequest(_message.Message):
    __slots__ = ("metric_descriptor", "update_mask", "cas", "allow_missing")
    class CAS(_message.Message):
        __slots__ = ("conditional_state", "field_mask")
        CONDITIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        conditional_state: _metric_descriptor_pb2.MetricDescriptor
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, conditional_state: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CAS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    metric_descriptor: _metric_descriptor_pb2.MetricDescriptor
    update_mask: _field_mask_pb2.FieldMask
    cas: UpdateMetricDescriptorRequest.CAS
    allow_missing: bool
    def __init__(self, metric_descriptor: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cas: _Optional[_Union[UpdateMetricDescriptorRequest.CAS, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteMetricDescriptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
