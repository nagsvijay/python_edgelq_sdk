# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1/plan_assignment_custom.proto
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
    'edgelq-sdk/limits/proto/v1/plan_assignment_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1 import plan_assignment_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__assignment__pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_change_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__assignment__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/limits/proto/v1/plan_assignment_custom.proto\x12\rntt.limits.v1\x1a\x30\x65\x64gelq-sdk/limits/proto/v1/plan_assignment.proto\x1a\x37\x65\x64gelq-sdk/limits/proto/v1/plan_assignment_change.proto\"V\n\x1cMigratePlanAssignmentRequest\x12\x36\n\x0fplan_assignment\x18\x02 \x01(\x0b\x32\x1d.ntt.limits.v1.PlanAssignmentB\x8b\x01\n\x14\x63om.ntt.limits.pb.v1B\x19PlanAssignmentCustomProtoP\x00ZVgithub.com/cloudwan/edgelq-sdk/limits/client/v1/plan_assignment;plan_assignment_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1.plan_assignment_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.ntt.limits.pb.v1B\031PlanAssignmentCustomProtoP\000ZVgithub.com/cloudwan/edgelq-sdk/limits/client/v1/plan_assignment;plan_assignment_client'
  _globals['_MIGRATEPLANASSIGNMENTREQUEST']._serialized_start=181
  _globals['_MIGRATEPLANASSIGNMENTREQUEST']._serialized_end=267
# @@protoc_insertion_point(module_scope)
