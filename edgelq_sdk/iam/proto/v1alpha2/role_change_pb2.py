# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/role_change.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/role_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import role_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_role__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/edgelq-sdk/iam/proto/v1alpha2/role_change.proto\x12\x10ntt.iam.v1alpha2\x1a(edgelq-sdk/iam/proto/v1alpha2/role.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xc0\x04\n\nRoleChange\x12\x33\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\".ntt.iam.v1alpha2.RoleChange.AddedH\x00\x12\x39\n\x08modified\x18\x02 \x01(\x0b\x32%.ntt.iam.v1alpha2.RoleChange.ModifiedH\x00\x12\x37\n\x07\x63urrent\x18\x04 \x01(\x0b\x32$.ntt.iam.v1alpha2.RoleChange.CurrentH\x00\x12\x37\n\x07removed\x18\x03 \x01(\x0b\x32$.ntt.iam.v1alpha2.RoleChange.RemovedH\x00\x1a\x41\n\x05\x41\x64\x64\x65\x64\x12$\n\x04role\x18\x01 \x01(\x0b\x32\x16.ntt.iam.v1alpha2.Role\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\x9f\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x04role\x18\x02 \x01(\x0b\x32\x16.ntt.iam.v1alpha2.Role\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a/\n\x07\x43urrent\x12$\n\x04role\x18\x01 \x01(\x0b\x32\x16.ntt.iam.v1alpha2.Role\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeBm\n\x17\x63om.ntt.iam.pb.v1alpha2B\x0fRoleChangeProtoP\x00Z?github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/role;roleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.role_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\017RoleChangeProtoP\000Z?github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/role;role'
  _globals['_ROLECHANGE']._serialized_start=173
  _globals['_ROLECHANGE']._serialized_end=749
  _globals['_ROLECHANGE_ADDED']._serialized_start=413
  _globals['_ROLECHANGE_ADDED']._serialized_end=478
  _globals['_ROLECHANGE_MODIFIED']._serialized_start=481
  _globals['_ROLECHANGE_MODIFIED']._serialized_end=640
  _globals['_ROLECHANGE_CURRENT']._serialized_start=642
  _globals['_ROLECHANGE_CURRENT']._serialized_end=689
  _globals['_ROLECHANGE_REMOVED']._serialized_start=691
  _globals['_ROLECHANGE_REMOVED']._serialized_end=734
# @@protoc_insertion_point(module_scope)
