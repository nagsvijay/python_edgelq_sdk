# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/provisioning_policy_custom.proto
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
    'edgelq-sdk/devices/proto/v1/provisioning_policy_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.common.api import credentials_pb2 as edgelq__sdk_dot_common_dot_api_dot_credentials__pb2
from edgelq_sdk.devices.proto.v1 import device_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2
from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__approval__request__pb2
from edgelq_sdk.devices.proto.v1 import provisioning_policy_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__policy__pb2
from edgelq_sdk.devices.proto.v1 import provisioning_policy_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__policy__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<edgelq-sdk/devices/proto/v1/provisioning_policy_custom.proto\x12\x0entt.devices.v1\x1a\'edgelq-sdk/common/api/credentials.proto\x1a(edgelq-sdk/devices/proto/v1/device.proto\x1a?edgelq-sdk/devices/proto/v1/provisioning_approval_request.proto\x1a\x35\x65\x64gelq-sdk/devices/proto/v1/provisioning_policy.proto\x1a<edgelq-sdk/devices/proto/v1/provisioning_policy_change.proto\"B\n2ProvisionServiceAccountToProvisioningPolicyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"g\n3ProvisionServiceAccountToProvisioningPolicyResponse\x12\x30\n\x0fservice_account\x18\x01 \x01(\x0b\x32\x17.ntt.api.ServiceAccount\"A\n1RemoveServiceAccountFromProvisioningPolicyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"E\n2RemoveServiceAccountFromProvisioningPolicyResponse\x12\x0f\n\x07removed\x18\x01 \x01(\x08\"~\n\x1fProvisionDeviceViaPolicyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\rdevice_status\x18\x02 \x01(\x0b\x32\x1d.ntt.devices.v1.Device.Status\x12\x17\n\x0f\x65xternal_pubkey\x18\x03 \x01(\t\"|\n ProvisionDeviceViaPolicyResponse\x12&\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x16.ntt.devices.v1.Device\x12\x30\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x17.ntt.api.ServiceAccount\"\x81\x01\n\"RequestProvisioningApprovalRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\rdevice_status\x18\x02 \x01(\x0b\x32\x1d.ntt.devices.v1.Device.Status\x12\x17\n\x0f\x65xternal_pubkey\x18\x03 \x01(\t\"\x95\x01\n#RequestProvisioningApprovalResponse\x12<\n\x07request\x18\x01 \x01(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\x12\x30\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x17.ntt.api.ServiceAccountB\x99\x01\n\x15\x63om.ntt.devices.pb.v1B\x1dProvisioningPolicyCustomProtoP\x00Z_github.com/cloudwan/edgelq-sdk/devices/client/v1/provisioning_policy;provisioning_policy_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.provisioning_policy_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\035ProvisioningPolicyCustomProtoP\000Z_github.com/cloudwan/edgelq-sdk/devices/client/v1/provisioning_policy;provisioning_policy_client'
  _globals['_PROVISIONSERVICEACCOUNTTOPROVISIONINGPOLICYREQUEST']._serialized_start=345
  _globals['_PROVISIONSERVICEACCOUNTTOPROVISIONINGPOLICYREQUEST']._serialized_end=411
  _globals['_PROVISIONSERVICEACCOUNTTOPROVISIONINGPOLICYRESPONSE']._serialized_start=413
  _globals['_PROVISIONSERVICEACCOUNTTOPROVISIONINGPOLICYRESPONSE']._serialized_end=516
  _globals['_REMOVESERVICEACCOUNTFROMPROVISIONINGPOLICYREQUEST']._serialized_start=518
  _globals['_REMOVESERVICEACCOUNTFROMPROVISIONINGPOLICYREQUEST']._serialized_end=583
  _globals['_REMOVESERVICEACCOUNTFROMPROVISIONINGPOLICYRESPONSE']._serialized_start=585
  _globals['_REMOVESERVICEACCOUNTFROMPROVISIONINGPOLICYRESPONSE']._serialized_end=654
  _globals['_PROVISIONDEVICEVIAPOLICYREQUEST']._serialized_start=656
  _globals['_PROVISIONDEVICEVIAPOLICYREQUEST']._serialized_end=782
  _globals['_PROVISIONDEVICEVIAPOLICYRESPONSE']._serialized_start=784
  _globals['_PROVISIONDEVICEVIAPOLICYRESPONSE']._serialized_end=908
  _globals['_REQUESTPROVISIONINGAPPROVALREQUEST']._serialized_start=911
  _globals['_REQUESTPROVISIONINGAPPROVALREQUEST']._serialized_end=1040
  _globals['_REQUESTPROVISIONINGAPPROVALRESPONSE']._serialized_start=1043
  _globals['_REQUESTPROVISIONINGAPPROVALRESPONSE']._serialized_end=1192
# @@protoc_insertion_point(module_scope)
