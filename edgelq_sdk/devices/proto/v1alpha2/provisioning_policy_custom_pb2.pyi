from edgelq_sdk.common.api import credentials_pb2 as _credentials_pb2
from edgelq_sdk.devices.proto.v1alpha2 import device_pb2 as _device_pb2
from edgelq_sdk.devices.proto.v1alpha2 import provisioning_approval_request_pb2 as _provisioning_approval_request_pb2
from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_pb2 as _provisioning_policy_pb2
from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_change_pb2 as _provisioning_policy_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionServiceAccountToProvisioningPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ProvisionServiceAccountToProvisioningPolicyResponse(_message.Message):
    __slots__ = ("service_account",)
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: _credentials_pb2.ServiceAccount
    def __init__(self, service_account: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...

class RemoveServiceAccountFromProvisioningPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RemoveServiceAccountFromProvisioningPolicyResponse(_message.Message):
    __slots__ = ("removed",)
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    removed: bool
    def __init__(self, removed: bool = ...) -> None: ...

class ProvisionDeviceViaPolicyRequest(_message.Message):
    __slots__ = ("name", "device_status", "external_pubkey")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_status: _device_pb2.Device.Status
    external_pubkey: str
    def __init__(self, name: _Optional[str] = ..., device_status: _Optional[_Union[_device_pb2.Device.Status, _Mapping]] = ..., external_pubkey: _Optional[str] = ...) -> None: ...

class ProvisionDeviceViaPolicyResponse(_message.Message):
    __slots__ = ("device", "service_account")
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    device: _device_pb2.Device
    service_account: _credentials_pb2.ServiceAccount
    def __init__(self, device: _Optional[_Union[_device_pb2.Device, _Mapping]] = ..., service_account: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...

class RequestProvisioningApprovalRequest(_message.Message):
    __slots__ = ("name", "external_pubkey")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    external_pubkey: str
    def __init__(self, name: _Optional[str] = ..., external_pubkey: _Optional[str] = ...) -> None: ...

class RequestProvisioningApprovalResponse(_message.Message):
    __slots__ = ("request", "service_account")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    request: _provisioning_approval_request_pb2.ProvisioningApprovalRequest
    service_account: _credentials_pb2.ServiceAccount
    def __init__(self, request: _Optional[_Union[_provisioning_approval_request_pb2.ProvisioningApprovalRequest, _Mapping]] = ..., service_account: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...
