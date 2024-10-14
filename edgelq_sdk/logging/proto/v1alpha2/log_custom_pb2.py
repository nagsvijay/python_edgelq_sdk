# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1alpha2/log_custom.proto
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
    'edgelq-sdk/logging/proto/v1alpha2/log_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.common.rpc import status_pb2 as edgelq__sdk_dot_common_dot_rpc_dot_status__pb2
from edgelq_sdk.logging.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1alpha2_dot_common__pb2
from edgelq_sdk.logging.proto.v1alpha2 import log_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1alpha2_dot_log__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/logging/proto/v1alpha2/log_custom.proto\x12\x14ntt.logging.v1alpha2\x1a\"edgelq-sdk/common/rpc/status.proto\x1a.edgelq-sdk/logging/proto/v1alpha2/common.proto\x1a+edgelq-sdk/logging/proto/v1alpha2/log.proto\"\x8f\x01\n\x0fListLogsRequest\x12\x0f\n\x07parents\x18\x01 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x34\n\x08interval\x18\x03 \x01(\x0b\x32\".ntt.logging.v1alpha2.TimeInterval\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"\xa2\x01\n\x10ListLogsResponse\x12\'\n\x04logs\x18\x01 \x03(\x0b\x32\x19.ntt.logging.v1alpha2.Log\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12)\n\x10\x65xecution_errors\x18\x03 \x03(\x0b\x32\x0f.ntt.rpc.Status\x1a!\n\x0c\x45rrorDetails\x12\x11\n\tregion_id\x18\x01 \x01(\t\"L\n\x11\x43reateLogsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\'\n\x04logs\x18\x02 \x03(\x0b\x32\x19.ntt.logging.v1alpha2.Log\"\xb4\x02\n\x12\x43reateLogsResponse\x12I\n\tlog_names\x18\x01 \x03(\x0b\x32\x36.ntt.logging.v1alpha2.CreateLogsResponse.LogNamesEntry\x12I\n\x0b\x66\x61iled_logs\x18\x02 \x03(\x0b\x32\x34.ntt.logging.v1alpha2.CreateLogsResponse.CreateError\x1a/\n\rLogNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aW\n\x0b\x43reateError\x12\'\n\x04logs\x18\x01 \x03(\x0b\x32\x19.ntt.logging.v1alpha2.Log\x12\x1f\n\x06status\x18\x02 \x01(\x0b\x32\x0f.ntt.rpc.StatusBv\n\x1b\x63om.ntt.logging.pb.v1alpha2B\x0eLogCustomProtoP\x00ZEgithub.com/cloudwan/edgelq-sdk/logging/client/v1alpha2/log;log_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1alpha2.log_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.logging.pb.v1alpha2B\016LogCustomProtoP\000ZEgithub.com/cloudwan/edgelq-sdk/logging/client/v1alpha2/log;log_client'
  _globals['_CREATELOGSRESPONSE_LOGNAMESENTRY']._loaded_options = None
  _globals['_CREATELOGSRESPONSE_LOGNAMESENTRY']._serialized_options = b'8\001'
  _globals['_LISTLOGSREQUEST']._serialized_start=206
  _globals['_LISTLOGSREQUEST']._serialized_end=349
  _globals['_LISTLOGSRESPONSE']._serialized_start=352
  _globals['_LISTLOGSRESPONSE']._serialized_end=514
  _globals['_LISTLOGSRESPONSE_ERRORDETAILS']._serialized_start=481
  _globals['_LISTLOGSRESPONSE_ERRORDETAILS']._serialized_end=514
  _globals['_CREATELOGSREQUEST']._serialized_start=516
  _globals['_CREATELOGSREQUEST']._serialized_end=592
  _globals['_CREATELOGSRESPONSE']._serialized_start=595
  _globals['_CREATELOGSRESPONSE']._serialized_end=903
  _globals['_CREATELOGSRESPONSE_LOGNAMESENTRY']._serialized_start=767
  _globals['_CREATELOGSRESPONSE_LOGNAMESENTRY']._serialized_end=814
  _globals['_CREATELOGSRESPONSE_CREATEERROR']._serialized_start=816
  _globals['_CREATELOGSRESPONSE_CREATEERROR']._serialized_end=903
# @@protoc_insertion_point(module_scope)