# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/limit_custom.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/limit_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1alpha2 import limit_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pb2
from edgelq_sdk.limits.proto.v1alpha2 import limit_change_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3edgelq-sdk/limits/proto/v1alpha2/limit_custom.proto\x12\x13ntt.limits.v1alpha2\x1a,edgelq-sdk/limits/proto/v1alpha2/limit.proto\x1a\x33\x65\x64gelq-sdk/limits/proto/v1alpha2/limit_change.proto\")\n\x19MigrateLimitSourceRequest\x12\x0c\n\x04name\x18\x01 \x01(\tBz\n\x1a\x63om.ntt.limits.pb.v1alpha2B\x10LimitCustomProtoP\x00ZHgithub.com/cloudwan/edgelq-sdk/limits/client/v1alpha2/limit;limit_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.limit_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\020LimitCustomProtoP\000ZHgithub.com/cloudwan/edgelq-sdk/limits/client/v1alpha2/limit;limit_client'
  _globals['_MIGRATELIMITSOURCEREQUEST']._serialized_start=175
  _globals['_MIGRATELIMITSOURCEREQUEST']._serialized_end=216
# @@protoc_insertion_point(module_scope)
