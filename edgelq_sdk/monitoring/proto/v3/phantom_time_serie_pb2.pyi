from edgelq_sdk.monitoring.proto.v3 import common_pb2 as _common_pb2
from edgelq_sdk.monitoring.proto.v3 import metric_descriptor_pb2 as _metric_descriptor_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhantomTimeSerie(_message.Message):
    __slots__ = ("metadata", "name", "key", "project", "metric", "resource", "metric_kind", "value_type", "value")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    metadata: _meta_pb2.Meta
    name: str
    key: bytes
    project: str
    metric: _common_pb2.Metric
    resource: _common_pb2.MonitoredResource
    metric_kind: _metric_descriptor_pb2.MetricDescriptor.MetricKind
    value_type: _metric_descriptor_pb2.MetricDescriptor.ValueType
    value: _common_pb2.TypedValue
    def __init__(self, metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., name: _Optional[str] = ..., key: _Optional[bytes] = ..., project: _Optional[str] = ..., metric: _Optional[_Union[_common_pb2.Metric, _Mapping]] = ..., resource: _Optional[_Union[_common_pb2.MonitoredResource, _Mapping]] = ..., metric_kind: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor.MetricKind, str]] = ..., value_type: _Optional[_Union[_metric_descriptor_pb2.MetricDescriptor.ValueType, str]] = ..., value: _Optional[_Union[_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
