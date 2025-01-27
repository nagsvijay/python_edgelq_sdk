# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/audit/proto/v1/resource_change_log_custom.proto
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
    'edgelq-sdk/audit/proto/v1/resource_change_log_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.audit.proto.v1 import common_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_common__pb2
from edgelq_sdk.audit.proto.v1 import resource_change_log_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_resource__change__log__pb2
from edgelq_sdk.common.rpc import status_pb2 as edgelq__sdk_dot_common_dot_rpc_dot_status__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:edgelq-sdk/audit/proto/v1/resource_change_log_custom.proto\x12\x0cntt.audit.v1\x1a&edgelq-sdk/audit/proto/v1/common.proto\x1a\x33\x65\x64gelq-sdk/audit/proto/v1/resource_change_log.proto\x1a\"edgelq-sdk/common/rpc/status.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x95\x01\n\x1dListResourceChangeLogsRequest\x12\x0f\n\x07parents\x18\x01 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12,\n\x08interval\x18\x04 \x01(\x0b\x32\x1a.ntt.audit.v1.TimeInterval\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"\xc6\x01\n\x1eListResourceChangeLogsResponse\x12=\n\x14resource_change_logs\x18\x01 \x03(\x0b\x32\x1f.ntt.audit.v1.ResourceChangeLog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12)\n\x10\x65xecution_errors\x18\x03 \x03(\x0b\x32\x0f.ntt.rpc.Status\x1a!\n\x0c\x45rrorDetails\x12\x11\n\tregion_id\x18\x01 \x01(\t\"\xd9\x02\n+CreatePreCommittedResourceChangeLogsRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\x04\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0e\x61uthentication\x18\x03 \x01(\x0b\x32\x1c.ntt.audit.v1.Authentication\x12*\n\x07service\x18\x04 \x01(\x0b\x32\x19.ntt.audit.v1.ServiceData\x12\x44\n\x0btransaction\x18\x05 \x01(\x0b\x32/.ntt.audit.v1.ResourceChangeLog.TransactionInfo\x12?\n\x07\x63hanges\x18\x06 \x03(\x0b\x32..ntt.audit.v1.ResourceChangeLog.ResourceChange\"@\n,CreatePreCommittedResourceChangeLogsResponse\x12\x10\n\x08log_keys\x18\x01 \x03(\x0c\"\xe0\x01\n\'SetResourceChangeLogsCommitStateRequest\x12\x10\n\x08log_keys\x18\x01 \x03(\x0c\x12*\n\x07service\x18\x04 \x01(\x0b\x32\x19.ntt.audit.v1.ServiceData\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\ttx_result\x18\x03 \x01(\x0e\x32\x35.ntt.audit.v1.ResourceChangeLog.TransactionInfo.State\"*\n(SetResourceChangeLogsCommitStateResponseB\x94\x01\n\x13\x63om.ntt.audit.pb.v1B\x1cResourceChangeLogCustomProtoP\x00Z]github.com/cloudwan/edgelq-sdk/audit/client/v1/resource_change_log;resource_change_log_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.audit.proto.v1.resource_change_log_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.ntt.audit.pb.v1B\034ResourceChangeLogCustomProtoP\000Z]github.com/cloudwan/edgelq-sdk/audit/client/v1/resource_change_log;resource_change_log_client'
  _globals['_LISTRESOURCECHANGELOGSREQUEST']._serialized_start=239
  _globals['_LISTRESOURCECHANGELOGSREQUEST']._serialized_end=388
  _globals['_LISTRESOURCECHANGELOGSRESPONSE']._serialized_start=391
  _globals['_LISTRESOURCECHANGELOGSRESPONSE']._serialized_end=589
  _globals['_LISTRESOURCECHANGELOGSRESPONSE_ERRORDETAILS']._serialized_start=556
  _globals['_LISTRESOURCECHANGELOGSRESPONSE_ERRORDETAILS']._serialized_end=589
  _globals['_CREATEPRECOMMITTEDRESOURCECHANGELOGSREQUEST']._serialized_start=592
  _globals['_CREATEPRECOMMITTEDRESOURCECHANGELOGSREQUEST']._serialized_end=937
  _globals['_CREATEPRECOMMITTEDRESOURCECHANGELOGSRESPONSE']._serialized_start=939
  _globals['_CREATEPRECOMMITTEDRESOURCECHANGELOGSRESPONSE']._serialized_end=1003
  _globals['_SETRESOURCECHANGELOGSCOMMITSTATEREQUEST']._serialized_start=1006
  _globals['_SETRESOURCECHANGELOGSCOMMITSTATEREQUEST']._serialized_end=1230
  _globals['_SETRESOURCECHANGELOGSCOMMITSTATERESPONSE']._serialized_start=1232
  _globals['_SETRESOURCECHANGELOGSCOMMITSTATERESPONSE']._serialized_end=1274
# @@protoc_insertion_point(module_scope)
