from edgelq_sdk.iam.proto.v1 import permission_pb2 as _permission_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("permission", "view_index")
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        permission: _permission_pb2.Permission
        view_index: int
        def __init__(self, permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "permission", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        permission: _permission_pb2.Permission
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("permission",)
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        permission: _permission_pb2.Permission
        def __init__(self, permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...
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
    added: PermissionChange.Added
    modified: PermissionChange.Modified
    current: PermissionChange.Current
    removed: PermissionChange.Removed
    def __init__(self, added: _Optional[_Union[PermissionChange.Added, _Mapping]] = ..., modified: _Optional[_Union[PermissionChange.Modified, _Mapping]] = ..., current: _Optional[_Union[PermissionChange.Current, _Mapping]] = ..., removed: _Optional[_Union[PermissionChange.Removed, _Mapping]] = ...) -> None: ...
