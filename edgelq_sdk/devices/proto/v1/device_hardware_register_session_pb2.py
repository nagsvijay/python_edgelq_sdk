# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/device_hardware_register_session.proto
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
    'edgelq-sdk/devices/proto/v1/device_hardware_register_session.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1 import device_hardware_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__hardware__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBedgelq-sdk/devices/proto/v1/device_hardware_register_session.proto\x12\x0entt.devices.v1\x1a\x31\x65\x64gelq-sdk/devices/proto/v1/device_hardware.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/meta.proto\"\xf3\x05\n\x1d\x44\x65viceHardwareRegisterSession\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x0e \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12.\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x65xpiration_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nuser_email\x18\x05 \x01(\t\x12\x1b\n\rinviter_email\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03\x12\x15\n\rlanguage_code\x18\x07 \x01(\t\x12I\n\x06\x65xtras\x18\x08 \x03(\x0b\x32\x39.ntt.devices.v1.DeviceHardwareRegisterSession.ExtrasEntry\x12 \n\x18provisioning_policy_name\x18\t \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\n \x01(\t\x12\x12\n\nsingle_use\x18\x0b \x01(\x08\x12\r\n\x05token\x18\x0c \x01(\t\x12\x44\n\x06status\x18\r \x01(\x0b\x32\x34.ntt.devices.v1.DeviceHardwareRegisterSession.Status\x1a-\n\x0b\x45xtrasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\"\n\x06Status\x12\x18\n\x10\x64\x65vice_hardwares\x18\x01 \x03(\t:\x9d\x01\xea\x41\x99\x01\n0devices.edgelq.com/DeviceHardwareRegisterSession\x12\x65projects/{project}/regions/{region}/deviceHardwareRegisterSessions/{device_hardware_register_session}B\xb4\x01\n\x15\x63om.ntt.devices.pb.v1B\"DeviceHardwareRegisterSessionProtoP\x01Zugithub.com/cloudwan/edgelq-sdk/devices/resources/v1/device_hardware_register_session;device_hardware_register_sessionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.device_hardware_register_session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\"DeviceHardwareRegisterSessionProtoP\001Zugithub.com/cloudwan/edgelq-sdk/devices/resources/v1/device_hardware_register_session;device_hardware_register_session'
  _globals['_DEVICEHARDWAREREGISTERSESSION_EXTRASENTRY']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSION_EXTRASENTRY']._serialized_options = b'8\001'
  _globals['_DEVICEHARDWAREREGISTERSESSION'].fields_by_name['inviter_email']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSION'].fields_by_name['inviter_email']._serialized_options = b'\342A\001\003'
  _globals['_DEVICEHARDWAREREGISTERSESSION']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSION']._serialized_options = b'\352A\231\001\n0devices.edgelq.com/DeviceHardwareRegisterSession\022eprojects/{project}/regions/{region}/deviceHardwareRegisterSessions/{device_hardware_register_session}'
  _globals['_DEVICEHARDWAREREGISTERSESSION']._serialized_start=259
  _globals['_DEVICEHARDWAREREGISTERSESSION']._serialized_end=1014
  _globals['_DEVICEHARDWAREREGISTERSESSION_EXTRASENTRY']._serialized_start=773
  _globals['_DEVICEHARDWAREREGISTERSESSION_EXTRASENTRY']._serialized_end=818
  _globals['_DEVICEHARDWAREREGISTERSESSION_STATUS']._serialized_start=820
  _globals['_DEVICEHARDWAREREGISTERSESSION_STATUS']._serialized_end=854
# @@protoc_insertion_point(module_scope)
