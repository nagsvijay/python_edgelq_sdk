from edgelq_sdk.meta.proto.v1alpha2 import service_pb2 as _service_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
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

class BusinessTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[BusinessTier]
    LARGE: _ClassVar[BusinessTier]
    MEDIUM: _ClassVar[BusinessTier]
    SMALL: _ClassVar[BusinessTier]
    XSMALL: _ClassVar[BusinessTier]
TPMVAGNOSTIC: TpmVersion
TPMV12: TpmVersion
TPMV20: TpmVersion
SHA1: DigestAlg
SHA256: DigestAlg
UNDEFINED: BusinessTier
LARGE: BusinessTier
MEDIUM: BusinessTier
SMALL: BusinessTier
XSMALL: BusinessTier

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

class ServiceBusinessTier(_message.Message):
    __slots__ = ("service", "business_tier")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TIER_FIELD_NUMBER: _ClassVar[int]
    service: str
    business_tier: BusinessTier
    def __init__(self, service: _Optional[str] = ..., business_tier: _Optional[_Union[BusinessTier, str]] = ...) -> None: ...

class ServiceErrors(_message.Message):
    __slots__ = ("errors",)
    class Error(_message.Message):
        __slots__ = ("service", "message")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        service: str
        message: str
        def __init__(self, service: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ServiceErrors.Error]
    def __init__(self, errors: _Optional[_Iterable[_Union[ServiceErrors.Error, _Mapping]]] = ...) -> None: ...
