from edgelq_sdk.iam.proto.v1 import attestation_domain_pb2 as _attestation_domain_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttestationDomainChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("attestation_domain", "view_index")
        ATTESTATION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        attestation_domain: _attestation_domain_pb2.AttestationDomain
        view_index: int
        def __init__(self, attestation_domain: _Optional[_Union[_attestation_domain_pb2.AttestationDomain, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "attestation_domain", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ATTESTATION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        attestation_domain: _attestation_domain_pb2.AttestationDomain
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., attestation_domain: _Optional[_Union[_attestation_domain_pb2.AttestationDomain, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("attestation_domain",)
        ATTESTATION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        attestation_domain: _attestation_domain_pb2.AttestationDomain
        def __init__(self, attestation_domain: _Optional[_Union[_attestation_domain_pb2.AttestationDomain, _Mapping]] = ...) -> None: ...
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
    added: AttestationDomainChange.Added
    modified: AttestationDomainChange.Modified
    current: AttestationDomainChange.Current
    removed: AttestationDomainChange.Removed
    def __init__(self, added: _Optional[_Union[AttestationDomainChange.Added, _Mapping]] = ..., modified: _Optional[_Union[AttestationDomainChange.Modified, _Mapping]] = ..., current: _Optional[_Union[AttestationDomainChange.Current, _Mapping]] = ..., removed: _Optional[_Union[AttestationDomainChange.Removed, _Mapping]] = ...) -> None: ...
