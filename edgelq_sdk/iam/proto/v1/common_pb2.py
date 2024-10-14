# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/common.proto
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
    'edgelq-sdk/iam/proto/v1/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as goten__sdk_dot_meta__service_dot_proto_dot_v1_dot_service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$edgelq-sdk/iam/proto/v1/common.proto\x12\nntt.iam.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-goten-sdk/meta-service/proto/v1/service.proto\"d\n\x03PCR\x12\r\n\x05index\x18\x01 \x01(\r\x12\x12\n\ndigest_hex\x18\x02 \x01(\t\x12)\n\ndigest_alg\x18\x03 \x01(\x0e\x32\x15.ntt.iam.v1.DigestAlg\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\"W\n\x13ServiceBusinessTier\x12\x0f\n\x07service\x18\x01 \x01(\t\x12/\n\rbusiness_tier\x18\x02 \x01(\x0e\x32\x18.ntt.iam.v1.BusinessTier\"k\n\rServiceErrors\x12/\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x1f.ntt.iam.v1.ServiceErrors.Error\x1a)\n\x05\x45rror\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t*6\n\nTpmVersion\x12\x10\n\x0cTPMVAGNOSTIC\x10\x00\x12\n\n\x06TPMV12\x10\x01\x12\n\n\x06TPMV20\x10\x02*!\n\tDigestAlg\x12\x08\n\x04SHA1\x10\x00\x12\n\n\x06SHA256\x10\x01*\xd0\x01\n\x0c\x42usinessTier\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05LARGE\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05SMALL\x10\x03\x12\n\n\x06XSMALL\x10\x04\x12\x08\n\x04SKU0\x10\x05\x12\x08\n\x04SKU1\x10\x06\x12\x08\n\x04SKU2\x10\x07\x12\x08\n\x04SKU3\x10\x08\x12\x08\n\x04SKU4\x10\t\x12\x08\n\x04SKU5\x10\n\x12\x08\n\x04SKU6\x10\x0b\x12\x08\n\x04SKU7\x10\x0c\x12\x08\n\x04SKU8\x10\r\x12\x08\n\x04SKU9\x10\x0e\x12\t\n\x05SKU10\x10\x0f\x12\t\n\x05SKU11\x10\x10\x12\t\n\x05SKU12\x10\x11\x42X\n\x11\x63om.ntt.iam.pb.v1P\x01ZAgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/common;iam_commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1P\001ZAgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/common;iam_common'
  _globals['_TPMVERSION']._serialized_start=522
  _globals['_TPMVERSION']._serialized_end=576
  _globals['_DIGESTALG']._serialized_start=578
  _globals['_DIGESTALG']._serialized_end=611
  _globals['_BUSINESSTIER']._serialized_start=614
  _globals['_BUSINESSTIER']._serialized_end=822
  _globals['_PCR']._serialized_start=222
  _globals['_PCR']._serialized_end=322
  _globals['_SERVICEBUSINESSTIER']._serialized_start=324
  _globals['_SERVICEBUSINESSTIER']._serialized_end=411
  _globals['_SERVICEERRORS']._serialized_start=413
  _globals['_SERVICEERRORS']._serialized_end=520
  _globals['_SERVICEERRORS_ERROR']._serialized_start=479
  _globals['_SERVICEERRORS_ERROR']._serialized_end=520
# @@protoc_insertion_point(module_scope)
