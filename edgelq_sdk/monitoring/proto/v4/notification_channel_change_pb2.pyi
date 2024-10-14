from edgelq_sdk.monitoring.proto.v4 import notification_channel_pb2 as _notification_channel_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannelChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("notification_channel", "view_index")
        NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        notification_channel: _notification_channel_pb2.NotificationChannel
        view_index: int
        def __init__(self, notification_channel: _Optional[_Union[_notification_channel_pb2.NotificationChannel, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "notification_channel", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        notification_channel: _notification_channel_pb2.NotificationChannel
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., notification_channel: _Optional[_Union[_notification_channel_pb2.NotificationChannel, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("notification_channel",)
        NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        notification_channel: _notification_channel_pb2.NotificationChannel
        def __init__(self, notification_channel: _Optional[_Union[_notification_channel_pb2.NotificationChannel, _Mapping]] = ...) -> None: ...
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
    added: NotificationChannelChange.Added
    modified: NotificationChannelChange.Modified
    current: NotificationChannelChange.Current
    removed: NotificationChannelChange.Removed
    def __init__(self, added: _Optional[_Union[NotificationChannelChange.Added, _Mapping]] = ..., modified: _Optional[_Union[NotificationChannelChange.Modified, _Mapping]] = ..., current: _Optional[_Union[NotificationChannelChange.Current, _Mapping]] = ..., removed: _Optional[_Union[NotificationChannelChange.Removed, _Mapping]] = ...) -> None: ...
