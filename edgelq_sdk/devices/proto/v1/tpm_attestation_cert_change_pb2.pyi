from edgelq_sdk.devices.proto.v1 import tpm_attestation_cert_pb2 as _tpm_attestation_cert_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TpmAttestationCertChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("tpm_attestation_cert", "view_index")
        TPM_ATTESTATION_CERT_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        tpm_attestation_cert: _tpm_attestation_cert_pb2.TpmAttestationCert
        view_index: int
        def __init__(self, tpm_attestation_cert: _Optional[_Union[_tpm_attestation_cert_pb2.TpmAttestationCert, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "tpm_attestation_cert", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TPM_ATTESTATION_CERT_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        tpm_attestation_cert: _tpm_attestation_cert_pb2.TpmAttestationCert
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., tpm_attestation_cert: _Optional[_Union[_tpm_attestation_cert_pb2.TpmAttestationCert, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("tpm_attestation_cert",)
        TPM_ATTESTATION_CERT_FIELD_NUMBER: _ClassVar[int]
        tpm_attestation_cert: _tpm_attestation_cert_pb2.TpmAttestationCert
        def __init__(self, tpm_attestation_cert: _Optional[_Union[_tpm_attestation_cert_pb2.TpmAttestationCert, _Mapping]] = ...) -> None: ...
    class Removed(_message.Message):
        __slots__ = ("name", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        view_index: int
        def __init__(self, name: _Optional[str] = ..., view_index: _Optional[int] = ...) -> None: ...
    ADDED_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    added: TpmAttestationCertChange.Added
    modified: TpmAttestationCertChange.Modified
    current: TpmAttestationCertChange.Current
    removed: TpmAttestationCertChange.Removed
    def __init__(self, added: _Optional[_Union[TpmAttestationCertChange.Added, _Mapping]] = ..., modified: _Optional[_Union[TpmAttestationCertChange.Modified, _Mapping]] = ..., current: _Optional[_Union[TpmAttestationCertChange.Current, _Mapping]] = ..., removed: _Optional[_Union[TpmAttestationCertChange.Removed, _Mapping]] = ...) -> None: ...
