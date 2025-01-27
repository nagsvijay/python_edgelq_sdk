# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/user.proto
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
    'edgelq-sdk/iam/proto/v1/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"edgelq-sdk/iam/proto/v1/user.proto\x12\nntt.iam.v1\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/meta.proto\"\x8a\x03\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x08 \x01(\x0b\x32\x11.goten.types.Meta\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x16\n\x0e\x65mail_verified\x18\x04 \x01(\x08\x12,\n\tauth_info\x18\x05 \x01(\x0b\x32\x19.ntt.iam.v1.User.AuthInfo\x12\x30\n\x08settings\x18\x07 \x03(\x0b\x32\x1e.ntt.iam.v1.User.SettingsEntry\x12\x32\n\x0erefreshed_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a/\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a(\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t:&\xea\x41#\n\x13iam.edgelq.com/User\x12\x0cusers/{user}B[\n\x11\x63om.ntt.iam.pb.v1B\tUserProtoP\x01Z9github.com/cloudwan/edgelq-sdk/iam/resources/v1/user;userb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\tUserProtoP\001Z9github.com/cloudwan/edgelq-sdk/iam/resources/v1/user;user'
  _globals['_USER_SETTINGSENTRY']._loaded_options = None
  _globals['_USER_SETTINGSENTRY']._serialized_options = b'8\001'
  _globals['_USER']._loaded_options = None
  _globals['_USER']._serialized_options = b'\352A#\n\023iam.edgelq.com/User\022\014users/{user}'
  _globals['_USER']._serialized_start=139
  _globals['_USER']._serialized_end=533
  _globals['_USER_SETTINGSENTRY']._serialized_start=404
  _globals['_USER_SETTINGSENTRY']._serialized_end=451
  _globals['_USER_AUTHINFO']._serialized_start=453
  _globals['_USER_AUTHINFO']._serialized_end=493
# @@protoc_insertion_point(module_scope)
