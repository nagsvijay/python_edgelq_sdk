from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupMember(_message.Message):
    __slots__ = ("name", "member", "parent_member", "min_ancestry_members", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PARENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    MIN_ANCESTRY_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    member: str
    parent_member: str
    min_ancestry_members: _containers.RepeatedScalarFieldContainer[str]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., member: _Optional[str] = ..., parent_member: _Optional[str] = ..., min_ancestry_members: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
