from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TpmVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TPMVAGNOSTIC: _ClassVar[TpmVersion]
    TPMV12: _ClassVar[TpmVersion]
    TPMV20: _ClassVar[TpmVersion]

class DigestAlg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHA1: _ClassVar[DigestAlg]
    SHA256: _ClassVar[DigestAlg]
TPMVAGNOSTIC: TpmVersion
TPMV12: TpmVersion
TPMV20: TpmVersion
SHA1: DigestAlg
SHA256: DigestAlg

class DeviceIdentity(_message.Message):
    __slots__ = ("serial_number", "manufacturer", "product_name", "tpm_version", "ek_tpm_pub", "ekcert", "ekcerturl", "idevid_cert_tpm_pub", "idevid_cert", "ldevid_cert_tpm_pub", "ldevid_cert", "ak_params", "challenge_format")
    class ChallengeFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TPM20_CREDENTIAL: _ClassVar[DeviceIdentity.ChallengeFormat]
    TPM20_CREDENTIAL: DeviceIdentity.ChallengeFormat
    class AttestationParams(_message.Message):
        __slots__ = ("akpub", "creation_data", "attest", "signature")
        AKPUB_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATA_FIELD_NUMBER: _ClassVar[int]
        ATTEST_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        akpub: bytes
        creation_data: bytes
        attest: bytes
        signature: bytes
        def __init__(self, akpub: _Optional[bytes] = ..., creation_data: _Optional[bytes] = ..., attest: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    TPM_VERSION_FIELD_NUMBER: _ClassVar[int]
    EK_TPM_PUB_FIELD_NUMBER: _ClassVar[int]
    EKCERT_FIELD_NUMBER: _ClassVar[int]
    EKCERTURL_FIELD_NUMBER: _ClassVar[int]
    IDEVID_CERT_TPM_PUB_FIELD_NUMBER: _ClassVar[int]
    IDEVID_CERT_FIELD_NUMBER: _ClassVar[int]
    LDEVID_CERT_TPM_PUB_FIELD_NUMBER: _ClassVar[int]
    LDEVID_CERT_FIELD_NUMBER: _ClassVar[int]
    AK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    manufacturer: str
    product_name: str
    tpm_version: TpmVersion
    ek_tpm_pub: bytes
    ekcert: bytes
    ekcerturl: str
    idevid_cert_tpm_pub: bytes
    idevid_cert: bytes
    ldevid_cert_tpm_pub: bytes
    ldevid_cert: bytes
    ak_params: DeviceIdentity.AttestationParams
    challenge_format: DeviceIdentity.ChallengeFormat
    def __init__(self, serial_number: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., tpm_version: _Optional[_Union[TpmVersion, str]] = ..., ek_tpm_pub: _Optional[bytes] = ..., ekcert: _Optional[bytes] = ..., ekcerturl: _Optional[str] = ..., idevid_cert_tpm_pub: _Optional[bytes] = ..., idevid_cert: _Optional[bytes] = ..., ldevid_cert_tpm_pub: _Optional[bytes] = ..., ldevid_cert: _Optional[bytes] = ..., ak_params: _Optional[_Union[DeviceIdentity.AttestationParams, _Mapping]] = ..., challenge_format: _Optional[_Union[DeviceIdentity.ChallengeFormat, str]] = ...) -> None: ...

class IdentityChallenge(_message.Message):
    __slots__ = ("platform_attestation_nonce", "cred_encrypted_by_ekpub", "secret_encrypted_by_ekcred", "cred_encrypted_by_idevid_pub", "secret_encrypted_by_idevid_cred", "cred_encrypted_by_ldevid_pub", "secret_encrypted_by_ldevid_cred", "digest_to_sign_with_idevid", "rsa_secret_to_decrypt_with_idevid", "digest_to_sign_with_ldevid", "rsa_secret_to_decrypt_with_ldevid")
    PLATFORM_ATTESTATION_NONCE_FIELD_NUMBER: _ClassVar[int]
    CRED_ENCRYPTED_BY_EKPUB_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENCRYPTED_BY_EKCRED_FIELD_NUMBER: _ClassVar[int]
    CRED_ENCRYPTED_BY_IDEVID_PUB_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENCRYPTED_BY_IDEVID_CRED_FIELD_NUMBER: _ClassVar[int]
    CRED_ENCRYPTED_BY_LDEVID_PUB_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENCRYPTED_BY_LDEVID_CRED_FIELD_NUMBER: _ClassVar[int]
    DIGEST_TO_SIGN_WITH_IDEVID_FIELD_NUMBER: _ClassVar[int]
    RSA_SECRET_TO_DECRYPT_WITH_IDEVID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_TO_SIGN_WITH_LDEVID_FIELD_NUMBER: _ClassVar[int]
    RSA_SECRET_TO_DECRYPT_WITH_LDEVID_FIELD_NUMBER: _ClassVar[int]
    platform_attestation_nonce: bytes
    cred_encrypted_by_ekpub: bytes
    secret_encrypted_by_ekcred: bytes
    cred_encrypted_by_idevid_pub: bytes
    secret_encrypted_by_idevid_cred: bytes
    cred_encrypted_by_ldevid_pub: bytes
    secret_encrypted_by_ldevid_cred: bytes
    digest_to_sign_with_idevid: bytes
    rsa_secret_to_decrypt_with_idevid: bytes
    digest_to_sign_with_ldevid: bytes
    rsa_secret_to_decrypt_with_ldevid: bytes
    def __init__(self, platform_attestation_nonce: _Optional[bytes] = ..., cred_encrypted_by_ekpub: _Optional[bytes] = ..., secret_encrypted_by_ekcred: _Optional[bytes] = ..., cred_encrypted_by_idevid_pub: _Optional[bytes] = ..., secret_encrypted_by_idevid_cred: _Optional[bytes] = ..., cred_encrypted_by_ldevid_pub: _Optional[bytes] = ..., secret_encrypted_by_ldevid_cred: _Optional[bytes] = ..., digest_to_sign_with_idevid: _Optional[bytes] = ..., rsa_secret_to_decrypt_with_idevid: _Optional[bytes] = ..., digest_to_sign_with_ldevid: _Optional[bytes] = ..., rsa_secret_to_decrypt_with_ldevid: _Optional[bytes] = ...) -> None: ...

class IdentityChallengeResponse(_message.Message):
    __slots__ = ("ak_activation_decrypted_secret", "idevid_activation_decrypted_secret", "ldevid_activation_decrypted_secret", "digest_signed_by_idevid", "digest_signed_by_ldevid", "rsa_decrypted_with_idevid", "rsa_decrypted_with_ldevid", "quotes", "pcrs", "eventlog")
    class Quote(_message.Message):
        __slots__ = ("quote", "signature")
        QUOTE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        quote: bytes
        signature: bytes
        def __init__(self, quote: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...
    AK_ACTIVATION_DECRYPTED_SECRET_FIELD_NUMBER: _ClassVar[int]
    IDEVID_ACTIVATION_DECRYPTED_SECRET_FIELD_NUMBER: _ClassVar[int]
    LDEVID_ACTIVATION_DECRYPTED_SECRET_FIELD_NUMBER: _ClassVar[int]
    DIGEST_SIGNED_BY_IDEVID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_SIGNED_BY_LDEVID_FIELD_NUMBER: _ClassVar[int]
    RSA_DECRYPTED_WITH_IDEVID_FIELD_NUMBER: _ClassVar[int]
    RSA_DECRYPTED_WITH_LDEVID_FIELD_NUMBER: _ClassVar[int]
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    PCRS_FIELD_NUMBER: _ClassVar[int]
    EVENTLOG_FIELD_NUMBER: _ClassVar[int]
    ak_activation_decrypted_secret: bytes
    idevid_activation_decrypted_secret: bytes
    ldevid_activation_decrypted_secret: bytes
    digest_signed_by_idevid: bytes
    digest_signed_by_ldevid: bytes
    rsa_decrypted_with_idevid: bytes
    rsa_decrypted_with_ldevid: bytes
    quotes: _containers.RepeatedCompositeFieldContainer[IdentityChallengeResponse.Quote]
    pcrs: _containers.RepeatedCompositeFieldContainer[PCR]
    eventlog: bytes
    def __init__(self, ak_activation_decrypted_secret: _Optional[bytes] = ..., idevid_activation_decrypted_secret: _Optional[bytes] = ..., ldevid_activation_decrypted_secret: _Optional[bytes] = ..., digest_signed_by_idevid: _Optional[bytes] = ..., digest_signed_by_ldevid: _Optional[bytes] = ..., rsa_decrypted_with_idevid: _Optional[bytes] = ..., rsa_decrypted_with_ldevid: _Optional[bytes] = ..., quotes: _Optional[_Iterable[_Union[IdentityChallengeResponse.Quote, _Mapping]]] = ..., pcrs: _Optional[_Iterable[_Union[PCR, _Mapping]]] = ..., eventlog: _Optional[bytes] = ...) -> None: ...

class PCR(_message.Message):
    __slots__ = ("index", "digest_hex", "digest_alg", "comment")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DIGEST_HEX_FIELD_NUMBER: _ClassVar[int]
    DIGEST_ALG_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    index: int
    digest_hex: str
    digest_alg: DigestAlg
    comment: str
    def __init__(self, index: _Optional[int] = ..., digest_hex: _Optional[str] = ..., digest_alg: _Optional[_Union[DigestAlg, str]] = ..., comment: _Optional[str] = ...) -> None: ...
