from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeSeriesView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FULL: _ClassVar[TimeSeriesView]
    HEADERS: _ClassVar[TimeSeriesView]
FULL: TimeSeriesView
HEADERS: TimeSeriesView

class LabelDescriptor(_message.Message):
    __slots__ = ("key", "value_type", "description", "default_value", "disabled")
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRING: _ClassVar[LabelDescriptor.ValueType]
        BOOL: _ClassVar[LabelDescriptor.ValueType]
        INT64: _ClassVar[LabelDescriptor.ValueType]
    STRING: LabelDescriptor.ValueType
    BOOL: LabelDescriptor.ValueType
    INT64: LabelDescriptor.ValueType
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    key: str
    value_type: LabelDescriptor.ValueType
    description: str
    default_value: str
    disabled: bool
    def __init__(self, key: _Optional[str] = ..., value_type: _Optional[_Union[LabelDescriptor.ValueType, str]] = ..., description: _Optional[str] = ..., default_value: _Optional[str] = ..., disabled: bool = ...) -> None: ...

class LabelKeySet(_message.Message):
    __slots__ = ("label_keys", "write_only")
    LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    WRITE_ONLY_FIELD_NUMBER: _ClassVar[int]
    label_keys: _containers.RepeatedScalarFieldContainer[str]
    write_only: bool
    def __init__(self, label_keys: _Optional[_Iterable[str]] = ..., write_only: bool = ...) -> None: ...

class Distribution(_message.Message):
    __slots__ = ("count", "mean", "sum_of_squared_deviation", "range", "bucket_options", "bucket_counts")
    class Range(_message.Message):
        __slots__ = ("min", "max")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: float
        max: float
        def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...
    class BucketOptions(_message.Message):
        __slots__ = ("linear_buckets", "exponential_buckets", "explicit_buckets", "dynamic_buckets")
        class Linear(_message.Message):
            __slots__ = ("num_finite_buckets", "width", "offset")
            NUM_FINITE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            num_finite_buckets: int
            width: float
            offset: float
            def __init__(self, num_finite_buckets: _Optional[int] = ..., width: _Optional[float] = ..., offset: _Optional[float] = ...) -> None: ...
        class Exponential(_message.Message):
            __slots__ = ("num_finite_buckets", "growth_factor", "scale")
            NUM_FINITE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
            GROWTH_FACTOR_FIELD_NUMBER: _ClassVar[int]
            SCALE_FIELD_NUMBER: _ClassVar[int]
            num_finite_buckets: int
            growth_factor: float
            scale: float
            def __init__(self, num_finite_buckets: _Optional[int] = ..., growth_factor: _Optional[float] = ..., scale: _Optional[float] = ...) -> None: ...
        class Explicit(_message.Message):
            __slots__ = ("bounds",)
            BOUNDS_FIELD_NUMBER: _ClassVar[int]
            bounds: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, bounds: _Optional[_Iterable[float]] = ...) -> None: ...
        class Dynamic(_message.Message):
            __slots__ = ("compression", "means")
            COMPRESSION_FIELD_NUMBER: _ClassVar[int]
            MEANS_FIELD_NUMBER: _ClassVar[int]
            compression: float
            means: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, compression: _Optional[float] = ..., means: _Optional[_Iterable[float]] = ...) -> None: ...
        LINEAR_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        EXPONENTIAL_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        EXPLICIT_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        linear_buckets: Distribution.BucketOptions.Linear
        exponential_buckets: Distribution.BucketOptions.Exponential
        explicit_buckets: Distribution.BucketOptions.Explicit
        dynamic_buckets: Distribution.BucketOptions.Dynamic
        def __init__(self, linear_buckets: _Optional[_Union[Distribution.BucketOptions.Linear, _Mapping]] = ..., exponential_buckets: _Optional[_Union[Distribution.BucketOptions.Exponential, _Mapping]] = ..., explicit_buckets: _Optional[_Union[Distribution.BucketOptions.Explicit, _Mapping]] = ..., dynamic_buckets: _Optional[_Union[Distribution.BucketOptions.Dynamic, _Mapping]] = ...) -> None: ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    SUM_OF_SQUARED_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_COUNTS_FIELD_NUMBER: _ClassVar[int]
    count: int
    mean: float
    sum_of_squared_deviation: float
    range: Distribution.Range
    bucket_options: Distribution.BucketOptions
    bucket_counts: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, count: _Optional[int] = ..., mean: _Optional[float] = ..., sum_of_squared_deviation: _Optional[float] = ..., range: _Optional[_Union[Distribution.Range, _Mapping]] = ..., bucket_options: _Optional[_Union[Distribution.BucketOptions, _Mapping]] = ..., bucket_counts: _Optional[_Iterable[int]] = ...) -> None: ...

