# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/plan.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_common__pb2
from edgelq_sdk.limits.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_common__pb2
from edgelq_sdk.meta.proto.v1alpha2 import service_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_service__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+edgelq-sdk/limits/proto/v1alpha2/plan.proto\x12\x13ntt.limits.v1alpha2\x1a*edgelq-sdk/iam/proto/v1alpha2/common.proto\x1a-edgelq-sdk/limits/proto/v1alpha2/common.proto\x1a,edgelq-sdk/meta/proto/v1alpha2/service.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xfb\x02\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x37\n\x0fresource_limits\x18\x04 \x03(\x0b\x32\x1e.ntt.limits.v1alpha2.Allowance\x12\x37\n\nplan_level\x18\x06 \x01(\x0e\x32#.ntt.limits.v1alpha2.Plan.PlanLevel\x12\x35\n\rbusiness_tier\x18\x07 \x01(\x0e\x32\x1e.ntt.iam.v1alpha2.BusinessTier\x12#\n\x08metadata\x18\x05 \x01(\x0b\x32\x11.goten.types.Meta\"E\n\tPlanLevel\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x10\n\x0cORGANIZATION\x10\x02\x12\x0b\n\x07PROJECT\x10\x03:)\xea\x41&\n\x16limits.edgelq.com/Plan\x12\x0cplans/{plan}Bm\n\x1a\x63om.ntt.limits.pb.v1alpha2B\tPlanProtoP\x01ZBgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/plan;planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\tPlanProtoP\001ZBgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/plan;plan'
  _globals['_PLAN']._loaded_options = None
  _globals['_PLAN']._serialized_options = b'\352A&\n\026limits.edgelq.com/Plan\022\014plans/{plan}'
  _globals['_PLAN']._serialized_start=261
  _globals['_PLAN']._serialized_end=640
  _globals['_PLAN_PLANLEVEL']._serialized_start=528
  _globals['_PLAN_PLANLEVEL']._serialized_end=597
# @@protoc_insertion_point(module_scope)
