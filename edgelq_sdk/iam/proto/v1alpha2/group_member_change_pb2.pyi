from edgelq_sdk.iam.proto.v1alpha2 import group_member_pb2 as _group_member_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupMemberChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("group_member", "view_index")
        GROUP_MEMBER_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        group_member: _group_member_pb2.GroupMember
        view_index: int
        def __init__(self, group_member: _Optional[_Union[_group_member_pb2.GroupMember, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "group_member", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_MEMBER_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        group_member: _group_member_pb2.GroupMember
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., group_member: _Optional[_Union[_group_member_pb2.GroupMember, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("group_member",)
        GROUP_MEMBER_FIELD_NUMBER: _ClassVar[int]
        group_member: _group_member_pb2.GroupMember
        def __init__(self, group_member: _Optional[_Union[_group_member_pb2.GroupMember, _Mapping]] = ...) -> None: ...
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
    added: GroupMemberChange.Added
    modified: GroupMemberChange.Modified
    current: GroupMemberChange.Current
    removed: GroupMemberChange.Removed
    def __init__(self, added: _Optional[_Union[GroupMemberChange.Added, _Mapping]] = ..., modified: _Optional[_Union[GroupMemberChange.Modified, _Mapping]] = ..., current: _Optional[_Union[GroupMemberChange.Current, _Mapping]] = ..., removed: _Optional[_Union[GroupMemberChange.Removed, _Mapping]] = ...) -> None: ...
