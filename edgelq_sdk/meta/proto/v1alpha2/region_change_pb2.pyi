from edgelq_sdk.meta.proto.v1alpha2 import region_pb2 as _region_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegionChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("region", "view_index")
        REGION_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        region: _region_pb2.Region
        view_index: int
        def __init__(self, region: _Optional[_Union[_region_pb2.Region, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "region", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        region: _region_pb2.Region
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., region: _Optional[_Union[_region_pb2.Region, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("region",)
        REGION_FIELD_NUMBER: _ClassVar[int]
        region: _region_pb2.Region
        def __init__(self, region: _Optional[_Union[_region_pb2.Region, _Mapping]] = ...) -> None: ...
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
    added: RegionChange.Added
    modified: RegionChange.Modified
    current: RegionChange.Current
    removed: RegionChange.Removed
    def __init__(self, added: _Optional[_Union[RegionChange.Added, _Mapping]] = ..., modified: _Optional[_Union[RegionChange.Modified, _Mapping]] = ..., current: _Optional[_Union[RegionChange.Current, _Mapping]] = ..., removed: _Optional[_Union[RegionChange.Removed, _Mapping]] = ...) -> None: ...
