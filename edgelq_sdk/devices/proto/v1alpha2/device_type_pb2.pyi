from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "hardware", "architecture", "description")
    class Hardware(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARDWARE_UNSPECIFIED: _ClassVar[DeviceType.Hardware]
        GENERIC: _ClassVar[DeviceType.Hardware]
        RASPBERRYPI: _ClassVar[DeviceType.Hardware]
    HARDWARE_UNSPECIFIED: DeviceType.Hardware
    GENERIC: DeviceType.Hardware
    RASPBERRYPI: DeviceType.Hardware
    class Architecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARCHITECTURE_UNSPECIFIED: _ClassVar[DeviceType.Architecture]
        AMD64: _ClassVar[DeviceType.Architecture]
        ARM64: _ClassVar[DeviceType.Architecture]
    ARCHITECTURE_UNSPECIFIED: DeviceType.Architecture
    AMD64: DeviceType.Architecture
    ARM64: DeviceType.Architecture
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    hardware: DeviceType.Hardware
    architecture: DeviceType.Architecture
    description: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., hardware: _Optional[_Union[DeviceType.Hardware, str]] = ..., architecture: _Optional[_Union[DeviceType.Architecture, str]] = ..., description: _Optional[str] = ...) -> None: ...
