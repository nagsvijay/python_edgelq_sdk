# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/applications/proto/v1/project_change.proto
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
    'edgelq-sdk/applications/proto/v1/project_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.applications.proto.v1 import project_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_project__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5edgelq-sdk/applications/proto/v1/project_change.proto\x12\x13ntt.applications.v1\x1a.edgelq-sdk/applications/proto/v1/project.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xf6\x04\n\rProjectChange\x12\x39\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32(.ntt.applications.v1.ProjectChange.AddedH\x00\x12?\n\x08modified\x18\x02 \x01(\x0b\x32+.ntt.applications.v1.ProjectChange.ModifiedH\x00\x12=\n\x07\x63urrent\x18\x04 \x01(\x0b\x32*.ntt.applications.v1.ProjectChange.CurrentH\x00\x12=\n\x07removed\x18\x03 \x01(\x0b\x32*.ntt.applications.v1.ProjectChange.RemovedH\x00\x1aJ\n\x05\x41\x64\x64\x65\x64\x12-\n\x07project\x18\x01 \x01(\x0b\x32\x1c.ntt.applications.v1.Project\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xa8\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07project\x18\x02 \x01(\x0b\x32\x1c.ntt.applications.v1.Project\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a\x38\n\x07\x43urrent\x12-\n\x07project\x18\x01 \x01(\x0b\x32\x1c.ntt.applications.v1.Project\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB|\n\x1a\x63om.ntt.applications.pb.v1B\x12ProjectChangeProtoP\x00ZHgithub.com/cloudwan/edgelq-sdk/applications/resources/v1/project;projectb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.applications.proto.v1.project_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.applications.pb.v1B\022ProjectChangeProtoP\000ZHgithub.com/cloudwan/edgelq-sdk/applications/resources/v1/project;project'
  _globals['_PROJECTCHANGE']._serialized_start=188
  _globals['_PROJECTCHANGE']._serialized_end=818
  _globals['_PROJECTCHANGE_ADDED']._serialized_start=455
  _globals['_PROJECTCHANGE_ADDED']._serialized_end=529
  _globals['_PROJECTCHANGE_MODIFIED']._serialized_start=532
  _globals['_PROJECTCHANGE_MODIFIED']._serialized_end=700
  _globals['_PROJECTCHANGE_CURRENT']._serialized_start=702
  _globals['_PROJECTCHANGE_CURRENT']._serialized_end=758
  _globals['_PROJECTCHANGE_REMOVED']._serialized_start=760
  _globals['_PROJECTCHANGE_REMOVED']._serialized_end=803
# @@protoc_insertion_point(module_scope)
