# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/ztp/proto/v1/hardware.proto
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
    'edgelq-sdk/ztp/proto/v1/hardware.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&edgelq-sdk/ztp/proto/v1/hardware.proto\x12\nntt.ztp.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xf5\x02\n\x08Hardware\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x15\n\rserial_number\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12\"\n\x1a\x61ssociated_edgelq_instance\x18\x06 \x01(\t\x12\x1a\n\x12\x61ssociated_project\x18\x07 \x01(\t\x12+\n#associated_provisioning_policy_name\x18\x08 \x01(\t\x12\x1e\n\x16\x61ssociated_device_name\x18\t \x01(\t\x12\x11\n\tsim_iccid\x18\n \x01(\t\x12\x0c\n\x04imei\x18\x0b \x01(\t:E\xea\x41\x42\n\x17ztp.edgelq.com/Hardware\x12\'projects/{project}/hardwares/{hardware}Bg\n\x11\x63om.ntt.ztp.pb.v1B\rHardwareProtoP\x01ZAgithub.com/cloudwan/edgelq-sdk/ztp/resources/v1/hardware;hardwareb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.ztp.proto.v1.hardware_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.ztp.pb.v1B\rHardwareProtoP\001ZAgithub.com/cloudwan/edgelq-sdk/ztp/resources/v1/hardware;hardware'
  _globals['_HARDWARE']._loaded_options = None
  _globals['_HARDWARE']._serialized_options = b'\352AB\n\027ztp.edgelq.com/Hardware\022\'projects/{project}/hardwares/{hardware}'
  _globals['_HARDWARE']._serialized_start=110
  _globals['_HARDWARE']._serialized_end=483
# @@protoc_insertion_point(module_scope)
