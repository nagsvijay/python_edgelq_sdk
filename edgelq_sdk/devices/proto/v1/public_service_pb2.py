# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/public_service.proto
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
    'edgelq-sdk/devices/proto/v1/public_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1 import device_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2
from edgelq_sdk.devices.proto.v1 import device_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__change__pb2
from edgelq_sdk.devices.proto.v1 import public_custom_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_public__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0edgelq-sdk/devices/proto/v1/public_service.proto\x12\x0entt.devices.v1\x1a(edgelq-sdk/devices/proto/v1/device.proto\x1a/edgelq-sdk/devices/proto/v1/device_change.proto\x1a/edgelq-sdk/devices/proto/v1/public_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto2\xf0\x01\n\rPublicService\x12\xad\x01\n\x11ListPublicDevices\x12(.ntt.devices.v1.ListPublicDevicesRequest\x1a).ntt.devices.v1.ListPublicDevicesResponse\"C\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/regions/*}/devices:listPublicDevices\x1a/\xca\x41\x12\x64\x65vices.edgelq.com\xd2\x41\x17https://apis.edgelq.comBt\n\x15\x63om.ntt.devices.pb.v1B\x12PublicServiceProtoP\x00ZEgithub.com/cloudwan/edgelq-sdk/devices/client/v1/public;public_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.public_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\022PublicServiceProtoP\000ZEgithub.com/cloudwan/edgelq-sdk/devices/client/v1/public;public_client'
  _globals['_PUBLICSERVICE']._loaded_options = None
  _globals['_PUBLICSERVICE']._serialized_options = b'\312A\022devices.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PUBLICSERVICE'].methods_by_name['ListPublicDevices']._loaded_options = None
  _globals['_PUBLICSERVICE'].methods_by_name['ListPublicDevices']._serialized_options = b'\202\323\344\223\002=\022;/v1/{parent=projects/*/regions/*}/devices:listPublicDevices'
  _globals['_PUBLICSERVICE']._serialized_start=422
  _globals['_PUBLICSERVICE']._serialized_end=662
# @@protoc_insertion_point(module_scope)