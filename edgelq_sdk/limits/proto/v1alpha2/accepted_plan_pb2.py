# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/accepted_plan.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/accepted_plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import organization_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_organization__pb2
from edgelq_sdk.iam.proto.v1alpha2 import project_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_project__pb2
from edgelq_sdk.limits.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4edgelq-sdk/limits/proto/v1alpha2/accepted_plan.proto\x12\x13ntt.limits.v1alpha2\x1a\x30\x65\x64gelq-sdk/iam/proto/v1alpha2/organization.proto\x1a+edgelq-sdk/iam/proto/v1alpha2/project.proto\x1a-edgelq-sdk/limits/proto/v1alpha2/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\x8d\x04\n\x0c\x41\x63\x63\x65ptedPlan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04plan\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x32\n\nextensions\x18\x04 \x03(\x0b\x32\x1e.ntt.limits.v1alpha2.Allowance\x12I\n\x16regional_distributions\x18\x05 \x03(\x0b\x32).ntt.limits.v1alpha2.RegionalDistribution\x12<\n\x08\x61ssignee\x18\x06 \x01(\x0b\x32*.ntt.limits.v1alpha2.AcceptedPlan.Assignee\x12#\n\x08metadata\x18\x07 \x01(\x0b\x32\x11.goten.types.Meta\x1an\n\x08\x41ssignee\x12\x1a\n\x10project_assignee\x18\x01 \x01(\tH\x00\x12\x1f\n\x15organization_assignee\x18\x02 \x01(\tH\x00\x12\x19\n\x0fsystem_assignee\x18\x03 \x01(\x08H\x00\x42\n\n\x08\x61ssignee:~\xea\x41{\n\x1elimits.edgelq.com/AcceptedPlan\x12\x1d\x61\x63\x63\x65ptedPlans/{accepted_plan}\x12:organizations/{organization}/acceptedPlans/{accepted_plan}B\x87\x01\n\x1a\x63om.ntt.limits.pb.v1alpha2B\x11\x41\x63\x63\x65ptedPlanProtoP\x01ZTgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/accepted_plan;accepted_planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.accepted_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\021AcceptedPlanProtoP\001ZTgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/accepted_plan;accepted_plan'
  _globals['_ACCEPTEDPLAN']._loaded_options = None
  _globals['_ACCEPTEDPLAN']._serialized_options = b'\352A{\n\036limits.edgelq.com/AcceptedPlan\022\035acceptedPlans/{accepted_plan}\022:organizations/{organization}/acceptedPlans/{accepted_plan}'
  _globals['_ACCEPTEDPLAN']._serialized_start=275
  _globals['_ACCEPTEDPLAN']._serialized_end=800
  _globals['_ACCEPTEDPLAN_ASSIGNEE']._serialized_start=562
  _globals['_ACCEPTEDPLAN_ASSIGNEE']._serialized_end=672
# @@protoc_insertion_point(module_scope)