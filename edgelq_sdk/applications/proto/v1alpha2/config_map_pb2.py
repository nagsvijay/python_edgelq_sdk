# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/applications/proto/v1alpha2/config_map.proto
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
    'edgelq-sdk/applications/proto/v1alpha2/config_map.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/applications/proto/v1alpha2/config_map.proto\x12\x19ntt.applications.v1alpha2\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xa2\x03\n\tConfigMap\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12#\n\x08metadata\x18\x03 \x01(\x0b\x32\x11.goten.types.Meta\x12<\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32..ntt.applications.v1alpha2.ConfigMap.DataEntry\x12I\n\x0b\x62inary_data\x18\x05 \x03(\x0b\x32\x34.ntt.applications.v1alpha2.ConfigMap.BinaryDataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0f\x42inaryDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01:c\xea\x41`\n!applications.edgelq.com/ConfigMap\x12;projects/{project}/regions/{region}/configMaps/{config_map}B\x8a\x01\n com.ntt.applications.pb.v1alpha2B\x0e\x43onfigMapProtoP\x01ZTgithub.com/cloudwan/edgelq-sdk/applications/resources/v1alpha2/config_map;config_mapb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.applications.proto.v1alpha2.config_map_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.ntt.applications.pb.v1alpha2B\016ConfigMapProtoP\001ZTgithub.com/cloudwan/edgelq-sdk/applications/resources/v1alpha2/config_map;config_map'
  _globals['_CONFIGMAP_DATAENTRY']._loaded_options = None
  _globals['_CONFIGMAP_DATAENTRY']._serialized_options = b'8\001'
  _globals['_CONFIGMAP_BINARYDATAENTRY']._loaded_options = None
  _globals['_CONFIGMAP_BINARYDATAENTRY']._serialized_options = b'8\001'
  _globals['_CONFIGMAP']._loaded_options = None
  _globals['_CONFIGMAP']._serialized_options = b'\352A`\n!applications.edgelq.com/ConfigMap\022;projects/{project}/regions/{region}/configMaps/{config_map}'
  _globals['_CONFIGMAP']._serialized_start=142
  _globals['_CONFIGMAP']._serialized_end=560
  _globals['_CONFIGMAP_DATAENTRY']._serialized_start=365
  _globals['_CONFIGMAP_DATAENTRY']._serialized_end=408
  _globals['_CONFIGMAP_BINARYDATAENTRY']._serialized_start=410
  _globals['_CONFIGMAP_BINARYDATAENTRY']._serialized_end=459
# @@protoc_insertion_point(module_scope)
