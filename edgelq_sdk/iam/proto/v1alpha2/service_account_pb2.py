# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/service_account.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/service_account.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3edgelq-sdk/iam/proto/v1alpha2/service_account.proto\x12\x10ntt.iam.v1alpha2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xd9\x01\n\x0eServiceAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x05\x65mail\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03\x12#\n\x08metadata\x18\x03 \x01(\x0b\x32\x11.goten.types.Meta:i\xea\x41\x66\n\x1diam.edgelq.com/ServiceAccount\x12\x45projects/{project}/regions/{region}/serviceAccounts/{service_account}B\x87\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x13ServiceAccountProtoP\x01ZUgithub.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/service_account;service_accountb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.service_account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\023ServiceAccountProtoP\001ZUgithub.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/service_account;service_account'
  _globals['_SERVICEACCOUNT'].fields_by_name['email']._loaded_options = None
  _globals['_SERVICEACCOUNT'].fields_by_name['email']._serialized_options = b'\342A\001\003'
  _globals['_SERVICEACCOUNT']._loaded_options = None
  _globals['_SERVICEACCOUNT']._serialized_options = b'\352Af\n\035iam.edgelq.com/ServiceAccount\022Eprojects/{project}/regions/{region}/serviceAccounts/{service_account}'
  _globals['_SERVICEACCOUNT']._serialized_start=162
  _globals['_SERVICEACCOUNT']._serialized_end=379
# @@protoc_insertion_point(module_scope)
