# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1/common.proto
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
    'edgelq-sdk/logging/proto/v1/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(edgelq-sdk/logging/proto/v1/common.proto\x12\x0entt.logging.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"3\n\x0fLabelDescriptor\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"!\n\x0bLabelKeySet\x12\x12\n\nlabel_keys\x18\x01 \x03(\t\"l\n\x0cTimeInterval\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampBb\n\x15\x63om.ntt.logging.pb.v1B\x0b\x43ommonProtoP\x01Z:github.com/cloudwan/edgelq-sdk/logging/resources/v1/commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.logging.pb.v1B\013CommonProtoP\001Z:github.com/cloudwan/edgelq-sdk/logging/resources/v1/common'
  _globals['_LABELDESCRIPTOR']._serialized_start=120
  _globals['_LABELDESCRIPTOR']._serialized_end=171
  _globals['_LABELKEYSET']._serialized_start=173
  _globals['_LABELKEYSET']._serialized_end=206
  _globals['_TIMEINTERVAL']._serialized_start=208
  _globals['_TIMEINTERVAL']._serialized_end=316
# @@protoc_insertion_point(module_scope)
