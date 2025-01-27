# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1/plan.proto
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
    'edgelq-sdk/limits/proto/v1/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_common__pb2
from edgelq_sdk.limits.proto.v1 import common_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as goten__sdk_dot_meta__service_dot_proto_dot_v1_dot_service__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%edgelq-sdk/limits/proto/v1/plan.proto\x12\rntt.limits.v1\x1a$edgelq-sdk/iam/proto/v1/common.proto\x1a\'edgelq-sdk/limits/proto/v1/common.proto\x1a\x19google/api/resource.proto\x1a-goten-sdk/meta-service/proto/v1/service.proto\x1a\x1agoten-sdk/types/meta.proto\"\xf1\x03\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x05 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x37\n\x0fresource_limits\x18\x04 \x03(\x0b\x32\x1e.ntt.limits.v1.Plan.LimitValue\x12\x31\n\nplan_level\x18\x06 \x01(\x0e\x32\x1d.ntt.limits.v1.Plan.PlanLevel\x12/\n\rbusiness_tier\x18\x07 \x01(\x0e\x32\x18.ntt.iam.v1.BusinessTier\x12\x12\n\ngeneration\x18\x08 \x01(\x03\x1a-\n\nLimitValue\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\"F\n\tPlanLevel\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SERVICE\x10\x01\x12\x10\n\x0cORGANIZATION\x10\x02\x12\x0b\n\x07PROJECT\x10\x03:g\xea\x41\x64\n\x16limits.edgelq.com/Plan\x12\x1fservices/{service}/plans/{plan}\x12)organizations/{organization}/plans/{plan}Ba\n\x14\x63om.ntt.limits.pb.v1B\tPlanProtoP\x01Z<github.com/cloudwan/edgelq-sdk/limits/resources/v1/plan;planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.ntt.limits.pb.v1B\tPlanProtoP\001Z<github.com/cloudwan/edgelq-sdk/limits/resources/v1/plan;plan'
  _globals['_PLAN']._loaded_options = None
  _globals['_PLAN']._serialized_options = b'\352Ad\n\026limits.edgelq.com/Plan\022\037services/{service}/plans/{plan}\022)organizations/{organization}/plans/{plan}'
  _globals['_PLAN']._serialized_start=238
  _globals['_PLAN']._serialized_end=735
  _globals['_PLAN_LIMITVALUE']._serialized_start=513
  _globals['_PLAN_LIMITVALUE']._serialized_end=558
  _globals['_PLAN_PLANLEVEL']._serialized_start=560
  _globals['_PLAN_PLANLEVEL']._serialized_end=630
# @@protoc_insertion_point(module_scope)
