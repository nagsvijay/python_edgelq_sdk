# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v3/phantom_time_serie.proto
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
    'edgelq-sdk/monitoring/proto/v3/phantom_time_serie.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v3 import common_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_common__pb2
from edgelq_sdk.monitoring.proto.v3 import metric_descriptor_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_metric__descriptor__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/monitoring/proto/v3/phantom_time_serie.proto\x12\x11ntt.monitoring.v3\x1a+edgelq-sdk/monitoring/proto/v3/common.proto\x1a\x36\x65\x64gelq-sdk/monitoring/proto/v3/metric_descriptor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/meta.proto\"\x8d\x04\n\x10PhantomTimeSerie\x12#\n\x08metadata\x18\x0b \x01(\x0b\x32\x11.goten.types.Meta\x12\x0c\n\x04name\x18\x64 \x01(\t\x12\x11\n\x03key\x18\x65 \x01(\x0c\x42\x04\xe2\x41\x01\x03\x12\x15\n\x07project\x18\x66 \x01(\tB\x04\xe2\x41\x01\x03\x12)\n\x06metric\x18\x01 \x01(\x0b\x32\x19.ntt.monitoring.v3.Metric\x12\x36\n\x08resource\x18\x02 \x01(\x0b\x32$.ntt.monitoring.v3.MonitoredResource\x12I\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32..ntt.monitoring.v3.MetricDescriptor.MetricKindB\x04\xe2\x41\x01\x03\x12G\n\nvalue_type\x18\x04 \x01(\x0e\x32-.ntt.monitoring.v3.MetricDescriptor.ValueTypeB\x04\xe2\x41\x01\x03\x12,\n\x05value\x18\x06 \x01(\x0b\x32\x1d.ntt.monitoring.v3.TypedValue:w\xea\x41t\n&monitoring.edgelq.com/PhantomTimeSerie\x12Jprojects/{project}/regions/{region}/phantomTimeSeries/{phantom_time_serie}B\x91\x01\n\x18\x63om.ntt.monitoring.pb.v3B\x15PhantomTimeSerieProtoP\x01Z\\github.com/cloudwan/edgelq-sdk/monitoring/resources/v3/phantom_time_serie;phantom_time_serieb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v3.phantom_time_serie_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v3B\025PhantomTimeSerieProtoP\001Z\\github.com/cloudwan/edgelq-sdk/monitoring/resources/v3/phantom_time_serie;phantom_time_serie'
  _globals['_PHANTOMTIMESERIE'].fields_by_name['key']._loaded_options = None
  _globals['_PHANTOMTIMESERIE'].fields_by_name['key']._serialized_options = b'\342A\001\003'
  _globals['_PHANTOMTIMESERIE'].fields_by_name['project']._loaded_options = None
  _globals['_PHANTOMTIMESERIE'].fields_by_name['project']._serialized_options = b'\342A\001\003'
  _globals['_PHANTOMTIMESERIE'].fields_by_name['metric_kind']._loaded_options = None
  _globals['_PHANTOMTIMESERIE'].fields_by_name['metric_kind']._serialized_options = b'\342A\001\003'
  _globals['_PHANTOMTIMESERIE'].fields_by_name['value_type']._loaded_options = None
  _globals['_PHANTOMTIMESERIE'].fields_by_name['value_type']._serialized_options = b'\342A\001\003'
  _globals['_PHANTOMTIMESERIE']._loaded_options = None
  _globals['_PHANTOMTIMESERIE']._serialized_options = b'\352At\n&monitoring.edgelq.com/PhantomTimeSerie\022Jprojects/{project}/regions/{region}/phantomTimeSeries/{phantom_time_serie}'
  _globals['_PHANTOMTIMESERIE']._serialized_start=301
  _globals['_PHANTOMTIMESERIE']._serialized_end=826
# @@protoc_insertion_point(module_scope)
