from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_pb2 as _monitored_resource_descriptor_pb2
from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_change_pb2 as _monitored_resource_descriptor_change_pb2
from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_custom_pb2 as _monitored_resource_descriptor_custom_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from goten_sdk.types import watch_type_pb2 as _watch_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchGetMonitoredResourceDescriptorsRequest(_message.Message):
    __slots__ = ("names", "field_mask", "view")
    NAMES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, names: _Optional[_Iterable[str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class BatchGetMonitoredResourceDescriptorsResponse(_message.Message):
    __slots__ = ("monitored_resource_descriptors", "missing")
    MONITORED_RESOURCE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_descriptors: _containers.RepeatedCompositeFieldContainer[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor]
    missing: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, monitored_resource_descriptors: _Optional[_Iterable[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]]] = ..., missing: _Optional[_Iterable[str]] = ...) -> None: ...

class WatchMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ("name", "field_mask", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class WatchMonitoredResourceDescriptorResponse(_message.Message):
    __slots__ = ("change",)
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    change: _monitored_resource_descriptor_change_pb2.MonitoredResourceDescriptorChange
    def __init__(self, change: _Optional[_Union[_monitored_resource_descriptor_change_pb2.MonitoredResourceDescriptorChange, _Mapping]] = ...) -> None: ...

class WatchMonitoredResourceDescriptorsRequest(_message.Message):
    __slots__ = ("type", "page_size", "page_token", "order_by", "resume_token", "starting_time", "filter", "field_mask", "view", "max_chunk_size")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STARTING_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    type: _watch_type_pb2.WatchType
    page_size: int
    page_token: str
    order_by: str
    resume_token: str
    starting_time: _timestamp_pb2.Timestamp
    filter: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    max_chunk_size: int
    def __init__(self, type: _Optional[_Union[_watch_type_pb2.WatchType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., resume_token: _Optional[str] = ..., starting_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., max_chunk_size: _Optional[int] = ...) -> None: ...

class WatchMonitoredResourceDescriptorsResponse(_message.Message):
    __slots__ = ("monitored_resource_descriptor_changes", "is_current", "page_token_change", "resume_token", "snapshot_size", "is_soft_reset", "is_hard_reset")
    class PageTokenChange(_message.Message):
        __slots__ = ("prev_page_token", "next_page_token")
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        prev_page_token: str
        next_page_token: str
        def __init__(self, prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    MONITORED_RESOURCE_DESCRIPTOR_CHANGES_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_SOFT_RESET_FIELD_NUMBER: _ClassVar[int]
    IS_HARD_RESET_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_descriptor_changes: _containers.RepeatedCompositeFieldContainer[_monitored_resource_descriptor_change_pb2.MonitoredResourceDescriptorChange]
    is_current: bool
    page_token_change: WatchMonitoredResourceDescriptorsResponse.PageTokenChange
    resume_token: str
    snapshot_size: int
    is_soft_reset: bool
    is_hard_reset: bool
    def __init__(self, monitored_resource_descriptor_changes: _Optional[_Iterable[_Union[_monitored_resource_descriptor_change_pb2.MonitoredResourceDescriptorChange, _Mapping]]] = ..., is_current: bool = ..., page_token_change: _Optional[_Union[WatchMonitoredResourceDescriptorsResponse.PageTokenChange, _Mapping]] = ..., resume_token: _Optional[str] = ..., snapshot_size: _Optional[int] = ..., is_soft_reset: bool = ..., is_hard_reset: bool = ...) -> None: ...

class CreateMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ("monitored_resource_descriptor",)
    MONITORED_RESOURCE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_descriptor: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
    def __init__(self, monitored_resource_descriptor: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ...) -> None: ...

class UpdateMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ("monitored_resource_descriptor", "update_mask", "cas", "allow_missing")
    class CAS(_message.Message):
        __slots__ = ("conditional_state", "field_mask")
        CONDITIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        conditional_state: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, conditional_state: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    MONITORED_RESOURCE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CAS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_descriptor: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
    update_mask: _field_mask_pb2.FieldMask
    cas: UpdateMonitoredResourceDescriptorRequest.CAS
    allow_missing: bool
    def __init__(self, monitored_resource_descriptor: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cas: _Optional[_Union[UpdateMonitoredResourceDescriptorRequest.CAS, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
