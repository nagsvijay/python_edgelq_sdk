# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/group.proto
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
    'edgelq-sdk/iam/proto/v1/group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#edgelq-sdk/iam/proto/v1/group.proto\x12\nntt.iam.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\x94\x02\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x05 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t:\x9d\x01\xea\x41\x99\x01\n\x14iam.edgelq.com/Group\x12\x0egroups/{group}\x12!projects/{project}/groups/{group}\x12+organizations/{organization}/groups/{group}\x12!services/{service}/groups/{group}B^\n\x11\x63om.ntt.iam.pb.v1B\nGroupProtoP\x01Z;github.com/cloudwan/edgelq-sdk/iam/resources/v1/group;groupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\nGroupProtoP\001Z;github.com/cloudwan/edgelq-sdk/iam/resources/v1/group;group'
  _globals['_GROUP']._loaded_options = None
  _globals['_GROUP']._serialized_options = b'\352A\231\001\n\024iam.edgelq.com/Group\022\016groups/{group}\022!projects/{project}/groups/{group}\022+organizations/{organization}/groups/{group}\022!services/{service}/groups/{group}'
  _globals['_GROUP']._serialized_start=107
  _globals['_GROUP']._serialized_end=383
# @@protoc_insertion_point(module_scope)
