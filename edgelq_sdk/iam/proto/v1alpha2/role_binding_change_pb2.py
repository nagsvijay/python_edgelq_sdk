# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/role_binding_change.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/role_binding_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import role_binding_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_role__binding__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/iam/proto/v1alpha2/role_binding_change.proto\x12\x10ntt.iam.v1alpha2\x1a\x30\x65\x64gelq-sdk/iam/proto/v1alpha2/role_binding.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\x90\x05\n\x11RoleBindingChange\x12:\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32).ntt.iam.v1alpha2.RoleBindingChange.AddedH\x00\x12@\n\x08modified\x18\x02 \x01(\x0b\x32,.ntt.iam.v1alpha2.RoleBindingChange.ModifiedH\x00\x12>\n\x07\x63urrent\x18\x04 \x01(\x0b\x32+.ntt.iam.v1alpha2.RoleBindingChange.CurrentH\x00\x12>\n\x07removed\x18\x03 \x01(\x0b\x32+.ntt.iam.v1alpha2.RoleBindingChange.RemovedH\x00\x1aP\n\x05\x41\x64\x64\x65\x64\x12\x33\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x1d.ntt.iam.v1alpha2.RoleBinding\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xae\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x0crole_binding\x18\x02 \x01(\x0b\x32\x1d.ntt.iam.v1alpha2.RoleBinding\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a>\n\x07\x43urrent\x12\x33\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x1d.ntt.iam.v1alpha2.RoleBinding\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x84\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x16RoleBindingChangeProtoP\x00ZOgithub.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/role_binding;role_bindingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.role_binding_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\026RoleBindingChangeProtoP\000ZOgithub.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/role_binding;role_binding'
  _globals['_ROLEBINDINGCHANGE']._serialized_start=189
  _globals['_ROLEBINDINGCHANGE']._serialized_end=845
  _globals['_ROLEBINDINGCHANGE_ADDED']._serialized_start=464
  _globals['_ROLEBINDINGCHANGE_ADDED']._serialized_end=544
  _globals['_ROLEBINDINGCHANGE_MODIFIED']._serialized_start=547
  _globals['_ROLEBINDINGCHANGE_MODIFIED']._serialized_end=721
  _globals['_ROLEBINDINGCHANGE_CURRENT']._serialized_start=723
  _globals['_ROLEBINDINGCHANGE_CURRENT']._serialized_end=785
  _globals['_ROLEBINDINGCHANGE_REMOVED']._serialized_start=787
  _globals['_ROLEBINDINGCHANGE_REMOVED']._serialized_end=830
# @@protoc_insertion_point(module_scope)
