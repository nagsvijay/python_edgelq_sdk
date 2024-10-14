from edgelq_sdk.common.api import attestation_pb2 as _attestation_pb2
from edgelq_sdk.ztp.proto.v1 import edgelq_instance_pb2 as _edgelq_instance_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZtpGetEdgeLQEndpointForDeviceRequest(_message.Message):
    __slots__ = ("identify", "challenge_response")
    IDENTIFY_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    identify: _attestation_pb2.DeviceIdentity
    challenge_response: _attestation_pb2.IdentityChallengeResponse
    def __init__(self, identify: _Optional[_Union[_attestation_pb2.DeviceIdentity, _Mapping]] = ..., challenge_response: _Optional[_Union[_attestation_pb2.IdentityChallengeResponse, _Mapping]] = ...) -> None: ...

class ZtpGetEdgeLQEndpointForDeviceResponse(_message.Message):
    __slots__ = ("identity_challenge", "endpoint_response")
    class EndpointResponse(_message.Message):
        __slots__ = ("edgelq_instance", "provisioning_policy_name", "device_name")
        EDGELQ_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        edgelq_instance: _edgelq_instance_pb2.EdgelqInstance
        provisioning_policy_name: str
        device_name: str
        def __init__(self, edgelq_instance: _Optional[_Union[_edgelq_instance_pb2.EdgelqInstance, _Mapping]] = ..., provisioning_policy_name: _Optional[str] = ..., device_name: _Optional[str] = ...) -> None: ...
    IDENTITY_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    identity_challenge: _attestation_pb2.IdentityChallenge
    endpoint_response: ZtpGetEdgeLQEndpointForDeviceResponse.EndpointResponse
    def __init__(self, identity_challenge: _Optional[_Union[_attestation_pb2.IdentityChallenge, _Mapping]] = ..., endpoint_response: _Optional[_Union[ZtpGetEdgeLQEndpointForDeviceResponse.EndpointResponse, _Mapping]] = ...) -> None: ...
