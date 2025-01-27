# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/member_assignment_service.proto
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
    'edgelq-sdk/iam/proto/v1/member_assignment_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import member_assignment_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2
from edgelq_sdk.iam.proto.v1 import member_assignment_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/iam/proto/v1/member_assignment_service.proto\x12\nntt.iam.v1\x1a/edgelq-sdk/iam/proto/v1/member_assignment.proto\x1a\x36\x65\x64gelq-sdk/iam/proto/v1/member_assignment_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"{\n\x1aGetMemberAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x88\x01\n BatchGetMemberAssignmentsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"n\n!BatchGetMemberAssignmentsResponse\x12\x38\n\x12member_assignments\x18\x01 \x03(\x0b\x32\x1c.ntt.iam.v1.MemberAssignment\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe5\x01\n\x1cListMemberAssignmentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xc0\x01\n\x1dListMemberAssignmentsResponse\x12\x38\n\x12member_assignments\x18\x01 \x03(\x0b\x32\x1c.ntt.iam.v1.MemberAssignment\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"}\n\x1cWatchMemberAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"S\n\x1dWatchMemberAssignmentResponse\x12\x32\n\x06\x63hange\x18\x01 \x01(\x0b\x32\".ntt.iam.v1.MemberAssignmentChange\"\xd0\x02\n\x1dWatchMemberAssignmentsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xf2\x02\n\x1eWatchMemberAssignmentsResponse\x12\x45\n\x19member_assignment_changes\x18\x02 \x03(\x0b\x32\".ntt.iam.v1.MemberAssignmentChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12U\n\x11page_token_change\x18\x03 \x01(\x0b\x32:.ntt.iam.v1.WatchMemberAssignmentsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb5\x02\n\x1dUpdateMemberAssignmentRequest\x12\x37\n\x11member_assignment\x18\x02 \x01(\x0b\x32\x1c.ntt.iam.v1.MemberAssignment\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12:\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32-.ntt.iam.v1.UpdateMemberAssignmentRequest.CAS\x1an\n\x03\x43\x41S\x12\x37\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1c.ntt.iam.v1.MemberAssignment\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"-\n\x1d\x44\x65leteMemberAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xba\t\n\x17MemberAssignmentService\x12\x8d\x01\n\x13GetMemberAssignment\x12&.ntt.iam.v1.GetMemberAssignmentRequest\x1a\x1c.ntt.iam.v1.MemberAssignment\"0\x82\xd3\xe4\x93\x02*\x12(/v1/{name=regions/*/memberAssignments/*}\x12\xa0\x01\n\x19\x42\x61tchGetMemberAssignments\x12,.ntt.iam.v1.BatchGetMemberAssignmentsRequest\x1a-.ntt.iam.v1.BatchGetMemberAssignmentsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/memberAssignments:batchGet\x12\x9e\x01\n\x15ListMemberAssignments\x12(.ntt.iam.v1.ListMemberAssignmentsRequest\x1a).ntt.iam.v1.ListMemberAssignmentsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=regions/*}/memberAssignments\x12\xa6\x01\n\x15WatchMemberAssignment\x12(.ntt.iam.v1.WatchMemberAssignmentRequest\x1a).ntt.iam.v1.WatchMemberAssignmentResponse\"6\x82\xd3\xe4\x93\x02\x30\"./v1/{name=regions/*/memberAssignments/*}:watch0\x01\x12\xa9\x01\n\x16WatchMemberAssignments\x12).ntt.iam.v1.WatchMemberAssignmentsRequest\x1a*.ntt.iam.v1.WatchMemberAssignmentsResponse\"6\x82\xd3\xe4\x93\x02\x30\"./v1/{parent=regions/*}/memberAssignments:watch0\x01\x12\xb8\x01\n\x16UpdateMemberAssignment\x12).ntt.iam.v1.UpdateMemberAssignmentRequest\x1a\x1c.ntt.iam.v1.MemberAssignment\"U\x82\xd3\xe4\x93\x02O\x1a:/v1/{member_assignment.name=regions/*/memberAssignments/*}:\x11member_assignment\x12\x8d\x01\n\x16\x44\x65leteMemberAssignment\x12).ntt.iam.v1.DeleteMemberAssignmentRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02**(/v1/{name=regions/*/memberAssignments/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x8c\x01\n\x11\x63om.ntt.iam.pb.v1B\x1cMemberAssignmentServiceProtoP\x00ZWgithub.com/cloudwan/edgelq-sdk/iam/client/v1/member_assignment;member_assignment_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.member_assignment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\034MemberAssignmentServiceProtoP\000ZWgithub.com/cloudwan/edgelq-sdk/iam/client/v1/member_assignment;member_assignment_client'
  _globals['_MEMBERASSIGNMENTSERVICE']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['GetMemberAssignment']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['GetMemberAssignment']._serialized_options = b'\202\323\344\223\002*\022(/v1/{name=regions/*/memberAssignments/*}'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['BatchGetMemberAssignments']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['BatchGetMemberAssignments']._serialized_options = b'\202\323\344\223\002 \022\036/v1/memberAssignments:batchGet'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['ListMemberAssignments']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['ListMemberAssignments']._serialized_options = b'\202\323\344\223\002*\022(/v1/{parent=regions/*}/memberAssignments'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['WatchMemberAssignment']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['WatchMemberAssignment']._serialized_options = b'\202\323\344\223\0020\"./v1/{name=regions/*/memberAssignments/*}:watch'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['WatchMemberAssignments']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['WatchMemberAssignments']._serialized_options = b'\202\323\344\223\0020\"./v1/{parent=regions/*}/memberAssignments:watch'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['UpdateMemberAssignment']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['UpdateMemberAssignment']._serialized_options = b'\202\323\344\223\002O\032:/v1/{member_assignment.name=regions/*/memberAssignments/*}:\021member_assignment'
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['DeleteMemberAssignment']._loaded_options = None
  _globals['_MEMBERASSIGNMENTSERVICE'].methods_by_name['DeleteMemberAssignment']._serialized_options = b'\202\323\344\223\002**(/v1/{name=regions/*/memberAssignments/*}'
  _globals['_GETMEMBERASSIGNMENTREQUEST']._serialized_start=389
  _globals['_GETMEMBERASSIGNMENTREQUEST']._serialized_end=512
  _globals['_BATCHGETMEMBERASSIGNMENTSREQUEST']._serialized_start=515
  _globals['_BATCHGETMEMBERASSIGNMENTSREQUEST']._serialized_end=651
  _globals['_BATCHGETMEMBERASSIGNMENTSRESPONSE']._serialized_start=653
  _globals['_BATCHGETMEMBERASSIGNMENTSRESPONSE']._serialized_end=763
  _globals['_LISTMEMBERASSIGNMENTSREQUEST']._serialized_start=766
  _globals['_LISTMEMBERASSIGNMENTSREQUEST']._serialized_end=995
  _globals['_LISTMEMBERASSIGNMENTSRESPONSE']._serialized_start=998
  _globals['_LISTMEMBERASSIGNMENTSRESPONSE']._serialized_end=1190
  _globals['_WATCHMEMBERASSIGNMENTREQUEST']._serialized_start=1192
  _globals['_WATCHMEMBERASSIGNMENTREQUEST']._serialized_end=1317
  _globals['_WATCHMEMBERASSIGNMENTRESPONSE']._serialized_start=1319
  _globals['_WATCHMEMBERASSIGNMENTRESPONSE']._serialized_end=1402
  _globals['_WATCHMEMBERASSIGNMENTSREQUEST']._serialized_start=1405
  _globals['_WATCHMEMBERASSIGNMENTSREQUEST']._serialized_end=1741
  _globals['_WATCHMEMBERASSIGNMENTSRESPONSE']._serialized_start=1744
  _globals['_WATCHMEMBERASSIGNMENTSRESPONSE']._serialized_end=2114
  _globals['_WATCHMEMBERASSIGNMENTSRESPONSE_PAGETOKENCHANGE']._serialized_start=2047
  _globals['_WATCHMEMBERASSIGNMENTSRESPONSE_PAGETOKENCHANGE']._serialized_end=2114
  _globals['_UPDATEMEMBERASSIGNMENTREQUEST']._serialized_start=2117
  _globals['_UPDATEMEMBERASSIGNMENTREQUEST']._serialized_end=2426
  _globals['_UPDATEMEMBERASSIGNMENTREQUEST_CAS']._serialized_start=2316
  _globals['_UPDATEMEMBERASSIGNMENTREQUEST_CAS']._serialized_end=2426
  _globals['_DELETEMEMBERASSIGNMENTREQUEST']._serialized_start=2428
  _globals['_DELETEMEMBERASSIGNMENTREQUEST']._serialized_end=2473
  _globals['_MEMBERASSIGNMENTSERVICE']._serialized_start=2476
  _globals['_MEMBERASSIGNMENTSERVICE']._serialized_end=3686
# @@protoc_insertion_point(module_scope)
