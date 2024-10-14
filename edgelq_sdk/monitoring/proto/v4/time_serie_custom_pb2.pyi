from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from edgelq_sdk.monitoring.proto.v4 import common_pb2 as _common_pb2
from edgelq_sdk.monitoring.proto.v4 import time_serie_pb2 as _time_serie_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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
    __slots__ = ("time_series", "execution_errors", "continuation_token", "total_point_counters")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_POINT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    continuation_token: str
    total_point_counters: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    def __init__(self, time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., continuation_token: _Optional[str] = ..., total_point_counters: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ...) -> None: ...

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

class StatsQuery(_message.Message):
    __slots__ = ("call_latencies", "executed_calls", "open_calls", "error_counts", "ingress_throughput", "egress_throughput", "store_usage", "resource_count", "logs_usage", "activity_logs_usage", "resource_change_logs_usage", "time_series_usage", "time_series_latencies")
    class CallLatencies(_message.Message):
        __slots__ = ("methods", "versions", "resources", "reducer", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.CallLatencies.Groups]
            VERSION: _ClassVar[StatsQuery.CallLatencies.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.CallLatencies.Groups]
        METHOD: StatsQuery.CallLatencies.Groups
        VERSION: StatsQuery.CallLatencies.Groups
        RESOURCE_TYPE: StatsQuery.CallLatencies.Groups
        class Reducer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUMMARY: _ClassVar[StatsQuery.CallLatencies.Reducer]
            MIN: _ClassVar[StatsQuery.CallLatencies.Reducer]
            MAX: _ClassVar[StatsQuery.CallLatencies.Reducer]
            P50: _ClassVar[StatsQuery.CallLatencies.Reducer]
            P95: _ClassVar[StatsQuery.CallLatencies.Reducer]
            P99: _ClassVar[StatsQuery.CallLatencies.Reducer]
            MEAN: _ClassVar[StatsQuery.CallLatencies.Reducer]
            STD_DEV: _ClassVar[StatsQuery.CallLatencies.Reducer]
        SUMMARY: StatsQuery.CallLatencies.Reducer
        MIN: StatsQuery.CallLatencies.Reducer
        MAX: StatsQuery.CallLatencies.Reducer
        P50: StatsQuery.CallLatencies.Reducer
        P95: StatsQuery.CallLatencies.Reducer
        P99: StatsQuery.CallLatencies.Reducer
        MEAN: StatsQuery.CallLatencies.Reducer
        STD_DEV: StatsQuery.CallLatencies.Reducer
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        REDUCER_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        reducer: StatsQuery.CallLatencies.Reducer
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.CallLatencies.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., reducer: _Optional[_Union[StatsQuery.CallLatencies.Reducer, str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.CallLatencies.Groups, str]]] = ...) -> None: ...
    class ExecutedCalls(_message.Message):
        __slots__ = ("methods", "versions", "resources", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.ExecutedCalls.Groups]
            VERSION: _ClassVar[StatsQuery.ExecutedCalls.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.ExecutedCalls.Groups]
        METHOD: StatsQuery.ExecutedCalls.Groups
        VERSION: StatsQuery.ExecutedCalls.Groups
        RESOURCE_TYPE: StatsQuery.ExecutedCalls.Groups
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.ExecutedCalls.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.ExecutedCalls.Groups, str]]] = ...) -> None: ...
    class OpenCalls(_message.Message):
        __slots__ = ("methods", "versions", "resources", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.OpenCalls.Groups]
            VERSION: _ClassVar[StatsQuery.OpenCalls.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.OpenCalls.Groups]
        METHOD: StatsQuery.OpenCalls.Groups
        VERSION: StatsQuery.OpenCalls.Groups
        RESOURCE_TYPE: StatsQuery.OpenCalls.Groups
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.OpenCalls.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.OpenCalls.Groups, str]]] = ...) -> None: ...
    class ErrorCounts(_message.Message):
        __slots__ = ("methods", "versions", "resources", "error_codes", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.ErrorCounts.Groups]
            VERSION: _ClassVar[StatsQuery.ErrorCounts.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.ErrorCounts.Groups]
            RESPONSE_CODE: _ClassVar[StatsQuery.ErrorCounts.Groups]
        METHOD: StatsQuery.ErrorCounts.Groups
        VERSION: StatsQuery.ErrorCounts.Groups
        RESOURCE_TYPE: StatsQuery.ErrorCounts.Groups
        RESPONSE_CODE: StatsQuery.ErrorCounts.Groups
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        error_codes: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.ErrorCounts.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., error_codes: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.ErrorCounts.Groups, str]]] = ...) -> None: ...
    class IngressThroughput(_message.Message):
        __slots__ = ("methods", "versions", "resources", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.IngressThroughput.Groups]
            VERSION: _ClassVar[StatsQuery.IngressThroughput.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.IngressThroughput.Groups]
        METHOD: StatsQuery.IngressThroughput.Groups
        VERSION: StatsQuery.IngressThroughput.Groups
        RESOURCE_TYPE: StatsQuery.IngressThroughput.Groups
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.IngressThroughput.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.IngressThroughput.Groups, str]]] = ...) -> None: ...
    class EgressThroughput(_message.Message):
        __slots__ = ("methods", "versions", "resources", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.EgressThroughput.Groups]
            VERSION: _ClassVar[StatsQuery.EgressThroughput.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.EgressThroughput.Groups]
        METHOD: StatsQuery.EgressThroughput.Groups
        VERSION: StatsQuery.EgressThroughput.Groups
        RESOURCE_TYPE: StatsQuery.EgressThroughput.Groups
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.EgressThroughput.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.EgressThroughput.Groups, str]]] = ...) -> None: ...
    class StoreOperations(_message.Message):
        __slots__ = ("methods", "versions", "resources", "operations", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.StoreOperations.Groups]
            VERSION: _ClassVar[StatsQuery.StoreOperations.Groups]
            RESOURCE_TYPE: _ClassVar[StatsQuery.StoreOperations.Groups]
            OPERATION: _ClassVar[StatsQuery.StoreOperations.Groups]
        METHOD: StatsQuery.StoreOperations.Groups
        VERSION: StatsQuery.StoreOperations.Groups
        RESOURCE_TYPE: StatsQuery.StoreOperations.Groups
        OPERATION: StatsQuery.StoreOperations.Groups
        class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[StatsQuery.StoreOperations.Operation]
            GET: _ClassVar[StatsQuery.StoreOperations.Operation]
            LIST: _ClassVar[StatsQuery.StoreOperations.Operation]
            SEARCH: _ClassVar[StatsQuery.StoreOperations.Operation]
            WATCH: _ClassVar[StatsQuery.StoreOperations.Operation]
            CREATE: _ClassVar[StatsQuery.StoreOperations.Operation]
            UPDATE: _ClassVar[StatsQuery.StoreOperations.Operation]
            DELETE: _ClassVar[StatsQuery.StoreOperations.Operation]
        UNDEFINED: StatsQuery.StoreOperations.Operation
        GET: StatsQuery.StoreOperations.Operation
        LIST: StatsQuery.StoreOperations.Operation
        SEARCH: StatsQuery.StoreOperations.Operation
        WATCH: StatsQuery.StoreOperations.Operation
        CREATE: StatsQuery.StoreOperations.Operation
        UPDATE: StatsQuery.StoreOperations.Operation
        DELETE: StatsQuery.StoreOperations.Operation
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        operations: _containers.RepeatedScalarFieldContainer[StatsQuery.StoreOperations.Operation]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.StoreOperations.Groups]
        def __init__(self, methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., operations: _Optional[_Iterable[_Union[StatsQuery.StoreOperations.Operation, str]]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.StoreOperations.Groups, str]]] = ...) -> None: ...
    class ResourceCount(_message.Message):
        __slots__ = ("resources",)
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, resources: _Optional[_Iterable[str]] = ...) -> None: ...
    class Logs(_message.Message):
        __slots__ = ("type", "log_types", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOG_TYPE: _ClassVar[StatsQuery.Logs.Groups]
        LOG_TYPE: StatsQuery.Logs.Groups
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[StatsQuery.Logs.Type]
            READS: _ClassVar[StatsQuery.Logs.Type]
            WRITES: _ClassVar[StatsQuery.Logs.Type]
        UNDEFINED: StatsQuery.Logs.Type
        READS: StatsQuery.Logs.Type
        WRITES: StatsQuery.Logs.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LOG_TYPES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        type: StatsQuery.Logs.Type
        log_types: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.Logs.Groups]
        def __init__(self, type: _Optional[_Union[StatsQuery.Logs.Type, str]] = ..., log_types: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.Logs.Groups, str]]] = ...) -> None: ...
    class ActivityLogs(_message.Message):
        __slots__ = ("type", "methods", "versions", "categories", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD: _ClassVar[StatsQuery.ActivityLogs.Groups]
            VERSION: _ClassVar[StatsQuery.ActivityLogs.Groups]
            CATEGORY: _ClassVar[StatsQuery.ActivityLogs.Groups]
        METHOD: StatsQuery.ActivityLogs.Groups
        VERSION: StatsQuery.ActivityLogs.Groups
        CATEGORY: StatsQuery.ActivityLogs.Groups
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[StatsQuery.ActivityLogs.Type]
            READS: _ClassVar[StatsQuery.ActivityLogs.Type]
            WRITES: _ClassVar[StatsQuery.ActivityLogs.Type]
        UNDEFINED: StatsQuery.ActivityLogs.Type
        READS: StatsQuery.ActivityLogs.Type
        WRITES: StatsQuery.ActivityLogs.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        METHODS_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        type: StatsQuery.ActivityLogs.Type
        methods: _containers.RepeatedScalarFieldContainer[str]
        versions: _containers.RepeatedScalarFieldContainer[str]
        categories: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.ActivityLogs.Groups]
        def __init__(self, type: _Optional[_Union[StatsQuery.ActivityLogs.Type, str]] = ..., methods: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.ActivityLogs.Groups, str]]] = ...) -> None: ...
    class ResourceChangeLogs(_message.Message):
        __slots__ = ("type", "resource_types", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESOURCE_TYPE: _ClassVar[StatsQuery.ResourceChangeLogs.Groups]
        RESOURCE_TYPE: StatsQuery.ResourceChangeLogs.Groups
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[StatsQuery.ResourceChangeLogs.Type]
            READS: _ClassVar[StatsQuery.ResourceChangeLogs.Type]
            WRITES: _ClassVar[StatsQuery.ResourceChangeLogs.Type]
        UNDEFINED: StatsQuery.ResourceChangeLogs.Type
        READS: StatsQuery.ResourceChangeLogs.Type
        WRITES: StatsQuery.ResourceChangeLogs.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        type: StatsQuery.ResourceChangeLogs.Type
        resource_types: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.ResourceChangeLogs.Groups]
        def __init__(self, type: _Optional[_Union[StatsQuery.ResourceChangeLogs.Type, str]] = ..., resource_types: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.ResourceChangeLogs.Groups, str]]] = ...) -> None: ...
    class TimeSeries(_message.Message):
        __slots__ = ("type", "resource_types", "metric_types", "group_by")
        class Groups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESOURCE_TYPE: _ClassVar[StatsQuery.TimeSeries.Groups]
            METRIC_TYPE: _ClassVar[StatsQuery.TimeSeries.Groups]
        RESOURCE_TYPE: StatsQuery.TimeSeries.Groups
        METRIC_TYPE: StatsQuery.TimeSeries.Groups
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[StatsQuery.TimeSeries.Type]
            READS: _ClassVar[StatsQuery.TimeSeries.Type]
            RAW_WRITES: _ClassVar[StatsQuery.TimeSeries.Type]
            ROLLUP_WRITES: _ClassVar[StatsQuery.TimeSeries.Type]
        UNDEFINED: StatsQuery.TimeSeries.Type
        READS: StatsQuery.TimeSeries.Type
        RAW_WRITES: StatsQuery.TimeSeries.Type
        ROLLUP_WRITES: StatsQuery.TimeSeries.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
        type: StatsQuery.TimeSeries.Type
        resource_types: _containers.RepeatedScalarFieldContainer[str]
        metric_types: _containers.RepeatedScalarFieldContainer[str]
        group_by: _containers.RepeatedScalarFieldContainer[StatsQuery.TimeSeries.Groups]
        def __init__(self, type: _Optional[_Union[StatsQuery.TimeSeries.Type, str]] = ..., resource_types: _Optional[_Iterable[str]] = ..., metric_types: _Optional[_Iterable[str]] = ..., group_by: _Optional[_Iterable[_Union[StatsQuery.TimeSeries.Groups, str]]] = ...) -> None: ...
    class TimeSeriesLatencies(_message.Message):
        __slots__ = ("of_ap", "reducer")
        class Reducer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUMMARY: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            MIN: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            MAX: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            P50: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            P95: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            P99: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            MEAN: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
            STD_DEV: _ClassVar[StatsQuery.TimeSeriesLatencies.Reducer]
        SUMMARY: StatsQuery.TimeSeriesLatencies.Reducer
        MIN: StatsQuery.TimeSeriesLatencies.Reducer
        MAX: StatsQuery.TimeSeriesLatencies.Reducer
        P50: StatsQuery.TimeSeriesLatencies.Reducer
        P95: StatsQuery.TimeSeriesLatencies.Reducer
        P99: StatsQuery.TimeSeriesLatencies.Reducer
        MEAN: StatsQuery.TimeSeriesLatencies.Reducer
        STD_DEV: StatsQuery.TimeSeriesLatencies.Reducer
        OF_AP_FIELD_NUMBER: _ClassVar[int]
        REDUCER_FIELD_NUMBER: _ClassVar[int]
        of_ap: _duration_pb2.Duration
        reducer: StatsQuery.TimeSeriesLatencies.Reducer
        def __init__(self, of_ap: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reducer: _Optional[_Union[StatsQuery.TimeSeriesLatencies.Reducer, str]] = ...) -> None: ...
    CALL_LATENCIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CALLS_FIELD_NUMBER: _ClassVar[int]
    OPEN_CALLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNTS_FIELD_NUMBER: _ClassVar[int]
    INGRESS_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    EGRESS_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    STORE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOGS_USAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_LOGS_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CHANGE_LOGS_USAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_USAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_LATENCIES_FIELD_NUMBER: _ClassVar[int]
    call_latencies: StatsQuery.CallLatencies
    executed_calls: StatsQuery.ExecutedCalls
    open_calls: StatsQuery.OpenCalls
    error_counts: StatsQuery.ErrorCounts
    ingress_throughput: StatsQuery.IngressThroughput
    egress_throughput: StatsQuery.EgressThroughput
    store_usage: StatsQuery.StoreOperations
    resource_count: StatsQuery.ResourceCount
    logs_usage: StatsQuery.Logs
    activity_logs_usage: StatsQuery.ActivityLogs
    resource_change_logs_usage: StatsQuery.ResourceChangeLogs
    time_series_usage: StatsQuery.TimeSeries
    time_series_latencies: StatsQuery.TimeSeriesLatencies
    def __init__(self, call_latencies: _Optional[_Union[StatsQuery.CallLatencies, _Mapping]] = ..., executed_calls: _Optional[_Union[StatsQuery.ExecutedCalls, _Mapping]] = ..., open_calls: _Optional[_Union[StatsQuery.OpenCalls, _Mapping]] = ..., error_counts: _Optional[_Union[StatsQuery.ErrorCounts, _Mapping]] = ..., ingress_throughput: _Optional[_Union[StatsQuery.IngressThroughput, _Mapping]] = ..., egress_throughput: _Optional[_Union[StatsQuery.EgressThroughput, _Mapping]] = ..., store_usage: _Optional[_Union[StatsQuery.StoreOperations, _Mapping]] = ..., resource_count: _Optional[_Union[StatsQuery.ResourceCount, _Mapping]] = ..., logs_usage: _Optional[_Union[StatsQuery.Logs, _Mapping]] = ..., activity_logs_usage: _Optional[_Union[StatsQuery.ActivityLogs, _Mapping]] = ..., resource_change_logs_usage: _Optional[_Union[StatsQuery.ResourceChangeLogs, _Mapping]] = ..., time_series_usage: _Optional[_Union[StatsQuery.TimeSeries, _Mapping]] = ..., time_series_latencies: _Optional[_Union[StatsQuery.TimeSeriesLatencies, _Mapping]] = ...) -> None: ...

