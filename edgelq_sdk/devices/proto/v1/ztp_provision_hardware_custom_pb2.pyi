from edgelq_sdk.common.api import attestation_pb2 as _attestation_pb2
from edgelq_sdk.common.api import credentials_pb2 as _credentials_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionHardwareRequest(_message.Message):
    __slots__ = ("provisioning_target", "identify", "challenge_response")
    class ProvisioningTarget(_message.Message):
        __slots__ = ("provisioning_policy_name", "device_name")
        PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        provisioning_policy_name: str
        device_name: str
        def __init__(self, provisioning_policy_name: _Optional[str] = ..., device_name: _Optional[str] = ...) -> None: ...
    PROVISIONING_TARGET_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    provisioning_target: ProvisionHardwareRequest.ProvisioningTarget
    identify: _attestation_pb2.DeviceIdentity
    challenge_response: _attestation_pb2.IdentityChallengeResponse
    def __init__(self, provisioning_target: _Optional[_Union[ProvisionHardwareRequest.ProvisioningTarget, _Mapping]] = ..., identify: _Optional[_Union[_attestation_pb2.DeviceIdentity, _Mapping]] = ..., challenge_response: _Optional[_Union[_attestation_pb2.IdentityChallengeResponse, _Mapping]] = ...) -> None: ...

class ProvisionHardwareResponse(_message.Message):
    __slots__ = ("identity_challenge", "provisioning_response")
    class ProvisioningResponse(_message.Message):
        __slots__ = ("service_account", "provisioning_policy_name", "device_name")
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        service_account: _credentials_pb2.ServiceAccount
        provisioning_policy_name: str
        device_name: str
        def __init__(self, service_account: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ..., provisioning_policy_name: _Optional[str] = ..., device_name: _Optional[str] = ...) -> None: ...
    IDENTITY_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    identity_challenge: _attestation_pb2.IdentityChallenge
    provisioning_response: ProvisionHardwareResponse.ProvisioningResponse
    def __init__(self, identity_challenge: _Optional[_Union[_attestation_pb2.IdentityChallenge, _Mapping]] = ..., provisioning_response: _Optional[_Union[ProvisionHardwareResponse.ProvisioningResponse, _Mapping]] = ...) -> None: ...
