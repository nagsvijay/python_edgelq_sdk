# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/plan_assignment_service.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/plan_assignment_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_change_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__change__pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_custom_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>edgelq-sdk/limits/proto/v1alpha2/plan_assignment_service.proto\x12\x13ntt.limits.v1alpha2\x1a\x36\x65\x64gelq-sdk/limits/proto/v1alpha2/plan_assignment.proto\x1a=edgelq-sdk/limits/proto/v1alpha2/plan_assignment_change.proto\x1a=edgelq-sdk/limits/proto/v1alpha2/plan_assignment_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"y\n\x18GetPlanAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x86\x01\n\x1e\x42\x61tchGetPlanAssignmentsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"q\n\x1f\x42\x61tchGetPlanAssignmentsResponse\x12=\n\x10plan_assignments\x18\x01 \x03(\x0b\x32#.ntt.limits.v1alpha2.PlanAssignment\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe3\x01\n\x1aListPlanAssignmentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xc3\x01\n\x1bListPlanAssignmentsResponse\x12=\n\x10plan_assignments\x18\x01 \x03(\x0b\x32#.ntt.limits.v1alpha2.PlanAssignment\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"{\n\x1aWatchPlanAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"X\n\x1bWatchPlanAssignmentResponse\x12\x39\n\x06\x63hange\x18\x01 \x01(\x0b\x32).ntt.limits.v1alpha2.PlanAssignmentChange\"\xce\x02\n\x1bWatchPlanAssignmentsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xfc\x02\n\x1cWatchPlanAssignmentsResponse\x12J\n\x17plan_assignment_changes\x18\x02 \x03(\x0b\x32).ntt.limits.v1alpha2.PlanAssignmentChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\\\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x41.ntt.limits.v1alpha2.WatchPlanAssignmentsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"k\n\x1b\x43reatePlanAssignmentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12<\n\x0fplan_assignment\x18\x02 \x01(\x0b\x32#.ntt.limits.v1alpha2.PlanAssignment\"\xdd\x02\n\x1bUpdatePlanAssignmentRequest\x12<\n\x0fplan_assignment\x18\x02 \x01(\x0b\x32#.ntt.limits.v1alpha2.PlanAssignment\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x41\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\x34.ntt.limits.v1alpha2.UpdatePlanAssignmentRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1au\n\x03\x43\x41S\x12>\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32#.ntt.limits.v1alpha2.PlanAssignment\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"+\n\x1b\x44\x65letePlanAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xed\x13\n\x15PlanAssignmentService\x12\xfc\x01\n\x11GetPlanAssignment\x12-.ntt.limits.v1alpha2.GetPlanAssignmentRequest\x1a#.ntt.limits.v1alpha2.PlanAssignment\"\x92\x01\x82\xd3\xe4\x93\x02\x8b\x01\x12\"/v1alpha2/{name=planAssignments/*}Z/\x12-/v1alpha2/{name=projects/*/planAssignments/*}Z4\x12\x32/v1alpha2/{name=organizations/*/planAssignments/*}\x12\xb0\x01\n\x17\x42\x61tchGetPlanAssignments\x12\x33.ntt.limits.v1alpha2.BatchGetPlanAssignmentsRequest\x1a\x34.ntt.limits.v1alpha2.BatchGetPlanAssignmentsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1alpha2/planAssignments:batchGet\x12\x84\x02\n\x13ListPlanAssignments\x12/.ntt.limits.v1alpha2.ListPlanAssignmentsRequest\x1a\x30.ntt.limits.v1alpha2.ListPlanAssignmentsResponse\"\x89\x01\x82\xd3\xe4\x93\x02\x82\x01\x12\x19/v1alpha2/planAssignmentsZ/\x12-/v1alpha2/{parent=projects/*}/planAssignmentsZ4\x12\x32/v1alpha2/{parent=organizations/*}/planAssignments\x12\xa1\x02\n\x13WatchPlanAssignment\x12/.ntt.limits.v1alpha2.WatchPlanAssignmentRequest\x1a\x30.ntt.limits.v1alpha2.WatchPlanAssignmentResponse\"\xa4\x01\x82\xd3\xe4\x93\x02\x9d\x01\"(/v1alpha2/{name=planAssignments/*}:watchZ5\"3/v1alpha2/{name=projects/*/planAssignments/*}:watchZ:\"8/v1alpha2/{name=organizations/*/planAssignments/*}:watch0\x01\x12\x9b\x02\n\x14WatchPlanAssignments\x12\x30.ntt.limits.v1alpha2.WatchPlanAssignmentsRequest\x1a\x31.ntt.limits.v1alpha2.WatchPlanAssignmentsResponse\"\x9b\x01\x82\xd3\xe4\x93\x02\x94\x01\"\x1f/v1alpha2/planAssignments:watchZ5\"3/v1alpha2/{parent=projects/*}/planAssignments:watchZ:\"8/v1alpha2/{parent=organizations/*}/planAssignments:watch0\x01\x12\x8a\x02\n\x14\x43reatePlanAssignment\x12\x30.ntt.limits.v1alpha2.CreatePlanAssignmentRequest\x1a#.ntt.limits.v1alpha2.PlanAssignment\"\x9a\x01\x82\xd3\xe4\x93\x02\x93\x01\"\x19/v1alpha2/planAssignments:\x0fplan_assignmentZ/\"-/v1alpha2/{parent=projects/*}/planAssignmentsZ4\"2/v1alpha2/{parent=organizations/*}/planAssignments\x12\xc3\x02\n\x14UpdatePlanAssignment\x12\x30.ntt.limits.v1alpha2.UpdatePlanAssignmentRequest\x1a#.ntt.limits.v1alpha2.PlanAssignment\"\xd3\x01\x82\xd3\xe4\x93\x02\xcc\x01\x1a\x32/v1alpha2/{plan_assignment.name=planAssignments/*}:\x0fplan_assignmentZ?\x1a=/v1alpha2/{plan_assignment.name=projects/*/planAssignments/*}ZD\x1a\x42/v1alpha2/{plan_assignment.name=organizations/*/planAssignments/*}\x12\xf5\x01\n\x14\x44\x65letePlanAssignment\x12\x30.ntt.limits.v1alpha2.DeletePlanAssignmentRequest\x1a\x16.google.protobuf.Empty\"\x92\x01\x82\xd3\xe4\x93\x02\x8b\x01*\"/v1alpha2/{name=planAssignments/*}Z/*-/v1alpha2/{name=projects/*/planAssignments/*}Z4*2/v1alpha2/{name=organizations/*/planAssignments/*}\x12\xdd\x02\n\x15MigratePlanAssignment\x12\x31.ntt.limits.v1alpha2.MigratePlanAssignmentRequest\x1a#.ntt.limits.v1alpha2.PlanAssignment\"\xeb\x01\x82\xd3\xe4\x93\x02\xe4\x01\x1a:/v1alpha2/{plan_assignment.name=planAssignments/*}:migrate:\x0fplan_assignmentZG\x1a\x45/v1alpha2/{plan_assignment.name=projects/*/planAssignments/*}:migrateZL\x1aJ/v1alpha2/{plan_assignment.name=organizations/*/planAssignments/*}:migrate\x1a.\xca\x41\x11limits.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x98\x01\n\x1a\x63om.ntt.limits.pb.v1alpha2B\x1aPlanAssignmentServiceProtoP\x00Z\\github.com/cloudwan/edgelq-sdk/limits/client/v1alpha2/plan_assignment;plan_assignment_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.plan_assignment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\032PlanAssignmentServiceProtoP\000Z\\github.com/cloudwan/edgelq-sdk/limits/client/v1alpha2/plan_assignment;plan_assignment_client'
  _globals['_PLANASSIGNMENTSERVICE']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE']._serialized_options = b'\312A\021limits.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['GetPlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['GetPlanAssignment']._serialized_options = b'\202\323\344\223\002\213\001\022\"/v1alpha2/{name=planAssignments/*}Z/\022-/v1alpha2/{name=projects/*/planAssignments/*}Z4\0222/v1alpha2/{name=organizations/*/planAssignments/*}'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['BatchGetPlanAssignments']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['BatchGetPlanAssignments']._serialized_options = b'\202\323\344\223\002$\022\"/v1alpha2/planAssignments:batchGet'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['ListPlanAssignments']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['ListPlanAssignments']._serialized_options = b'\202\323\344\223\002\202\001\022\031/v1alpha2/planAssignmentsZ/\022-/v1alpha2/{parent=projects/*}/planAssignmentsZ4\0222/v1alpha2/{parent=organizations/*}/planAssignments'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['WatchPlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['WatchPlanAssignment']._serialized_options = b'\202\323\344\223\002\235\001\"(/v1alpha2/{name=planAssignments/*}:watchZ5\"3/v1alpha2/{name=projects/*/planAssignments/*}:watchZ:\"8/v1alpha2/{name=organizations/*/planAssignments/*}:watch'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['WatchPlanAssignments']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['WatchPlanAssignments']._serialized_options = b'\202\323\344\223\002\224\001\"\037/v1alpha2/planAssignments:watchZ5\"3/v1alpha2/{parent=projects/*}/planAssignments:watchZ:\"8/v1alpha2/{parent=organizations/*}/planAssignments:watch'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['CreatePlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['CreatePlanAssignment']._serialized_options = b'\202\323\344\223\002\223\001\"\031/v1alpha2/planAssignments:\017plan_assignmentZ/\"-/v1alpha2/{parent=projects/*}/planAssignmentsZ4\"2/v1alpha2/{parent=organizations/*}/planAssignments'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['UpdatePlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['UpdatePlanAssignment']._serialized_options = b'\202\323\344\223\002\314\001\0322/v1alpha2/{plan_assignment.name=planAssignments/*}:\017plan_assignmentZ?\032=/v1alpha2/{plan_assignment.name=projects/*/planAssignments/*}ZD\032B/v1alpha2/{plan_assignment.name=organizations/*/planAssignments/*}'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['DeletePlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['DeletePlanAssignment']._serialized_options = b'\202\323\344\223\002\213\001*\"/v1alpha2/{name=planAssignments/*}Z/*-/v1alpha2/{name=projects/*/planAssignments/*}Z4*2/v1alpha2/{name=organizations/*/planAssignments/*}'
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['MigratePlanAssignment']._loaded_options = None
  _globals['_PLANASSIGNMENTSERVICE'].methods_by_name['MigratePlanAssignment']._serialized_options = b'\202\323\344\223\002\344\001\032:/v1alpha2/{plan_assignment.name=planAssignments/*}:migrate:\017plan_assignmentZG\032E/v1alpha2/{plan_assignment.name=projects/*/planAssignments/*}:migrateZL\032J/v1alpha2/{plan_assignment.name=organizations/*/planAssignments/*}:migrate'
  _globals['_GETPLANASSIGNMENTREQUEST']._serialized_start=482
  _globals['_GETPLANASSIGNMENTREQUEST']._serialized_end=603
  _globals['_BATCHGETPLANASSIGNMENTSREQUEST']._serialized_start=606
  _globals['_BATCHGETPLANASSIGNMENTSREQUEST']._serialized_end=740
  _globals['_BATCHGETPLANASSIGNMENTSRESPONSE']._serialized_start=742
  _globals['_BATCHGETPLANASSIGNMENTSRESPONSE']._serialized_end=855
  _globals['_LISTPLANASSIGNMENTSREQUEST']._serialized_start=858
  _globals['_LISTPLANASSIGNMENTSREQUEST']._serialized_end=1085
  _globals['_LISTPLANASSIGNMENTSRESPONSE']._serialized_start=1088
  _globals['_LISTPLANASSIGNMENTSRESPONSE']._serialized_end=1283
  _globals['_WATCHPLANASSIGNMENTREQUEST']._serialized_start=1285
  _globals['_WATCHPLANASSIGNMENTREQUEST']._serialized_end=1408
  _globals['_WATCHPLANASSIGNMENTRESPONSE']._serialized_start=1410
  _globals['_WATCHPLANASSIGNMENTRESPONSE']._serialized_end=1498
  _globals['_WATCHPLANASSIGNMENTSREQUEST']._serialized_start=1501
  _globals['_WATCHPLANASSIGNMENTSREQUEST']._serialized_end=1835
  _globals['_WATCHPLANASSIGNMENTSRESPONSE']._serialized_start=1838
  _globals['_WATCHPLANASSIGNMENTSRESPONSE']._serialized_end=2218
  _globals['_WATCHPLANASSIGNMENTSRESPONSE_PAGETOKENCHANGE']._serialized_start=2151
  _globals['_WATCHPLANASSIGNMENTSRESPONSE_PAGETOKENCHANGE']._serialized_end=2218
  _globals['_CREATEPLANASSIGNMENTREQUEST']._serialized_start=2220
  _globals['_CREATEPLANASSIGNMENTREQUEST']._serialized_end=2327
  _globals['_UPDATEPLANASSIGNMENTREQUEST']._serialized_start=2330
  _globals['_UPDATEPLANASSIGNMENTREQUEST']._serialized_end=2679
  _globals['_UPDATEPLANASSIGNMENTREQUEST_CAS']._serialized_start=2562
  _globals['_UPDATEPLANASSIGNMENTREQUEST_CAS']._serialized_end=2679
  _globals['_DELETEPLANASSIGNMENTREQUEST']._serialized_start=2681
  _globals['_DELETEPLANASSIGNMENTREQUEST']._serialized_end=2724
  _globals['_PLANASSIGNMENTSERVICE']._serialized_start=2727
  _globals['_PLANASSIGNMENTSERVICE']._serialized_end=5268
# @@protoc_insertion_point(module_scope)
