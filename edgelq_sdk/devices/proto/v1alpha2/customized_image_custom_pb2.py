# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1alpha2/customized_image_custom.proto
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
    'edgelq-sdk/devices/proto/v1alpha2/customized_image_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1alpha2 import customized_image_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_customized__image__pb2
from edgelq_sdk.devices.proto.v1alpha2 import customized_image_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_customized__image__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/devices/proto/v1alpha2/customized_image_custom.proto\x12\x14ntt.devices.v1alpha2\x1a\x38\x65\x64gelq-sdk/devices/proto/v1alpha2/customized_image.proto\x1a?edgelq-sdk/devices/proto/v1alpha2/customized_image_change.proto\"!\n\x11RequestUrlRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"2\n\x12RequestUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07headers\x18\x02 \x03(\tB\x9c\x01\n\x1b\x63om.ntt.devices.pb.v1alpha2B\x1a\x43ustomizedImageCustomProtoP\x00Z_github.com/cloudwan/edgelq-sdk/devices/client/v1alpha2/customized_image;customized_image_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1alpha2.customized_image_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.devices.pb.v1alpha2B\032CustomizedImageCustomProtoP\000Z_github.com/cloudwan/edgelq-sdk/devices/client/v1alpha2/customized_image;customized_image_client'
  _globals['_REQUESTURLREQUEST']._serialized_start=212
  _globals['_REQUESTURLREQUEST']._serialized_end=245
  _globals['_REQUESTURLRESPONSE']._serialized_start=247
  _globals['_REQUESTURLRESPONSE']._serialized_end=297
# @@protoc_insertion_point(module_scope)
