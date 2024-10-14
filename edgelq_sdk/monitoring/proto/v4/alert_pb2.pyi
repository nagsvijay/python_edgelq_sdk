from edgelq_sdk.monitoring.proto.v4 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alert(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "info", "state")
    class Info(_message.Message):
        __slots__ = ("time_serie", "observed_values")
        class TimeSerie(_message.Message):
            __slots__ = ("key", "metric", "monitored_resource", "data")
            KEY_FIELD_NUMBER: _ClassVar[int]
            METRIC_FIELD_NUMBER: _ClassVar[int]
            MONITORED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            key: bytes
            metric: _common_pb2.Metric
            monitored_resource: _common_pb2.MonitoredResource
            data: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, key: _Optional[bytes] = ..., metric: _Optional[_Union[_common_pb2.Metric, _Mapping]] = ..., monitored_resource: _Optional[_Union[_common_pb2.MonitoredResource, _Mapping]] = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...
        class ObservedValues(_message.Message):
            __slots__ = ("example_value", "per_metric")
            class PerMetricEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            EXAMPLE_VALUE_FIELD_NUMBER: _ClassVar[int]
            PER_METRIC_FIELD_NUMBER: _ClassVar[int]
            example_value: float
            per_metric: _containers.ScalarMap[str, float]
            def __init__(self, example_value: _Optional[float] = ..., per_metric: _Optional[_Mapping[str, float]] = ...) -> None: ...
        TIME_SERIE_FIELD_NUMBER: _ClassVar[int]
        OBSERVED_VALUES_FIELD_NUMBER: _ClassVar[int]
        time_serie: Alert.Info.TimeSerie
        observed_values: Alert.Info.ObservedValues
        def __init__(self, time_serie: _Optional[_Union[Alert.Info.TimeSerie, _Mapping]] = ..., observed_values: _Optional[_Union[Alert.Info.ObservedValues, _Mapping]] = ...) -> None: ...
    class State(_message.Message):
        __slots__ = ("is_firing", "is_acknowledged", "is_silenced", "lifetime", "needs_notification", "notification_created", "lifecycle_completed")
        IS_FIRING_FIELD_NUMBER: _ClassVar[int]
        IS_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
        IS_SILENCED_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_FIELD_NUMBER: _ClassVar[int]
        NEEDS_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_CREATED_FIELD_NUMBER: _ClassVar[int]
        LIFECYCLE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        is_firing: bool
        is_acknowledged: bool
        is_silenced: bool
        lifetime: _common_pb2.TimeRange
        needs_notification: bool
        notification_created: bool
        lifecycle_completed: bool
        def __init__(self, is_firing: bool = ..., is_acknowledged: bool = ..., is_silenced: bool = ..., lifetime: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., needs_notification: bool = ..., notification_created: bool = ..., lifecycle_completed: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    info: Alert.Info
    state: Alert.State
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., info: _Optional[_Union[Alert.Info, _Mapping]] = ..., state: _Optional[_Union[Alert.State, _Mapping]] = ...) -> None: ...
