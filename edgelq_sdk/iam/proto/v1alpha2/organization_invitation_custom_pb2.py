# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/organization_invitation_custom.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/organization_invitation_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import organization_invitation_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_organization__invitation__pb2
from edgelq_sdk.iam.proto.v1alpha2 import organization_invitation_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_organization__invitation__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBedgelq-sdk/iam/proto/v1alpha2/organization_invitation_custom.proto\x12\x10ntt.iam.v1alpha2\x1a;edgelq-sdk/iam/proto/v1alpha2/organization_invitation.proto\x1a\x42\x65\x64gelq-sdk/iam/proto/v1alpha2/organization_invitation_change.proto\"3\n#AcceptOrganizationInvitationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n$AcceptOrganizationInvitationResponse\"D\n$DeclineOrganizationInvitationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\"\'\n%DeclineOrganizationInvitationResponse\"F\n$ListMyOrganizationInvitationsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\"s\n%ListMyOrganizationInvitationsResponse\x12J\n\x18organization_invitations\x18\x01 \x03(\x0b\x32(.ntt.iam.v1alpha2.OrganizationInvitationB\xa9\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B!OrganizationInvitationCustomProtoP\x00Zigithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/organization_invitation;organization_invitation_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.organization_invitation_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B!OrganizationInvitationCustomProtoP\000Zigithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/organization_invitation;organization_invitation_client'
  _globals['_ACCEPTORGANIZATIONINVITATIONREQUEST']._serialized_start=217
  _globals['_ACCEPTORGANIZATIONINVITATIONREQUEST']._serialized_end=268
  _globals['_ACCEPTORGANIZATIONINVITATIONRESPONSE']._serialized_start=270
  _globals['_ACCEPTORGANIZATIONINVITATIONRESPONSE']._serialized_end=308
  _globals['_DECLINEORGANIZATIONINVITATIONREQUEST']._serialized_start=310
  _globals['_DECLINEORGANIZATIONINVITATIONREQUEST']._serialized_end=378
  _globals['_DECLINEORGANIZATIONINVITATIONRESPONSE']._serialized_start=380
  _globals['_DECLINEORGANIZATIONINVITATIONRESPONSE']._serialized_end=419
  _globals['_LISTMYORGANIZATIONINVITATIONSREQUEST']._serialized_start=421
  _globals['_LISTMYORGANIZATIONINVITATIONSREQUEST']._serialized_end=491
  _globals['_LISTMYORGANIZATIONINVITATIONSRESPONSE']._serialized_start=493
  _globals['_LISTMYORGANIZATIONINVITATIONSRESPONSE']._serialized_end=608
# @@protoc_insertion_point(module_scope)
