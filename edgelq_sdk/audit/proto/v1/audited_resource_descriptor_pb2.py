# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/audit/proto/v1/audited_resource_descriptor.proto
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
    'edgelq-sdk/audit/proto/v1/audited_resource_descriptor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.audit.proto.v1 import common_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;edgelq-sdk/audit/proto/v1/audited_resource_descriptor.proto\x12\x0cntt.audit.v1\x1a&edgelq-sdk/audit/proto/v1/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xb4\x03\n\x19\x41uditedResourceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12-\n\x06labels\x18\x04 \x03(\x0b\x32\x1d.ntt.audit.v1.LabelDescriptor\x12:\n\x17promoted_label_key_sets\x18\x05 \x03(\x0b\x32\x19.ntt.audit.v1.LabelKeySet\x12\x10\n\x08versions\x18\x06 \x03(\t\x12\x13\n\x0bspec_fields\x18\x07 \x03(\t\x12\x14\n\x0cstate_fields\x18\x08 \x03(\t\x12\x13\n\x0bmeta_fields\x18\t \x03(\t\x12#\n\x08metadata\x18\n \x01(\x0b\x32\x11.goten.types.Meta:|\xea\x41y\n*audit.edgelq.com/AuditedResourceDescriptor\x12Kservices/{service}/auditedResourceDescriptors/{audited_resource_descriptor}B\xa2\x01\n\x13\x63om.ntt.audit.pb.v1B\x1e\x41uditedResourceDescriptorProtoP\x01Zigithub.com/cloudwan/edgelq-sdk/audit/resources/v1/audited_resource_descriptor;audited_resource_descriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.audit.proto.v1.audited_resource_descriptor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.ntt.audit.pb.v1B\036AuditedResourceDescriptorProtoP\001Zigithub.com/cloudwan/edgelq-sdk/audit/resources/v1/audited_resource_descriptor;audited_resource_descriptor'
  _globals['_AUDITEDRESOURCEDESCRIPTOR']._loaded_options = None
  _globals['_AUDITEDRESOURCEDESCRIPTOR']._serialized_options = b'\352Ay\n*audit.edgelq.com/AuditedResourceDescriptor\022Kservices/{service}/auditedResourceDescriptors/{audited_resource_descriptor}'
  _globals['_AUDITEDRESOURCEDESCRIPTOR']._serialized_start=173
  _globals['_AUDITEDRESOURCEDESCRIPTOR']._serialized_end=609
# @@protoc_insertion_point(module_scope)