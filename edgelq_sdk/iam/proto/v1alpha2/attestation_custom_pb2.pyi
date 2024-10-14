from edgelq_sdk.iam.proto.v1alpha2 import attestation_domain_pb2 as _attestation_domain_pb2
from edgelq_sdk.iam.proto.v1alpha2 import attestation_domain_change_pb2 as _attestation_domain_change_pb2
from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyRequest(_message.Message):
    __slots__ = ("ask_for_challenge", "challenge_response")
    class AskForChallenge(_message.Message):
        __slots__ = ("subject", "attestation_domain", "tpm_version", "ekpub", "ekcert", "ekcerturl", "akpub", "creation_data", "attest", "signature", "challenge_format")
        class ChallengeFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TPM20_CREDENTIAL: _ClassVar[VerifyRequest.AskForChallenge.ChallengeFormat]
            TPM12_EKBLOB: _ClassVar[VerifyRequest.AskForChallenge.ChallengeFormat]
            TSPI_EKBLOB: _ClassVar[VerifyRequest.AskForChallenge.ChallengeFormat]
        TPM20_CREDENTIAL: VerifyRequest.AskForChallenge.ChallengeFormat
        TPM12_EKBLOB: VerifyRequest.AskForChallenge.ChallengeFormat
        TSPI_EKBLOB: VerifyRequest.AskForChallenge.ChallengeFormat
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        ATTESTATION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        TPM_VERSION_FIELD_NUMBER: _ClassVar[int]
        EKPUB_FIELD_NUMBER: _ClassVar[int]
        EKCERT_FIELD_NUMBER: _ClassVar[int]
        EKCERTURL_FIELD_NUMBER: _ClassVar[int]
        AKPUB_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATA_FIELD_NUMBER: _ClassVar[int]
        ATTEST_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        CHALLENGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
        subject: str
        attestation_domain: str
        tpm_version: _common_pb2.TpmVersion
        ekpub: bytes
        ekcert: bytes
        ekcerturl: str
        akpub: bytes
        creation_data: bytes
        attest: bytes
        signature: bytes
        challenge_format: VerifyRequest.AskForChallenge.ChallengeFormat
        def __init__(self, subject: _Optional[str] = ..., attestation_domain: _Optional[str] = ..., tpm_version: _Optional[_Union[_common_pb2.TpmVersion, str]] = ..., ekpub: _Optional[bytes] = ..., ekcert: _Optional[bytes] = ..., ekcerturl: _Optional[str] = ..., akpub: _Optional[bytes] = ..., creation_data: _Optional[bytes] = ..., attest: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., challenge_format: _Optional[_Union[VerifyRequest.AskForChallenge.ChallengeFormat, str]] = ...) -> None: ...
    class ChallengeResponse(_message.Message):
        __slots__ = ("ak_activation_decrypted_secret", "quotes", "pcrs", "eventlog")
        class Quote(_message.Message):
            __slots__ = ("quote", "signature")
            QUOTE_FIELD_NUMBER: _ClassVar[int]
            SIGNATURE_FIELD_NUMBER: _ClassVar[int]
            quote: bytes
            signature: bytes
            def __init__(self, quote: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...
        AK_ACTIVATION_DECRYPTED_SECRET_FIELD_NUMBER: _ClassVar[int]
        QUOTES_FIELD_NUMBER: _ClassVar[int]
        PCRS_FIELD_NUMBER: _ClassVar[int]
        EVENTLOG_FIELD_NUMBER: _ClassVar[int]
        ak_activation_decrypted_secret: bytes
        quotes: _containers.RepeatedCompositeFieldContainer[VerifyRequest.ChallengeResponse.Quote]
        pcrs: _containers.RepeatedCompositeFieldContainer[_common_pb2.PCR]
        eventlog: bytes
        def __init__(self, ak_activation_decrypted_secret: _Optional[bytes] = ..., quotes: _Optional[_Iterable[_Union[VerifyRequest.ChallengeResponse.Quote, _Mapping]]] = ..., pcrs: _Optional[_Iterable[_Union[_common_pb2.PCR, _Mapping]]] = ..., eventlog: _Optional[bytes] = ...) -> None: ...
    ASK_FOR_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ask_for_challenge: VerifyRequest.AskForChallenge
    challenge_response: VerifyRequest.ChallengeResponse
    def __init__(self, ask_for_challenge: _Optional[_Union[VerifyRequest.AskForChallenge, _Mapping]] = ..., challenge_response: _Optional[_Union[VerifyRequest.ChallengeResponse, _Mapping]] = ...) -> None: ...

class VerifyResponse(_message.Message):
    __slots__ = ("challenge", "attestation_successful")
    class Challenge(_message.Message):
        __slots__ = ("platform_attestation_nonce", "cred_encrypted_by_ekpub", "secret_encrypted_by_cred")
        PLATFORM_ATTESTATION_NONCE_FIELD_NUMBER: _ClassVar[int]
        CRED_ENCRYPTED_BY_EKPUB_FIELD_NUMBER: _ClassVar[int]
        SECRET_ENCRYPTED_BY_CRED_FIELD_NUMBER: _ClassVar[int]
        platform_attestation_nonce: bytes
        cred_encrypted_by_ekpub: bytes
        secret_encrypted_by_cred: bytes
        def __init__(self, platform_attestation_nonce: _Optional[bytes] = ..., cred_encrypted_by_ekpub: _Optional[bytes] = ..., secret_encrypted_by_cred: _Optional[bytes] = ...) -> None: ...
    class AttestationSuccessful(_message.Message):
        __slots__ = ("attestation_token",)
        ATTESTATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        attestation_token: str
        def __init__(self, attestation_token: _Optional[str] = ...) -> None: ...
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    challenge: VerifyResponse.Challenge
    attestation_successful: VerifyResponse.AttestationSuccessful
    def __init__(self, challenge: _Optional[_Union[VerifyResponse.Challenge, _Mapping]] = ..., attestation_successful: _Optional[_Union[VerifyResponse.AttestationSuccessful, _Mapping]] = ...) -> None: ...
