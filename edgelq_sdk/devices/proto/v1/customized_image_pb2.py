# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/customized_image.proto
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
    'edgelq-sdk/devices/proto/v1/customized_image.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/devices/proto/v1/customized_image.proto\x12\x0entt.devices.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xf0\x05\n\x0f\x43ustomizedImage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x32\n\x04spec\x18\x03 \x01(\x0b\x32$.ntt.devices.v1.CustomizedImage.Spec\x12\x36\n\x06status\x18\x04 \x01(\x0b\x32&.ntt.devices.v1.CustomizedImage.Status\x1a\xa1\x02\n\x04Spec\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\t\x12\x1b\n\x13provisioning_policy\x18\x03 \x01(\t\x12\x1e\n\x16install_ai_accelerator\x18\x04 \x01(\x08\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x12\n\nencryption\x18\x06 \x01(\x08\x12\x1b\n\x13\x65ncryption_password\x18\x07 \x01(\t\x12\x14\n\x0c\x64isk_mapping\x18\x08 \x01(\t\x12\x15\n\rnetwork_agent\x18\t \x01(\t\x12\x0b\n\x03ntp\x18\n \x01(\t\x12\x12\n\nhttp_proxy\x18\x0b \x01(\t\x12\x13\n\x0bhttps_proxy\x18\x0c \x01(\t\x12\x10\n\x08no_proxy\x18\r \x01(\t\x1a\xa7\x01\n\x06Status\x12;\n\x05state\x18\x01 \x01(\x0e\x32,.ntt.devices.v1.CustomizedImage.Status.State\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0c\n\x04\x66ile\x18\x05 \x01(\t\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\t\n\x05READY\x10\x03:p\xea\x41m\n\"devices.edgelq.com/CustomizedImage\x12Gprojects/{project}/regions/{region}/customizedImages/{customized_image}B\x86\x01\n\x15\x63om.ntt.devices.pb.v1B\x14\x43ustomizedImageProtoP\x01ZUgithub.com/cloudwan/edgelq-sdk/devices/resources/v1/customized_image;customized_imageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.customized_image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\024CustomizedImageProtoP\001ZUgithub.com/cloudwan/edgelq-sdk/devices/resources/v1/customized_image;customized_image'
  _globals['_CUSTOMIZEDIMAGE']._loaded_options = None
  _globals['_CUSTOMIZEDIMAGE']._serialized_options = b'\352Am\n\"devices.edgelq.com/CustomizedImage\022Gprojects/{project}/regions/{region}/customizedImages/{customized_image}'
  _globals['_CUSTOMIZEDIMAGE']._serialized_start=126
  _globals['_CUSTOMIZEDIMAGE']._serialized_end=878
  _globals['_CUSTOMIZEDIMAGE_SPEC']._serialized_start=305
  _globals['_CUSTOMIZEDIMAGE_SPEC']._serialized_end=594
  _globals['_CUSTOMIZEDIMAGE_STATUS']._serialized_start=597
  _globals['_CUSTOMIZEDIMAGE_STATUS']._serialized_end=764
  _globals['_CUSTOMIZEDIMAGE_STATUS_STATE']._serialized_start=695
  _globals['_CUSTOMIZEDIMAGE_STATUS_STATE']._serialized_end=764
# @@protoc_insertion_point(module_scope)
