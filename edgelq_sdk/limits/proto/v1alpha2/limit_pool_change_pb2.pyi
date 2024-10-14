from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_pb2 as _limit_pool_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LimitPoolChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("limit_pool", "view_index")
        LIMIT_POOL_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        limit_pool: _limit_pool_pb2.LimitPool
        view_index: int
        def __init__(self, limit_pool: _Optional[_Union[_limit_pool_pb2.LimitPool, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "limit_pool", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        LIMIT_POOL_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        limit_pool: _limit_pool_pb2.LimitPool
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., limit_pool: _Optional[_Union[_limit_pool_pb2.LimitPool, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("limit_pool",)
        LIMIT_POOL_FIELD_NUMBER: _ClassVar[int]
        limit_pool: _limit_pool_pb2.LimitPool
        def __init__(self, limit_pool: _Optional[_Union[_limit_pool_pb2.LimitPool, _Mapping]] = ...) -> None: ...
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
    added: LimitPoolChange.Added
    modified: LimitPoolChange.Modified
    current: LimitPoolChange.Current
    removed: LimitPoolChange.Removed
    def __init__(self, added: _Optional[_Union[LimitPoolChange.Added, _Mapping]] = ..., modified: _Optional[_Union[LimitPoolChange.Modified, _Mapping]] = ..., current: _Optional[_Union[LimitPoolChange.Current, _Mapping]] = ..., removed: _Optional[_Union[LimitPoolChange.Removed, _Mapping]] = ...) -> None: ...
