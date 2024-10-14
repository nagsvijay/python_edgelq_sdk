from edgelq_sdk.devices.proto.v1 import device_hardware_pb2 as _device_hardware_pb2
from edgelq_sdk.devices.proto.v1 import device_hardware_register_session_pb2 as _device_hardware_register_session_pb2
from edgelq_sdk.devices.proto.v1 import device_hardware_register_session_change_pb2 as _device_hardware_register_session_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterHardwareRequest(_message.Message):
    __slots__ = ("token", "serial_number", "manufacturer", "product_name", "mac_address", "sim_iccid", "imei", "md5_hmac_digest")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIM_ICCID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    MD5_HMAC_DIGEST_FIELD_NUMBER: _ClassVar[int]
    token: str
    serial_number: str
    manufacturer: str
    product_name: str
    mac_address: _containers.RepeatedScalarFieldContainer[str]
    sim_iccid: str
    imei: str
    md5_hmac_digest: str
    def __init__(self, token: _Optional[str] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., mac_address: _Optional[_Iterable[str]] = ..., sim_iccid: _Optional[str] = ..., imei: _Optional[str] = ..., md5_hmac_digest: _Optional[str] = ...) -> None: ...

class RegisterHardwareResponse(_message.Message):
    __slots__ = ("hardware",)
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    hardware: _device_hardware_pb2.DeviceHardware
    def __init__(self, hardware: _Optional[_Union[_device_hardware_pb2.DeviceHardware, _Mapping]] = ...) -> None: ...

class HardwareStatusRequest(_message.Message):
    __slots__ = ("token", "serial_number", "manufacturer", "product_name")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    token: str
    serial_number: str
    manufacturer: str
    product_name: str
    def __init__(self, token: _Optional[str] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ...) -> None: ...

class HardwareStatusResponse(_message.Message):
    __slots__ = ("device_hardwares",)
    DEVICE_HARDWARES_FIELD_NUMBER: _ClassVar[int]
    device_hardwares: _containers.RepeatedCompositeFieldContainer[_device_hardware_pb2.DeviceHardware]
    def __init__(self, device_hardwares: _Optional[_Iterable[_Union[_device_hardware_pb2.DeviceHardware, _Mapping]]] = ...) -> None: ...

class GetDeviceHardwareRegisterSessionFromTokenRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetDeviceHardwareRegisterSessionFromTokenResponse(_message.Message):
    __slots__ = ("device_hardware_register_session", "project_display_name")
    DEVICE_HARDWARE_REGISTER_SESSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    device_hardware_register_session: _device_hardware_register_session_pb2.DeviceHardwareRegisterSession
    project_display_name: str
    def __init__(self, device_hardware_register_session: _Optional[_Union[_device_hardware_register_session_pb2.DeviceHardwareRegisterSession, _Mapping]] = ..., project_display_name: _Optional[str] = ...) -> None: ...
