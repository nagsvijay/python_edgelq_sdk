# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/time_serie.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'edgelq-sdk/monitoring/proto/v4/time_serie.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import common_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_common__pb2
from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_metric__descriptor__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/edgelq-sdk/monitoring/proto/v4/time_serie.proto\x12\x11ntt.monitoring.v4\x1a+edgelq-sdk/monitoring/proto/v4/common.proto\x1a\x36\x65\x64gelq-sdk/monitoring/proto/v4/metric_descriptor.proto\x1a\x19google/api/resource.proto\"\x9d\x01\n\x05Point\x12\x31\n\x08interval\x18\x01 \x01(\x0b\x32\x1f.ntt.monitoring.v4.TimeInterval\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.ntt.monitoring.v4.TypedValue\x12\x33\n\x0b\x61ggregation\x18\x65 \x01(\x0b\x32\x1e.ntt.monitoring.v4.Aggregation\"\xf6\x03\n\tTimeSerie\x12\x0b\n\x03key\x18\x65 \x01(\x0c\x12\x0f\n\x07project\x18\x66 \x01(\t\x12\x0e\n\x06region\x18g \x01(\t\x12)\n\x06metric\x18\x01 \x01(\x0b\x32\x19.ntt.monitoring.v4.Metric\x12\x36\n\x08resource\x18\x02 \x01(\x0b\x32$.ntt.monitoring.v4.MonitoredResource\x12\x43\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32..ntt.monitoring.v4.MetricDescriptor.MetricKind\x12\x41\n\nvalue_type\x18\x04 \x01(\x0e\x32-.ntt.monitoring.v4.MetricDescriptor.ValueType\x12(\n\x06points\x18\x05 \x03(\x0b\x32\x18.ntt.monitoring.v4.Point:\x9f\x01\xea\x41\x9b\x01\n\x1fmonitoring.edgelq.com/TimeSerie\x12*projects/{project}/timeSeries/{time_serie}\x12Lprojects/{project}/regions/{region}/buckets/{bucket}/timeSeries/{time_serie}J\x04\x08\x07\x10\x08\"Y\n\x0e\x42ulkTimeSeries\x12\x31\n\x0btime_series\x18\x01 \x03(\x0b\x32\x1c.ntt.monitoring.v4.TimeSerie\x12\x14\n\x0cphantom_flag\x18\x02 \x01(\x08\x42z\n\x18\x63om.ntt.monitoring.pb.v4B\x0eTimeSerieProtoP\x01ZLgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/time_serie;time_serieb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.time_serie_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\016TimeSerieProtoP\001ZLgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/time_serie;time_serie'
  _globals['_TIMESERIE']._loaded_options = None
  _globals['_TIMESERIE']._serialized_options = b'\352A\233\001\n\037monitoring.edgelq.com/TimeSerie\022*projects/{project}/timeSeries/{time_serie}\022Lprojects/{project}/regions/{region}/buckets/{bucket}/timeSeries/{time_serie}'
  _globals['_POINT']._serialized_start=199
  _globals['_POINT']._serialized_end=356
  _globals['_TIMESERIE']._serialized_start=359
  _globals['_TIMESERIE']._serialized_end=861
  _globals['_BULKTIMESERIES']._serialized_start=863
  _globals['_BULKTIMESERIES']._serialized_end=952
# @@protoc_insertion_point(module_scope)
