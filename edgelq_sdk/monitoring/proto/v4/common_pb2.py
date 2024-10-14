# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/common.proto
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
    'edgelq-sdk/monitoring/proto/v4/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+edgelq-sdk/monitoring/proto/v4/common.proto\x12\x11ntt.monitoring.v4\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcc\x01\n\x0fLabelDescriptor\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\nvalue_type\x18\x02 \x01(\x0e\x32,.ntt.monitoring.v4.LabelDescriptor.ValueType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x0c \x01(\t\x12\x10\n\x08\x64isabled\x18\r \x01(\x08\",\n\tValueType\x12\n\n\x06STRING\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\t\n\x05INT64\x10\x02\"\'\n\x0bLabelKeySet\x12\x12\n\nlabel_keys\x18\x01 \x03(\tJ\x04\x08\x02\x10\x03\"\xd2\x06\n\x0c\x44istribution\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x01\x12 \n\x18sum_of_squared_deviation\x18\x03 \x01(\x01\x12\x34\n\x05range\x18\x04 \x01(\x0b\x32%.ntt.monitoring.v4.Distribution.Range\x12\x45\n\x0e\x62ucket_options\x18\x06 \x01(\x0b\x32-.ntt.monitoring.v4.Distribution.BucketOptions\x12\x15\n\rbucket_counts\x18\x07 \x03(\x03\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x1a\xcb\x04\n\rBucketOptions\x12N\n\x0elinear_buckets\x18\x01 \x01(\x0b\x32\x34.ntt.monitoring.v4.Distribution.BucketOptions.LinearH\x00\x12X\n\x13\x65xponential_buckets\x18\x02 \x01(\x0b\x32\x39.ntt.monitoring.v4.Distribution.BucketOptions.ExponentialH\x00\x12R\n\x10\x65xplicit_buckets\x18\x03 \x01(\x0b\x32\x36.ntt.monitoring.v4.Distribution.BucketOptions.ExplicitH\x00\x12P\n\x0f\x64ynamic_buckets\x18\t \x01(\x0b\x32\x35.ntt.monitoring.v4.Distribution.BucketOptions.DynamicH\x00\x1a\x43\n\x06Linear\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x1aO\n\x0b\x45xponential\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x01\x12\r\n\x05scale\x18\x03 \x01(\x01\x1a\x1a\n\x08\x45xplicit\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x01\x1a-\n\x07\x44ynamic\x12\x13\n\x0b\x63ompression\x18\x01 \x01(\x01\x12\r\n\x05means\x18\x02 \x03(\x01\x42\t\n\x07options\"\xb1\x01\n\nTypedValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12=\n\x12\x64istribution_value\x18\x05 \x01(\x0b\x32\x1f.ntt.monitoring.v4.DistributionH\x00\x42\x07\n\x05value\"l\n\x0cTimeInterval\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"i\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf8\x05\n\x0b\x41ggregation\x12\x33\n\x10\x61lignment_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x42\n\x12per_series_aligner\x18\x02 \x01(\x0e\x32&.ntt.monitoring.v4.Aggregation.Aligner\x12\x44\n\x14\x63ross_series_reducer\x18\x04 \x01(\x0e\x32&.ntt.monitoring.v4.Aggregation.Reducer\x12\x17\n\x0fgroup_by_fields\x18\x05 \x03(\t\"\x91\x02\n\x07\x41ligner\x12\x0e\n\nALIGN_NONE\x10\x00\x12\x0f\n\x0b\x41LIGN_DELTA\x10\x01\x12\x0e\n\nALIGN_RATE\x10\x02\x12\r\n\tALIGN_MIN\x10\n\x12\r\n\tALIGN_MAX\x10\x0b\x12\x0e\n\nALIGN_MEAN\x10\x0c\x12\x0f\n\x0b\x41LIGN_COUNT\x10\r\x12\r\n\tALIGN_SUM\x10\x0e\x12\x10\n\x0c\x41LIGN_STDDEV\x10\x0f\x12\x17\n\x13\x41LIGN_PERCENTILE_99\x10\x12\x12\x17\n\x13\x41LIGN_PERCENTILE_95\x10\x13\x12\x17\n\x13\x41LIGN_PERCENTILE_50\x10\x14\x12\x17\n\x13\x41LIGN_PERCENTILE_05\x10\x15\x12\x11\n\rALIGN_SUMMARY\x10-\"\xfc\x01\n\x07Reducer\x12\x0f\n\x0bREDUCE_NONE\x10\x00\x12\x0f\n\x0bREDUCE_MEAN\x10\x01\x12\x0e\n\nREDUCE_MIN\x10\x02\x12\x0e\n\nREDUCE_MAX\x10\x03\x12\x0e\n\nREDUCE_SUM\x10\x04\x12\x11\n\rREDUCE_STDDEV\x10\x05\x12\x10\n\x0cREDUCE_COUNT\x10\x06\x12\x18\n\x14REDUCE_PERCENTILE_99\x10\t\x12\x18\n\x14REDUCE_PERCENTILE_95\x10\n\x12\x18\n\x14REDUCE_PERCENTILE_50\x10\x0b\x12\x18\n\x14REDUCE_PERCENTILE_05\x10\x0c\x12\x12\n\x0eREDUCE_SUMMARY\x10\r\"\x80\x01\n\nPagination\x12\x0c\n\x04view\x18\x01 \x01(\t\x12\x10\n\x08\x66unction\x18\x02 \x01(\t\x12\x33\n\x10\x61lignment_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x05\"\x94\x01\n\x06Metric\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x35\n\x06labels\x18\x02 \x03(\x0b\x32%.ntt.monitoring.v4.Metric.LabelsEntry\x12\x16\n\x0ereduced_labels\x18\x0b \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xaa\x01\n\x11MonitoredResource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12@\n\x06labels\x18\x02 \x03(\x0b\x32\x30.ntt.monitoring.v4.MonitoredResource.LabelsEntry\x12\x16\n\x0ereduced_labels\x18\x0b \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x19\n\x07Strings\x12\x0e\n\x06values\x18\x01 \x03(\t\"\xbf\x01\n\x19MonitoredResourceSelector\x12\r\n\x05types\x18\x01 \x03(\t\x12H\n\x06labels\x18\x02 \x03(\x0b\x32\x38.ntt.monitoring.v4.MonitoredResourceSelector.LabelsEntry\x1aI\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.ntt.monitoring.v4.Strings:\x02\x38\x01\"\xa9\x01\n\x0eMetricSelector\x12\r\n\x05types\x18\x01 \x03(\t\x12=\n\x06labels\x18\x02 \x03(\x0b\x32-.ntt.monitoring.v4.MetricSelector.LabelsEntry\x1aI\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.ntt.monitoring.v4.Strings:\x02\x38\x01\"\x87\x01\n\x12TimeSeriesSelector\x12\x31\n\x06metric\x18\x01 \x01(\x0b\x32!.ntt.monitoring.v4.MetricSelector\x12>\n\x08resource\x18\x02 \x01(\x0b\x32,.ntt.monitoring.v4.MonitoredResourceSelector*\'\n\x0eTimeSeriesView\x12\x08\n\x04\x46ULL\x10\x00\x12\x0b\n\x07HEADERS\x10\x01\x42o\n\x18\x63om.ntt.monitoring.pb.v4B\x0b\x43ommonProtoP\x00ZDgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/common;commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\013CommonProtoP\000ZDgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/common;common'
  _globals['_METRIC_LABELSENTRY']._loaded_options = None
  _globals['_METRIC_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_MONITOREDRESOURCE_LABELSENTRY']._loaded_options = None
  _globals['_MONITOREDRESOURCE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_MONITOREDRESOURCESELECTOR_LABELSENTRY']._loaded_options = None
  _globals['_MONITOREDRESOURCESELECTOR_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_METRICSELECTOR_LABELSENTRY']._loaded_options = None
  _globals['_METRICSELECTOR_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_TIMESERIESVIEW']._serialized_start=3378
  _globals['_TIMESERIESVIEW']._serialized_end=3417
  _globals['_LABELDESCRIPTOR']._serialized_start=132
  _globals['_LABELDESCRIPTOR']._serialized_end=336
  _globals['_LABELDESCRIPTOR_VALUETYPE']._serialized_start=292
  _globals['_LABELDESCRIPTOR_VALUETYPE']._serialized_end=336
  _globals['_LABELKEYSET']._serialized_start=338
  _globals['_LABELKEYSET']._serialized_end=377
  _globals['_DISTRIBUTION']._serialized_start=380
  _globals['_DISTRIBUTION']._serialized_end=1230
  _globals['_DISTRIBUTION_RANGE']._serialized_start=607
  _globals['_DISTRIBUTION_RANGE']._serialized_end=640
  _globals['_DISTRIBUTION_BUCKETOPTIONS']._serialized_start=643
  _globals['_DISTRIBUTION_BUCKETOPTIONS']._serialized_end=1230
  _globals['_DISTRIBUTION_BUCKETOPTIONS_LINEAR']._serialized_start=996
  _globals['_DISTRIBUTION_BUCKETOPTIONS_LINEAR']._serialized_end=1063
  _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL']._serialized_start=1065
  _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL']._serialized_end=1144
  _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT']._serialized_start=1146
  _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT']._serialized_end=1172
  _globals['_DISTRIBUTION_BUCKETOPTIONS_DYNAMIC']._serialized_start=1174
  _globals['_DISTRIBUTION_BUCKETOPTIONS_DYNAMIC']._serialized_end=1219
  _globals['_TYPEDVALUE']._serialized_start=1233
  _globals['_TYPEDVALUE']._serialized_end=1410
  _globals['_TIMEINTERVAL']._serialized_start=1412
  _globals['_TIMEINTERVAL']._serialized_end=1520
  _globals['_TIMERANGE']._serialized_start=1522
  _globals['_TIMERANGE']._serialized_end=1627
  _globals['_AGGREGATION']._serialized_start=1630
  _globals['_AGGREGATION']._serialized_end=2390
  _globals['_AGGREGATION_ALIGNER']._serialized_start=1862
  _globals['_AGGREGATION_ALIGNER']._serialized_end=2135
  _globals['_AGGREGATION_REDUCER']._serialized_start=2138
  _globals['_AGGREGATION_REDUCER']._serialized_end=2390
  _globals['_PAGINATION']._serialized_start=2393
  _globals['_PAGINATION']._serialized_end=2521
  _globals['_METRIC']._serialized_start=2524
  _globals['_METRIC']._serialized_end=2672
  _globals['_METRIC_LABELSENTRY']._serialized_start=2627
  _globals['_METRIC_LABELSENTRY']._serialized_end=2672
  _globals['_MONITOREDRESOURCE']._serialized_start=2675
  _globals['_MONITOREDRESOURCE']._serialized_end=2845
  _globals['_MONITOREDRESOURCE_LABELSENTRY']._serialized_start=2627
  _globals['_MONITOREDRESOURCE_LABELSENTRY']._serialized_end=2672
  _globals['_STRINGS']._serialized_start=2847
  _globals['_STRINGS']._serialized_end=2872
  _globals['_MONITOREDRESOURCESELECTOR']._serialized_start=2875
  _globals['_MONITOREDRESOURCESELECTOR']._serialized_end=3066
  _globals['_MONITOREDRESOURCESELECTOR_LABELSENTRY']._serialized_start=2993
  _globals['_MONITOREDRESOURCESELECTOR_LABELSENTRY']._serialized_end=3066
  _globals['_METRICSELECTOR']._serialized_start=3069
  _globals['_METRICSELECTOR']._serialized_end=3238
  _globals['_METRICSELECTOR_LABELSENTRY']._serialized_start=2993
  _globals['_METRICSELECTOR_LABELSENTRY']._serialized_end=3066
  _globals['_TIMESERIESSELECTOR']._serialized_start=3241
  _globals['_TIMESERIESSELECTOR']._serialized_end=3376
# @@protoc_insertion_point(module_scope)
