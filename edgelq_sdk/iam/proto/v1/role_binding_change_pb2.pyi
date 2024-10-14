from edgelq_sdk.iam.proto.v1 import role_binding_pb2 as _role_binding_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleBindingChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("role_binding", "view_index")
        ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        role_binding: _role_binding_pb2.RoleBinding
        view_index: int
        def __init__(self, role_binding: _Optional[_Union[_role_binding_pb2.RoleBinding, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "role_binding", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        role_binding: _role_binding_pb2.RoleBinding
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., role_binding: _Optional[_Union[_role_binding_pb2.RoleBinding, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("role_binding",)
        ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
        role_binding: _role_binding_pb2.RoleBinding
        def __init__(self, role_binding: _Optional[_Union[_role_binding_pb2.RoleBinding, _Mapping]] = ...) -> None: ...
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
    added: RoleBindingChange.Added
    modified: RoleBindingChange.Modified
    current: RoleBindingChange.Current
    removed: RoleBindingChange.Removed
    def __init__(self, added: _Optional[_Union[RoleBindingChange.Added, _Mapping]] = ..., modified: _Optional[_Union[RoleBindingChange.Modified, _Mapping]] = ..., current: _Optional[_Union[RoleBindingChange.Current, _Mapping]] = ..., removed: _Optional[_Union[RoleBindingChange.Removed, _Mapping]] = ...) -> None: ...
