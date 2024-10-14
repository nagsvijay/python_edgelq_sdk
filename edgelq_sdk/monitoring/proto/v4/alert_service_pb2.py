# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/alert_service.proto
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
    'edgelq-sdk/monitoring/proto/v4/alert_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import alert_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_alert__pb2
from edgelq_sdk.monitoring.proto.v4 import alert_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_alert__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/monitoring/proto/v4/alert_service.proto\x12\x11ntt.monitoring.v4\x1a*edgelq-sdk/monitoring/proto/v4/alert.proto\x1a\x31\x65\x64gelq-sdk/monitoring/proto/v4/alert_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"p\n\x0fGetAlertRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"}\n\x15\x42\x61tchGetAlertsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"S\n\x16\x42\x61tchGetAlertsResponse\x12(\n\x06\x61lerts\x18\x01 \x03(\x0b\x32\x18.ntt.monitoring.v4.Alert\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xda\x01\n\x11ListAlertsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xa5\x01\n\x12ListAlertsResponse\x12(\n\x06\x61lerts\x18\x01 \x03(\x0b\x32\x18.ntt.monitoring.v4.Alert\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"r\n\x11WatchAlertRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"D\n\x12WatchAlertResponse\x12.\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1e.ntt.monitoring.v4.AlertChange\"\xc5\x02\n\x12WatchAlertsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xd3\x02\n\x13WatchAlertsResponse\x12\x35\n\ralert_changes\x18\x02 \x03(\x0b\x32\x1e.ntt.monitoring.v4.AlertChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12Q\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x36.ntt.monitoring.v4.WatchAlertsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"M\n\x12\x43reateAlertRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\'\n\x05\x61lert\x18\x02 \x01(\x0b\x32\x18.ntt.monitoring.v4.Alert\"\xa9\x02\n\x12UpdateAlertRequest\x12\'\n\x05\x61lert\x18\x02 \x01(\x0b\x32\x18.ntt.monitoring.v4.Alert\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x36\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32).ntt.monitoring.v4.UpdateAlertRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1aj\n\x03\x43\x41S\x12\x33\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x18.ntt.monitoring.v4.Alert\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\"\n\x12\x44\x65leteAlertRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xb4\x0b\n\x0c\x41lertService\x12\xa2\x01\n\x08GetAlert\x12\".ntt.monitoring.v4.GetAlertRequest\x1a\x18.ntt.monitoring.v4.Alert\"X\x82\xd3\xe4\x93\x02R\x12P/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}\x12\x82\x01\n\x0e\x42\x61tchGetAlerts\x12(.ntt.monitoring.v4.BatchGetAlertsRequest\x1a).ntt.monitoring.v4.BatchGetAlertsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v4/alerts:batchGet\x12\xb3\x01\n\nListAlerts\x12$.ntt.monitoring.v4.ListAlertsRequest\x1a%.ntt.monitoring.v4.ListAlertsResponse\"X\x82\xd3\xe4\x93\x02R\x12P/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts\x12\xbb\x01\n\nWatchAlert\x12$.ntt.monitoring.v4.WatchAlertRequest\x1a%.ntt.monitoring.v4.WatchAlertResponse\"^\x82\xd3\xe4\x93\x02X\"V/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}:watch0\x01\x12\xbe\x01\n\x0bWatchAlerts\x12%.ntt.monitoring.v4.WatchAlertsRequest\x1a&.ntt.monitoring.v4.WatchAlertsResponse\"^\x82\xd3\xe4\x93\x02X\"V/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts:watch0\x01\x12\xaf\x01\n\x0b\x43reateAlert\x12%.ntt.monitoring.v4.CreateAlertRequest\x1a\x18.ntt.monitoring.v4.Alert\"_\x82\xd3\xe4\x93\x02Y\"P/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts:\x05\x61lert\x12\xb5\x01\n\x0bUpdateAlert\x12%.ntt.monitoring.v4.UpdateAlertRequest\x1a\x18.ntt.monitoring.v4.Alert\"e\x82\xd3\xe4\x93\x02_\x1aV/v4/{alert.name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}:\x05\x61lert\x12\xa6\x01\n\x0b\x44\x65leteAlert\x12%.ntt.monitoring.v4.DeleteAlertRequest\x1a\x16.google.protobuf.Empty\"X\x82\xd3\xe4\x93\x02R*P/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comBw\n\x18\x63om.ntt.monitoring.pb.v4B\x11\x41lertServiceProtoP\x00ZFgithub.com/cloudwan/edgelq-sdk/monitoring/client/v4/alert;alert_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.alert_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\021AlertServiceProtoP\000ZFgithub.com/cloudwan/edgelq-sdk/monitoring/client/v4/alert;alert_client'
  _globals['_ALERTSERVICE']._loaded_options = None
  _globals['_ALERTSERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_ALERTSERVICE'].methods_by_name['GetAlert']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['GetAlert']._serialized_options = b'\202\323\344\223\002R\022P/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}'
  _globals['_ALERTSERVICE'].methods_by_name['BatchGetAlerts']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['BatchGetAlerts']._serialized_options = b'\202\323\344\223\002\025\022\023/v4/alerts:batchGet'
  _globals['_ALERTSERVICE'].methods_by_name['ListAlerts']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['ListAlerts']._serialized_options = b'\202\323\344\223\002R\022P/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts'
  _globals['_ALERTSERVICE'].methods_by_name['WatchAlert']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['WatchAlert']._serialized_options = b'\202\323\344\223\002X\"V/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}:watch'
  _globals['_ALERTSERVICE'].methods_by_name['WatchAlerts']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['WatchAlerts']._serialized_options = b'\202\323\344\223\002X\"V/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts:watch'
  _globals['_ALERTSERVICE'].methods_by_name['CreateAlert']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['CreateAlert']._serialized_options = b'\202\323\344\223\002Y\"P/v4/{parent=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}/alerts:\005alert'
  _globals['_ALERTSERVICE'].methods_by_name['UpdateAlert']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['UpdateAlert']._serialized_options = b'\202\323\344\223\002_\032V/v4/{alert.name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}:\005alert'
  _globals['_ALERTSERVICE'].methods_by_name['DeleteAlert']._loaded_options = None
  _globals['_ALERTSERVICE'].methods_by_name['DeleteAlert']._serialized_options = b'\202\323\344\223\002R*P/v4/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*/alerts/*}'
  _globals['_GETALERTREQUEST']._serialized_start=381
  _globals['_GETALERTREQUEST']._serialized_end=493
  _globals['_BATCHGETALERTSREQUEST']._serialized_start=495
  _globals['_BATCHGETALERTSREQUEST']._serialized_end=620
  _globals['_BATCHGETALERTSRESPONSE']._serialized_start=622
  _globals['_BATCHGETALERTSRESPONSE']._serialized_end=705
  _globals['_LISTALERTSREQUEST']._serialized_start=708
  _globals['_LISTALERTSREQUEST']._serialized_end=926
  _globals['_LISTALERTSRESPONSE']._serialized_start=929
  _globals['_LISTALERTSRESPONSE']._serialized_end=1094
  _globals['_WATCHALERTREQUEST']._serialized_start=1096
  _globals['_WATCHALERTREQUEST']._serialized_end=1210
  _globals['_WATCHALERTRESPONSE']._serialized_start=1212
  _globals['_WATCHALERTRESPONSE']._serialized_end=1280
  _globals['_WATCHALERTSREQUEST']._serialized_start=1283
  _globals['_WATCHALERTSREQUEST']._serialized_end=1608
  _globals['_WATCHALERTSRESPONSE']._serialized_start=1611
  _globals['_WATCHALERTSRESPONSE']._serialized_end=1950
  _globals['_WATCHALERTSRESPONSE_PAGETOKENCHANGE']._serialized_start=1883
  _globals['_WATCHALERTSRESPONSE_PAGETOKENCHANGE']._serialized_end=1950
  _globals['_CREATEALERTREQUEST']._serialized_start=1952
  _globals['_CREATEALERTREQUEST']._serialized_end=2029
  _globals['_UPDATEALERTREQUEST']._serialized_start=2032
  _globals['_UPDATEALERTREQUEST']._serialized_end=2329
  _globals['_UPDATEALERTREQUEST_CAS']._serialized_start=2223
  _globals['_UPDATEALERTREQUEST_CAS']._serialized_end=2329
  _globals['_DELETEALERTREQUEST']._serialized_start=2331
  _globals['_DELETEALERTREQUEST']._serialized_end=2365
  _globals['_ALERTSERVICE']._serialized_start=2368
  _globals['_ALERTSERVICE']._serialized_end=3828
# @@protoc_insertion_point(module_scope)