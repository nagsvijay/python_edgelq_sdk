# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/provisioning_policy_change.proto
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
    'edgelq-sdk/devices/proto/v1/provisioning_policy_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1 import provisioning_policy_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__policy__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<edgelq-sdk/devices/proto/v1/provisioning_policy_change.proto\x12\x0entt.devices.v1\x1a\x35\x65\x64gelq-sdk/devices/proto/v1/provisioning_policy.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xcf\x05\n\x18ProvisioningPolicyChange\x12?\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32..ntt.devices.v1.ProvisioningPolicyChange.AddedH\x00\x12\x45\n\x08modified\x18\x02 \x01(\x0b\x32\x31.ntt.devices.v1.ProvisioningPolicyChange.ModifiedH\x00\x12\x43\n\x07\x63urrent\x18\x04 \x01(\x0b\x32\x30.ntt.devices.v1.ProvisioningPolicyChange.CurrentH\x00\x12\x43\n\x07removed\x18\x03 \x01(\x0b\x32\x30.ntt.devices.v1.ProvisioningPolicyChange.RemovedH\x00\x1a\\\n\x05\x41\x64\x64\x65\x64\x12?\n\x13provisioning_policy\x18\x01 \x01(\x0b\x32\".ntt.devices.v1.ProvisioningPolicy\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xba\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x13provisioning_policy\x18\x02 \x01(\x0b\x32\".ntt.devices.v1.ProvisioningPolicy\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1aJ\n\x07\x43urrent\x12?\n\x13provisioning_policy\x18\x01 \x01(\x0b\x32\".ntt.devices.v1.ProvisioningPolicy\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x95\x01\n\x15\x63om.ntt.devices.pb.v1B\x1dProvisioningPolicyChangeProtoP\x00Z[github.com/cloudwan/edgelq-sdk/devices/resources/v1/provisioning_policy;provisioning_policyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.provisioning_policy_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\035ProvisioningPolicyChangeProtoP\000Z[github.com/cloudwan/edgelq-sdk/devices/resources/v1/provisioning_policy;provisioning_policy'
  _globals['_PROVISIONINGPOLICYCHANGE']._serialized_start=197
  _globals['_PROVISIONINGPOLICYCHANGE']._serialized_end=916
  _globals['_PROVISIONINGPOLICYCHANGE_ADDED']._serialized_start=499
  _globals['_PROVISIONINGPOLICYCHANGE_ADDED']._serialized_end=591
  _globals['_PROVISIONINGPOLICYCHANGE_MODIFIED']._serialized_start=594
  _globals['_PROVISIONINGPOLICYCHANGE_MODIFIED']._serialized_end=780
  _globals['_PROVISIONINGPOLICYCHANGE_CURRENT']._serialized_start=782
  _globals['_PROVISIONINGPOLICYCHANGE_CURRENT']._serialized_end=856
  _globals['_PROVISIONINGPOLICYCHANGE_REMOVED']._serialized_start=858
  _globals['_PROVISIONINGPOLICYCHANGE_REMOVED']._serialized_end=901
# @@protoc_insertion_point(module_scope)
