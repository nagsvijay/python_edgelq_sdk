# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1/limit_pool.proto
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
    'edgelq-sdk/limits/proto/v1/limit_pool.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import organization_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_organization__pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_project__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as goten__sdk_dot_meta__service_dot_proto_dot_v1_dot_service__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+edgelq-sdk/limits/proto/v1/limit_pool.proto\x12\rntt.limits.v1\x1a*edgelq-sdk/iam/proto/v1/organization.proto\x1a%edgelq-sdk/iam/proto/v1/project.proto\x1a\x19google/api/resource.proto\x1a-goten-sdk/meta-service/proto/v1/service.proto\x1a\x1agoten-sdk/types/meta.proto\"\xc6\x02\n\tLimitPool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x08 \x01(\x0b\x32\x11.goten.types.Meta\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\t \x01(\t\x12\x17\n\x0f\x63onfigured_size\x18\x04 \x01(\x03\x12\x13\n\x0b\x61\x63tive_size\x18\x05 \x01(\x03\x12\x10\n\x08reserved\x18\x06 \x01(\x03\x12\x0e\n\x06source\x18\x07 \x01(\t:\x82\x01\xea\x41\x7f\n\x1blimits.edgelq.com/LimitPool\x12*services/{service}/limitPools/{limit_pool}\x12\x34organizations/{organization}/limitPools/{limit_pool}Br\n\x14\x63om.ntt.limits.pb.v1B\x0eLimitPoolProtoP\x01ZHgithub.com/cloudwan/edgelq-sdk/limits/resources/v1/limit_pool;limit_poolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1.limit_pool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.ntt.limits.pb.v1B\016LimitPoolProtoP\001ZHgithub.com/cloudwan/edgelq-sdk/limits/resources/v1/limit_pool;limit_pool'
  _globals['_LIMITPOOL']._loaded_options = None
  _globals['_LIMITPOOL']._serialized_options = b'\352A\177\n\033limits.edgelq.com/LimitPool\022*services/{service}/limitPools/{limit_pool}\0224organizations/{organization}/limitPools/{limit_pool}'
  _globals['_LIMITPOOL']._serialized_start=248
  _globals['_LIMITPOOL']._serialized_end=574
# @@protoc_insertion_point(module_scope)
