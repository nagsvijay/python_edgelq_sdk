# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1/log_descriptor_change.proto
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
    'edgelq-sdk/logging/proto/v1/log_descriptor_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.logging.proto.v1 import log_descriptor_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1_dot_log__descriptor__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/logging/proto/v1/log_descriptor_change.proto\x12\x0entt.logging.v1\x1a\x30\x65\x64gelq-sdk/logging/proto/v1/log_descriptor.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\x98\x05\n\x13LogDescriptorChange\x12:\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32).ntt.logging.v1.LogDescriptorChange.AddedH\x00\x12@\n\x08modified\x18\x02 \x01(\x0b\x32,.ntt.logging.v1.LogDescriptorChange.ModifiedH\x00\x12>\n\x07\x63urrent\x18\x04 \x01(\x0b\x32+.ntt.logging.v1.LogDescriptorChange.CurrentH\x00\x12>\n\x07removed\x18\x03 \x01(\x0b\x32+.ntt.logging.v1.LogDescriptorChange.RemovedH\x00\x1aR\n\x05\x41\x64\x64\x65\x64\x12\x35\n\x0elog_descriptor\x18\x01 \x01(\x0b\x32\x1d.ntt.logging.v1.LogDescriptor\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xb0\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0elog_descriptor\x18\x02 \x01(\x0b\x32\x1d.ntt.logging.v1.LogDescriptor\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a@\n\x07\x43urrent\x12\x35\n\x0elog_descriptor\x18\x01 \x01(\x0b\x32\x1d.ntt.logging.v1.LogDescriptor\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x86\x01\n\x15\x63om.ntt.logging.pb.v1B\x18LogDescriptorChangeProtoP\x00ZQgithub.com/cloudwan/edgelq-sdk/logging/resources/v1/log_descriptor;log_descriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1.log_descriptor_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.logging.pb.v1B\030LogDescriptorChangeProtoP\000ZQgithub.com/cloudwan/edgelq-sdk/logging/resources/v1/log_descriptor;log_descriptor'
  _globals['_LOGDESCRIPTORCHANGE']._serialized_start=187
  _globals['_LOGDESCRIPTORCHANGE']._serialized_end=851
  _globals['_LOGDESCRIPTORCHANGE_ADDED']._serialized_start=464
  _globals['_LOGDESCRIPTORCHANGE_ADDED']._serialized_end=546
  _globals['_LOGDESCRIPTORCHANGE_MODIFIED']._serialized_start=549
  _globals['_LOGDESCRIPTORCHANGE_MODIFIED']._serialized_end=725
  _globals['_LOGDESCRIPTORCHANGE_CURRENT']._serialized_start=727
  _globals['_LOGDESCRIPTORCHANGE_CURRENT']._serialized_end=791
  _globals['_LOGDESCRIPTORCHANGE_REMOVED']._serialized_start=793
  _globals['_LOGDESCRIPTORCHANGE_REMOVED']._serialized_end=836
# @@protoc_insertion_point(module_scope)