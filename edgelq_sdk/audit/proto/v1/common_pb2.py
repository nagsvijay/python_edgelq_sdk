# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/audit/proto/v1/common.proto
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
    'edgelq-sdk/audit/proto/v1/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&edgelq-sdk/audit/proto/v1/common.proto\x12\x0cntt.audit.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\";\n\x0e\x41uthentication\x12\x11\n\tprincipal\x18\x01 \x01(\t\x12\x16\n\x0eprincipal_type\x18\x02 \x01(\t\"H\n\rAuthorization\x12\x1b\n\x13granted_permissions\x18\x01 \x03(\t\x12\x1a\n\x12\x64\x65nied_permissions\x18\x02 \x03(\t\".\n\x0bServiceData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x02 \x01(\t\"\x97\x01\n\x0bObjectState\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x35\n\x06labels\x18\x02 \x03(\x0b\x32%.ntt.audit.v1.ObjectState.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"0\n\x0fLabelDescriptor\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08versions\x18\x02 \x03(\t\"3\n\x0bLabelKeySet\x12\x12\n\nlabel_keys\x18\x01 \x03(\t\x12\x10\n\x08versions\x18\x02 \x03(\t\"l\n\x0cTimeInterval\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB^\n\x13\x63om.ntt.audit.pb.v1B\x0b\x43ommonProtoP\x01Z8github.com/cloudwan/edgelq-sdk/audit/resources/v1/commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.audit.proto.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.ntt.audit.pb.v1B\013CommonProtoP\001Z8github.com/cloudwan/edgelq-sdk/audit/resources/v1/common'
  _globals['_OBJECTSTATE_LABELSENTRY']._loaded_options = None
  _globals['_OBJECTSTATE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_AUTHENTICATION']._serialized_start=116
  _globals['_AUTHENTICATION']._serialized_end=175
  _globals['_AUTHORIZATION']._serialized_start=177
  _globals['_AUTHORIZATION']._serialized_end=249
  _globals['_SERVICEDATA']._serialized_start=251
  _globals['_SERVICEDATA']._serialized_end=297
  _globals['_OBJECTSTATE']._serialized_start=300
  _globals['_OBJECTSTATE']._serialized_end=451
  _globals['_OBJECTSTATE_LABELSENTRY']._serialized_start=406
  _globals['_OBJECTSTATE_LABELSENTRY']._serialized_end=451
  _globals['_LABELDESCRIPTOR']._serialized_start=453
  _globals['_LABELDESCRIPTOR']._serialized_end=501
  _globals['_LABELKEYSET']._serialized_start=503
  _globals['_LABELKEYSET']._serialized_end=554
  _globals['_TIMEINTERVAL']._serialized_start=556
  _globals['_TIMEINTERVAL']._serialized_end=664
# @@protoc_insertion_point(module_scope)
