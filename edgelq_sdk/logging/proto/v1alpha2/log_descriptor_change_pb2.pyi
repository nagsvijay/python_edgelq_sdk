from edgelq_sdk.logging.proto.v1alpha2 import log_descriptor_pb2 as _log_descriptor_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogDescriptorChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("log_descriptor", "view_index")
        LOG_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        log_descriptor: _log_descriptor_pb2.LogDescriptor
        view_index: int
        def __init__(self, log_descriptor: _Optional[_Union[_log_descriptor_pb2.LogDescriptor, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "log_descriptor", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOG_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        log_descriptor: _log_descriptor_pb2.LogDescriptor
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., log_descriptor: _Optional[_Union[_log_descriptor_pb2.LogDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("log_descriptor",)
        LOG_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        log_descriptor: _log_descriptor_pb2.LogDescriptor
        def __init__(self, log_descriptor: _Optional[_Union[_log_descriptor_pb2.LogDescriptor, _Mapping]] = ...) -> None: ...
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
    added: LogDescriptorChange.Added
    modified: LogDescriptorChange.Modified
    current: LogDescriptorChange.Current
    removed: LogDescriptorChange.Removed
    def __init__(self, added: _Optional[_Union[LogDescriptorChange.Added, _Mapping]] = ..., modified: _Optional[_Union[LogDescriptorChange.Modified, _Mapping]] = ..., current: _Optional[_Union[LogDescriptorChange.Current, _Mapping]] = ..., removed: _Optional[_Union[LogDescriptorChange.Removed, _Mapping]] = ...) -> None: ...
