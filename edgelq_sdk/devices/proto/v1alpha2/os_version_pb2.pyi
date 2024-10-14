from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OsVersion(_message.Message):
    __slots__ = ("name", "metadata", "version", "device_type", "minimum_previous_version", "channel")
    class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_UNSPECIFIED: _ClassVar[OsVersion.Channel]
        NORMAL: _ClassVar[OsVersion.Channel]
        BETA: _ClassVar[OsVersion.Channel]
    CHANNEL_UNSPECIFIED: OsVersion.Channel
    NORMAL: OsVersion.Channel
    BETA: OsVersion.Channel
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PREVIOUS_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    version: str
    device_type: str
    minimum_previous_version: str
    channel: OsVersion.Channel
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., version: _Optional[str] = ..., device_type: _Optional[str] = ..., minimum_previous_version: _Optional[str] = ..., channel: _Optional[_Union[OsVersion.Channel, str]] = ...) -> None: ...
