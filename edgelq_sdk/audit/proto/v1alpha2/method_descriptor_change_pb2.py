# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/audit/proto/v1alpha2/method_descriptor_change.proto
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
    'edgelq-sdk/audit/proto/v1alpha2/method_descriptor_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.audit.proto.v1alpha2 import method_descriptor_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1alpha2_dot_method__descriptor__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>edgelq-sdk/audit/proto/v1alpha2/method_descriptor_change.proto\x12\x12ntt.audit.v1alpha2\x1a\x37\x65\x64gelq-sdk/audit/proto/v1alpha2/method_descriptor.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xd5\x05\n\x16MethodDescriptorChange\x12\x41\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\x30.ntt.audit.v1alpha2.MethodDescriptorChange.AddedH\x00\x12G\n\x08modified\x18\x02 \x01(\x0b\x32\x33.ntt.audit.v1alpha2.MethodDescriptorChange.ModifiedH\x00\x12\x45\n\x07\x63urrent\x18\x04 \x01(\x0b\x32\x32.ntt.audit.v1alpha2.MethodDescriptorChange.CurrentH\x00\x12\x45\n\x07removed\x18\x03 \x01(\x0b\x32\x32.ntt.audit.v1alpha2.MethodDescriptorChange.RemovedH\x00\x1a\\\n\x05\x41\x64\x64\x65\x64\x12?\n\x11method_descriptor\x18\x01 \x01(\x0b\x32$.ntt.audit.v1alpha2.MethodDescriptor\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xba\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x11method_descriptor\x18\x02 \x01(\x0b\x32$.ntt.audit.v1alpha2.MethodDescriptor\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1aJ\n\x07\x43urrent\x12?\n\x11method_descriptor\x18\x01 \x01(\x0b\x32$.ntt.audit.v1alpha2.MethodDescriptor\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x97\x01\n\x19\x63om.ntt.audit.pb.v1alpha2B\x1bMethodDescriptorChangeProtoP\x00Z[github.com/cloudwan/edgelq-sdk/audit/resources/v1alpha2/method_descriptor;method_descriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.audit.proto.v1alpha2.method_descriptor_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.ntt.audit.pb.v1alpha2B\033MethodDescriptorChangeProtoP\000Z[github.com/cloudwan/edgelq-sdk/audit/resources/v1alpha2/method_descriptor;method_descriptor'
  _globals['_METHODDESCRIPTORCHANGE']._serialized_start=205
  _globals['_METHODDESCRIPTORCHANGE']._serialized_end=930
  _globals['_METHODDESCRIPTORCHANGE_ADDED']._serialized_start=513
  _globals['_METHODDESCRIPTORCHANGE_ADDED']._serialized_end=605
  _globals['_METHODDESCRIPTORCHANGE_MODIFIED']._serialized_start=608
  _globals['_METHODDESCRIPTORCHANGE_MODIFIED']._serialized_end=794
  _globals['_METHODDESCRIPTORCHANGE_CURRENT']._serialized_start=796
  _globals['_METHODDESCRIPTORCHANGE_CURRENT']._serialized_end=870
  _globals['_METHODDESCRIPTORCHANGE_REMOVED']._serialized_start=872
  _globals['_METHODDESCRIPTORCHANGE_REMOVED']._serialized_end=915
# @@protoc_insertion_point(module_scope)
