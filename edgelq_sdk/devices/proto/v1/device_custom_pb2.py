# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/device_custom.proto
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
    'edgelq-sdk/devices/proto/v1/device_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.common.api import credentials_pb2 as edgelq__sdk_dot_common_dot_api_dot_credentials__pb2
from edgelq_sdk.devices.proto.v1 import device_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2
from edgelq_sdk.devices.proto.v1 import device_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__change__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/edgelq-sdk/devices/proto/v1/device_custom.proto\x12\x0entt.devices.v1\x1a\'edgelq-sdk/common/api/credentials.proto\x1a(edgelq-sdk/devices/proto/v1/device.proto\x1a/edgelq-sdk/devices/proto/v1/device_change.proto\x1a\x1egoogle/protobuf/duration.proto\"O\n&ProvisionServiceAccountToDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x65xternal_pubkey\x18\x02 \x01(\t\"[\n\'ProvisionServiceAccountToDeviceResponse\x12\x30\n\x0fservice_account\x18\x01 \x01(\x0b\x32\x17.ntt.api.ServiceAccount\"5\n%RemoveServiceAccountFromDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n&RemoveServiceAccountFromDeviceResponse\"\xb4\x01\n\x0cHeartbeatMsg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x08register\x18\x02 \x01(\x0b\x32%.ntt.devices.v1.HeartbeatMsg.RegisterH\x00\x12;\n\theartbeat\x18\x03 \x01(\x0b\x32&.ntt.devices.v1.HeartbeatMsg.HeartbeatH\x00\x1a\n\n\x08Register\x1a\x0b\n\tHeartbeatB\x05\n\x03msg\"R\n\x11HeartbeatResponse\x12=\n\x1a\x64\x65sired_heartbeat_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationBs\n\x15\x63om.ntt.devices.pb.v1B\x11\x44\x65viceCustomProtoP\x00ZEgithub.com/cloudwan/edgelq-sdk/devices/client/v1/device;device_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.device_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\021DeviceCustomProtoP\000ZEgithub.com/cloudwan/edgelq-sdk/devices/client/v1/device;device_client'
  _globals['_PROVISIONSERVICEACCOUNTTODEVICEREQUEST']._serialized_start=231
  _globals['_PROVISIONSERVICEACCOUNTTODEVICEREQUEST']._serialized_end=310
  _globals['_PROVISIONSERVICEACCOUNTTODEVICERESPONSE']._serialized_start=312
  _globals['_PROVISIONSERVICEACCOUNTTODEVICERESPONSE']._serialized_end=403
  _globals['_REMOVESERVICEACCOUNTFROMDEVICEREQUEST']._serialized_start=405
  _globals['_REMOVESERVICEACCOUNTFROMDEVICEREQUEST']._serialized_end=458
  _globals['_REMOVESERVICEACCOUNTFROMDEVICERESPONSE']._serialized_start=460
  _globals['_REMOVESERVICEACCOUNTFROMDEVICERESPONSE']._serialized_end=500
  _globals['_HEARTBEATMSG']._serialized_start=503
  _globals['_HEARTBEATMSG']._serialized_end=683
  _globals['_HEARTBEATMSG_REGISTER']._serialized_start=653
  _globals['_HEARTBEATMSG_REGISTER']._serialized_end=663
  _globals['_HEARTBEATMSG_HEARTBEAT']._serialized_start=665
  _globals['_HEARTBEATMSG_HEARTBEAT']._serialized_end=676
  _globals['_HEARTBEATRESPONSE']._serialized_start=685
  _globals['_HEARTBEATRESPONSE']._serialized_end=767
# @@protoc_insertion_point(module_scope)