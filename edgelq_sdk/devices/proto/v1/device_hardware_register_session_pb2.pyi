from edgelq_sdk.devices.proto.v1 import device_hardware_pb2 as _device_hardware_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceHardwareRegisterSession(_message.Message):
    __slots__ = ("name", "display_name", "metadata", "start_time", "expiration_time", "user_email", "inviter_email", "language_code", "extras", "provisioning_policy_name", "device_name", "single_use", "token", "status")
    class ExtrasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("device_hardwares",)
        DEVICE_HARDWARES_FIELD_NUMBER: _ClassVar[int]
        device_hardwares: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, device_hardwares: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    INVITER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SINGLE_USE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metadata: _meta_pb2.Meta
    start_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    user_email: str
    inviter_email: str
    language_code: str
    extras: _containers.ScalarMap[str, str]
    provisioning_policy_name: str
    device_name: str
    single_use: bool
    token: str
    status: DeviceHardwareRegisterSession.Status
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_email: _Optional[str] = ..., inviter_email: _Optional[str] = ..., language_code: _Optional[str] = ..., extras: _Optional[_Mapping[str, str]] = ..., provisioning_policy_name: _Optional[str] = ..., device_name: _Optional[str] = ..., single_use: bool = ..., token: _Optional[str] = ..., status: _Optional[_Union[DeviceHardwareRegisterSession.Status, _Mapping]] = ...) -> None: ...
