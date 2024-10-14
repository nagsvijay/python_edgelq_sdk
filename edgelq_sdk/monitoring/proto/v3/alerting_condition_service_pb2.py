# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v3/alerting_condition_service.proto
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
    'edgelq-sdk/monitoring/proto/v3/alerting_condition_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v3 import alerting_condition_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__condition__pb2
from edgelq_sdk.monitoring.proto.v3 import alerting_condition_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__condition__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/monitoring/proto/v3/alerting_condition_service.proto\x12\x11ntt.monitoring.v3\x1a\x37\x65\x64gelq-sdk/monitoring/proto/v3/alerting_condition.proto\x1a>edgelq-sdk/monitoring/proto/v3/alerting_condition_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"|\n\x1bGetAlertingConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x89\x01\n!BatchGetAlertingConditionsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"x\n\"BatchGetAlertingConditionsResponse\x12\x41\n\x13\x61lerting_conditions\x18\x01 \x03(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe6\x01\n\x1dListAlertingConditionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xca\x01\n\x1eListAlertingConditionsResponse\x12\x41\n\x13\x61lerting_conditions\x18\x01 \x03(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"~\n\x1dWatchAlertingConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\\\n\x1eWatchAlertingConditionResponse\x12:\n\x06\x63hange\x18\x01 \x01(\x0b\x32*.ntt.monitoring.v3.AlertingConditionChange\"\xd1\x02\n\x1eWatchAlertingConditionsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\x84\x03\n\x1fWatchAlertingConditionsResponse\x12N\n\x1a\x61lerting_condition_changes\x18\x02 \x03(\x0b\x32*.ntt.monitoring.v3.AlertingConditionChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12]\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x42.ntt.monitoring.v3.WatchAlertingConditionsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"r\n\x1e\x43reateAlertingConditionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x12\x61lerting_condition\x18\x02 \x01(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\"\xe6\x02\n\x1eUpdateAlertingConditionRequest\x12@\n\x12\x61lerting_condition\x18\x02 \x01(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x42\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\x35.ntt.monitoring.v3.UpdateAlertingConditionRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1av\n\x03\x43\x41S\x12?\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\".\n\x1e\x44\x65leteAlertingConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xdb\x01\n\x1fSearchAlertingConditionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x0e\n\x06phrase\x18\x08 \x01(\t\"\xcc\x01\n SearchAlertingConditionsResponse\x12\x41\n\x13\x61lerting_conditions\x18\x01 \x03(\x0b\x32$.ntt.monitoring.v3.AlertingCondition\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\x32\xa6\x0f\n\x18\x41lertingConditionService\x12\xbd\x01\n\x14GetAlertingCondition\x12..ntt.monitoring.v3.GetAlertingConditionRequest\x1a$.ntt.monitoring.v3.AlertingCondition\"O\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}\x12\xb2\x01\n\x1a\x42\x61tchGetAlertingConditions\x12\x34.ntt.monitoring.v3.BatchGetAlertingConditionsRequest\x1a\x35.ntt.monitoring.v3.BatchGetAlertingConditionsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v3/alertingConditions:batchGet\x12\xce\x01\n\x16ListAlertingConditions\x12\x30.ntt.monitoring.v3.ListAlertingConditionsRequest\x1a\x31.ntt.monitoring.v3.ListAlertingConditionsResponse\"O\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions\x12\xd6\x01\n\x16WatchAlertingCondition\x12\x30.ntt.monitoring.v3.WatchAlertingConditionRequest\x1a\x31.ntt.monitoring.v3.WatchAlertingConditionResponse\"U\x82\xd3\xe4\x93\x02O\"M/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}:watch0\x01\x12\xd9\x01\n\x17WatchAlertingConditions\x12\x31.ntt.monitoring.v3.WatchAlertingConditionsRequest\x1a\x32.ntt.monitoring.v3.WatchAlertingConditionsResponse\"U\x82\xd3\xe4\x93\x02O\"M/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:watch0\x01\x12\xd7\x01\n\x17\x43reateAlertingCondition\x12\x31.ntt.monitoring.v3.CreateAlertingConditionRequest\x1a$.ntt.monitoring.v3.AlertingCondition\"c\x82\xd3\xe4\x93\x02]\"G/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:\x12\x61lerting_condition\x12\xea\x01\n\x17UpdateAlertingCondition\x12\x31.ntt.monitoring.v3.UpdateAlertingConditionRequest\x1a$.ntt.monitoring.v3.AlertingCondition\"v\x82\xd3\xe4\x93\x02p\x1aZ/v3/{alerting_condition.name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}:\x12\x61lerting_condition\x12\xb5\x01\n\x17\x44\x65leteAlertingCondition\x12\x31.ntt.monitoring.v3.DeleteAlertingConditionRequest\x1a\x16.google.protobuf.Empty\"O\x82\xd3\xe4\x93\x02I*G/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}\x12\xdb\x01\n\x18SearchAlertingConditions\x12\x32.ntt.monitoring.v3.SearchAlertingConditionsRequest\x1a\x33.ntt.monitoring.v3.SearchAlertingConditionsResponse\"V\x82\xd3\xe4\x93\x02P\x12N/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:search\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x9d\x01\n\x18\x63om.ntt.monitoring.pb.v3B\x1d\x41lertingConditionServiceProtoP\x00Z`github.com/cloudwan/edgelq-sdk/monitoring/client/v3/alerting_condition;alerting_condition_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v3.alerting_condition_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v3B\035AlertingConditionServiceProtoP\000Z`github.com/cloudwan/edgelq-sdk/monitoring/client/v3/alerting_condition;alerting_condition_client'
  _globals['_ALERTINGCONDITIONSERVICE']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['GetAlertingCondition']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['GetAlertingCondition']._serialized_options = b'\202\323\344\223\002I\022G/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['BatchGetAlertingConditions']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['BatchGetAlertingConditions']._serialized_options = b'\202\323\344\223\002!\022\037/v3/alertingConditions:batchGet'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['ListAlertingConditions']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['ListAlertingConditions']._serialized_options = b'\202\323\344\223\002I\022G/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['WatchAlertingCondition']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['WatchAlertingCondition']._serialized_options = b'\202\323\344\223\002O\"M/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}:watch'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['WatchAlertingConditions']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['WatchAlertingConditions']._serialized_options = b'\202\323\344\223\002O\"M/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:watch'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['CreateAlertingCondition']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['CreateAlertingCondition']._serialized_options = b'\202\323\344\223\002]\"G/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:\022alerting_condition'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['UpdateAlertingCondition']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['UpdateAlertingCondition']._serialized_options = b'\202\323\344\223\002p\032Z/v3/{alerting_condition.name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}:\022alerting_condition'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['DeleteAlertingCondition']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['DeleteAlertingCondition']._serialized_options = b'\202\323\344\223\002I*G/v3/{name=projects/*/regions/*/alertingPolicies/*/alertingConditions/*}'
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['SearchAlertingConditions']._loaded_options = None
  _globals['_ALERTINGCONDITIONSERVICE'].methods_by_name['SearchAlertingConditions']._serialized_options = b'\202\323\344\223\002P\022N/v3/{parent=projects/*/regions/*/alertingPolicies/*}/alertingConditions:search'
  _globals['_GETALERTINGCONDITIONREQUEST']._serialized_start=420
  _globals['_GETALERTINGCONDITIONREQUEST']._serialized_end=544
  _globals['_BATCHGETALERTINGCONDITIONSREQUEST']._serialized_start=547
  _globals['_BATCHGETALERTINGCONDITIONSREQUEST']._serialized_end=684
  _globals['_BATCHGETALERTINGCONDITIONSRESPONSE']._serialized_start=686
  _globals['_BATCHGETALERTINGCONDITIONSRESPONSE']._serialized_end=806
  _globals['_LISTALERTINGCONDITIONSREQUEST']._serialized_start=809
  _globals['_LISTALERTINGCONDITIONSREQUEST']._serialized_end=1039
  _globals['_LISTALERTINGCONDITIONSRESPONSE']._serialized_start=1042
  _globals['_LISTALERTINGCONDITIONSRESPONSE']._serialized_end=1244
  _globals['_WATCHALERTINGCONDITIONREQUEST']._serialized_start=1246
  _globals['_WATCHALERTINGCONDITIONREQUEST']._serialized_end=1372
  _globals['_WATCHALERTINGCONDITIONRESPONSE']._serialized_start=1374
  _globals['_WATCHALERTINGCONDITIONRESPONSE']._serialized_end=1466
  _globals['_WATCHALERTINGCONDITIONSREQUEST']._serialized_start=1469
  _globals['_WATCHALERTINGCONDITIONSREQUEST']._serialized_end=1806
  _globals['_WATCHALERTINGCONDITIONSRESPONSE']._serialized_start=1809
  _globals['_WATCHALERTINGCONDITIONSRESPONSE']._serialized_end=2197
  _globals['_WATCHALERTINGCONDITIONSRESPONSE_PAGETOKENCHANGE']._serialized_start=2130
  _globals['_WATCHALERTINGCONDITIONSRESPONSE_PAGETOKENCHANGE']._serialized_end=2197
  _globals['_CREATEALERTINGCONDITIONREQUEST']._serialized_start=2199
  _globals['_CREATEALERTINGCONDITIONREQUEST']._serialized_end=2313
  _globals['_UPDATEALERTINGCONDITIONREQUEST']._serialized_start=2316
  _globals['_UPDATEALERTINGCONDITIONREQUEST']._serialized_end=2674
  _globals['_UPDATEALERTINGCONDITIONREQUEST_CAS']._serialized_start=2556
  _globals['_UPDATEALERTINGCONDITIONREQUEST_CAS']._serialized_end=2674
  _globals['_DELETEALERTINGCONDITIONREQUEST']._serialized_start=2676
  _globals['_DELETEALERTINGCONDITIONREQUEST']._serialized_end=2722
  _globals['_SEARCHALERTINGCONDITIONSREQUEST']._serialized_start=2725
  _globals['_SEARCHALERTINGCONDITIONSREQUEST']._serialized_end=2944
  _globals['_SEARCHALERTINGCONDITIONSRESPONSE']._serialized_start=2947
  _globals['_SEARCHALERTINGCONDITIONSRESPONSE']._serialized_end=3151
  _globals['_ALERTINGCONDITIONSERVICE']._serialized_start=3154
  _globals['_ALERTINGCONDITIONSERVICE']._serialized_end=5112
# @@protoc_insertion_point(module_scope)
