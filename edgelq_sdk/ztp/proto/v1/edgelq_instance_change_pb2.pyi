from edgelq_sdk.ztp.proto.v1 import edgelq_instance_pb2 as _edgelq_instance_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EdgelqInstanceChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("edgelq_instance", "view_index")
        EDGELQ_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        edgelq_instance: _edgelq_instance_pb2.EdgelqInstance
        view_index: int
        def __init__(self, edgelq_instance: _Optional[_Union[_edgelq_instance_pb2.EdgelqInstance, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "edgelq_instance", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        EDGELQ_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        edgelq_instance: _edgelq_instance_pb2.EdgelqInstance
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., edgelq_instance: _Optional[_Union[_edgelq_instance_pb2.EdgelqInstance, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("edgelq_instance",)
        EDGELQ_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        edgelq_instance: _edgelq_instance_pb2.EdgelqInstance
        def __init__(self, edgelq_instance: _Optional[_Union[_edgelq_instance_pb2.EdgelqInstance, _Mapping]] = ...) -> None: ...
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
    added: EdgelqInstanceChange.Added
    modified: EdgelqInstanceChange.Modified
    current: EdgelqInstanceChange.Current
    removed: EdgelqInstanceChange.Removed
    def __init__(self, added: _Optional[_Union[EdgelqInstanceChange.Added, _Mapping]] = ..., modified: _Optional[_Union[EdgelqInstanceChange.Modified, _Mapping]] = ..., current: _Optional[_Union[EdgelqInstanceChange.Current, _Mapping]] = ..., removed: _Optional[_Union[EdgelqInstanceChange.Removed, _Mapping]] = ...) -> None: ...
