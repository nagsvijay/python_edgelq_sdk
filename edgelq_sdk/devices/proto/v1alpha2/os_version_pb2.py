# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1alpha2/os_version.proto
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
    'edgelq-sdk/devices/proto/v1alpha2/os_version.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/devices/proto/v1alpha2/os_version.proto\x12\x14ntt.devices.v1alpha2\x1a*edgelq-sdk/iam/proto/v1alpha2/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xb6\x02\n\tOsVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x04 \x01(\t\x12 \n\x18minimum_previous_version\x18\x05 \x01(\t\x12\x38\n\x07\x63hannel\x18\x06 \x01(\x0e\x32\'.ntt.devices.v1alpha2.OsVersion.Channel\"8\n\x07\x43hannel\x12\x17\n\x13\x43HANNEL_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04\x42\x45TA\x10\x02::\xea\x41\x37\n\x1c\x64\x65vices.edgelq.com/OsVersion\x12\x17osVersions/{os_version}B\x80\x01\n\x1b\x63om.ntt.devices.pb.v1alpha2B\x0eOsVersionProtoP\x01ZOgithub.com/cloudwan/edgelq-sdk/devices/resources/v1alpha2/os_version;os_versionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1alpha2.os_version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.devices.pb.v1alpha2B\016OsVersionProtoP\001ZOgithub.com/cloudwan/edgelq-sdk/devices/resources/v1alpha2/os_version;os_version'
  _globals['_OSVERSION']._loaded_options = None
  _globals['_OSVERSION']._serialized_options = b'\352A7\n\034devices.edgelq.com/OsVersion\022\027osVersions/{os_version}'
  _globals['_OSVERSION']._serialized_start=176
  _globals['_OSVERSION']._serialized_end=486
  _globals['_OSVERSION_CHANNEL']._serialized_start=370
  _globals['_OSVERSION_CHANNEL']._serialized_end=426
# @@protoc_insertion_point(module_scope)
