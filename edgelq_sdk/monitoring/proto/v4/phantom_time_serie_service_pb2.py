# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/phantom_time_serie_service.proto
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
    'edgelq-sdk/monitoring/proto/v4/phantom_time_serie_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import phantom_time_serie_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_phantom__time__serie__pb2
from edgelq_sdk.monitoring.proto.v4 import phantom_time_serie_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_phantom__time__serie__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/monitoring/proto/v4/phantom_time_serie_service.proto\x12\x11ntt.monitoring.v4\x1a\x37\x65\x64gelq-sdk/monitoring/proto/v4/phantom_time_serie.proto\x1a>edgelq-sdk/monitoring/proto/v4/phantom_time_serie_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"{\n\x1aGetPhantomTimeSerieRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x88\x01\n BatchGetPhantomTimeSeriesRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"v\n!BatchGetPhantomTimeSeriesResponse\x12@\n\x13phantom_time_series\x18\x01 \x03(\x0b\x32#.ntt.monitoring.v4.PhantomTimeSerie\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe5\x01\n\x1cListPhantomTimeSeriesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xc8\x01\n\x1dListPhantomTimeSeriesResponse\x12@\n\x13phantom_time_series\x18\x01 \x03(\x0b\x32#.ntt.monitoring.v4.PhantomTimeSerie\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"}\n\x1cWatchPhantomTimeSerieRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"Z\n\x1dWatchPhantomTimeSerieResponse\x12\x39\n\x06\x63hange\x18\x01 \x01(\x0b\x32).ntt.monitoring.v4.PhantomTimeSerieChange\"\xd0\x02\n\x1dWatchPhantomTimeSeriesRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\x81\x03\n\x1eWatchPhantomTimeSeriesResponse\x12M\n\x1aphantom_time_serie_changes\x18\x02 \x03(\x0b\x32).ntt.monitoring.v4.PhantomTimeSerieChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\\\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x41.ntt.monitoring.v4.WatchPhantomTimeSeriesResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"p\n\x1d\x43reatePhantomTimeSerieRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12?\n\x12phantom_time_serie\x18\x02 \x01(\x0b\x32#.ntt.monitoring.v4.PhantomTimeSerie\"\xe2\x02\n\x1dUpdatePhantomTimeSerieRequest\x12?\n\x12phantom_time_serie\x18\x02 \x01(\x0b\x32#.ntt.monitoring.v4.PhantomTimeSerie\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x41\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\x34.ntt.monitoring.v4.UpdatePhantomTimeSerieRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1au\n\x03\x43\x41S\x12>\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32#.ntt.monitoring.v4.PhantomTimeSerie\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"-\n\x1d\x44\x65letePhantomTimeSerieRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xa3\x0c\n\x17PhantomTimeSerieService\x12\xa6\x01\n\x13GetPhantomTimeSerie\x12-.ntt.monitoring.v4.GetPhantomTimeSerieRequest\x1a#.ntt.monitoring.v4.PhantomTimeSerie\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v4/{name=projects/*/regions/*/phantomTimeSeries/*}\x12\xae\x01\n\x19\x42\x61tchGetPhantomTimeSeries\x12\x33.ntt.monitoring.v4.BatchGetPhantomTimeSeriesRequest\x1a\x34.ntt.monitoring.v4.BatchGetPhantomTimeSeriesResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v4/phantomTimeSeries:batchGet\x12\xb7\x01\n\x15ListPhantomTimeSeries\x12/.ntt.monitoring.v4.ListPhantomTimeSeriesRequest\x1a\x30.ntt.monitoring.v4.ListPhantomTimeSeriesResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v4/{parent=projects/*/regions/*}/phantomTimeSeries\x12\xbf\x01\n\x15WatchPhantomTimeSerie\x12/.ntt.monitoring.v4.WatchPhantomTimeSerieRequest\x1a\x30.ntt.monitoring.v4.WatchPhantomTimeSerieResponse\"A\x82\xd3\xe4\x93\x02;\"9/v4/{name=projects/*/regions/*/phantomTimeSeries/*}:watch0\x01\x12\xc2\x01\n\x16WatchPhantomTimeSeries\x12\x30.ntt.monitoring.v4.WatchPhantomTimeSeriesRequest\x1a\x31.ntt.monitoring.v4.WatchPhantomTimeSeriesResponse\"A\x82\xd3\xe4\x93\x02;\"9/v4/{parent=projects/*/regions/*}/phantomTimeSeries:watch0\x01\x12\xc0\x01\n\x16\x43reatePhantomTimeSerie\x12\x30.ntt.monitoring.v4.CreatePhantomTimeSerieRequest\x1a#.ntt.monitoring.v4.PhantomTimeSerie\"O\x82\xd3\xe4\x93\x02I\"3/v4/{parent=projects/*/regions/*}/phantomTimeSeries:\x12phantom_time_serie\x12\xd3\x01\n\x16UpdatePhantomTimeSerie\x12\x30.ntt.monitoring.v4.UpdatePhantomTimeSerieRequest\x1a#.ntt.monitoring.v4.PhantomTimeSerie\"b\x82\xd3\xe4\x93\x02\\\x1a\x46/v4/{phantom_time_serie.name=projects/*/regions/*/phantomTimeSeries/*}:\x12phantom_time_serie\x12\x9f\x01\n\x16\x44\x65letePhantomTimeSerie\x12\x30.ntt.monitoring.v4.DeletePhantomTimeSerieRequest\x1a\x16.google.protobuf.Empty\";\x82\xd3\xe4\x93\x02\x35*3/v4/{name=projects/*/regions/*/phantomTimeSeries/*}\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x9c\x01\n\x18\x63om.ntt.monitoring.pb.v4B\x1cPhantomTimeSerieServiceProtoP\x00Z`github.com/cloudwan/edgelq-sdk/monitoring/client/v4/phantom_time_serie;phantom_time_serie_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.phantom_time_serie_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\034PhantomTimeSerieServiceProtoP\000Z`github.com/cloudwan/edgelq-sdk/monitoring/client/v4/phantom_time_serie;phantom_time_serie_client'
  _globals['_PHANTOMTIMESERIESERVICE']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['GetPhantomTimeSerie']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['GetPhantomTimeSerie']._serialized_options = b'\202\323\344\223\0025\0223/v4/{name=projects/*/regions/*/phantomTimeSeries/*}'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['BatchGetPhantomTimeSeries']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['BatchGetPhantomTimeSeries']._serialized_options = b'\202\323\344\223\002 \022\036/v4/phantomTimeSeries:batchGet'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['ListPhantomTimeSeries']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['ListPhantomTimeSeries']._serialized_options = b'\202\323\344\223\0025\0223/v4/{parent=projects/*/regions/*}/phantomTimeSeries'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['WatchPhantomTimeSerie']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['WatchPhantomTimeSerie']._serialized_options = b'\202\323\344\223\002;\"9/v4/{name=projects/*/regions/*/phantomTimeSeries/*}:watch'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['WatchPhantomTimeSeries']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['WatchPhantomTimeSeries']._serialized_options = b'\202\323\344\223\002;\"9/v4/{parent=projects/*/regions/*}/phantomTimeSeries:watch'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['CreatePhantomTimeSerie']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['CreatePhantomTimeSerie']._serialized_options = b'\202\323\344\223\002I\"3/v4/{parent=projects/*/regions/*}/phantomTimeSeries:\022phantom_time_serie'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['UpdatePhantomTimeSerie']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['UpdatePhantomTimeSerie']._serialized_options = b'\202\323\344\223\002\\\032F/v4/{phantom_time_serie.name=projects/*/regions/*/phantomTimeSeries/*}:\022phantom_time_serie'
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['DeletePhantomTimeSerie']._loaded_options = None
  _globals['_PHANTOMTIMESERIESERVICE'].methods_by_name['DeletePhantomTimeSerie']._serialized_options = b'\202\323\344\223\0025*3/v4/{name=projects/*/regions/*/phantomTimeSeries/*}'
  _globals['_GETPHANTOMTIMESERIEREQUEST']._serialized_start=420
  _globals['_GETPHANTOMTIMESERIEREQUEST']._serialized_end=543
  _globals['_BATCHGETPHANTOMTIMESERIESREQUEST']._serialized_start=546
  _globals['_BATCHGETPHANTOMTIMESERIESREQUEST']._serialized_end=682
  _globals['_BATCHGETPHANTOMTIMESERIESRESPONSE']._serialized_start=684
  _globals['_BATCHGETPHANTOMTIMESERIESRESPONSE']._serialized_end=802
  _globals['_LISTPHANTOMTIMESERIESREQUEST']._serialized_start=805
  _globals['_LISTPHANTOMTIMESERIESREQUEST']._serialized_end=1034
  _globals['_LISTPHANTOMTIMESERIESRESPONSE']._serialized_start=1037
  _globals['_LISTPHANTOMTIMESERIESRESPONSE']._serialized_end=1237
  _globals['_WATCHPHANTOMTIMESERIEREQUEST']._serialized_start=1239
  _globals['_WATCHPHANTOMTIMESERIEREQUEST']._serialized_end=1364
  _globals['_WATCHPHANTOMTIMESERIERESPONSE']._serialized_start=1366
  _globals['_WATCHPHANTOMTIMESERIERESPONSE']._serialized_end=1456
  _globals['_WATCHPHANTOMTIMESERIESREQUEST']._serialized_start=1459
  _globals['_WATCHPHANTOMTIMESERIESREQUEST']._serialized_end=1795
  _globals['_WATCHPHANTOMTIMESERIESRESPONSE']._serialized_start=1798
  _globals['_WATCHPHANTOMTIMESERIESRESPONSE']._serialized_end=2183
  _globals['_WATCHPHANTOMTIMESERIESRESPONSE_PAGETOKENCHANGE']._serialized_start=2116
  _globals['_WATCHPHANTOMTIMESERIESRESPONSE_PAGETOKENCHANGE']._serialized_end=2183
  _globals['_CREATEPHANTOMTIMESERIEREQUEST']._serialized_start=2185
  _globals['_CREATEPHANTOMTIMESERIEREQUEST']._serialized_end=2297
  _globals['_UPDATEPHANTOMTIMESERIEREQUEST']._serialized_start=2300
  _globals['_UPDATEPHANTOMTIMESERIEREQUEST']._serialized_end=2654
  _globals['_UPDATEPHANTOMTIMESERIEREQUEST_CAS']._serialized_start=2537
  _globals['_UPDATEPHANTOMTIMESERIEREQUEST_CAS']._serialized_end=2654
  _globals['_DELETEPHANTOMTIMESERIEREQUEST']._serialized_start=2656
  _globals['_DELETEPHANTOMTIMESERIEREQUEST']._serialized_end=2701
  _globals['_PHANTOMTIMESERIESERVICE']._serialized_start=2704
  _globals['_PHANTOMTIMESERIESERVICE']._serialized_end=4275
# @@protoc_insertion_point(module_scope)
