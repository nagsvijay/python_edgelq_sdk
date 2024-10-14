from edgelq_sdk.devices.proto.v1 import device_pb2 as _device_pb2
from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_pb2 as _provisioning_approval_request_pb2
from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_change_pb2 as _provisioning_approval_request_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionDeviceForApprovedRequestRequest(_message.Message):
    __slots__ = ("name", "device_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_status: _device_pb2.Device.Status
    def __init__(self, name: _Optional[str] = ..., device_status: _Optional[_Union[_device_pb2.Device.Status, _Mapping]] = ...) -> None: ...

class ProvisionDeviceForApprovedRequestResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: _device_pb2.Device
    def __init__(self, device: _Optional[_Union[_device_pb2.Device, _Mapping]] = ...) -> None: ...