class TypedValue(_message.Message):
    __slots__ = ("bool_value", "int64_value", "double_value", "string_value", "distribution_value")
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    int64_value: int
    double_value: float
    string_value: str
    distribution_value: Distribution
    def __init__(self, bool_value: bool = ..., int64_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., distribution_value: _Optional[_Union[Distribution, _Mapping]] = ...) -> None: ...

class TimeInterval(_message.Message):
    __slots__ = ("end_time", "start_time")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Aggregation(_message.Message):
    __slots__ = ("alignment_period", "per_series_aligner", "cross_series_reducer", "group_by_fields")
    class Aligner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALIGN_NONE: _ClassVar[Aggregation.Aligner]
        ALIGN_DELTA: _ClassVar[Aggregation.Aligner]
        ALIGN_RATE: _ClassVar[Aggregation.Aligner]
        ALIGN_INTERPOLATE: _ClassVar[Aggregation.Aligner]
        ALIGN_NEXT_OLDER: _ClassVar[Aggregation.Aligner]
        ALIGN_MIN: _ClassVar[Aggregation.Aligner]
        ALIGN_MAX: _ClassVar[Aggregation.Aligner]
        ALIGN_MEAN: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT: _ClassVar[Aggregation.Aligner]
        ALIGN_SUM: _ClassVar[Aggregation.Aligner]
        ALIGN_STDDEV: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT_TRUE: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT_FALSE: _ClassVar[Aggregation.Aligner]
        ALIGN_FRACTION_TRUE: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_99: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_95: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_50: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_05: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENT_CHANGE: _ClassVar[Aggregation.Aligner]
        ALIGN_SUMMARY: _ClassVar[Aggregation.Aligner]
        ALIGN_TDIGEST_SUMMARY: _ClassVar[Aggregation.Aligner]
    ALIGN_NONE: Aggregation.Aligner
    ALIGN_DELTA: Aggregation.Aligner
    ALIGN_RATE: Aggregation.Aligner
    ALIGN_INTERPOLATE: Aggregation.Aligner
    ALIGN_NEXT_OLDER: Aggregation.Aligner
    ALIGN_MIN: Aggregation.Aligner
    ALIGN_MAX: Aggregation.Aligner
    ALIGN_MEAN: Aggregation.Aligner
    ALIGN_COUNT: Aggregation.Aligner
    ALIGN_SUM: Aggregation.Aligner
    ALIGN_STDDEV: Aggregation.Aligner
    ALIGN_COUNT_TRUE: Aggregation.Aligner
    ALIGN_COUNT_FALSE: Aggregation.Aligner
    ALIGN_FRACTION_TRUE: Aggregation.Aligner
    ALIGN_PERCENTILE_99: Aggregation.Aligner
    ALIGN_PERCENTILE_95: Aggregation.Aligner
    ALIGN_PERCENTILE_50: Aggregation.Aligner
    ALIGN_PERCENTILE_05: Aggregation.Aligner
    ALIGN_PERCENT_CHANGE: Aggregation.Aligner
    ALIGN_SUMMARY: Aggregation.Aligner
    ALIGN_TDIGEST_SUMMARY: Aggregation.Aligner
    class Reducer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDUCE_NONE: _ClassVar[Aggregation.Reducer]
        REDUCE_MEAN: _ClassVar[Aggregation.Reducer]
        REDUCE_MIN: _ClassVar[Aggregation.Reducer]
        REDUCE_MAX: _ClassVar[Aggregation.Reducer]
        REDUCE_SUM: _ClassVar[Aggregation.Reducer]
        REDUCE_STDDEV: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT_TRUE: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT_FALSE: _ClassVar[Aggregation.Reducer]
        REDUCE_FRACTION_TRUE: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_99: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_95: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_50: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_05: _ClassVar[Aggregation.Reducer]
        REDUCE_SUMMARY: _ClassVar[Aggregation.Reducer]
    REDUCE_NONE: Aggregation.Reducer
    REDUCE_MEAN: Aggregation.Reducer
    REDUCE_MIN: Aggregation.Reducer
    REDUCE_MAX: Aggregation.Reducer
    REDUCE_SUM: Aggregation.Reducer
    REDUCE_STDDEV: Aggregation.Reducer
    REDUCE_COUNT: Aggregation.Reducer
    REDUCE_COUNT_TRUE: Aggregation.Reducer
    REDUCE_COUNT_FALSE: Aggregation.Reducer
    REDUCE_FRACTION_TRUE: Aggregation.Reducer
    REDUCE_PERCENTILE_99: Aggregation.Reducer
    REDUCE_PERCENTILE_95: Aggregation.Reducer
    REDUCE_PERCENTILE_50: Aggregation.Reducer
    REDUCE_PERCENTILE_05: Aggregation.Reducer
    REDUCE_SUMMARY: Aggregation.Reducer
    ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PER_SERIES_ALIGNER_FIELD_NUMBER: _ClassVar[int]
    CROSS_SERIES_REDUCER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    alignment_period: _duration_pb2.Duration
    per_series_aligner: Aggregation.Aligner
    cross_series_reducer: Aggregation.Reducer
    group_by_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., per_series_aligner: _Optional[_Union[Aggregation.Aligner, str]] = ..., cross_series_reducer: _Optional[_Union[Aggregation.Reducer, str]] = ..., group_by_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class Pagination(_message.Message):
    __slots__ = ("view", "function", "alignment_period", "limit", "offset")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    view: str
    function: str
    alignment_period: _duration_pb2.Duration
    limit: int
    offset: int
    def __init__(self, view: _Optional[str] = ..., function: _Optional[str] = ..., alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("type", "labels", "reduced_labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REDUCED_LABELS_FIELD_NUMBER: _ClassVar[int]
    type: str
    labels: _containers.ScalarMap[str, str]
    reduced_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., reduced_labels: _Optional[_Iterable[str]] = ...) -> None: ...

class MonitoredResource(_message.Message):
    __slots__ = ("type", "labels", "reduced_labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REDUCED_LABELS_FIELD_NUMBER: _ClassVar[int]
    type: str
    labels: _containers.ScalarMap[str, str]
    reduced_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., reduced_labels: _Optional[_Iterable[str]] = ...) -> None: ...

class Strings(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class MonitoredResourceSelector(_message.Message):
    __slots__ = ("types", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Strings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Strings, _Mapping]] = ...) -> None: ...
    TYPES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.MessageMap[str, Strings]
    def __init__(self, types: _Optional[_Iterable[str]] = ..., labels: _Optional[_Mapping[str, Strings]] = ...) -> None: ...

class MetricSelector(_message.Message):
    __slots__ = ("types", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Strings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Strings, _Mapping]] = ...) -> None: ...
    TYPES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.MessageMap[str, Strings]
    def __init__(self, types: _Optional[_Iterable[str]] = ..., labels: _Optional[_Mapping[str, Strings]] = ...) -> None: ...

class TimeSeriesSelector(_message.Message):
    __slots__ = ("metric", "resource")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    metric: MetricSelector
    resource: MonitoredResourceSelector
    def __init__(self, metric: _Optional[_Union[MetricSelector, _Mapping]] = ..., resource: _Optional[_Union[MonitoredResourceSelector, _Mapping]] = ...) -> None: ...
