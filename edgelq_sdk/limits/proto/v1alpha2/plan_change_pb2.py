# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/plan_change.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/plan_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1alpha2 import plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/limits/proto/v1alpha2/plan_change.proto\x12\x13ntt.limits.v1alpha2\x1a+edgelq-sdk/limits/proto/v1alpha2/plan.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xd5\x04\n\nPlanChange\x12\x36\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32%.ntt.limits.v1alpha2.PlanChange.AddedH\x00\x12<\n\x08modified\x18\x02 \x01(\x0b\x32(.ntt.limits.v1alpha2.PlanChange.ModifiedH\x00\x12:\n\x07\x63urrent\x18\x04 \x01(\x0b\x32\'.ntt.limits.v1alpha2.PlanChange.CurrentH\x00\x12:\n\x07removed\x18\x03 \x01(\x0b\x32\'.ntt.limits.v1alpha2.PlanChange.RemovedH\x00\x1a\x44\n\x05\x41\x64\x64\x65\x64\x12\'\n\x04plan\x18\x01 \x01(\x0b\x32\x19.ntt.limits.v1alpha2.Plan\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xa2\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x04plan\x18\x02 \x01(\x0b\x32\x19.ntt.limits.v1alpha2.Plan\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a\x32\n\x07\x43urrent\x12\'\n\x04plan\x18\x01 \x01(\x0b\x32\x19.ntt.limits.v1alpha2.Plan\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeBs\n\x1a\x63om.ntt.limits.pb.v1alpha2B\x0fPlanChangeProtoP\x00ZBgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/plan;planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.plan_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\017PlanChangeProtoP\000ZBgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/plan;plan'
  _globals['_PLANCHANGE']._serialized_start=182
  _globals['_PLANCHANGE']._serialized_end=779
  _globals['_PLANCHANGE_ADDED']._serialized_start=434
  _globals['_PLANCHANGE_ADDED']._serialized_end=502
  _globals['_PLANCHANGE_MODIFIED']._serialized_start=505
  _globals['_PLANCHANGE_MODIFIED']._serialized_end=667
  _globals['_PLANCHANGE_CURRENT']._serialized_start=669
  _globals['_PLANCHANGE_CURRENT']._serialized_end=719
  _globals['_PLANCHANGE_REMOVED']._serialized_start=721
  _globals['_PLANCHANGE_REMOVED']._serialized_end=764
# @@protoc_insertion_point(module_scope)
