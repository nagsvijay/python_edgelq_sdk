from edgelq_sdk.iam.proto.v1alpha2 import service_account_key_pb2 as _service_account_key_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccountKeyChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("service_account_key", "view_index")
        SERVICE_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        service_account_key: _service_account_key_pb2.ServiceAccountKey
        view_index: int
        def __init__(self, service_account_key: _Optional[_Union[_service_account_key_pb2.ServiceAccountKey, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "service_account_key", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        service_account_key: _service_account_key_pb2.ServiceAccountKey
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., service_account_key: _Optional[_Union[_service_account_key_pb2.ServiceAccountKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("service_account_key",)
        SERVICE_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        service_account_key: _service_account_key_pb2.ServiceAccountKey
        def __init__(self, service_account_key: _Optional[_Union[_service_account_key_pb2.ServiceAccountKey, _Mapping]] = ...) -> None: ...
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
    added: ServiceAccountKeyChange.Added
    modified: ServiceAccountKeyChange.Modified
    current: ServiceAccountKeyChange.Current
    removed: ServiceAccountKeyChange.Removed
    def __init__(self, added: _Optional[_Union[ServiceAccountKeyChange.Added, _Mapping]] = ..., modified: _Optional[_Union[ServiceAccountKeyChange.Modified, _Mapping]] = ..., current: _Optional[_Union[ServiceAccountKeyChange.Current, _Mapping]] = ..., removed: _Optional[_Union[ServiceAccountKeyChange.Removed, _Mapping]] = ...) -> None: ...
