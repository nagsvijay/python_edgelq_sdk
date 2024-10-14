from edgelq_sdk.monitoring.proto.v3 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertingCondition(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "description", "spec", "state")
    class Spec(_message.Message):
        __slots__ = ("time_series", "trigger")
        class TimeSeries(_message.Message):
            __slots__ = ("query", "threshold", "combine_threshold", "duration")
            class Query(_message.Message):
                __slots__ = ("selector", "aggregation")
                SELECTOR_FIELD_NUMBER: _ClassVar[int]
                AGGREGATION_FIELD_NUMBER: _ClassVar[int]
                selector: _common_pb2.TimeSeriesSelector
                aggregation: _common_pb2.Aggregation
                def __init__(self, selector: _Optional[_Union[_common_pb2.TimeSeriesSelector, _Mapping]] = ..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]] = ...) -> None: ...
            class Threshold(_message.Message):
                __slots__ = ("compare", "value")
                class Compare(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    COMPARE_UNSPECIFIED: _ClassVar[AlertingCondition.Spec.TimeSeries.Threshold.Compare]
                    GT: _ClassVar[AlertingCondition.Spec.TimeSeries.Threshold.Compare]
                    LT: _ClassVar[AlertingCondition.Spec.TimeSeries.Threshold.Compare]
                COMPARE_UNSPECIFIED: AlertingCondition.Spec.TimeSeries.Threshold.Compare
                GT: AlertingCondition.Spec.TimeSeries.Threshold.Compare
                LT: AlertingCondition.Spec.TimeSeries.Threshold.Compare
                COMPARE_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                compare: AlertingCondition.Spec.TimeSeries.Threshold.Compare
                value: float
                def __init__(self, compare: _Optional[_Union[AlertingCondition.Spec.TimeSeries.Threshold.Compare, str]] = ..., value: _Optional[float] = ...) -> None: ...
            class CombineThreshold(_message.Message):
                __slots__ = ("per_metric", "combine")
                class CombineOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    OR: _ClassVar[AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator]
                    AND: _ClassVar[AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator]
                OR: AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator
                AND: AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator
                class PerMetricEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: AlertingCondition.Spec.TimeSeries.Threshold
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AlertingCondition.Spec.TimeSeries.Threshold, _Mapping]] = ...) -> None: ...
                PER_METRIC_FIELD_NUMBER: _ClassVar[int]
                COMBINE_FIELD_NUMBER: _ClassVar[int]
                per_metric: _containers.MessageMap[str, AlertingCondition.Spec.TimeSeries.Threshold]
                combine: AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator
                def __init__(self, per_metric: _Optional[_Mapping[str, AlertingCondition.Spec.TimeSeries.Threshold]] = ..., combine: _Optional[_Union[AlertingCondition.Spec.TimeSeries.CombineThreshold.CombineOperator, str]] = ...) -> None: ...
            QUERY_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            COMBINE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            query: AlertingCondition.Spec.TimeSeries.Query
            threshold: AlertingCondition.Spec.TimeSeries.Threshold
            combine_threshold: AlertingCondition.Spec.TimeSeries.CombineThreshold
            duration: _duration_pb2.Duration
            def __init__(self, query: _Optional[_Union[AlertingCondition.Spec.TimeSeries.Query, _Mapping]] = ..., threshold: _Optional[_Union[AlertingCondition.Spec.TimeSeries.Threshold, _Mapping]] = ..., combine_threshold: _Optional[_Union[AlertingCondition.Spec.TimeSeries.CombineThreshold, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class Trigger(_message.Message):
            __slots__ = ("type",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                EACH: _ClassVar[AlertingCondition.Spec.Trigger.Type]
            EACH: AlertingCondition.Spec.Trigger.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: AlertingCondition.Spec.Trigger.Type
            def __init__(self, type: _Optional[_Union[AlertingCondition.Spec.Trigger.Type, str]] = ...) -> None: ...
        TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        time_series: AlertingCondition.Spec.TimeSeries
        trigger: AlertingCondition.Spec.Trigger
        def __init__(self, time_series: _Optional[_Union[AlertingCondition.Spec.TimeSeries, _Mapping]] = ..., trigger: _Optional[_Union[AlertingCondition.Spec.Trigger, _Mapping]] = ...) -> None: ...
    class State(_message.Message):
        __slots__ = ("firing_alerts_count",)
        FIRING_ALERTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        firing_alerts_count: int
        def __init__(self, firing_alerts_count: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    description: str
    spec: AlertingCondition.Spec
    state: AlertingCondition.State
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., spec: _Optional[_Union[AlertingCondition.Spec, _Mapping]] = ..., state: _Optional[_Union[AlertingCondition.State, _Mapping]] = ...) -> None: ...
