# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1/accepted_plan_service.proto
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
    'edgelq-sdk/limits/proto/v1/accepted_plan_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1 import accepted_plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2
from edgelq_sdk.limits.proto.v1 import accepted_plan_change_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/limits/proto/v1/accepted_plan_service.proto\x12\rntt.limits.v1\x1a.edgelq-sdk/limits/proto/v1/accepted_plan.proto\x1a\x35\x65\x64gelq-sdk/limits/proto/v1/accepted_plan_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"w\n\x16GetAcceptedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x84\x01\n\x1c\x42\x61tchGetAcceptedPlansRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"e\n\x1d\x42\x61tchGetAcceptedPlansResponse\x12\x33\n\x0e\x61\x63\x63\x65pted_plans\x18\x01 \x03(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe1\x01\n\x18ListAcceptedPlansRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xb7\x01\n\x19ListAcceptedPlansResponse\x12\x33\n\x0e\x61\x63\x63\x65pted_plans\x18\x01 \x03(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"y\n\x18WatchAcceptedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"N\n\x19WatchAcceptedPlanResponse\x12\x31\n\x06\x63hange\x18\x01 \x01(\x0b\x32!.ntt.limits.v1.AcceptedPlanChange\"\xcc\x02\n\x19WatchAcceptedPlansRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xe8\x02\n\x1aWatchAcceptedPlansResponse\x12@\n\x15\x61\x63\x63\x65pted_plan_changes\x18\x02 \x03(\x0b\x32!.ntt.limits.v1.AcceptedPlanChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12T\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x39.ntt.limits.v1.WatchAcceptedPlansResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"_\n\x19\x43reateAcceptedPlanRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x32\n\raccepted_plan\x18\x02 \x01(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\"\xc1\x02\n\x19UpdateAcceptedPlanRequest\x12\x32\n\raccepted_plan\x18\x02 \x01(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x39\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32,.ntt.limits.v1.UpdateAcceptedPlanRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1am\n\x03\x43\x41S\x12\x36\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\")\n\x19\x44\x65leteAcceptedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xec\x0c\n\x13\x41\x63\x63\x65ptedPlanService\x12\xb2\x01\n\x0fGetAcceptedPlan\x12%.ntt.limits.v1.GetAcceptedPlanRequest\x1a\x1b.ntt.limits.v1.AcceptedPlan\"[\x82\xd3\xe4\x93\x02U\x12%/v1/{name=services/*/acceptedPlans/*}Z,\x12*/v1/{name=organizations/*/acceptedPlans/*}\x12\x96\x01\n\x15\x42\x61tchGetAcceptedPlans\x12+.ntt.limits.v1.BatchGetAcceptedPlansRequest\x1a,.ntt.limits.v1.BatchGetAcceptedPlansResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/acceptedPlans:batchGet\x12\xc3\x01\n\x11ListAcceptedPlans\x12\'.ntt.limits.v1.ListAcceptedPlansRequest\x1a(.ntt.limits.v1.ListAcceptedPlansResponse\"[\x82\xd3\xe4\x93\x02U\x12%/v1/{parent=services/*}/acceptedPlansZ,\x12*/v1/{parent=organizations/*}/acceptedPlans\x12\xd1\x01\n\x11WatchAcceptedPlan\x12\'.ntt.limits.v1.WatchAcceptedPlanRequest\x1a(.ntt.limits.v1.WatchAcceptedPlanResponse\"g\x82\xd3\xe4\x93\x02\x61\"+/v1/{name=services/*/acceptedPlans/*}:watchZ2\"0/v1/{name=organizations/*/acceptedPlans/*}:watch0\x01\x12\xd4\x01\n\x12WatchAcceptedPlans\x12(.ntt.limits.v1.WatchAcceptedPlansRequest\x1a).ntt.limits.v1.WatchAcceptedPlansResponse\"g\x82\xd3\xe4\x93\x02\x61\"+/v1/{parent=services/*}/acceptedPlans:watchZ2\"0/v1/{parent=organizations/*}/acceptedPlans:watch0\x01\x12\xc7\x01\n\x12\x43reateAcceptedPlan\x12(.ntt.limits.v1.CreateAcceptedPlanRequest\x1a\x1b.ntt.limits.v1.AcceptedPlan\"j\x82\xd3\xe4\x93\x02\x64\"%/v1/{parent=services/*}/acceptedPlans:\raccepted_planZ,\"*/v1/{parent=organizations/*}/acceptedPlans\x12\xe5\x01\n\x12UpdateAcceptedPlan\x12(.ntt.limits.v1.UpdateAcceptedPlanRequest\x1a\x1b.ntt.limits.v1.AcceptedPlan\"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x1a\x33/v1/{accepted_plan.name=services/*/acceptedPlans/*}:\raccepted_planZ:\x1a\x38/v1/{accepted_plan.name=organizations/*/acceptedPlans/*}\x12\xb3\x01\n\x12\x44\x65leteAcceptedPlan\x12(.ntt.limits.v1.DeleteAcceptedPlanRequest\x1a\x16.google.protobuf.Empty\"[\x82\xd3\xe4\x93\x02U*%/v1/{name=services/*/acceptedPlans/*}Z,**/v1/{name=organizations/*/acceptedPlans/*}\x1a.\xca\x41\x11limits.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x86\x01\n\x14\x63om.ntt.limits.pb.v1B\x18\x41\x63\x63\x65ptedPlanServiceProtoP\x00ZRgithub.com/cloudwan/edgelq-sdk/limits/client/v1/accepted_plan;accepted_plan_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1.accepted_plan_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.ntt.limits.pb.v1B\030AcceptedPlanServiceProtoP\000ZRgithub.com/cloudwan/edgelq-sdk/limits/client/v1/accepted_plan;accepted_plan_client'
  _globals['_ACCEPTEDPLANSERVICE']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE']._serialized_options = b'\312A\021limits.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['GetAcceptedPlan']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['GetAcceptedPlan']._serialized_options = b'\202\323\344\223\002U\022%/v1/{name=services/*/acceptedPlans/*}Z,\022*/v1/{name=organizations/*/acceptedPlans/*}'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['BatchGetAcceptedPlans']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['BatchGetAcceptedPlans']._serialized_options = b'\202\323\344\223\002\034\022\032/v1/acceptedPlans:batchGet'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['ListAcceptedPlans']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['ListAcceptedPlans']._serialized_options = b'\202\323\344\223\002U\022%/v1/{parent=services/*}/acceptedPlansZ,\022*/v1/{parent=organizations/*}/acceptedPlans'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['WatchAcceptedPlan']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['WatchAcceptedPlan']._serialized_options = b'\202\323\344\223\002a\"+/v1/{name=services/*/acceptedPlans/*}:watchZ2\"0/v1/{name=organizations/*/acceptedPlans/*}:watch'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['WatchAcceptedPlans']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['WatchAcceptedPlans']._serialized_options = b'\202\323\344\223\002a\"+/v1/{parent=services/*}/acceptedPlans:watchZ2\"0/v1/{parent=organizations/*}/acceptedPlans:watch'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['CreateAcceptedPlan']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['CreateAcceptedPlan']._serialized_options = b'\202\323\344\223\002d\"%/v1/{parent=services/*}/acceptedPlans:\raccepted_planZ,\"*/v1/{parent=organizations/*}/acceptedPlans'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['UpdateAcceptedPlan']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['UpdateAcceptedPlan']._serialized_options = b'\202\323\344\223\002\200\001\0323/v1/{accepted_plan.name=services/*/acceptedPlans/*}:\raccepted_planZ:\0328/v1/{accepted_plan.name=organizations/*/acceptedPlans/*}'
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['DeleteAcceptedPlan']._loaded_options = None
  _globals['_ACCEPTEDPLANSERVICE'].methods_by_name['DeleteAcceptedPlan']._serialized_options = b'\202\323\344\223\002U*%/v1/{name=services/*/acceptedPlans/*}Z,**/v1/{name=organizations/*/acceptedPlans/*}'
  _globals['_GETACCEPTEDPLANREQUEST']._serialized_start=389
  _globals['_GETACCEPTEDPLANREQUEST']._serialized_end=508
  _globals['_BATCHGETACCEPTEDPLANSREQUEST']._serialized_start=511
  _globals['_BATCHGETACCEPTEDPLANSREQUEST']._serialized_end=643
  _globals['_BATCHGETACCEPTEDPLANSRESPONSE']._serialized_start=645
  _globals['_BATCHGETACCEPTEDPLANSRESPONSE']._serialized_end=746
  _globals['_LISTACCEPTEDPLANSREQUEST']._serialized_start=749
  _globals['_LISTACCEPTEDPLANSREQUEST']._serialized_end=974
  _globals['_LISTACCEPTEDPLANSRESPONSE']._serialized_start=977
  _globals['_LISTACCEPTEDPLANSRESPONSE']._serialized_end=1160
  _globals['_WATCHACCEPTEDPLANREQUEST']._serialized_start=1162
  _globals['_WATCHACCEPTEDPLANREQUEST']._serialized_end=1283
  _globals['_WATCHACCEPTEDPLANRESPONSE']._serialized_start=1285
  _globals['_WATCHACCEPTEDPLANRESPONSE']._serialized_end=1363
  _globals['_WATCHACCEPTEDPLANSREQUEST']._serialized_start=1366
  _globals['_WATCHACCEPTEDPLANSREQUEST']._serialized_end=1698
  _globals['_WATCHACCEPTEDPLANSRESPONSE']._serialized_start=1701
  _globals['_WATCHACCEPTEDPLANSRESPONSE']._serialized_end=2061
  _globals['_WATCHACCEPTEDPLANSRESPONSE_PAGETOKENCHANGE']._serialized_start=1994
  _globals['_WATCHACCEPTEDPLANSRESPONSE_PAGETOKENCHANGE']._serialized_end=2061
  _globals['_CREATEACCEPTEDPLANREQUEST']._serialized_start=2063
  _globals['_CREATEACCEPTEDPLANREQUEST']._serialized_end=2158
  _globals['_UPDATEACCEPTEDPLANREQUEST']._serialized_start=2161
  _globals['_UPDATEACCEPTEDPLANREQUEST']._serialized_end=2482
  _globals['_UPDATEACCEPTEDPLANREQUEST_CAS']._serialized_start=2373
  _globals['_UPDATEACCEPTEDPLANREQUEST_CAS']._serialized_end=2482
  _globals['_DELETEACCEPTEDPLANREQUEST']._serialized_start=2484
  _globals['_DELETEACCEPTEDPLANREQUEST']._serialized_end=2525
  _globals['_ACCEPTEDPLANSERVICE']._serialized_start=2528
  _globals['_ACCEPTEDPLANSERVICE']._serialized_end=4172
# @@protoc_insertion_point(module_scope)
