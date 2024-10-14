from edgelq_sdk.applications.proto.v1alpha2 import distribution_pb2 as _distribution_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DistributionChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("distribution", "view_index")
        DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        distribution: _distribution_pb2.Distribution
        view_index: int
        def __init__(self, distribution: _Optional[_Union[_distribution_pb2.Distribution, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "distribution", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        distribution: _distribution_pb2.Distribution
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., distribution: _Optional[_Union[_distribution_pb2.Distribution, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("distribution",)
        DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
        distribution: _distribution_pb2.Distribution
        def __init__(self, distribution: _Optional[_Union[_distribution_pb2.Distribution, _Mapping]] = ...) -> None: ...
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
    added: DistributionChange.Added
    modified: DistributionChange.Modified
    current: DistributionChange.Current
    removed: DistributionChange.Removed
    def __init__(self, added: _Optional[_Union[DistributionChange.Added, _Mapping]] = ..., modified: _Optional[_Union[DistributionChange.Modified, _Mapping]] = ..., current: _Optional[_Union[DistributionChange.Current, _Mapping]] = ..., removed: _Optional[_Union[DistributionChange.Removed, _Mapping]] = ...) -> None: ...
