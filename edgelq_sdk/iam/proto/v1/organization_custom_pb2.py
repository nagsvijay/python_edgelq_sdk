# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/organization_custom.proto
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
    'edgelq-sdk/iam/proto/v1/organization_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import organization_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_organization__pb2
from edgelq_sdk.iam.proto.v1 import organization_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_organization__change__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1edgelq-sdk/iam/proto/v1/organization_custom.proto\x12\nntt.iam.v1\x1a*edgelq-sdk/iam/proto/v1/organization.proto\x1a\x31\x65\x64gelq-sdk/iam/proto/v1/organization_change.proto\x1a google/protobuf/field_mask.proto\"\x95\x01\n\x1aListMyOrganizationsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x80\x01\n\x1bListMyOrganizationsResponse\x12/\n\rorganizations\x18\x01 \x03(\x0b\x32\x18.ntt.iam.v1.Organization\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\tB}\n\x11\x63om.ntt.iam.pb.v1B\x17OrganizationCustomProtoP\x00ZMgithub.com/cloudwan/edgelq-sdk/iam/client/v1/organization;organization_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.organization_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\027OrganizationCustomProtoP\000ZMgithub.com/cloudwan/edgelq-sdk/iam/client/v1/organization;organization_client'
  _globals['_LISTMYORGANIZATIONSREQUEST']._serialized_start=195
  _globals['_LISTMYORGANIZATIONSREQUEST']._serialized_end=344
  _globals['_LISTMYORGANIZATIONSRESPONSE']._serialized_start=347
  _globals['_LISTMYORGANIZATIONSRESPONSE']._serialized_end=475
# @@protoc_insertion_point(module_scope)
