from edgelq_sdk.monitoring.proto.v4 import common_pb2 as _common_pb2
from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_pb2 as _metric_descriptor_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Point(_message.Message):
    __slots__ = ("interval", "value", "aggregation")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    interval: _common_pb2.TimeInterval
    value: _common_pb2.TypedValue
    aggregation: _common_pb2.Aggregation
    def __init__(self, interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]] = ..., value: _Optional[_Union[_common_pb2.TypedValue, _Mapping]] = ..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]] = ...) -> None: ...

class TimeSerie(_message.Message):
    __slots__ = ("key", "project", "region", "metric", "resource", "metric_kind", "value_type", "points")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    project: str
    region: str
    metric: _common_pb2.Metric
    resource: _common_pb2.MonitoredResource
    metric_kind: _metric_descriptor_pb2.MetricDescriptor.MetricKind
    value_type: _metric_descriptor_pb2.MetricDescriptor.ValueType
    points: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, key: _Optional[bytes] = ..., project: _Optional[str] = ..., region: _Optional[str] = ..., metric: _Optional[_Union[_common_pb2.Metric, _Mapping]] = ..., resource: _Optional[_Union[_common_pb2.MonitoredResource, _Mapping]] = ..., metric_kind: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor.MetricKind, str]] = ..., value_type: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor.ValueType, str]] = ..., points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class BulkTimeSeries(_message.Message):
    __slots__ = ("time_series", "phantom_flag")
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    PHANTOM_FLAG_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[TimeSerie]
    phantom_flag: bool
    def __init__(self, time_series: _Optional[_Iterable[_Union[TimeSerie, _Mapping]]] = ..., phantom_flag: bool = ...) -> None: ...
