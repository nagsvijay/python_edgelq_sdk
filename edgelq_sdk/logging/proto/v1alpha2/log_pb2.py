# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1alpha2/log.proto
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
    'edgelq-sdk/logging/proto/v1alpha2/log.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+edgelq-sdk/logging/proto/v1alpha2/log.proto\x12\x14ntt.logging.v1alpha2\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x97\x03\n\x03Log\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x16\n\x0elog_descriptor\x18\x06 \x01(\t\x12\x35\n\x06labels\x18\x07 \x03(\x0b\x32%.ntt.logging.v1alpha2.Log.LabelsEntry\x12(\n\x04time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x07payload\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:o\xea\x41l\n\x16logging.edgelq.com/Log\x12\nlogs/{log}\x12\x1dprojects/{project}/logs/{log}\x12\'organizations/{organization}/logs/{log}Bl\n\x1b\x63om.ntt.logging.pb.v1alpha2B\x08LogProtoP\x01ZAgithub.com/cloudwan/edgelq-sdk/logging/resources/v1alpha2/log;logb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1alpha2.log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.logging.pb.v1alpha2B\010LogProtoP\001ZAgithub.com/cloudwan/edgelq-sdk/logging/resources/v1alpha2/log;log'
  _globals['_LOG_LABELSENTRY']._loaded_options = None
  _globals['_LOG_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_LOG']._loaded_options = None
  _globals['_LOG']._serialized_options = b'\352Al\n\026logging.edgelq.com/Log\022\nlogs/{log}\022\035projects/{project}/logs/{log}\022\'organizations/{organization}/logs/{log}'
  _globals['_LOG']._serialized_start=160
  _globals['_LOG']._serialized_end=567
  _globals['_LOG_LABELSENTRY']._serialized_start=409
  _globals['_LOG_LABELSENTRY']._serialized_end=454
# @@protoc_insertion_point(module_scope)