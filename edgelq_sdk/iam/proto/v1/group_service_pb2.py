# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/group_service.proto
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
    'edgelq-sdk/iam/proto/v1/group_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import group_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__pb2
from edgelq_sdk.iam.proto.v1 import group_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+edgelq-sdk/iam/proto/v1/group_service.proto\x12\nntt.iam.v1\x1a#edgelq-sdk/iam/proto/v1/group.proto\x1a*edgelq-sdk/iam/proto/v1/group_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"p\n\x0fGetGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"}\n\x15\x42\x61tchGetGroupsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"L\n\x16\x42\x61tchGetGroupsResponse\x12!\n\x06groups\x18\x01 \x03(\x0b\x32\x11.ntt.iam.v1.Group\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xda\x01\n\x11ListGroupsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\x9e\x01\n\x12ListGroupsResponse\x12!\n\x06groups\x18\x01 \x03(\x0b\x32\x11.ntt.iam.v1.Group\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"r\n\x11WatchGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"=\n\x12WatchGroupResponse\x12\'\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x17.ntt.iam.v1.GroupChange\"\xc5\x02\n\x12WatchGroupsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xc5\x02\n\x13WatchGroupsResponse\x12.\n\rgroup_changes\x18\x02 \x03(\x0b\x32\x17.ntt.iam.v1.GroupChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12J\n\x11page_token_change\x18\x03 \x01(\x0b\x32/.ntt.iam.v1.WatchGroupsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"F\n\x12\x43reateGroupRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12 \n\x05group\x18\x02 \x01(\x0b\x32\x11.ntt.iam.v1.Group\"\x94\x02\n\x12UpdateGroupRequest\x12 \n\x05group\x18\x02 \x01(\x0b\x32\x11.ntt.iam.v1.Group\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\".ntt.iam.v1.UpdateGroupRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1a\x63\n\x03\x43\x41S\x12,\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x11.ntt.iam.v1.Group\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\"\n\x12\x44\x65leteGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xab\r\n\x0cGroupService\x12\xc4\x01\n\x08GetGroup\x12\x1b.ntt.iam.v1.GetGroupRequest\x1a\x11.ntt.iam.v1.Group\"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x12\x13/v1/{name=groups/*}Z \x12\x1e/v1/{name=projects/*/groups/*}Z%\x12#/v1/{name=organizations/*/groups/*}Z \x12\x1e/v1/{name=services/*/groups/*}\x12t\n\x0e\x42\x61tchGetGroups\x12!.ntt.iam.v1.BatchGetGroupsRequest\x1a\".ntt.iam.v1.BatchGetGroupsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/groups:batchGet\x12\xca\x01\n\nListGroups\x12\x1d.ntt.iam.v1.ListGroupsRequest\x1a\x1e.ntt.iam.v1.ListGroupsResponse\"}\x82\xd3\xe4\x93\x02w\x12\n/v1/groupsZ \x12\x1e/v1/{parent=projects/*}/groupsZ%\x12#/v1/{parent=organizations/*}/groupsZ \x12\x1e/v1/{parent=services/*}/groups\x12\xef\x01\n\nWatchGroup\x12\x1d.ntt.iam.v1.WatchGroupRequest\x1a\x1e.ntt.iam.v1.WatchGroupResponse\"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x01\"\x19/v1/{name=groups/*}:watchZ&\"$/v1/{name=projects/*/groups/*}:watchZ+\")/v1/{name=organizations/*/groups/*}:watchZ&\"$/v1/{name=services/*/groups/*}:watch0\x01\x12\xe9\x01\n\x0bWatchGroups\x12\x1e.ntt.iam.v1.WatchGroupsRequest\x1a\x1f.ntt.iam.v1.WatchGroupsResponse\"\x96\x01\x82\xd3\xe4\x93\x02\x8f\x01\"\x10/v1/groups:watchZ&\"$/v1/{parent=projects/*}/groups:watchZ+\")/v1/{parent=organizations/*}/groups:watchZ&\"$/v1/{parent=services/*}/groups:watch0\x01\x12\xc7\x01\n\x0b\x43reateGroup\x12\x1e.ntt.iam.v1.CreateGroupRequest\x1a\x11.ntt.iam.v1.Group\"\x84\x01\x82\xd3\xe4\x93\x02~\"\n/v1/groups:\x05groupZ \"\x1e/v1/{parent=projects/*}/groupsZ%\"#/v1/{parent=organizations/*}/groupsZ \"\x1e/v1/{parent=services/*}/groups\x12\xe9\x01\n\x0bUpdateGroup\x12\x1e.ntt.iam.v1.UpdateGroupRequest\x1a\x11.ntt.iam.v1.Group\"\xa6\x01\x82\xd3\xe4\x93\x02\x9f\x01\x1a\x19/v1/{group.name=groups/*}:\x05groupZ&\x1a$/v1/{group.name=projects/*/groups/*}Z+\x1a)/v1/{group.name=organizations/*/groups/*}Z&\x1a$/v1/{group.name=services/*/groups/*}\x12\xcf\x01\n\x0b\x44\x65leteGroup\x12\x1e.ntt.iam.v1.DeleteGroupRequest\x1a\x16.google.protobuf.Empty\"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01*\x13/v1/{name=groups/*}Z *\x1e/v1/{name=projects/*/groups/*}Z%*#/v1/{name=organizations/*/groups/*}Z *\x1e/v1/{name=services/*/groups/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comBi\n\x11\x63om.ntt.iam.pb.v1B\x11GroupServiceProtoP\x00Z?github.com/cloudwan/edgelq-sdk/iam/client/v1/group;group_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\021GroupServiceProtoP\000Z?github.com/cloudwan/edgelq-sdk/iam/client/v1/group;group_client'
  _globals['_GROUPSERVICE']._loaded_options = None
  _globals['_GROUPSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_GROUPSERVICE'].methods_by_name['GetGroup']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['GetGroup']._serialized_options = b'\202\323\344\223\002\200\001\022\023/v1/{name=groups/*}Z \022\036/v1/{name=projects/*/groups/*}Z%\022#/v1/{name=organizations/*/groups/*}Z \022\036/v1/{name=services/*/groups/*}'
  _globals['_GROUPSERVICE'].methods_by_name['BatchGetGroups']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['BatchGetGroups']._serialized_options = b'\202\323\344\223\002\025\022\023/v1/groups:batchGet'
  _globals['_GROUPSERVICE'].methods_by_name['ListGroups']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['ListGroups']._serialized_options = b'\202\323\344\223\002w\022\n/v1/groupsZ \022\036/v1/{parent=projects/*}/groupsZ%\022#/v1/{parent=organizations/*}/groupsZ \022\036/v1/{parent=services/*}/groups'
  _globals['_GROUPSERVICE'].methods_by_name['WatchGroup']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['WatchGroup']._serialized_options = b'\202\323\344\223\002\230\001\"\031/v1/{name=groups/*}:watchZ&\"$/v1/{name=projects/*/groups/*}:watchZ+\")/v1/{name=organizations/*/groups/*}:watchZ&\"$/v1/{name=services/*/groups/*}:watch'
  _globals['_GROUPSERVICE'].methods_by_name['WatchGroups']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['WatchGroups']._serialized_options = b'\202\323\344\223\002\217\001\"\020/v1/groups:watchZ&\"$/v1/{parent=projects/*}/groups:watchZ+\")/v1/{parent=organizations/*}/groups:watchZ&\"$/v1/{parent=services/*}/groups:watch'
  _globals['_GROUPSERVICE'].methods_by_name['CreateGroup']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['CreateGroup']._serialized_options = b'\202\323\344\223\002~\"\n/v1/groups:\005groupZ \"\036/v1/{parent=projects/*}/groupsZ%\"#/v1/{parent=organizations/*}/groupsZ \"\036/v1/{parent=services/*}/groups'
  _globals['_GROUPSERVICE'].methods_by_name['UpdateGroup']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['UpdateGroup']._serialized_options = b'\202\323\344\223\002\237\001\032\031/v1/{group.name=groups/*}:\005groupZ&\032$/v1/{group.name=projects/*/groups/*}Z+\032)/v1/{group.name=organizations/*/groups/*}Z&\032$/v1/{group.name=services/*/groups/*}'
  _globals['_GROUPSERVICE'].methods_by_name['DeleteGroup']._loaded_options = None
  _globals['_GROUPSERVICE'].methods_by_name['DeleteGroup']._serialized_options = b'\202\323\344\223\002\200\001*\023/v1/{name=groups/*}Z *\036/v1/{name=projects/*/groups/*}Z%*#/v1/{name=organizations/*/groups/*}Z *\036/v1/{name=services/*/groups/*}'
  _globals['_GETGROUPREQUEST']._serialized_start=353
  _globals['_GETGROUPREQUEST']._serialized_end=465
  _globals['_BATCHGETGROUPSREQUEST']._serialized_start=467
  _globals['_BATCHGETGROUPSREQUEST']._serialized_end=592
  _globals['_BATCHGETGROUPSRESPONSE']._serialized_start=594
  _globals['_BATCHGETGROUPSRESPONSE']._serialized_end=670
  _globals['_LISTGROUPSREQUEST']._serialized_start=673
  _globals['_LISTGROUPSREQUEST']._serialized_end=891
  _globals['_LISTGROUPSRESPONSE']._serialized_start=894
  _globals['_LISTGROUPSRESPONSE']._serialized_end=1052
  _globals['_WATCHGROUPREQUEST']._serialized_start=1054
  _globals['_WATCHGROUPREQUEST']._serialized_end=1168
  _globals['_WATCHGROUPRESPONSE']._serialized_start=1170
  _globals['_WATCHGROUPRESPONSE']._serialized_end=1231
  _globals['_WATCHGROUPSREQUEST']._serialized_start=1234
  _globals['_WATCHGROUPSREQUEST']._serialized_end=1559
  _globals['_WATCHGROUPSRESPONSE']._serialized_start=1562
  _globals['_WATCHGROUPSRESPONSE']._serialized_end=1887
  _globals['_WATCHGROUPSRESPONSE_PAGETOKENCHANGE']._serialized_start=1820
  _globals['_WATCHGROUPSRESPONSE_PAGETOKENCHANGE']._serialized_end=1887
  _globals['_CREATEGROUPREQUEST']._serialized_start=1889
  _globals['_CREATEGROUPREQUEST']._serialized_end=1959
  _globals['_UPDATEGROUPREQUEST']._serialized_start=1962
  _globals['_UPDATEGROUPREQUEST']._serialized_end=2238
  _globals['_UPDATEGROUPREQUEST_CAS']._serialized_start=2139
  _globals['_UPDATEGROUPREQUEST_CAS']._serialized_end=2238
  _globals['_DELETEGROUPREQUEST']._serialized_start=2240
  _globals['_DELETEGROUPREQUEST']._serialized_end=2274
  _globals['_GROUPSERVICE']._serialized_start=2277
  _globals['_GROUPSERVICE']._serialized_end=3984
# @@protoc_insertion_point(module_scope)
