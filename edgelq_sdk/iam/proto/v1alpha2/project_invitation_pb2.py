# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/project_invitation.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/project_invitation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import invitation_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_invitation__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/iam/proto/v1alpha2/project_invitation.proto\x12\x10ntt.iam.v1alpha2\x1a.edgelq-sdk/iam/proto/v1alpha2/invitation.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xff\x01\n\x11ProjectInvitation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x14project_display_name\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03\x12\x30\n\ninvitation\x18\x02 \x01(\x0b\x32\x1c.ntt.iam.v1alpha2.Invitation\x12#\n\x08metadata\x18\x03 \x01(\x0b\x32\x11.goten.types.Meta:a\xea\x41^\n iam.edgelq.com/ProjectInvitation\x12:projects/{project}/projectInvitations/{project_invitation}B\x90\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x16ProjectInvitationProtoP\x01Z[github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/project_invitation;project_invitationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.project_invitation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\026ProjectInvitationProtoP\001Z[github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/project_invitation;project_invitation'
  _globals['_PROJECTINVITATION'].fields_by_name['project_display_name']._loaded_options = None
  _globals['_PROJECTINVITATION'].fields_by_name['project_display_name']._serialized_options = b'\342A\001\003'
  _globals['_PROJECTINVITATION']._loaded_options = None
  _globals['_PROJECTINVITATION']._serialized_options = b'\352A^\n iam.edgelq.com/ProjectInvitation\022:projects/{project}/projectInvitations/{project_invitation}'
  _globals['_PROJECTINVITATION']._serialized_start=213
  _globals['_PROJECTINVITATION']._serialized_end=468
# @@protoc_insertion_point(module_scope)
