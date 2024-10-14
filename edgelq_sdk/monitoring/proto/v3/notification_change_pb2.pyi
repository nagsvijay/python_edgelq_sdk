from edgelq_sdk.monitoring.proto.v3 import notification_pb2 as _notification_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("notification", "view_index")
        NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        notification: _notification_pb2.Notification
        view_index: int
        def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "notification", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        notification: _notification_pb2.Notification
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("notification",)
        NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        notification: _notification_pb2.Notification
        def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...
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
    added: NotificationChange.Added
    modified: NotificationChange.Modified
    current: NotificationChange.Current
    removed: NotificationChange.Removed
    def __init__(self, added: _Optional[_Union[NotificationChange.Added, _Mapping]] = ..., modified: _Optional[_Union[NotificationChange.Modified, _Mapping]] = ..., current: _Optional[_Union[NotificationChange.Current, _Mapping]] = ..., removed: _Optional[_Union[NotificationChange.Removed, _Mapping]] = ...) -> None: ...
