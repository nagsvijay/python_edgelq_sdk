# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/service_account_change.proto
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
    'edgelq-sdk/iam/proto/v1/service_account_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import service_account_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4edgelq-sdk/iam/proto/v1/service_account_change.proto\x12\nntt.iam.v1\x1a-edgelq-sdk/iam/proto/v1/service_account.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\x87\x05\n\x14ServiceAccountChange\x12\x37\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32&.ntt.iam.v1.ServiceAccountChange.AddedH\x00\x12=\n\x08modified\x18\x02 \x01(\x0b\x32).ntt.iam.v1.ServiceAccountChange.ModifiedH\x00\x12;\n\x07\x63urrent\x18\x04 \x01(\x0b\x32(.ntt.iam.v1.ServiceAccountChange.CurrentH\x00\x12;\n\x07removed\x18\x03 \x01(\x0b\x32(.ntt.iam.v1.ServiceAccountChange.RemovedH\x00\x1aP\n\x05\x41\x64\x64\x65\x64\x12\x33\n\x0fservice_account\x18\x01 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xae\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a>\n\x07\x43urrent\x12\x33\n\x0fservice_account\x18\x01 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x81\x01\n\x11\x63om.ntt.iam.pb.v1B\x19ServiceAccountChangeProtoP\x00ZOgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/service_account;service_accountb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.service_account_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\031ServiceAccountChangeProtoP\000ZOgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/service_account;service_account'
  _globals['_SERVICEACCOUNTCHANGE']._serialized_start=177
  _globals['_SERVICEACCOUNTCHANGE']._serialized_end=824
  _globals['_SERVICEACCOUNTCHANGE_ADDED']._serialized_start=443
  _globals['_SERVICEACCOUNTCHANGE_ADDED']._serialized_end=523
  _globals['_SERVICEACCOUNTCHANGE_MODIFIED']._serialized_start=526
  _globals['_SERVICEACCOUNTCHANGE_MODIFIED']._serialized_end=700
  _globals['_SERVICEACCOUNTCHANGE_CURRENT']._serialized_start=702
  _globals['_SERVICEACCOUNTCHANGE_CURRENT']._serialized_end=764
  _globals['_SERVICEACCOUNTCHANGE_REMOVED']._serialized_start=766
  _globals['_SERVICEACCOUNTCHANGE_REMOVED']._serialized_end=809
# @@protoc_insertion_point(module_scope)
