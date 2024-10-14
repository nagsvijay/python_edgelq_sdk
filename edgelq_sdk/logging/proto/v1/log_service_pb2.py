# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/logging/proto/v1/log_service.proto
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
    'edgelq-sdk/logging/proto/v1/log_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.logging.proto.v1 import log_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1_dot_log__pb2
from edgelq_sdk.logging.proto.v1 import log_custom_pb2 as edgelq__sdk_dot_logging_dot_proto_dot_v1_dot_log__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-edgelq-sdk/logging/proto/v1/log_service.proto\x12\x0entt.logging.v1\x1a%edgelq-sdk/logging/proto/v1/log.proto\x1a,edgelq-sdk/logging/proto/v1/log_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto2\x8b\x02\n\nLogService\x12_\n\x08ListLogs\x12\x1f.ntt.logging.v1.ListLogsRequest\x1a .ntt.logging.v1.ListLogsResponse\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/logs\x12k\n\nCreateLogs\x12!.ntt.logging.v1.CreateLogsRequest\x1a\".ntt.logging.v1.CreateLogsResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x08/v1/logs:\x04logs\x1a/\xca\x41\x12logging.edgelq.com\xd2\x41\x17https://apis.edgelq.comBk\n\x15\x63om.ntt.logging.pb.v1B\x0fLogServiceProtoP\x00Z?github.com/cloudwan/edgelq-sdk/logging/client/v1/log;log_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.logging.proto.v1.log_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.logging.pb.v1B\017LogServiceProtoP\000Z?github.com/cloudwan/edgelq-sdk/logging/client/v1/log;log_client'
  _globals['_LOGSERVICE']._loaded_options = None
  _globals['_LOGSERVICE']._serialized_options = b'\312A\022logging.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_LOGSERVICE'].methods_by_name['ListLogs']._loaded_options = None
  _globals['_LOGSERVICE'].methods_by_name['ListLogs']._serialized_options = b'\202\323\344\223\002\n\022\010/v1/logs'
  _globals['_LOGSERVICE'].methods_by_name['CreateLogs']._loaded_options = None
  _globals['_LOGSERVICE'].methods_by_name['CreateLogs']._serialized_options = b'\202\323\344\223\002\020\"\010/v1/logs:\004logs'
  _globals['_LOGSERVICE']._serialized_start=364
  _globals['_LOGSERVICE']._serialized_end=631
# @@protoc_insertion_point(module_scope)
