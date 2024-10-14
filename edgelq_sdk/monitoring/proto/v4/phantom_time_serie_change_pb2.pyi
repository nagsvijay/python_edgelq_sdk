from edgelq_sdk.monitoring.proto.v4 import phantom_time_serie_pb2 as _phantom_time_serie_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhantomTimeSerieChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("phantom_time_serie", "view_index")
        PHANTOM_TIME_SERIE_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        phantom_time_serie: _phantom_time_serie_pb2.PhantomTimeSerie
        view_index: int
        def __init__(self, phantom_time_serie: _Optional[_Union[_phantom_time_serie_pb2.PhantomTimeSerie, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "phantom_time_serie", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PHANTOM_TIME_SERIE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        phantom_time_serie: _phantom_time_serie_pb2.PhantomTimeSerie
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., phantom_time_serie: _Optional[_Union[_phantom_time_serie_pb2.PhantomTimeSerie, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("phantom_time_serie",)
        PHANTOM_TIME_SERIE_FIELD_NUMBER: _ClassVar[int]
        phantom_time_serie: _phantom_time_serie_pb2.PhantomTimeSerie
        def __init__(self, phantom_time_serie: _Optional[_Union[_phantom_time_serie_pb2.PhantomTimeSerie, _Mapping]] = ...) -> None: ...
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
    added: PhantomTimeSerieChange.Added
    modified: PhantomTimeSerieChange.Modified
    current: PhantomTimeSerieChange.Current
    removed: PhantomTimeSerieChange.Removed
    def __init__(self, added: _Optional[_Union[PhantomTimeSerieChange.Added, _Mapping]] = ..., modified: _Optional[_Union[PhantomTimeSerieChange.Modified, _Mapping]] = ..., current: _Optional[_Union[PhantomTimeSerieChange.Current, _Mapping]] = ..., removed: _Optional[_Union[PhantomTimeSerieChange.Removed, _Mapping]] = ...) -> None: ...
