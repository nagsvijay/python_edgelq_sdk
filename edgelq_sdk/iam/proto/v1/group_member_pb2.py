# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/group_member.proto
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
    'edgelq-sdk/iam/proto/v1/group_member.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*edgelq-sdk/iam/proto/v1/group_member.proto\x12\nntt.iam.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\x9b\x03\n\x0bGroupMember\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x07 \x01(\x0b\x32\x11.goten.types.Meta\x12\x0e\n\x06member\x18\x02 \x01(\t\x12\x15\n\rparent_member\x18\x05 \x01(\t\x12\x1c\n\x14min_ancestry_members\x18\x06 \x03(\t:\x93\x02\xea\x41\x8f\x02\n\x1aiam.edgelq.com/GroupMember\x12*groups/{group}/groupMembers/{group_member}\x12=projects/{project}/groups/{group}/groupMembers/{group_member}\x12Gorganizations/{organization}/groups/{group}/groupMembers/{group_member}\x12=services/{service}/groups/{group}/groupMembers/{group_member}Br\n\x11\x63om.ntt.iam.pb.v1B\x10GroupMemberProtoP\x01ZIgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/group_member;group_memberb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.group_member_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\020GroupMemberProtoP\001ZIgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/group_member;group_member'
  _globals['_GROUPMEMBER']._loaded_options = None
  _globals['_GROUPMEMBER']._serialized_options = b'\352A\217\002\n\032iam.edgelq.com/GroupMember\022*groups/{group}/groupMembers/{group_member}\022=projects/{project}/groups/{group}/groupMembers/{group_member}\022Gorganizations/{organization}/groups/{group}/groupMembers/{group_member}\022=services/{service}/groups/{group}/groupMembers/{group_member}'
  _globals['_GROUPMEMBER']._serialized_start=114
  _globals['_GROUPMEMBER']._serialized_end=525
# @@protoc_insertion_point(module_scope)