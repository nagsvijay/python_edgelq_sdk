from edgelq_sdk.monitoring.proto.v3 import alert_pb2 as _alert_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("alert", "view_index")
        ALERT_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        alert: _alert_pb2.Alert
        view_index: int
        def __init__(self, alert: _Optional[_Union[_alert_pb2.Alert, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "alert", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ALERT_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        alert: _alert_pb2.Alert
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., alert: _Optional[_Union[_alert_pb2.Alert, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("alert",)
        ALERT_FIELD_NUMBER: _ClassVar[int]
        alert: _alert_pb2.Alert
        def __init__(self, alert: _Optional[_Union[_alert_pb2.Alert, _Mapping]] = ...) -> None: ...
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
    added: AlertChange.Added
    modified: AlertChange.Modified
    current: AlertChange.Current
    removed: AlertChange.Removed
    def __init__(self, added: _Optional[_Union[AlertChange.Added, _Mapping]] = ..., modified: _Optional[_Union[AlertChange.Modified, _Mapping]] = ..., current: _Optional[_Union[AlertChange.Current, _Mapping]] = ..., removed: _Optional[_Union[AlertChange.Removed, _Mapping]] = ...) -> None: ...
