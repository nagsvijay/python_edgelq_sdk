# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/device_type.proto
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
    'edgelq-sdk/devices/proto/v1/device_type.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-edgelq-sdk/devices/proto/v1/device_type.proto\x12\x0entt.devices.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xa7\x03\n\nDeviceType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x35\n\x08hardware\x18\x04 \x01(\x0e\x32#.ntt.devices.v1.DeviceType.Hardware\x12=\n\x0c\x61rchitecture\x18\x05 \x01(\x0e\x32\'.ntt.devices.v1.DeviceType.Architecture\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"B\n\x08Hardware\x12\x18\n\x14HARDWARE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\x0f\n\x0bRASPBERRYPI\x10\x02\"B\n\x0c\x41rchitecture\x12\x1c\n\x18\x41RCHITECTURE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41MD64\x10\x01\x12\t\n\x05\x41RM64\x10\x02:=\xea\x41:\n\x1d\x64\x65vices.edgelq.com/DeviceType\x12\x19\x64\x65viceTypes/{device_type}Bw\n\x15\x63om.ntt.devices.pb.v1B\x0f\x44\x65viceTypeProtoP\x01ZKgithub.com/cloudwan/edgelq-sdk/devices/resources/v1/device_type;device_typeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.device_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\017DeviceTypeProtoP\001ZKgithub.com/cloudwan/edgelq-sdk/devices/resources/v1/device_type;device_type'
  _globals['_DEVICETYPE']._loaded_options = None
  _globals['_DEVICETYPE']._serialized_options = b'\352A:\n\035devices.edgelq.com/DeviceType\022\031deviceTypes/{device_type}'
  _globals['_DEVICETYPE']._serialized_start=121
  _globals['_DEVICETYPE']._serialized_end=544
  _globals['_DEVICETYPE_HARDWARE']._serialized_start=347
  _globals['_DEVICETYPE_HARDWARE']._serialized_end=413
  _globals['_DEVICETYPE_ARCHITECTURE']._serialized_start=415
  _globals['_DEVICETYPE_ARCHITECTURE']._serialized_end=481
# @@protoc_insertion_point(module_scope)
