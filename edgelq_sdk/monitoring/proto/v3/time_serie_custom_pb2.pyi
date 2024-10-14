from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from edgelq_sdk.monitoring.proto.v3 import common_pb2 as _common_pb2
from edgelq_sdk.monitoring.proto.v3 import time_serie_pb2 as _time_serie_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTimeSeriesRequest(_message.Message):
    __slots__ = ("parent", "filter", "interval", "aggregation", "pagination", "view", "field_mask", "points_cap", "continuation_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    POINTS_CAP_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    interval: _common_pb2.TimeInterval
    aggregation: _common_pb2.Aggregation
    pagination: _common_pb2.Pagination
    view: _common_pb2.TimeSeriesView
    field_mask: _field_mask_pb2.FieldMask
    points_cap: int
    continuation_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]] = ..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.Pagination, _Mapping]] = ..., view: _Optional[_Union[_common_pb2.TimeSeriesView, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., points_cap: _Optional[int] = ..., continuation_token: _Optional[str] = ...) -> None: ...

class ListTimeSeriesResponse(_message.Message):
    __slots__ = ("time_series", "continuation_token", "total_point_counters")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_POINT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    continuation_token: str
    total_point_counters: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    def __init__(self, time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ..., continuation_token: _Optional[str] = ..., total_point_counters: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ...) -> None: ...

class CreateTimeSeriesRequest(_message.Message):
    __slots__ = ("parent", "time_series")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    def __init__(self, parent: _Optional[str] = ..., time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ...) -> None: ...

class CreateTimeSeriesResponse(_message.Message):
    __slots__ = ("time_serie_keys", "failed_time_series")
    class TimeSerieKeysEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    TIME_SERIE_KEYS_FIELD_NUMBER: _ClassVar[int]
    FAILED_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    time_serie_keys: _containers.ScalarMap[int, bytes]
    failed_time_series: _containers.RepeatedCompositeFieldContainer[CreateTimeSeriesError]
    def __init__(self, time_serie_keys: _Optional[_Mapping[int, bytes]] = ..., failed_time_series: _Optional[_Iterable[_Union[CreateTimeSeriesError, _Mapping]]] = ...) -> None: ...

class CreateTimeSeriesError(_message.Message):
    __slots__ = ("time_series", "status")
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    time_series: _time_serie_pb2.TimeSerie
    status: _status_pb2.Status
    def __init__(self, time_series: _Optional[_Union[_time_serie_pb2.TimeSerie, _Mapping]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
