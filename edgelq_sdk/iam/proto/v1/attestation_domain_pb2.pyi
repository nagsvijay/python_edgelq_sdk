from edgelq_sdk.iam.proto.v1 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttestationDomain(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "insecure_skip_manufacturer_ekcert_verification", "policies", "enrollment_list")
    class Policy(_message.Message):
        __slots__ = ("manufacturer_root_ca_certs_pem", "require_enrollment", "verify_event_log", "expected_pcrs")
        MANUFACTURER_ROOT_CA_CERTS_PEM_FIELD_NUMBER: _ClassVar[int]
        REQUIRE_ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
        VERIFY_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_PCRS_FIELD_NUMBER: _ClassVar[int]
        manufacturer_root_ca_certs_pem: str
        require_enrollment: bool
        verify_event_log: bool
        expected_pcrs: _containers.RepeatedCompositeFieldContainer[_common_pb2.PCR]
        def __init__(self, manufacturer_root_ca_certs_pem: _Optional[str] = ..., require_enrollment: bool = ..., verify_event_log: bool = ..., expected_pcrs: _Optional[_Iterable[_Union[_common_pb2.PCR, _Mapping]]] = ...) -> None: ...
    class EnrolledKey(_message.Message):
        __slots__ = ("pubkey_pem", "comment")
        PUBKEY_PEM_FIELD_NUMBER: _ClassVar[int]
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        pubkey_pem: str
        comment: str
        def __init__(self, pubkey_pem: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INSECURE_SKIP_MANUFACTURER_EKCERT_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    insecure_skip_manufacturer_ekcert_verification: bool
    policies: _containers.RepeatedCompositeFieldContainer[AttestationDomain.Policy]
    enrollment_list: _containers.RepeatedCompositeFieldContainer[AttestationDomain.EnrolledKey]
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., insecure_skip_manufacturer_ekcert_verification: bool = ..., policies: _Optional[_Iterable[_Union[AttestationDomain.Policy, _Mapping]]] = ..., enrollment_list: _Optional[_Iterable[_Union[AttestationDomain.EnrolledKey, _Mapping]]] = ...) -> None: ...
