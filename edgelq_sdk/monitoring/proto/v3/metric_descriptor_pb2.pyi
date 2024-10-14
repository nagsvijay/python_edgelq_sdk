from edgelq_sdk.common.api import launch_stage_pb2 as _launch_stage_pb2
from edgelq_sdk.monitoring.proto.v3 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDescriptor(_message.Message):
    __slots__ = ("metadata", "name", "type", "resource_types", "labels", "metric_kind", "value_type", "unit", "description", "display_name", "metric_descriptor_metadata", "distribution_bucket_options", "promoted_label_key_sets", "index_spec", "storage_config")
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
        STRING: _ClassVar[MetricDescriptor.ValueType]
        DISTRIBUTION: _ClassVar[MetricDescriptor.ValueType]
        MONEY: _ClassVar[MetricDescriptor.ValueType]
    VALUE_TYPE_UNSPECIFIED: MetricDescriptor.ValueType
    BOOL: MetricDescriptor.ValueType
    INT64: MetricDescriptor.ValueType
    DOUBLE: MetricDescriptor.ValueType
    STRING: MetricDescriptor.ValueType
    DISTRIBUTION: MetricDescriptor.ValueType
    MONEY: MetricDescriptor.ValueType
    class MetricDescriptorMetadata(_message.Message):
        __slots__ = ("launch_stage",)
        LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
        launch_stage: _launch_stage_pb2.LaunchStage
        def __init__(self, launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]] = ...) -> None: ...
    class IndexSpec(_message.Message):
        __slots__ = ("per_resource",)
        class Index(_message.Message):
            __slots__ = ("promoted_labels", "write_only")
            PROMOTED_LABELS_FIELD_NUMBER: _ClassVar[int]
            WRITE_ONLY_FIELD_NUMBER: _ClassVar[int]
            promoted_labels: _containers.RepeatedScalarFieldContainer[str]
            write_only: bool
            def __init__(self, promoted_labels: _Optional[_Iterable[str]] = ..., write_only: bool = ...) -> None: ...
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
    class StorageConfig(_message.Message):
        __slots__ = ("store_raw_points",)
        STORE_RAW_POINTS_FIELD_NUMBER: _ClassVar[int]
        store_raw_points: bool
        def __init__(self, store_raw_points: bool = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
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
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metadata: _meta_pb2.Meta
    name: str
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
    storage_config: MetricDescriptor.StorageConfig
    def __init__(self, metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.LabelDescriptor, _Mapping]]] = ..., metric_kind: _Optional[_Union[MetricDescriptor.MetricKind, str]] = ..., value_type: _Optional[_Union[MetricDescriptor.ValueType, str]] = ..., unit: _Optional[str] = ..., description: _Optional[str] = ..., display_name: _Optional[str] = ..., metric_descriptor_metadata: _Optional[_Union[MetricDescriptor.MetricDescriptorMetadata, _Mapping]] = ..., distribution_bucket_options: _Optional[_Union[_common_pb2.Distribution.BucketOptions, _Mapping]] = ..., promoted_label_key_sets: _Optional[_Iterable[_Union[_common_pb2.LabelKeySet, _Mapping]]] = ..., index_spec: _Optional[_Union[MetricDescriptor.IndexSpec, _Mapping]] = ..., storage_config: _Optional[_Union[MetricDescriptor.StorageConfig, _Mapping]] = ...) -> None: ...
