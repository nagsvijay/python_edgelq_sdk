# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/secrets/proto/v1/crypto_key.proto
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
    'edgelq-sdk/secrets/proto/v1/crypto_key.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,edgelq-sdk/secrets/proto/v1/crypto_key.proto\x12\x0entt.secrets.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xab\x01\n\tCryptoKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x0b\n\x03key\x18\x03 \x01(\t:^\xea\x41[\n\x1csecrets.edgelq.com/CryptoKey\x12;projects/{project}/regions/{region}/cryptoKeys/{crypto_key}Bt\n\x15\x63om.ntt.secrets.pb.v1B\x0e\x43ryptoKeyProtoP\x01ZIgithub.com/cloudwan/edgelq-sdk/secrets/resources/v1/crypto_key;crypto_keyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.secrets.proto.v1.crypto_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.secrets.pb.v1B\016CryptoKeyProtoP\001ZIgithub.com/cloudwan/edgelq-sdk/secrets/resources/v1/crypto_key;crypto_key'
  _globals['_CRYPTOKEY']._loaded_options = None
  _globals['_CRYPTOKEY']._serialized_options = b'\352A[\n\034secrets.edgelq.com/CryptoKey\022;projects/{project}/regions/{region}/cryptoKeys/{crypto_key}'
  _globals['_CRYPTOKEY']._serialized_start=120
  _globals['_CRYPTOKEY']._serialized_end=291
# @@protoc_insertion_point(module_scope)