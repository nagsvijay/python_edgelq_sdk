# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1alpha2/device_type_change.proto
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
    'edgelq-sdk/devices/proto/v1alpha2/device_type_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1alpha2 import device_type_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_device__type__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:edgelq-sdk/devices/proto/v1alpha2/device_type_change.proto\x12\x14ntt.devices.v1alpha2\x1a\x33\x65\x64gelq-sdk/devices/proto/v1alpha2/device_type.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xa1\x05\n\x10\x44\x65viceTypeChange\x12=\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32,.ntt.devices.v1alpha2.DeviceTypeChange.AddedH\x00\x12\x43\n\x08modified\x18\x02 \x01(\x0b\x32/.ntt.devices.v1alpha2.DeviceTypeChange.ModifiedH\x00\x12\x41\n\x07\x63urrent\x18\x04 \x01(\x0b\x32..ntt.devices.v1alpha2.DeviceTypeChange.CurrentH\x00\x12\x41\n\x07removed\x18\x03 \x01(\x0b\x32..ntt.devices.v1alpha2.DeviceTypeChange.RemovedH\x00\x1aR\n\x05\x41\x64\x64\x65\x64\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xb0\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a@\n\x07\x43urrent\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x89\x01\n\x1b\x63om.ntt.devices.pb.v1alpha2B\x15\x44\x65viceTypeChangeProtoP\x00ZQgithub.com/cloudwan/edgelq-sdk/devices/resources/v1alpha2/device_type;device_typeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1alpha2.device_type_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.devices.pb.v1alpha2B\025DeviceTypeChangeProtoP\000ZQgithub.com/cloudwan/edgelq-sdk/devices/resources/v1alpha2/device_type;device_type'
  _globals['_DEVICETYPECHANGE']._serialized_start=199
  _globals['_DEVICETYPECHANGE']._serialized_end=872
  _globals['_DEVICETYPECHANGE_ADDED']._serialized_start=485
  _globals['_DEVICETYPECHANGE_ADDED']._serialized_end=567
  _globals['_DEVICETYPECHANGE_MODIFIED']._serialized_start=570
  _globals['_DEVICETYPECHANGE_MODIFIED']._serialized_end=746
  _globals['_DEVICETYPECHANGE_CURRENT']._serialized_start=748
  _globals['_DEVICETYPECHANGE_CURRENT']._serialized_end=812
  _globals['_DEVICETYPECHANGE_REMOVED']._serialized_start=814
  _globals['_DEVICETYPECHANGE_REMOVED']._serialized_end=857
# @@protoc_insertion_point(module_scope)
