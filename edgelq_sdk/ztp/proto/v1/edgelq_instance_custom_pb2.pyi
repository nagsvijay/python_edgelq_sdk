from edgelq_sdk.ztp.proto.v1 import edgelq_instance_pb2 as _edgelq_instance_pb2
from edgelq_sdk.ztp.proto.v1 import edgelq_instance_change_pb2 as _edgelq_instance_change_pb2
from edgelq_sdk.ztp.proto.v1 import hardware_pb2 as _hardware_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssociateHardwareRequest(_message.Message):
    __slots__ = ("name", "serial_number", "manufacturer", "product_name", "associated_project_name", "associated_provisioning_policy_name", "associated_device_name", "sim_iccid", "imei")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIM_ICCID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    name: str
    serial_number: str
    manufacturer: str
    product_name: str
    associated_project_name: str
    associated_provisioning_policy_name: str
    associated_device_name: str
    sim_iccid: str
    imei: str
    def __init__(self, name: _Optional[str] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., associated_project_name: _Optional[str] = ..., associated_provisioning_policy_name: _Optional[str] = ..., associated_device_name: _Optional[str] = ..., sim_iccid: _Optional[str] = ..., imei: _Optional[str] = ...) -> None: ...

class AssociateHardwareResponse(_message.Message):
    __slots__ = ("hardware",)
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    hardware: _hardware_pb2.Hardware
    def __init__(self, hardware: _Optional[_Union[_hardware_pb2.Hardware, _Mapping]] = ...) -> None: ...

class DissociateHardwareRequest(_message.Message):
    __slots__ = ("name", "serial_number", "manufacturer", "product_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    serial_number: str
    manufacturer: str
    product_name: str
    def __init__(self, name: _Optional[str] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ...) -> None: ...
