# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/group_member_service.proto
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
    'edgelq-sdk/iam/proto/v1/group_member_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import group_member_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2
from edgelq_sdk.iam.proto.v1 import group_member_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/iam/proto/v1/group_member_service.proto\x12\nntt.iam.v1\x1a*edgelq-sdk/iam/proto/v1/group_member.proto\x1a\x31\x65\x64gelq-sdk/iam/proto/v1/group_member_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"v\n\x15GetGroupMemberRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x83\x01\n\x1b\x42\x61tchGetGroupMembersRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"_\n\x1c\x42\x61tchGetGroupMembersResponse\x12.\n\rgroup_members\x18\x01 \x03(\x0b\x32\x17.ntt.iam.v1.GroupMember\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe0\x01\n\x17ListGroupMembersRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xb1\x01\n\x18ListGroupMembersResponse\x12.\n\rgroup_members\x18\x01 \x03(\x0b\x32\x17.ntt.iam.v1.GroupMember\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"x\n\x17WatchGroupMemberRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"I\n\x18WatchGroupMemberResponse\x12-\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1d.ntt.iam.v1.GroupMemberChange\"\xcb\x02\n\x18WatchGroupMembersRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xde\x02\n\x19WatchGroupMembersResponse\x12;\n\x14group_member_changes\x18\x02 \x03(\x0b\x32\x1d.ntt.iam.v1.GroupMemberChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12P\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x35.ntt.iam.v1.WatchGroupMembersResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Y\n\x18\x43reateGroupMemberRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12-\n\x0cgroup_member\x18\x02 \x01(\x0b\x32\x17.ntt.iam.v1.GroupMember\"\xb3\x02\n\x18UpdateGroupMemberRequest\x12-\n\x0cgroup_member\x18\x02 \x01(\x0b\x32\x17.ntt.iam.v1.GroupMember\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x35\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32(.ntt.iam.v1.UpdateGroupMemberRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1ai\n\x03\x43\x41S\x12\x32\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x17.ntt.iam.v1.GroupMember\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"(\n\x18\x44\x65leteGroupMemberRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xae\x12\n\x12GroupMemberService\x12\x92\x02\n\x0eGetGroupMember\x12!.ntt.iam.v1.GetGroupMemberRequest\x1a\x17.ntt.iam.v1.GroupMember\"\xc3\x01\x82\xd3\xe4\x93\x02\xbc\x01\x12\"/v1/{name=groups/*/groupMembers/*}Z/\x12-/v1/{name=projects/*/groups/*/groupMembers/*}Z4\x12\x32/v1/{name=organizations/*/groups/*/groupMembers/*}Z/\x12-/v1/{name=services/*/groups/*/groupMembers/*}\x12\x8c\x01\n\x14\x42\x61tchGetGroupMembers\x12\'.ntt.iam.v1.BatchGetGroupMembersRequest\x1a(.ntt.iam.v1.BatchGetGroupMembersResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/groupMembers:batchGet\x12\xa3\x02\n\x10ListGroupMembers\x12#.ntt.iam.v1.ListGroupMembersRequest\x1a$.ntt.iam.v1.ListGroupMembersResponse\"\xc3\x01\x82\xd3\xe4\x93\x02\xbc\x01\x12\"/v1/{parent=groups/*}/groupMembersZ/\x12-/v1/{parent=projects/*/groups/*}/groupMembersZ4\x12\x32/v1/{parent=organizations/*/groups/*}/groupMembersZ/\x12-/v1/{parent=services/*/groups/*}/groupMembers\x12\xbd\x02\n\x10WatchGroupMember\x12#.ntt.iam.v1.WatchGroupMemberRequest\x1a$.ntt.iam.v1.WatchGroupMemberResponse\"\xdb\x01\x82\xd3\xe4\x93\x02\xd4\x01\"(/v1/{name=groups/*/groupMembers/*}:watchZ5\"3/v1/{name=projects/*/groups/*/groupMembers/*}:watchZ:\"8/v1/{name=organizations/*/groups/*/groupMembers/*}:watchZ5\"3/v1/{name=services/*/groups/*/groupMembers/*}:watch0\x01\x12\xc0\x02\n\x11WatchGroupMembers\x12$.ntt.iam.v1.WatchGroupMembersRequest\x1a%.ntt.iam.v1.WatchGroupMembersResponse\"\xdb\x01\x82\xd3\xe4\x93\x02\xd4\x01\"(/v1/{parent=groups/*}/groupMembers:watchZ5\"3/v1/{parent=projects/*/groups/*}/groupMembers:watchZ:\"8/v1/{parent=organizations/*/groups/*}/groupMembers:watchZ5\"3/v1/{parent=services/*/groups/*}/groupMembers:watch0\x01\x12\xa6\x02\n\x11\x43reateGroupMember\x12$.ntt.iam.v1.CreateGroupMemberRequest\x1a\x17.ntt.iam.v1.GroupMember\"\xd1\x01\x82\xd3\xe4\x93\x02\xca\x01\"\"/v1/{parent=groups/*}/groupMembers:\x0cgroup_memberZ/\"-/v1/{parent=projects/*/groups/*}/groupMembersZ4\"2/v1/{parent=organizations/*/groups/*}/groupMembersZ/\"-/v1/{parent=services/*/groups/*}/groupMembers\x12\xda\x02\n\x11UpdateGroupMember\x12$.ntt.iam.v1.UpdateGroupMemberRequest\x1a\x17.ntt.iam.v1.GroupMember\"\x85\x02\x82\xd3\xe4\x93\x02\xfe\x01\x1a//v1/{group_member.name=groups/*/groupMembers/*}:\x0cgroup_memberZ<\x1a:/v1/{group_member.name=projects/*/groups/*/groupMembers/*}ZA\x1a?/v1/{group_member.name=organizations/*/groups/*/groupMembers/*}Z<\x1a:/v1/{group_member.name=services/*/groups/*/groupMembers/*}\x12\x97\x02\n\x11\x44\x65leteGroupMember\x12$.ntt.iam.v1.DeleteGroupMemberRequest\x1a\x16.google.protobuf.Empty\"\xc3\x01\x82\xd3\xe4\x93\x02\xbc\x01*\"/v1/{name=groups/*/groupMembers/*}Z/*-/v1/{name=projects/*/groups/*/groupMembers/*}Z4*2/v1/{name=organizations/*/groups/*/groupMembers/*}Z/*-/v1/{name=services/*/groups/*/groupMembers/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB}\n\x11\x63om.ntt.iam.pb.v1B\x17GroupMemberServiceProtoP\x00ZMgithub.com/cloudwan/edgelq-sdk/iam/client/v1/group_member;group_member_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.group_member_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\027GroupMemberServiceProtoP\000ZMgithub.com/cloudwan/edgelq-sdk/iam/client/v1/group_member;group_member_client'
  _globals['_GROUPMEMBERSERVICE']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['GetGroupMember']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['GetGroupMember']._serialized_options = b'\202\323\344\223\002\274\001\022\"/v1/{name=groups/*/groupMembers/*}Z/\022-/v1/{name=projects/*/groups/*/groupMembers/*}Z4\0222/v1/{name=organizations/*/groups/*/groupMembers/*}Z/\022-/v1/{name=services/*/groups/*/groupMembers/*}'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['BatchGetGroupMembers']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['BatchGetGroupMembers']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/groupMembers:batchGet'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['ListGroupMembers']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['ListGroupMembers']._serialized_options = b'\202\323\344\223\002\274\001\022\"/v1/{parent=groups/*}/groupMembersZ/\022-/v1/{parent=projects/*/groups/*}/groupMembersZ4\0222/v1/{parent=organizations/*/groups/*}/groupMembersZ/\022-/v1/{parent=services/*/groups/*}/groupMembers'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['WatchGroupMember']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['WatchGroupMember']._serialized_options = b'\202\323\344\223\002\324\001\"(/v1/{name=groups/*/groupMembers/*}:watchZ5\"3/v1/{name=projects/*/groups/*/groupMembers/*}:watchZ:\"8/v1/{name=organizations/*/groups/*/groupMembers/*}:watchZ5\"3/v1/{name=services/*/groups/*/groupMembers/*}:watch'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['WatchGroupMembers']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['WatchGroupMembers']._serialized_options = b'\202\323\344\223\002\324\001\"(/v1/{parent=groups/*}/groupMembers:watchZ5\"3/v1/{parent=projects/*/groups/*}/groupMembers:watchZ:\"8/v1/{parent=organizations/*/groups/*}/groupMembers:watchZ5\"3/v1/{parent=services/*/groups/*}/groupMembers:watch'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['CreateGroupMember']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['CreateGroupMember']._serialized_options = b'\202\323\344\223\002\312\001\"\"/v1/{parent=groups/*}/groupMembers:\014group_memberZ/\"-/v1/{parent=projects/*/groups/*}/groupMembersZ4\"2/v1/{parent=organizations/*/groups/*}/groupMembersZ/\"-/v1/{parent=services/*/groups/*}/groupMembers'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['UpdateGroupMember']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['UpdateGroupMember']._serialized_options = b'\202\323\344\223\002\376\001\032//v1/{group_member.name=groups/*/groupMembers/*}:\014group_memberZ<\032:/v1/{group_member.name=projects/*/groups/*/groupMembers/*}ZA\032?/v1/{group_member.name=organizations/*/groups/*/groupMembers/*}Z<\032:/v1/{group_member.name=services/*/groups/*/groupMembers/*}'
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['DeleteGroupMember']._loaded_options = None
  _globals['_GROUPMEMBERSERVICE'].methods_by_name['DeleteGroupMember']._serialized_options = b'\202\323\344\223\002\274\001*\"/v1/{name=groups/*/groupMembers/*}Z/*-/v1/{name=projects/*/groups/*/groupMembers/*}Z4*2/v1/{name=organizations/*/groups/*/groupMembers/*}Z/*-/v1/{name=services/*/groups/*/groupMembers/*}'
  _globals['_GETGROUPMEMBERREQUEST']._serialized_start=374
  _globals['_GETGROUPMEMBERREQUEST']._serialized_end=492
  _globals['_BATCHGETGROUPMEMBERSREQUEST']._serialized_start=495
  _globals['_BATCHGETGROUPMEMBERSREQUEST']._serialized_end=626
  _globals['_BATCHGETGROUPMEMBERSRESPONSE']._serialized_start=628
  _globals['_BATCHGETGROUPMEMBERSRESPONSE']._serialized_end=723
  _globals['_LISTGROUPMEMBERSREQUEST']._serialized_start=726
  _globals['_LISTGROUPMEMBERSREQUEST']._serialized_end=950
  _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_start=953
  _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_end=1130
  _globals['_WATCHGROUPMEMBERREQUEST']._serialized_start=1132
  _globals['_WATCHGROUPMEMBERREQUEST']._serialized_end=1252
  _globals['_WATCHGROUPMEMBERRESPONSE']._serialized_start=1254
  _globals['_WATCHGROUPMEMBERRESPONSE']._serialized_end=1327
  _globals['_WATCHGROUPMEMBERSREQUEST']._serialized_start=1330
  _globals['_WATCHGROUPMEMBERSREQUEST']._serialized_end=1661
  _globals['_WATCHGROUPMEMBERSRESPONSE']._serialized_start=1664
  _globals['_WATCHGROUPMEMBERSRESPONSE']._serialized_end=2014
  _globals['_WATCHGROUPMEMBERSRESPONSE_PAGETOKENCHANGE']._serialized_start=1947
  _globals['_WATCHGROUPMEMBERSRESPONSE_PAGETOKENCHANGE']._serialized_end=2014
  _globals['_CREATEGROUPMEMBERREQUEST']._serialized_start=2016
  _globals['_CREATEGROUPMEMBERREQUEST']._serialized_end=2105
  _globals['_UPDATEGROUPMEMBERREQUEST']._serialized_start=2108
  _globals['_UPDATEGROUPMEMBERREQUEST']._serialized_end=2415
  _globals['_UPDATEGROUPMEMBERREQUEST_CAS']._serialized_start=2310
  _globals['_UPDATEGROUPMEMBERREQUEST_CAS']._serialized_end=2415
  _globals['_DELETEGROUPMEMBERREQUEST']._serialized_start=2417
  _globals['_DELETEGROUPMEMBERREQUEST']._serialized_end=2457
  _globals['_GROUPMEMBERSERVICE']._serialized_start=2460
  _globals['_GROUPMEMBERSERVICE']._serialized_end=4810
# @@protoc_insertion_point(module_scope)