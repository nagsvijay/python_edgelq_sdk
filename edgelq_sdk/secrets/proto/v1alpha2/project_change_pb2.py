# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/secrets/proto/v1alpha2/project_change.proto
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
    'edgelq-sdk/secrets/proto/v1alpha2/project_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.secrets.proto.v1alpha2 import project_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1alpha2_dot_project__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/secrets/proto/v1alpha2/project_change.proto\x12\x14ntt.secrets.v1alpha2\x1a/edgelq-sdk/secrets/proto/v1alpha2/project.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xfd\x04\n\rProjectChange\x12:\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32).ntt.secrets.v1alpha2.ProjectChange.AddedH\x00\x12@\n\x08modified\x18\x02 \x01(\x0b\x32,.ntt.secrets.v1alpha2.ProjectChange.ModifiedH\x00\x12>\n\x07\x63urrent\x18\x04 \x01(\x0b\x32+.ntt.secrets.v1alpha2.ProjectChange.CurrentH\x00\x12>\n\x07removed\x18\x03 \x01(\x0b\x32+.ntt.secrets.v1alpha2.ProjectChange.RemovedH\x00\x1aK\n\x05\x41\x64\x64\x65\x64\x12.\n\x07project\x18\x01 \x01(\x0b\x32\x1d.ntt.secrets.v1alpha2.Project\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xa9\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x07project\x18\x02 \x01(\x0b\x32\x1d.ntt.secrets.v1alpha2.Project\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a\x39\n\x07\x43urrent\x12.\n\x07project\x18\x01 \x01(\x0b\x32\x1d.ntt.secrets.v1alpha2.Project\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB~\n\x1b\x63om.ntt.secrets.pb.v1alpha2B\x12ProjectChangeProtoP\x00ZIgithub.com/cloudwan/edgelq-sdk/secrets/resources/v1alpha2/project;projectb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.secrets.proto.v1alpha2.project_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.secrets.pb.v1alpha2B\022ProjectChangeProtoP\000ZIgithub.com/cloudwan/edgelq-sdk/secrets/resources/v1alpha2/project;project'
  _globals['_PROJECTCHANGE']._serialized_start=191
  _globals['_PROJECTCHANGE']._serialized_end=828
  _globals['_PROJECTCHANGE_ADDED']._serialized_start=462
  _globals['_PROJECTCHANGE_ADDED']._serialized_end=537
  _globals['_PROJECTCHANGE_MODIFIED']._serialized_start=540
  _globals['_PROJECTCHANGE_MODIFIED']._serialized_end=709
  _globals['_PROJECTCHANGE_CURRENT']._serialized_start=711
  _globals['_PROJECTCHANGE_CURRENT']._serialized_end=768
  _globals['_PROJECTCHANGE_REMOVED']._serialized_start=770
  _globals['_PROJECTCHANGE_REMOVED']._serialized_end=813
# @@protoc_insertion_point(module_scope)