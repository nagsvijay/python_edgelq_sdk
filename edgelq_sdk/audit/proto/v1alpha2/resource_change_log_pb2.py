# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/audit/proto/v1alpha2/resource_change_log.proto
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
    'edgelq-sdk/audit/proto/v1alpha2/resource_change_log.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.audit.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1alpha2_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9edgelq-sdk/audit/proto/v1alpha2/resource_change_log.proto\x12\x12ntt.audit.v1alpha2\x1a,edgelq-sdk/audit/proto/v1alpha2/common.proto\x1a\x19google/api/resource.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf0\n\n\x11ResourceChangeLog\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x0e\x61uthentication\x18\x05 \x01(\x0b\x32\".ntt.audit.v1alpha2.Authentication\x12\x30\n\x07service\x18\x06 \x01(\x0b\x32\x1f.ntt.audit.v1alpha2.ServiceData\x12\x46\n\x08resource\x18\x07 \x01(\x0b\x32\x34.ntt.audit.v1alpha2.ResourceChangeLog.ResourceChange\x12J\n\x0btransaction\x18\x08 \x01(\x0b\x32\x35.ntt.audit.v1alpha2.ResourceChangeLog.TransactionInfo\x1a\xcb\x04\n\x0eResourceChange\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12K\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32;.ntt.audit.v1alpha2.ResourceChangeLog.ResourceChange.Action\x12\x32\n\x0eupdated_fields\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12&\n\x08previous\x18\x07 \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\x07\x63urrent\x18\x08 \x01(\x0b\x32\x14.google.protobuf.Any\x12P\n\x06labels\x18\t \x03(\x0b\x32@.ntt.audit.v1alpha2.ResourceChangeLog.ResourceChange.LabelsEntry\x12,\n\x03pre\x18\x04 \x01(\x0b\x32\x1f.ntt.audit.v1alpha2.ObjectState\x12-\n\x04post\x18\x05 \x01(\x0b\x32\x1f.ntt.audit.v1alpha2.ObjectState\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"o\n\x06\x41\x63tion\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x03\x12\x0f\n\x0bSPEC_UPDATE\x10\x04\x12\x10\n\x0cSTATE_UPDATE\x10\x05\x12\x0f\n\x0bMETA_UPDATE\x10\x06\x12\n\n\x06UPDATE\x10\x02\x1a\xd1\x01\n\x0fTransactionInfo\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x13\n\x0btry_counter\x18\x02 \x01(\x05\x12J\n\x05state\x18\x03 \x01(\x0e\x32;.ntt.audit.v1alpha2.ResourceChangeLog.TransactionInfo.State\"I\n\x05State\x12\r\n\tUNDEFINED\x10\x00\x12\x11\n\rPRE_COMMITTED\x10\x01\x12\r\n\tCOMMITTED\x10\x02\x12\x0f\n\x0bROLLED_BACK\x10\x03:\xd6\x01\xea\x41\xd2\x01\n\"audit.edgelq.com/ResourceChangeLog\x12(resourceChangeLogs/{resource_change_log}\x12;projects/{project}/resourceChangeLogs/{resource_change_log}\x12\x45organizations/{organization}/resourceChangeLogs/{resource_change_log}B\x96\x01\n\x19\x63om.ntt.audit.pb.v1alpha2B\x16ResourceChangeLogProtoP\x01Z_github.com/cloudwan/edgelq-sdk/audit/resources/v1alpha2/resource_change_log;resource_change_logb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.audit.proto.v1alpha2.resource_change_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.ntt.audit.pb.v1alpha2B\026ResourceChangeLogProtoP\001Z_github.com/cloudwan/edgelq-sdk/audit/resources/v1alpha2/resource_change_log;resource_change_log'
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_LABELSENTRY']._loaded_options = None
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCECHANGELOG']._loaded_options = None
  _globals['_RESOURCECHANGELOG']._serialized_options = b'\352A\322\001\n\"audit.edgelq.com/ResourceChangeLog\022(resourceChangeLogs/{resource_change_log}\022;projects/{project}/resourceChangeLogs/{resource_change_log}\022Eorganizations/{organization}/resourceChangeLogs/{resource_change_log}'
  _globals['_RESOURCECHANGELOG']._serialized_start=249
  _globals['_RESOURCECHANGELOG']._serialized_end=1641
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE']._serialized_start=625
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE']._serialized_end=1212
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_LABELSENTRY']._serialized_start=1054
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_LABELSENTRY']._serialized_end=1099
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_ACTION']._serialized_start=1101
  _globals['_RESOURCECHANGELOG_RESOURCECHANGE_ACTION']._serialized_end=1212
  _globals['_RESOURCECHANGELOG_TRANSACTIONINFO']._serialized_start=1215
  _globals['_RESOURCECHANGELOG_TRANSACTIONINFO']._serialized_end=1424
  _globals['_RESOURCECHANGELOG_TRANSACTIONINFO_STATE']._serialized_start=1351
  _globals['_RESOURCECHANGELOG_TRANSACTIONINFO_STATE']._serialized_end=1424
# @@protoc_insertion_point(module_scope)
