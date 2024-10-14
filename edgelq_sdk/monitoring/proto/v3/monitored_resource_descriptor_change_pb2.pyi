from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_pb2 as _monitored_resource_descriptor_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoredResourceDescriptorChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("monitored_resource_descriptor", "view_index")
        MONITORED_RESOURCE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        monitored_resource_descriptor: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
        view_index: int
        def __init__(self, monitored_resource_descriptor: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "monitored_resource_descriptor", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        MONITORED_RESOURCE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        monitored_resource_descriptor: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., monitored_resource_descriptor: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("monitored_resource_descriptor",)
        MONITORED_RESOURCE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        monitored_resource_descriptor: _monitored_resource_descriptor_pb2.MonitoredResourceDescriptor
        def __init__(self, monitored_resource_descriptor: _Optional[_Union[_monitored_resource_descriptor_pb2.MonitoredResourceDescriptor, _Mapping]] = ...) -> None: ...
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
    added: MonitoredResourceDescriptorChange.Added
    modified: MonitoredResourceDescriptorChange.Modified
    current: MonitoredResourceDescriptorChange.Current
    removed: MonitoredResourceDescriptorChange.Removed
    def __init__(self, added: _Optional[_Union[MonitoredResourceDescriptorChange.Added, _Mapping]] = ..., modified: _Optional[_Union[MonitoredResourceDescriptorChange.Modified, _Mapping]] = ..., current: _Optional[_Union[MonitoredResourceDescriptorChange.Current, _Mapping]] = ..., removed: _Optional[_Union[MonitoredResourceDescriptorChange.Removed, _Mapping]] = ...) -> None: ...
