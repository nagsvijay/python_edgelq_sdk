# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/group_change.proto
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
    'edgelq-sdk/iam/proto/v1/group_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import group_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*edgelq-sdk/iam/proto/v1/group_change.proto\x12\nntt.iam.v1\x1a#edgelq-sdk/iam/proto/v1/group.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xa1\x04\n\x0bGroupChange\x12.\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\x1d.ntt.iam.v1.GroupChange.AddedH\x00\x12\x34\n\x08modified\x18\x02 \x01(\x0b\x32 .ntt.iam.v1.GroupChange.ModifiedH\x00\x12\x32\n\x07\x63urrent\x18\x04 \x01(\x0b\x32\x1f.ntt.iam.v1.GroupChange.CurrentH\x00\x12\x32\n\x07removed\x18\x03 \x01(\x0b\x32\x1f.ntt.iam.v1.GroupChange.RemovedH\x00\x1a=\n\x05\x41\x64\x64\x65\x64\x12 \n\x05group\x18\x01 \x01(\x0b\x32\x11.ntt.iam.v1.Group\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\x9b\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x05group\x18\x02 \x01(\x0b\x32\x11.ntt.iam.v1.Group\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a+\n\x07\x43urrent\x12 \n\x05group\x18\x01 \x01(\x0b\x32\x11.ntt.iam.v1.Group\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeBd\n\x11\x63om.ntt.iam.pb.v1B\x10GroupChangeProtoP\x00Z;github.com/cloudwan/edgelq-sdk/iam/resources/v1/group;groupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.group_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\020GroupChangeProtoP\000Z;github.com/cloudwan/edgelq-sdk/iam/resources/v1/group;group'
  _globals['_GROUPCHANGE']._serialized_start=157
  _globals['_GROUPCHANGE']._serialized_end=702
  _globals['_GROUPCHANGE_ADDED']._serialized_start=378
  _globals['_GROUPCHANGE_ADDED']._serialized_end=439
  _globals['_GROUPCHANGE_MODIFIED']._serialized_start=442
  _globals['_GROUPCHANGE_MODIFIED']._serialized_end=597
  _globals['_GROUPCHANGE_CURRENT']._serialized_start=599
  _globals['_GROUPCHANGE_CURRENT']._serialized_end=642
  _globals['_GROUPCHANGE_REMOVED']._serialized_start=644
  _globals['_GROUPCHANGE_REMOVED']._serialized_end=687
# @@protoc_insertion_point(module_scope)