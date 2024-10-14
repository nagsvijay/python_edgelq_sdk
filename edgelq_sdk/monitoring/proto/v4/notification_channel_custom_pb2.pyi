from edgelq_sdk.monitoring.proto.v4 import notification_channel_pb2 as _notification_channel_pb2
from edgelq_sdk.monitoring.proto.v4 import notification_channel_change_pb2 as _notification_channel_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestNotificationChannelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
