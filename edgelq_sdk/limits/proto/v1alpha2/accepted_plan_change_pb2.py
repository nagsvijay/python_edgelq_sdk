# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/limits/proto/v1alpha2/accepted_plan_change.proto
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
    'edgelq-sdk/limits/proto/v1alpha2/accepted_plan_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.limits.proto.v1alpha2 import accepted_plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_accepted__plan__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;edgelq-sdk/limits/proto/v1alpha2/accepted_plan_change.proto\x12\x13ntt.limits.v1alpha2\x1a\x34\x65\x64gelq-sdk/limits/proto/v1alpha2/accepted_plan.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xb0\x05\n\x12\x41\x63\x63\x65ptedPlanChange\x12>\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32-.ntt.limits.v1alpha2.AcceptedPlanChange.AddedH\x00\x12\x44\n\x08modified\x18\x02 \x01(\x0b\x32\x30.ntt.limits.v1alpha2.AcceptedPlanChange.ModifiedH\x00\x12\x42\n\x07\x63urrent\x18\x04 \x01(\x0b\x32/.ntt.limits.v1alpha2.AcceptedPlanChange.CurrentH\x00\x12\x42\n\x07removed\x18\x03 \x01(\x0b\x32/.ntt.limits.v1alpha2.AcceptedPlanChange.RemovedH\x00\x1aU\n\x05\x41\x64\x64\x65\x64\x12\x38\n\raccepted_plan\x18\x01 \x01(\x0b\x32!.ntt.limits.v1alpha2.AcceptedPlan\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xb3\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\raccepted_plan\x18\x02 \x01(\x0b\x32!.ntt.limits.v1alpha2.AcceptedPlan\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a\x43\n\x07\x43urrent\x12\x38\n\raccepted_plan\x18\x01 \x01(\x0b\x32!.ntt.limits.v1alpha2.AcceptedPlan\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x8d\x01\n\x1a\x63om.ntt.limits.pb.v1alpha2B\x17\x41\x63\x63\x65ptedPlanChangeProtoP\x00ZTgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/accepted_plan;accepted_planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.limits.proto.v1alpha2.accepted_plan_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.limits.pb.v1alpha2B\027AcceptedPlanChangeProtoP\000ZTgithub.com/cloudwan/edgelq-sdk/limits/resources/v1alpha2/accepted_plan;accepted_plan'
  _globals['_ACCEPTEDPLANCHANGE']._serialized_start=200
  _globals['_ACCEPTEDPLANCHANGE']._serialized_end=888
  _globals['_ACCEPTEDPLANCHANGE_ADDED']._serialized_start=492
  _globals['_ACCEPTEDPLANCHANGE_ADDED']._serialized_end=577
  _globals['_ACCEPTEDPLANCHANGE_MODIFIED']._serialized_start=580
  _globals['_ACCEPTEDPLANCHANGE_MODIFIED']._serialized_end=759
  _globals['_ACCEPTEDPLANCHANGE_CURRENT']._serialized_start=761
  _globals['_ACCEPTEDPLANCHANGE_CURRENT']._serialized_end=828
  _globals['_ACCEPTEDPLANCHANGE_REMOVED']._serialized_start=830
  _globals['_ACCEPTEDPLANCHANGE_REMOVED']._serialized_end=873
# @@protoc_insertion_point(module_scope)