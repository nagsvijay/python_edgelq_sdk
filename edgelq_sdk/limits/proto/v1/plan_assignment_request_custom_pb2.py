# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1/plan_assignment_request_custom.proto
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
    'edgelq-sdk/limits/proto/v1/plan_assignment_request_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import organization_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_organization__pb2
from edgelq_sdk.limits.proto.v1 import accepted_plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_request_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__assignment__request__pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_request_change_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__assignment__request__change__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/limits/proto/v1/plan_assignment_request_custom.proto\x12\rntt.limits.v1\x1a*edgelq-sdk/iam/proto/v1/organization.proto\x1a.edgelq-sdk/limits/proto/v1/accepted_plan.proto\x1a\x38\x65\x64gelq-sdk/limits/proto/v1/plan_assignment_request.proto\x1a?edgelq-sdk/limits/proto/v1/plan_assignment_request_change.proto\x1a google/protobuf/field_mask.proto\x1a\x1agoten-sdk/types/view.proto\"=\n\x1b\x41\x63\x63\x65ptPlanAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x61pprover\x18\x02 \x01(\t\"R\n\x1c\x41\x63\x63\x65ptPlanAssignmentResponse\x12\x32\n\raccepted_plan\x18\x01 \x01(\x0b\x32\x1b.ntt.limits.v1.AcceptedPlan\"N\n\x1c\x44\x65\x63linePlanAssignmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x61pprover\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\"\x1f\n\x1d\x44\x65\x63linePlanAssignmentResponse\"\xd7\x01\n)ListApproverPlanAssignmentRequestsRequest\x12\x10\n\x08\x61pprover\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.ViewB\xa2\x01\n\x14\x63om.ntt.limits.pb.v1B PlanAssignmentRequestCustomProtoP\x00Zfgithub.com/cloudwan/edgelq-sdk/limits/client/v1/plan_assignment_request;plan_assignment_request_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1.plan_assignment_request_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.ntt.limits.pb.v1B PlanAssignmentRequestCustomProtoP\000Zfgithub.com/cloudwan/edgelq-sdk/limits/client/v1/plan_assignment_request;plan_assignment_request_client'
  _globals['_ACCEPTPLANASSIGNMENTREQUEST']._serialized_start=359
  _globals['_ACCEPTPLANASSIGNMENTREQUEST']._serialized_end=420
  _globals['_ACCEPTPLANASSIGNMENTRESPONSE']._serialized_start=422
  _globals['_ACCEPTPLANASSIGNMENTRESPONSE']._serialized_end=504
  _globals['_DECLINEPLANASSIGNMENTREQUEST']._serialized_start=506
  _globals['_DECLINEPLANASSIGNMENTREQUEST']._serialized_end=584
  _globals['_DECLINEPLANASSIGNMENTRESPONSE']._serialized_start=586
  _globals['_DECLINEPLANASSIGNMENTRESPONSE']._serialized_end=617
  _globals['_LISTAPPROVERPLANASSIGNMENTREQUESTSREQUEST']._serialized_start=620
  _globals['_LISTAPPROVERPLANASSIGNMENTREQUESTSREQUEST']._serialized_end=835
# @@protoc_insertion_point(module_scope)
