# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/metric_descriptor_service.proto
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
    'edgelq-sdk/monitoring/proto/v4/metric_descriptor_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_metric__descriptor__pb2
from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_metric__descriptor__change__pb2
from edgelq_sdk.monitoring.proto.v4 import metric_descriptor_custom_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_metric__descriptor__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>edgelq-sdk/monitoring/proto/v4/metric_descriptor_service.proto\x12\x11ntt.monitoring.v4\x1a\x36\x65\x64gelq-sdk/monitoring/proto/v4/metric_descriptor.proto\x1a=edgelq-sdk/monitoring/proto/v4/metric_descriptor_change.proto\x1a=edgelq-sdk/monitoring/proto/v4/metric_descriptor_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"\x88\x01\n BatchGetMetricDescriptorsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"u\n!BatchGetMetricDescriptorsResponse\x12?\n\x12metric_descriptors\x18\x01 \x03(\x0b\x32#.ntt.monitoring.v4.MetricDescriptor\x12\x0f\n\x07missing\x18\x02 \x03(\t\"}\n\x1cWatchMetricDescriptorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"Z\n\x1dWatchMetricDescriptorResponse\x12\x39\n\x06\x63hange\x18\x01 \x01(\x0b\x32).ntt.monitoring.v4.MetricDescriptorChange\"\xd0\x02\n\x1dWatchMetricDescriptorsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\x80\x03\n\x1eWatchMetricDescriptorsResponse\x12L\n\x19metric_descriptor_changes\x18\x02 \x03(\x0b\x32).ntt.monitoring.v4.MetricDescriptorChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\\\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x41.ntt.monitoring.v4.WatchMetricDescriptorsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xda\x0b\n\x17MetricDescriptorService\x12\xae\x01\n\x19\x42\x61tchGetMetricDescriptors\x12\x33.ntt.monitoring.v4.BatchGetMetricDescriptorsRequest\x1a\x34.ntt.monitoring.v4.BatchGetMetricDescriptorsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v4/metricDescriptors:batchGet\x12\xb5\x01\n\x15WatchMetricDescriptor\x12/.ntt.monitoring.v4.WatchMetricDescriptorRequest\x1a\x30.ntt.monitoring.v4.WatchMetricDescriptorResponse\"7\x82\xd3\xe4\x93\x02\x31\"//v4/{name=projects/*/metricDescriptors/*}:watch0\x01\x12\xb8\x01\n\x16WatchMetricDescriptors\x12\x30.ntt.monitoring.v4.WatchMetricDescriptorsRequest\x1a\x31.ntt.monitoring.v4.WatchMetricDescriptorsResponse\"7\x82\xd3\xe4\x93\x02\x31\"//v4/{parent=projects/*}/metricDescriptors:watch0\x01\x12\x9c\x01\n\x13GetMetricDescriptor\x12-.ntt.monitoring.v4.GetMetricDescriptorRequest\x1a#.ntt.monitoring.v4.MetricDescriptor\"1\x82\xd3\xe4\x93\x02+\x12)/v4/{name=projects/*/metricDescriptors/*}\x12\xb5\x01\n\x16\x43reateMetricDescriptor\x12\x30.ntt.monitoring.v4.CreateMetricDescriptorRequest\x1a#.ntt.monitoring.v4.MetricDescriptor\"D\x82\xd3\xe4\x93\x02>\")/v4/{parent=projects/*}/metricDescriptors:\x11metric_descriptor\x12\xc7\x01\n\x16UpdateMetricDescriptor\x12\x30.ntt.monitoring.v4.UpdateMetricDescriptorRequest\x1a#.ntt.monitoring.v4.MetricDescriptor\"V\x82\xd3\xe4\x93\x02P\x1a;/v4/{metric_descriptor.name=projects/*/metricDescriptors/*}:\x11metric_descriptor\x12\x95\x01\n\x16\x44\x65leteMetricDescriptor\x12\x30.ntt.monitoring.v4.DeleteMetricDescriptorRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/v4/{name=projects/*/metricDescriptors/*}\x12\xad\x01\n\x15ListMetricDescriptors\x12/.ntt.monitoring.v4.ListMetricDescriptorsRequest\x1a\x30.ntt.monitoring.v4.ListMetricDescriptorsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/v4/{parent=projects/*}/metricDescriptors\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x9a\x01\n\x18\x63om.ntt.monitoring.pb.v4B\x1cMetricDescriptorServiceProtoP\x00Z^github.com/cloudwan/edgelq-sdk/monitoring/client/v4/metric_descriptor;metric_descriptor_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.metric_descriptor_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\034MetricDescriptorServiceProtoP\000Z^github.com/cloudwan/edgelq-sdk/monitoring/client/v4/metric_descriptor;metric_descriptor_client'
  _globals['_METRICDESCRIPTORSERVICE']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['BatchGetMetricDescriptors']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['BatchGetMetricDescriptors']._serialized_options = b'\202\323\344\223\002 \022\036/v4/metricDescriptors:batchGet'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['WatchMetricDescriptor']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['WatchMetricDescriptor']._serialized_options = b'\202\323\344\223\0021\"//v4/{name=projects/*/metricDescriptors/*}:watch'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['WatchMetricDescriptors']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['WatchMetricDescriptors']._serialized_options = b'\202\323\344\223\0021\"//v4/{parent=projects/*}/metricDescriptors:watch'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['GetMetricDescriptor']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['GetMetricDescriptor']._serialized_options = b'\202\323\344\223\002+\022)/v4/{name=projects/*/metricDescriptors/*}'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['CreateMetricDescriptor']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['CreateMetricDescriptor']._serialized_options = b'\202\323\344\223\002>\")/v4/{parent=projects/*}/metricDescriptors:\021metric_descriptor'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['UpdateMetricDescriptor']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['UpdateMetricDescriptor']._serialized_options = b'\202\323\344\223\002P\032;/v4/{metric_descriptor.name=projects/*/metricDescriptors/*}:\021metric_descriptor'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['DeleteMetricDescriptor']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['DeleteMetricDescriptor']._serialized_options = b'\202\323\344\223\002+*)/v4/{name=projects/*/metricDescriptors/*}'
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['ListMetricDescriptors']._loaded_options = None
  _globals['_METRICDESCRIPTORSERVICE'].methods_by_name['ListMetricDescriptors']._serialized_options = b'\202\323\344\223\002+\022)/v4/{parent=projects/*}/metricDescriptors'
  _globals['_BATCHGETMETRICDESCRIPTORSREQUEST']._serialized_start=481
  _globals['_BATCHGETMETRICDESCRIPTORSREQUEST']._serialized_end=617
  _globals['_BATCHGETMETRICDESCRIPTORSRESPONSE']._serialized_start=619
  _globals['_BATCHGETMETRICDESCRIPTORSRESPONSE']._serialized_end=736
  _globals['_WATCHMETRICDESCRIPTORREQUEST']._serialized_start=738
  _globals['_WATCHMETRICDESCRIPTORREQUEST']._serialized_end=863
  _globals['_WATCHMETRICDESCRIPTORRESPONSE']._serialized_start=865
  _globals['_WATCHMETRICDESCRIPTORRESPONSE']._serialized_end=955
  _globals['_WATCHMETRICDESCRIPTORSREQUEST']._serialized_start=958
  _globals['_WATCHMETRICDESCRIPTORSREQUEST']._serialized_end=1294
  _globals['_WATCHMETRICDESCRIPTORSRESPONSE']._serialized_start=1297
  _globals['_WATCHMETRICDESCRIPTORSRESPONSE']._serialized_end=1681
  _globals['_WATCHMETRICDESCRIPTORSRESPONSE_PAGETOKENCHANGE']._serialized_start=1614
  _globals['_WATCHMETRICDESCRIPTORSRESPONSE_PAGETOKENCHANGE']._serialized_end=1681
  _globals['_METRICDESCRIPTORSERVICE']._serialized_start=1684
  _globals['_METRICDESCRIPTORSERVICE']._serialized_end=3182
# @@protoc_insertion_point(module_scope)
