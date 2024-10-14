from edgelq_sdk.secrets.proto.v1alpha2 import secret_pb2 as _secret_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecretChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("secret", "view_index")
        SECRET_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        secret: _secret_pb2.Secret
        view_index: int
        def __init__(self, secret: _Optional[_Union[_secret_pb2.Secret, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "secret", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        secret: _secret_pb2.Secret
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., secret: _Optional[_Union[_secret_pb2.Secret, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("secret",)
        SECRET_FIELD_NUMBER: _ClassVar[int]
        secret: _secret_pb2.Secret
        def __init__(self, secret: _Optional[_Union[_secret_pb2.Secret, _Mapping]] = ...) -> None: ...
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
    added: SecretChange.Added
    modified: SecretChange.Modified
    current: SecretChange.Current
    removed: SecretChange.Removed
    def __init__(self, added: _Optional[_Union[SecretChange.Added, _Mapping]] = ..., modified: _Optional[_Union[SecretChange.Modified, _Mapping]] = ..., current: _Optional[_Union[SecretChange.Current, _Mapping]] = ..., removed: _Optional[_Union[SecretChange.Removed, _Mapping]] = ...) -> None: ...
