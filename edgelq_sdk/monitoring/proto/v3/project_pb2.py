# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v3/project.proto
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
    'edgelq-sdk/monitoring/proto/v3/project.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2
from goten_sdk.types import multi_region_policy_pb2 as goten__sdk_dot_types_dot_multi__region__policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,edgelq-sdk/monitoring/proto/v3/project.proto\x12\x11ntt.monitoring.v3\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\x1a)goten-sdk/types/multi_region_policy.proto\"\xc0\x01\n\x07Project\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12#\n\x08metadata\x18\x03 \x01(\x0b\x32\x11.goten.types.Meta\x12;\n\x13multi_region_policy\x18\x04 \x01(\x0b\x32\x1e.goten.types.MultiRegionPolicy:6\xea\x41\x33\n\x1dmonitoring.edgelq.com/Project\x12\x12projects/{project}Br\n\x18\x63om.ntt.monitoring.pb.v3B\x0cProjectProtoP\x01ZFgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v3/project;projectb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v3.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v3B\014ProjectProtoP\001ZFgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v3/project;project'
  _globals['_PROJECT']._loaded_options = None
  _globals['_PROJECT']._serialized_options = b'\352A3\n\035monitoring.edgelq.com/Project\022\022projects/{project}'
  _globals['_PROJECT']._serialized_start=166
  _globals['_PROJECT']._serialized_end=358
# @@protoc_insertion_point(module_scope)
