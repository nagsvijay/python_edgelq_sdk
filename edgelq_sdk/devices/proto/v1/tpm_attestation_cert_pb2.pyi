from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TpmAttestationCert(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "manufacturer", "product_name", "tpm_manufacturer_ca_cert", "idevid_issuer_ca_cert", "ldevid_issuer_ca_cert")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    TPM_MANUFACTURER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    IDEVID_ISSUER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    LDEVID_ISSUER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    manufacturer: str
    product_name: str
    tpm_manufacturer_ca_cert: str
    idevid_issuer_ca_cert: str
    ldevid_issuer_ca_cert: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., tpm_manufacturer_ca_cert: _Optional[str] = ..., idevid_issuer_ca_cert: _Optional[str] = ..., ldevid_issuer_ca_cert: _Optional[str] = ...) -> None: ...
