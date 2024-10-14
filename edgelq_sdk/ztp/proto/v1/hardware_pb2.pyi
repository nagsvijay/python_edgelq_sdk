from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hardware(_message.Message):
    __slots__ = ("name", "metadata", "serial_number", "manufacturer", "product_name", "associated_edgelq_instance", "associated_project", "associated_provisioning_policy_name", "associated_device_name", "sim_iccid", "imei")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_EDGELQ_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIM_ICCID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    serial_number: str
    manufacturer: str
    product_name: str
    associated_edgelq_instance: str
    associated_project: str
    associated_provisioning_policy_name: str
    associated_device_name: str
    sim_iccid: str
    imei: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., associated_edgelq_instance: _Optional[str] = ..., associated_project: _Optional[str] = ..., associated_provisioning_policy_name: _Optional[str] = ..., associated_device_name: _Optional[str] = ..., sim_iccid: _Optional[str] = ..., imei: _Optional[str] = ...) -> None: ...
