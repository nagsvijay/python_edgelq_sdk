# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/condition_change.proto
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
    'edgelq-sdk/iam/proto/v1/condition_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import condition_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_condition__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.edgelq-sdk/iam/proto/v1/condition_change.proto\x12\nntt.iam.v1\x1a\'edgelq-sdk/iam/proto/v1/condition.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xcd\x04\n\x0f\x43onditionChange\x12\x32\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32!.ntt.iam.v1.ConditionChange.AddedH\x00\x12\x38\n\x08modified\x18\x02 \x01(\x0b\x32$.ntt.iam.v1.ConditionChange.ModifiedH\x00\x12\x36\n\x07\x63urrent\x18\x04 \x01(\x0b\x32#.ntt.iam.v1.ConditionChange.CurrentH\x00\x12\x36\n\x07removed\x18\x03 \x01(\x0b\x32#.ntt.iam.v1.ConditionChange.RemovedH\x00\x1a\x45\n\x05\x41\x64\x64\x65\x64\x12(\n\tcondition\x18\x01 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xa3\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\tcondition\x18\x02 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a\x33\n\x07\x43urrent\x12(\n\tcondition\x18\x01 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeBp\n\x11\x63om.ntt.iam.pb.v1B\x14\x43onditionChangeProtoP\x00ZCgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/condition;conditionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.condition_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\024ConditionChangeProtoP\000ZCgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/condition;condition'
  _globals['_CONDITIONCHANGE']._serialized_start=165
  _globals['_CONDITIONCHANGE']._serialized_end=754
  _globals['_CONDITIONCHANGE_ADDED']._serialized_start=406
  _globals['_CONDITIONCHANGE_ADDED']._serialized_end=475
  _globals['_CONDITIONCHANGE_MODIFIED']._serialized_start=478
  _globals['_CONDITIONCHANGE_MODIFIED']._serialized_end=641
  _globals['_CONDITIONCHANGE_CURRENT']._serialized_start=643
  _globals['_CONDITIONCHANGE_CURRENT']._serialized_end=694
  _globals['_CONDITIONCHANGE_REMOVED']._serialized_start=696
  _globals['_CONDITIONCHANGE_REMOVED']._serialized_end=739
# @@protoc_insertion_point(module_scope)
