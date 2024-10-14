from edgelq_sdk.common.api import launch_stage_pb2 as _launch_stage_pb2
from edgelq_sdk.monitoring.proto.v4 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDescriptor(_message.Message):
    __slots__ = ("name", "metadata", "type", "resource_types", "labels", "metric_kind", "value_type", "unit", "description", "display_name", "metric_descriptor_metadata", "distribution_bucket_options", "promoted_label_key_sets", "index_spec", "indices", "storage_config", "binary_indices")
    class MetricKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_KIND_UNSPECIFIED: _ClassVar[MetricDescriptor.MetricKind]
        GAUGE: _ClassVar[MetricDescriptor.MetricKind]
        DELTA: _ClassVar[MetricDescriptor.MetricKind]
        CUMULATIVE: _ClassVar[MetricDescriptor.MetricKind]
    METRIC_KIND_UNSPECIFIED: MetricDescriptor.MetricKind
    GAUGE: MetricDescriptor.MetricKind
    DELTA: MetricDescriptor.MetricKind
    CUMULATIVE: MetricDescriptor.MetricKind
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[MetricDescriptor.ValueType]
        BOOL: _ClassVar[MetricDescriptor.ValueType]
        INT64: _ClassVar[MetricDescriptor.ValueType]
        DOUBLE: _ClassVar[MetricDescriptor.ValueType]
        DISTRIBUTION: _ClassVar[MetricDescriptor.ValueType]
    VALUE_TYPE_UNSPECIFIED: MetricDescriptor.ValueType
    BOOL: MetricDescriptor.ValueType
    INT64: MetricDescriptor.ValueType
    DOUBLE: MetricDescriptor.ValueType
    DISTRIBUTION: MetricDescriptor.ValueType
    class MetricDescriptorMetadata(_message.Message):
        __slots__ = ("launch_stage",)
        LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
        launch_stage: _launch_stage_pb2.LaunchStage
        def __init__(self, launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]] = ...) -> None: ...
    class IndexSpec(_message.Message):
        __slots__ = ("per_resource",)
        class Index(_message.Message):
            __slots__ = ("promoted_labels",)
            PROMOTED_LABELS_FIELD_NUMBER: _ClassVar[int]
            promoted_labels: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, promoted_labels: _Optional[_Iterable[str]] = ...) -> None: ...
        class PerMonitoredResource(_message.Message):
            __slots__ = ("resource", "indices")
            RESOURCE_FIELD_NUMBER: _ClassVar[int]
            INDICES_FIELD_NUMBER: _ClassVar[int]
            resource: str
            indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.IndexSpec.Index]
            def __init__(self, resource: _Optional[str] = ..., indices: _Optional[_Iterable[_Union[MetricDescriptor.IndexSpec.Index, _Mapping]]] = ...) -> None: ...
        PER_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        per_resource: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.IndexSpec.PerMonitoredResource]
        def __init__(self, per_resource: _Optional[_Iterable[_Union[MetricDescriptor.IndexSpec.PerMonitoredResource, _Mapping]]] = ...) -> None: ...
    class Indices(_message.Message):
        __slots__ = ("built_in", "user_defined", "legacy_migrated")
        class CloseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[MetricDescriptor.Indices.CloseStatus]
            SUSPENDED: _ClassVar[MetricDescriptor.Indices.CloseStatus]
            CLOSED: _ClassVar[MetricDescriptor.Indices.CloseStatus]
        UNDEFINED: MetricDescriptor.Indices.CloseStatus
        SUSPENDED: MetricDescriptor.Indices.CloseStatus
        CLOSED: MetricDescriptor.Indices.CloseStatus
        class LabelsGroup(_message.Message):
            __slots__ = ("name", "metric_keys", "resource_keys", "closing_status")
            NAME_FIELD_NUMBER: _ClassVar[int]
            METRIC_KEYS_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_KEYS_FIELD_NUMBER: _ClassVar[int]
            CLOSING_STATUS_FIELD_NUMBER: _ClassVar[int]
            name: str
            metric_keys: _containers.RepeatedScalarFieldContainer[str]
            resource_keys: _containers.RepeatedScalarFieldContainer[str]
            closing_status: MetricDescriptor.Indices.CloseStatus
            def __init__(self, name: _Optional[str] = ..., metric_keys: _Optional[_Iterable[str]] = ..., resource_keys: _Optional[_Iterable[str]] = ..., closing_status: _Optional[_Union[MetricDescriptor.Indices.CloseStatus, str]] = ...) -> None: ...
        class PaginationView(_message.Message):
            __slots__ = ("name", "filterable_metric_keys", "filterable_resource_keys", "paginated_metric_keys", "paginated_resource_keys", "closing_status")
            NAME_FIELD_NUMBER: _ClassVar[int]
            FILTERABLE_METRIC_KEYS_FIELD_NUMBER: _ClassVar[int]
            FILTERABLE_RESOURCE_KEYS_FIELD_NUMBER: _ClassVar[int]
            PAGINATED_METRIC_KEYS_FIELD_NUMBER: _ClassVar[int]
            PAGINATED_RESOURCE_KEYS_FIELD_NUMBER: _ClassVar[int]
            CLOSING_STATUS_FIELD_NUMBER: _ClassVar[int]
            name: str
            filterable_metric_keys: _containers.RepeatedScalarFieldContainer[str]
            filterable_resource_keys: _containers.RepeatedScalarFieldContainer[str]
            paginated_metric_keys: _containers.RepeatedScalarFieldContainer[str]
            paginated_resource_keys: _containers.RepeatedScalarFieldContainer[str]
            closing_status: MetricDescriptor.Indices.CloseStatus
            def __init__(self, name: _Optional[str] = ..., filterable_metric_keys: _Optional[_Iterable[str]] = ..., filterable_resource_keys: _Optional[_Iterable[str]] = ..., paginated_metric_keys: _Optional[_Iterable[str]] = ..., paginated_resource_keys: _Optional[_Iterable[str]] = ..., closing_status: _Optional[_Union[MetricDescriptor.Indices.CloseStatus, str]] = ...) -> None: ...
        class AggregationsGroup(_message.Message):
            __slots__ = ("name", "per_series_aligners", "cross_series_reducers", "closing_status", "storage_aligners")
            NAME_FIELD_NUMBER: _ClassVar[int]
            PER_SERIES_ALIGNERS_FIELD_NUMBER: _ClassVar[int]
            CROSS_SERIES_REDUCERS_FIELD_NUMBER: _ClassVar[int]
            CLOSING_STATUS_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ALIGNERS_FIELD_NUMBER: _ClassVar[int]
            name: str
            per_series_aligners: _containers.RepeatedScalarFieldContainer[_common_pb2.Aggregation.Aligner]
            cross_series_reducers: _containers.RepeatedScalarFieldContainer[_common_pb2.Aggregation.Reducer]
            closing_status: MetricDescriptor.Indices.CloseStatus
            storage_aligners: _containers.RepeatedScalarFieldContainer[_common_pb2.Aggregation.Aligner]
            def __init__(self, name: _Optional[str] = ..., per_series_aligners: _Optional[_Iterable[_Union[_common_pb2.Aggregation.Aligner, str]]] = ..., cross_series_reducers: _Optional[_Iterable[_Union[_common_pb2.Aggregation.Reducer, str]]] = ..., closing_status: _Optional[_Union[MetricDescriptor.Indices.CloseStatus, str]] = ..., storage_aligners: _Optional[_Iterable[_Union[_common_pb2.Aggregation.Aligner, str]]] = ...) -> None: ...
        class SortingFunction(_message.Message):
            __slots__ = ("name", "aligner", "reducer", "closing_status", "sorting")
            class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNDEFINED: _ClassVar[MetricDescriptor.Indices.SortingFunction.Direction]
                ASCENDING: _ClassVar[MetricDescriptor.Indices.SortingFunction.Direction]
                DESCENDING: _ClassVar[MetricDescriptor.Indices.SortingFunction.Direction]
            UNDEFINED: MetricDescriptor.Indices.SortingFunction.Direction
            ASCENDING: MetricDescriptor.Indices.SortingFunction.Direction
            DESCENDING: MetricDescriptor.Indices.SortingFunction.Direction
            NAME_FIELD_NUMBER: _ClassVar[int]
            ALIGNER_FIELD_NUMBER: _ClassVar[int]
            REDUCER_FIELD_NUMBER: _ClassVar[int]
            CLOSING_STATUS_FIELD_NUMBER: _ClassVar[int]
            SORTING_FIELD_NUMBER: _ClassVar[int]
            name: str
            aligner: _common_pb2.Aggregation.Aligner
            reducer: _common_pb2.Aggregation.Reducer
            closing_status: MetricDescriptor.Indices.CloseStatus
            sorting: MetricDescriptor.Indices.SortingFunction.Direction
            def __init__(self, name: _Optional[str] = ..., aligner: _Optional[_Union[_common_pb2.Aggregation.Aligner, str]] = ..., reducer: _Optional[_Union[_common_pb2.Aggregation.Reducer, str]] = ..., closing_status: _Optional[_Union[MetricDescriptor.Indices.CloseStatus, str]] = ..., sorting: _Optional[_Union[MetricDescriptor.Indices.SortingFunction.Direction, str]] = ...) -> None: ...
        class PreAggregatedIndices(_message.Message):
            __slots__ = ("name", "resource_types", "partition_label_sets", "filter_and_group_label_sets", "supported_aggregations")
            NAME_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
            PARTITION_LABEL_SETS_FIELD_NUMBER: _ClassVar[int]
            FILTER_AND_GROUP_LABEL_SETS_FIELD_NUMBER: _ClassVar[int]
            SUPPORTED_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
            name: str
            resource_types: _containers.RepeatedScalarFieldContainer[str]
            partition_label_sets: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.LabelsGroup]
            filter_and_group_label_sets: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.LabelsGroup]
            supported_aggregations: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.AggregationsGroup]
            def __init__(self, name: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., partition_label_sets: _Optional[_Iterable[_Union[MetricDescriptor.Indices.LabelsGroup, _Mapping]]] = ..., filter_and_group_label_sets: _Optional[_Iterable[_Union[MetricDescriptor.Indices.LabelsGroup, _Mapping]]] = ..., supported_aggregations: _Optional[_Iterable[_Union[MetricDescriptor.Indices.AggregationsGroup, _Mapping]]] = ...) -> None: ...
        class NonAggregatedIndices(_message.Message):
            __slots__ = ("name", "resource_types", "partition_label_sets")
            NAME_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
            PARTITION_LABEL_SETS_FIELD_NUMBER: _ClassVar[int]
            name: str
            resource_types: _containers.RepeatedScalarFieldContainer[str]
            partition_label_sets: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.LabelsGroup]
            def __init__(self, name: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., partition_label_sets: _Optional[_Iterable[_Union[MetricDescriptor.Indices.LabelsGroup, _Mapping]]] = ...) -> None: ...
        class PaginationIndices(_message.Message):
            __slots__ = ("name", "resource_types", "partition_label_sets", "views", "functions")
            NAME_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
            PARTITION_LABEL_SETS_FIELD_NUMBER: _ClassVar[int]
            VIEWS_FIELD_NUMBER: _ClassVar[int]
            FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
            name: str
            resource_types: _containers.RepeatedScalarFieldContainer[str]
            partition_label_sets: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.LabelsGroup]
            views: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.PaginationView]
            functions: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.SortingFunction]
            def __init__(self, name: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., partition_label_sets: _Optional[_Iterable[_Union[MetricDescriptor.Indices.LabelsGroup, _Mapping]]] = ..., views: _Optional[_Iterable[_Union[MetricDescriptor.Indices.PaginationView, _Mapping]]] = ..., functions: _Optional[_Iterable[_Union[MetricDescriptor.Indices.SortingFunction, _Mapping]]] = ...) -> None: ...
        class IndexGroups(_message.Message):
            __slots__ = ("pre_aggregated_indices", "non_aggregated_indices", "pagination_indices")
            PRE_AGGREGATED_INDICES_FIELD_NUMBER: _ClassVar[int]
            NON_AGGREGATED_INDICES_FIELD_NUMBER: _ClassVar[int]
            PAGINATION_INDICES_FIELD_NUMBER: _ClassVar[int]
            pre_aggregated_indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.PreAggregatedIndices]
            non_aggregated_indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.NonAggregatedIndices]
            pagination_indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.PaginationIndices]
            def __init__(self, pre_aggregated_indices: _Optional[_Iterable[_Union[MetricDescriptor.Indices.PreAggregatedIndices, _Mapping]]] = ..., non_aggregated_indices: _Optional[_Iterable[_Union[MetricDescriptor.Indices.NonAggregatedIndices, _Mapping]]] = ..., pagination_indices: _Optional[_Iterable[_Union[MetricDescriptor.Indices.PaginationIndices, _Mapping]]] = ...) -> None: ...
        BUILT_IN_FIELD_NUMBER: _ClassVar[int]
        USER_DEFINED_FIELD_NUMBER: _ClassVar[int]
        LEGACY_MIGRATED_FIELD_NUMBER: _ClassVar[int]
        built_in: MetricDescriptor.Indices.IndexGroups
        user_defined: MetricDescriptor.Indices.IndexGroups
        legacy_migrated: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.Indices.NonAggregatedIndices]
        def __init__(self, built_in: _Optional[_Union[MetricDescriptor.Indices.IndexGroups, _Mapping]] = ..., user_defined: _Optional[_Union[MetricDescriptor.Indices.IndexGroups, _Mapping]] = ..., legacy_migrated: _Optional[_Iterable[_Union[MetricDescriptor.Indices.NonAggregatedIndices, _Mapping]]] = ...) -> None: ...
    class StorageConfig(_message.Message):
        __slots__ = ("store_raw_points",)
        STORE_RAW_POINTS_FIELD_NUMBER: _ClassVar[int]
        store_raw_points: bool
        def __init__(self, store_raw_points: bool = ...) -> None: ...
    class BinaryIndices(_message.Message):
        __slots__ = ("by_resources",)
        class PreAggregatedIndex(_message.Message):
            __slots__ = ("key_data", "writing_aligners", "closed_aligners")
            KEY_DATA_FIELD_NUMBER: _ClassVar[int]
            WRITING_ALIGNERS_FIELD_NUMBER: _ClassVar[int]
            CLOSED_ALIGNERS_FIELD_NUMBER: _ClassVar[int]
            key_data: bytes
            writing_aligners: _containers.RepeatedScalarFieldContainer[bytes]
            closed_aligners: _containers.RepeatedScalarFieldContainer[bytes]
            def __init__(self, key_data: _Optional[bytes] = ..., writing_aligners: _Optional[_Iterable[bytes]] = ..., closed_aligners: _Optional[_Iterable[bytes]] = ...) -> None: ...
        class PaginatingIndex(_message.Message):
            __slots__ = ("key_data", "writing_functions", "closed_functions")
            KEY_DATA_FIELD_NUMBER: _ClassVar[int]
            WRITING_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
            CLOSED_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
            key_data: bytes
            writing_functions: _containers.RepeatedScalarFieldContainer[bytes]
            closed_functions: _containers.RepeatedScalarFieldContainer[bytes]
            def __init__(self, key_data: _Optional[bytes] = ..., writing_functions: _Optional[_Iterable[bytes]] = ..., closed_functions: _Optional[_Iterable[bytes]] = ...) -> None: ...
        class ByResourceType(_message.Message):
            __slots__ = ("resource_type", "aggs_encoder", "pre_aggregated_indices", "paginating_indices", "non_aggregated_indices", "name_parts")
            RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            AGGS_ENCODER_FIELD_NUMBER: _ClassVar[int]
            PRE_AGGREGATED_INDICES_FIELD_NUMBER: _ClassVar[int]
            PAGINATING_INDICES_FIELD_NUMBER: _ClassVar[int]
            NON_AGGREGATED_INDICES_FIELD_NUMBER: _ClassVar[int]
            NAME_PARTS_FIELD_NUMBER: _ClassVar[int]
            resource_type: str
            aggs_encoder: _containers.RepeatedScalarFieldContainer[bytes]
            pre_aggregated_indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.BinaryIndices.PreAggregatedIndex]
            paginating_indices: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.BinaryIndices.PaginatingIndex]
            non_aggregated_indices: _containers.RepeatedScalarFieldContainer[bytes]
            name_parts: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, resource_type: _Optional[str] = ..., aggs_encoder: _Optional[_Iterable[bytes]] = ..., pre_aggregated_indices: _Optional[_Iterable[_Union[MetricDescriptor.BinaryIndices.PreAggregatedIndex, _Mapping]]] = ..., paginating_indices: _Optional[_Iterable[_Union[MetricDescriptor.BinaryIndices.PaginatingIndex, _Mapping]]] = ..., non_aggregated_indices: _Optional[_Iterable[bytes]] = ..., name_parts: _Optional[_Iterable[str]] = ...) -> None: ...
        BY_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        by_resources: _containers.RepeatedCompositeFieldContainer[MetricDescriptor.BinaryIndices.ByResourceType]
        def __init__(self, by_resources: _Optional[_Iterable[_Union[MetricDescriptor.BinaryIndices.ByResourceType, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTOR_METADATA_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_BUCKET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_LABEL_KEY_SETS_FIELD_NUMBER: _ClassVar[int]
    INDEX_SPEC_FIELD_NUMBER: _ClassVar[int]
    INDICES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BINARY_INDICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    type: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.LabelDescriptor]
    metric_kind: MetricDescriptor.MetricKind
    value_type: MetricDescriptor.ValueType
    unit: str
    description: str
    display_name: str
    metric_descriptor_metadata: MetricDescriptor.MetricDescriptorMetadata
    distribution_bucket_options: _common_pb2.Distribution.BucketOptions
    promoted_label_key_sets: _containers.RepeatedCompositeFieldContainer[_common_pb2.LabelKeySet]
    index_spec: MetricDescriptor.IndexSpec
    indices: MetricDescriptor.Indices
    storage_config: MetricDescriptor.StorageConfig
    binary_indices: MetricDescriptor.BinaryIndices
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., type: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.LabelDescriptor, _Mapping]]] = ..., metric_kind: _Optional[_Union[MetricDescriptor.MetricKind, str]] = ..., value_type: _Optional[_Union[MetricDescriptor.ValueType, str]] = ..., unit: _Optional[str] = ..., description: _Optional[str] = ..., display_name: _Optional[str] = ..., metric_descriptor_metadata: _Optional[_Union[MetricDescriptor.MetricDescriptorMetadata, _Mapping]] = ..., distribution_bucket_options: _Optional[_Union[_common_pb2.Distribution.BucketOptions, _Mapping]] = ..., promoted_label_key_sets: _Optional[_Iterable[_Union[_common_pb2.LabelKeySet, _Mapping]]] = ..., index_spec: _Optional[_Union[MetricDescriptor.IndexSpec, _Mapping]] = ..., indices: _Optional[_Union[MetricDescriptor.Indices, _Mapping]] = ..., storage_config: _Optional[_Union[MetricDescriptor.StorageConfig, _Mapping]] = ..., binary_indices: _Optional[_Union[MetricDescriptor.BinaryIndices, _Mapping]] = ...) -> None: ...
