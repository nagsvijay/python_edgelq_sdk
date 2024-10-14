from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_pb2 as _monitored_resource_descriptor_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ("name", "field_mask", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class ListMonitoredResourceDescriptorsRequest(_message.Message):
    __slots__ = ("filter", "page_size", "order_by", "page_token", "field_mask", "view", "include_paging_info")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAGING_INFO_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    order_by: str
    page_token: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    include_paging_info: bool
    def __init__(self, filter: _Optional[str] = ..., page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., include_paging_info: bool = ...) -> None: ...

class ListMonitoredResourceDescriptorsResponse(_message.Message):
    __slots__ = ("monitored_resource_descriptors", "next_page_token", "prev_page_token", "current_offset", "total_results_count")
    MONITORED_RESOURCE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_descriptors: _containers.RepeatedCompositeFieldContainer[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor]
    next_page_token: str
    prev_page_token: str
    current_offset: int
    total_results_count: int
    def __init__(self, monitored_resource_descriptors: _Optional[_Iterable[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ..., current_offset: _Optional[int] = ..., total_results_count: _Optional[int] = ...) -> None: ...
