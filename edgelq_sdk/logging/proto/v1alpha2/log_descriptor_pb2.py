# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1alpha2/log_descriptor.proto
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
    'edgelq-sdk/logging/proto/v1alpha2/log_descriptor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.logging.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1alpha2_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/logging/proto/v1alpha2/log_descriptor.proto\x12\x14ntt.logging.v1alpha2\x1a.edgelq-sdk/logging/proto/v1alpha2/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xa4\x03\n\rLogDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x35\n\x06labels\x18\x04 \x03(\x0b\x32%.ntt.logging.v1alpha2.LabelDescriptor\x12\x42\n\x17promoted_label_key_sets\x18\x05 \x03(\x0b\x32!.ntt.logging.v1alpha2.LabelKeySet\x12#\n\x08metadata\x18\x06 \x01(\x0b\x32\x11.goten.types.Meta:\xb9\x01\xea\x41\xb5\x01\n logging.edgelq.com/LogDescriptor\x12\x1flogDescriptors/{log_descriptor}\x12\x32projects/{project}/logDescriptors/{log_descriptor}\x12<organizations/{organization}/logDescriptors/{log_descriptor}B\x8c\x01\n\x1b\x63om.ntt.logging.pb.v1alpha2B\x12LogDescriptorProtoP\x01ZWgithub.com/cloudwan/edgelq-sdk/logging/resources/v1alpha2/log_descriptor;log_descriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1alpha2.log_descriptor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.logging.pb.v1alpha2B\022LogDescriptorProtoP\001ZWgithub.com/cloudwan/edgelq-sdk/logging/resources/v1alpha2/log_descriptor;log_descriptor'
  _globals['_LOGDESCRIPTOR']._loaded_options = None
  _globals['_LOGDESCRIPTOR']._serialized_options = b'\352A\265\001\n logging.edgelq.com/LogDescriptor\022\037logDescriptors/{log_descriptor}\0222projects/{project}/logDescriptors/{log_descriptor}\022<organizations/{organization}/logDescriptors/{log_descriptor}'
  _globals['_LOGDESCRIPTOR']._serialized_start=184
  _globals['_LOGDESCRIPTOR']._serialized_end=604
# @@protoc_insertion_point(module_scope)
