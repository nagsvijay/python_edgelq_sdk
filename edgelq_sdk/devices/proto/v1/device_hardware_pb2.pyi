from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceHardware(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "serial_number", "manufacturer", "product_name", "mac_address", "sim_iccid", "imei", "associated_provisioning_policy_name", "associated_device", "status")
    class Status(_message.Message):
        __slots__ = ("provisioning_state",)
        class PROVISIONING_STATE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[DeviceHardware.Status.PROVISIONING_STATE]
            NOT_PROVISIONED: _ClassVar[DeviceHardware.Status.PROVISIONING_STATE]
            PROVISIONED: _ClassVar[DeviceHardware.Status.PROVISIONING_STATE]
            REVOKED: _ClassVar[DeviceHardware.Status.PROVISIONING_STATE]
        UNKNOWN: DeviceHardware.Status.PROVISIONING_STATE
        NOT_PROVISIONED: DeviceHardware.Status.PROVISIONING_STATE
        PROVISIONED: DeviceHardware.Status.PROVISIONING_STATE
        REVOKED: DeviceHardware.Status.PROVISIONING_STATE
        PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
        provisioning_state: DeviceHardware.Status.PROVISIONING_STATE
        def __init__(self, provisioning_state: _Optional[_Union[DeviceHardware.Status.PROVISIONING_STATE, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIM_ICCID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DEVICE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    serial_number: str
    manufacturer: str
    product_name: str
    mac_address: _containers.RepeatedScalarFieldContainer[str]
    sim_iccid: str
    imei: str
    associated_provisioning_policy_name: str
    associated_device: str
    status: DeviceHardware.Status
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., mac_address: _Optional[_Iterable[str]] = ..., sim_iccid: _Optional[str] = ..., imei: _Optional[str] = ..., associated_provisioning_policy_name: _Optional[str] = ..., associated_device: _Optional[str] = ..., status: _Optional[_Union[DeviceHardware.Status, _Mapping]] = ...) -> None: ...