class QueryProjectTimeSeriesStatsRequest(_message.Message):
    __slots__ = ("project", "service", "region_id", "ap", "interval", "page_size", "page_token", "query")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    AP_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    project: str
    service: str
    region_id: str
    ap: _duration_pb2.Duration
    interval: _common_pb2.TimeInterval
    page_size: int
    page_token: str
    query: StatsQuery
    def __init__(self, project: _Optional[str] = ..., service: _Optional[str] = ..., region_id: _Optional[str] = ..., ap: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., query: _Optional[_Union[StatsQuery, _Mapping]] = ...) -> None: ...

class QueryProjectTimeSeriesStatsResponse(_message.Message):
    __slots__ = ("time_series", "next_page_token", "execution_errors")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class QueryServiceTimeSeriesStatsRequest(_message.Message):
    __slots__ = ("service", "region_id", "ap", "interval", "page_size", "page_token", "user_project_ids", "query")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    AP_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    service: str
    region_id: str
    ap: _duration_pb2.Duration
    interval: _common_pb2.TimeInterval
    page_size: int
    page_token: str
    user_project_ids: _containers.RepeatedScalarFieldContainer[str]
    query: StatsQuery
    def __init__(self, service: _Optional[str] = ..., region_id: _Optional[str] = ..., ap: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., user_project_ids: _Optional[_Iterable[str]] = ..., query: _Optional[_Union[StatsQuery, _Mapping]] = ...) -> None: ...

class QueryServiceTimeSeriesStatsResponse(_message.Message):
    __slots__ = ("time_series", "next_page_token", "execution_errors")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class WatchTimeSeriesRequest(_message.Message):
    __slots__ = ("parent", "filter", "aggregation", "snapshot_interval_to_fetch")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INTERVAL_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    aggregation: _common_pb2.Aggregation
    snapshot_interval_to_fetch: _duration_pb2.Duration
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]] = ..., snapshot_interval_to_fetch: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class WatchTimeSeriesResponse(_message.Message):
    __slots__ = ("time_series",)
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_time_serie_pb2.TimeSerie]
    def __init__(self, time_series: _Optional[_Iterable[_Union[_time_serie_pb2.TimeSerie, _Mapping]]] = ...) -> None: ...
