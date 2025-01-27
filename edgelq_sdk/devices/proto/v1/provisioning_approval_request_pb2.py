# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/provisioning_approval_request.proto
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
    'edgelq-sdk/devices/proto/v1/provisioning_approval_request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/devices/proto/v1/provisioning_approval_request.proto\x12\x0entt.devices.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xdd\x04\n\x1bProvisioningApprovalRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x05 \x01(\x0b\x32\x11.goten.types.Meta\x12>\n\x04spec\x18\x03 \x01(\x0b\x32\x30.ntt.devices.v1.ProvisioningApprovalRequest.Spec\x12\x42\n\x06status\x18\x04 \x01(\x0b\x32\x32.ntt.devices.v1.ProvisioningApprovalRequest.Status\x1a\xb7\x01\n\x04Spec\x12O\n\nconclusion\x18\x01 \x01(\x0e\x32;.ntt.devices.v1.ProvisioningApprovalRequest.Spec.Conclusion\x12\x17\n\x0fservice_account\x18\x02 \x01(\t\"E\n\nConclusion\x12\x1c\n\x18\x43ONCLUSION_NOT_SPECIFIED\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\x0b\n\x07REVOKED\x10\x02\x1a\x08\n\x06Status:\xc2\x01\xea\x41\xbe\x01\n.devices.edgelq.com/ProvisioningApprovalRequest\x12\x8b\x01projects/{project}/regions/{region}/provisioningPolicies/{provisioning_policy}/provisioningApprovalRequests/{provisioning_approval_request}B\xac\x01\n\x15\x63om.ntt.devices.pb.v1B ProvisioningApprovalRequestProtoP\x01Zogithub.com/cloudwan/edgelq-sdk/devices/resources/v1/provisioning_approval_request;provisioning_approval_requestb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.provisioning_approval_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B ProvisioningApprovalRequestProtoP\001Zogithub.com/cloudwan/edgelq-sdk/devices/resources/v1/provisioning_approval_request;provisioning_approval_request'
  _globals['_PROVISIONINGAPPROVALREQUEST']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUEST']._serialized_options = b'\352A\276\001\n.devices.edgelq.com/ProvisioningApprovalRequest\022\213\001projects/{project}/regions/{region}/provisioningPolicies/{provisioning_policy}/provisioningApprovalRequests/{provisioning_approval_request}'
  _globals['_PROVISIONINGAPPROVALREQUEST']._serialized_start=139
  _globals['_PROVISIONINGAPPROVALREQUEST']._serialized_end=744
  _globals['_PROVISIONINGAPPROVALREQUEST_SPEC']._serialized_start=354
  _globals['_PROVISIONINGAPPROVALREQUEST_SPEC']._serialized_end=537
  _globals['_PROVISIONINGAPPROVALREQUEST_SPEC_CONCLUSION']._serialized_start=468
  _globals['_PROVISIONINGAPPROVALREQUEST_SPEC_CONCLUSION']._serialized_end=537
  _globals['_PROVISIONINGAPPROVALREQUEST_STATUS']._serialized_start=539
  _globals['_PROVISIONINGAPPROVALREQUEST_STATUS']._serialized_end=547
# @@protoc_insertion_point(module_scope)
