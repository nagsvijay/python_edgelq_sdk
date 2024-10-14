# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/ztp_provision_hardware_custom.proto
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
    'edgelq-sdk/devices/proto/v1/ztp_provision_hardware_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.common.api import attestation_pb2 as edgelq__sdk_dot_common_dot_api_dot_attestation__pb2
from edgelq_sdk.common.api import credentials_pb2 as edgelq__sdk_dot_common_dot_api_dot_credentials__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/devices/proto/v1/ztp_provision_hardware_custom.proto\x12\x0entt.devices.v1\x1a\'edgelq-sdk/common/api/attestation.proto\x1a\'edgelq-sdk/common/api/credentials.proto\"\xb9\x02\n\x18ProvisionHardwareRequest\x12Z\n\x13provisioning_target\x18\x01 \x01(\x0b\x32;.ntt.devices.v1.ProvisionHardwareRequest.ProvisioningTargetH\x00\x12+\n\x08identify\x18\x02 \x01(\x0b\x32\x17.ntt.api.DeviceIdentityH\x00\x12@\n\x12\x63hallenge_response\x18\x03 \x01(\x0b\x32\".ntt.api.IdentityChallengeResponseH\x00\x1aK\n\x12ProvisioningTarget\x12 \n\x18provisioning_policy_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\tB\x05\n\x03msg\"\xbe\x02\n\x19ProvisionHardwareResponse\x12\x38\n\x12identity_challenge\x18\x01 \x01(\x0b\x32\x1a.ntt.api.IdentityChallengeH\x00\x12_\n\x15provisioning_response\x18\x02 \x01(\x0b\x32>.ntt.devices.v1.ProvisionHardwareResponse.ProvisioningResponseH\x00\x1a\x7f\n\x14ProvisioningResponse\x12\x30\n\x0fservice_account\x18\x01 \x01(\x0b\x32\x17.ntt.api.ServiceAccount\x12 \n\x18provisioning_policy_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\tB\x05\n\x03msgB\xa1\x01\n\x15\x63om.ntt.devices.pb.v1B\x1fZtpProvisionHardwareCustomProtoP\x00Zegithub.com/cloudwan/edgelq-sdk/devices/client/v1/ztp_provision_hardware;ztp_provision_hardware_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.ztp_provision_hardware_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\037ZtpProvisionHardwareCustomProtoP\000Zegithub.com/cloudwan/edgelq-sdk/devices/client/v1/ztp_provision_hardware;ztp_provision_hardware_client'
  _globals['_PROVISIONHARDWAREREQUEST']._serialized_start=166
  _globals['_PROVISIONHARDWAREREQUEST']._serialized_end=479
  _globals['_PROVISIONHARDWAREREQUEST_PROVISIONINGTARGET']._serialized_start=397
  _globals['_PROVISIONHARDWAREREQUEST_PROVISIONINGTARGET']._serialized_end=472
  _globals['_PROVISIONHARDWARERESPONSE']._serialized_start=482
  _globals['_PROVISIONHARDWARERESPONSE']._serialized_end=800
  _globals['_PROVISIONHARDWARERESPONSE_PROVISIONINGRESPONSE']._serialized_start=666
  _globals['_PROVISIONHARDWARERESPONSE_PROVISIONINGRESPONSE']._serialized_end=793
# @@protoc_insertion_point(module_scope)
