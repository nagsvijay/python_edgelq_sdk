from edgelq_sdk.iam.proto.v1 import service_account_pb2 as _service_account_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccountChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("service_account", "view_index")
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        service_account: _service_account_pb2.ServiceAccount
        view_index: int
        def __init__(self, service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "service_account", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        service_account: _service_account_pb2.ServiceAccount
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("service_account",)
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        service_account: _service_account_pb2.ServiceAccount
        def __init__(self, service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...
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
    added: ServiceAccountChange.Added
    modified: ServiceAccountChange.Modified
    current: ServiceAccountChange.Current
    removed: ServiceAccountChange.Removed
    def __init__(self, added: _Optional[_Union[ServiceAccountChange.Added, _Mapping]] = ..., modified: _Optional[_Union[ServiceAccountChange.Modified, _Mapping]] = ..., current: _Optional[_Union[ServiceAccountChange.Current, _Mapping]] = ..., removed: _Optional[_Union[ServiceAccountChange.Removed, _Mapping]] = ...) -> None: ...
