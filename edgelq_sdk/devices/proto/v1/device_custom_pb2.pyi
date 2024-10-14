from edgelq_sdk.common.api import credentials_pb2 as _credentials_pb2
from edgelq_sdk.devices.proto.v1 import device_pb2 as _device_pb2
from edgelq_sdk.devices.proto.v1 import device_change_pb2 as _device_change_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionServiceAccountToDeviceRequest(_message.Message):
    __slots__ = ("name", "external_pubkey")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    external_pubkey: str
    def __init__(self, name: _Optional[str] = ..., external_pubkey: _Optional[str] = ...) -> None: ...

class ProvisionServiceAccountToDeviceResponse(_message.Message):
    __slots__ = ("service_account",)
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: _credentials_pb2.ServiceAccount
    def __init__(self, service_account: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...

class RemoveServiceAccountFromDeviceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RemoveServiceAccountFromDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeartbeatMsg(_message.Message):
    __slots__ = ("name", "register", "heartbeat")
    class Register(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Heartbeat(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTER_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    register: HeartbeatMsg.Register
    heartbeat: HeartbeatMsg.Heartbeat
    def __init__(self, name: _Optional[str] = ..., register: _Optional[_Union[HeartbeatMsg.Register, _Mapping]] = ..., heartbeat: _Optional[_Union[HeartbeatMsg.Heartbeat, _Mapping]] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ("desired_heartbeat_interval",)
    DESIRED_HEARTBEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    desired_heartbeat_interval: _duration_pb2.Duration
    def __init__(self, desired_heartbeat_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
