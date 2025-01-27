# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/secrets/proto/v1/crypto_key_service.proto
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
    'edgelq-sdk/secrets/proto/v1/crypto_key_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.secrets.proto.v1 import crypto_key_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__pb2
from edgelq_sdk.secrets.proto.v1 import crypto_key_change_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4edgelq-sdk/secrets/proto/v1/crypto_key_service.proto\x12\x0entt.secrets.v1\x1a,edgelq-sdk/secrets/proto/v1/crypto_key.proto\x1a\x33\x65\x64gelq-sdk/secrets/proto/v1/crypto_key_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"t\n\x13GetCryptoKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x81\x01\n\x19\x42\x61tchGetCryptoKeysRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"]\n\x1a\x42\x61tchGetCryptoKeysResponse\x12.\n\x0b\x63rypto_keys\x18\x01 \x03(\x0b\x32\x19.ntt.secrets.v1.CryptoKey\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xde\x01\n\x15ListCryptoKeysRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xaf\x01\n\x16ListCryptoKeysResponse\x12.\n\x0b\x63rypto_keys\x18\x01 \x03(\x0b\x32\x19.ntt.secrets.v1.CryptoKey\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"v\n\x15WatchCryptoKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"I\n\x16WatchCryptoKeyResponse\x12/\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1f.ntt.secrets.v1.CryptoKeyChange\"\xc9\x02\n\x16WatchCryptoKeysRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xde\x02\n\x17WatchCryptoKeysResponse\x12;\n\x12\x63rypto_key_changes\x18\x02 \x03(\x0b\x32\x1f.ntt.secrets.v1.CryptoKeyChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12R\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x37.ntt.secrets.v1.WatchCryptoKeysResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"&\n\x16\x44\x65leteCryptoKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xbe\x07\n\x10\x43ryptoKeyService\x12\x84\x01\n\x0cGetCryptoKey\x12#.ntt.secrets.v1.GetCryptoKeyRequest\x1a\x19.ntt.secrets.v1.CryptoKey\"4\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/regions/*/cryptoKeys/*}\x12\x8c\x01\n\x12\x42\x61tchGetCryptoKeys\x12).ntt.secrets.v1.BatchGetCryptoKeysRequest\x1a*.ntt.secrets.v1.BatchGetCryptoKeysResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/cryptoKeys:batchGet\x12\x95\x01\n\x0eListCryptoKeys\x12%.ntt.secrets.v1.ListCryptoKeysRequest\x1a&.ntt.secrets.v1.ListCryptoKeysResponse\"4\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/regions/*}/cryptoKeys\x12\x9d\x01\n\x0eWatchCryptoKey\x12%.ntt.secrets.v1.WatchCryptoKeyRequest\x1a&.ntt.secrets.v1.WatchCryptoKeyResponse\":\x82\xd3\xe4\x93\x02\x34\"2/v1/{name=projects/*/regions/*/cryptoKeys/*}:watch0\x01\x12\xa0\x01\n\x0fWatchCryptoKeys\x12&.ntt.secrets.v1.WatchCryptoKeysRequest\x1a\'.ntt.secrets.v1.WatchCryptoKeysResponse\":\x82\xd3\xe4\x93\x02\x34\"2/v1/{parent=projects/*/regions/*}/cryptoKeys:watch0\x01\x12\x87\x01\n\x0f\x44\x65leteCryptoKey\x12&.ntt.secrets.v1.DeleteCryptoKeyRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/regions/*/cryptoKeys/*}\x1a/\xca\x41\x12secrets.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x7f\n\x15\x63om.ntt.secrets.pb.v1B\x15\x43ryptoKeyServiceProtoP\x00ZMgithub.com/cloudwan/edgelq-sdk/secrets/client/v1/crypto_key;crypto_key_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.secrets.proto.v1.crypto_key_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.secrets.pb.v1B\025CryptoKeyServiceProtoP\000ZMgithub.com/cloudwan/edgelq-sdk/secrets/client/v1/crypto_key;crypto_key_client'
  _globals['_CRYPTOKEYSERVICE']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE']._serialized_options = b'\312A\022secrets.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['GetCryptoKey']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['GetCryptoKey']._serialized_options = b'\202\323\344\223\002.\022,/v1/{name=projects/*/regions/*/cryptoKeys/*}'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['BatchGetCryptoKeys']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['BatchGetCryptoKeys']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/cryptoKeys:batchGet'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['ListCryptoKeys']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['ListCryptoKeys']._serialized_options = b'\202\323\344\223\002.\022,/v1/{parent=projects/*/regions/*}/cryptoKeys'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['WatchCryptoKey']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['WatchCryptoKey']._serialized_options = b'\202\323\344\223\0024\"2/v1/{name=projects/*/regions/*/cryptoKeys/*}:watch'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['WatchCryptoKeys']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['WatchCryptoKeys']._serialized_options = b'\202\323\344\223\0024\"2/v1/{parent=projects/*/regions/*}/cryptoKeys:watch'
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['DeleteCryptoKey']._loaded_options = None
  _globals['_CRYPTOKEYSERVICE'].methods_by_name['DeleteCryptoKey']._serialized_options = b'\202\323\344\223\002.*,/v1/{name=projects/*/regions/*/cryptoKeys/*}'
  _globals['_GETCRYPTOKEYREQUEST']._serialized_start=384
  _globals['_GETCRYPTOKEYREQUEST']._serialized_end=500
  _globals['_BATCHGETCRYPTOKEYSREQUEST']._serialized_start=503
  _globals['_BATCHGETCRYPTOKEYSREQUEST']._serialized_end=632
  _globals['_BATCHGETCRYPTOKEYSRESPONSE']._serialized_start=634
  _globals['_BATCHGETCRYPTOKEYSRESPONSE']._serialized_end=727
  _globals['_LISTCRYPTOKEYSREQUEST']._serialized_start=730
  _globals['_LISTCRYPTOKEYSREQUEST']._serialized_end=952
  _globals['_LISTCRYPTOKEYSRESPONSE']._serialized_start=955
  _globals['_LISTCRYPTOKEYSRESPONSE']._serialized_end=1130
  _globals['_WATCHCRYPTOKEYREQUEST']._serialized_start=1132
  _globals['_WATCHCRYPTOKEYREQUEST']._serialized_end=1250
  _globals['_WATCHCRYPTOKEYRESPONSE']._serialized_start=1252
  _globals['_WATCHCRYPTOKEYRESPONSE']._serialized_end=1325
  _globals['_WATCHCRYPTOKEYSREQUEST']._serialized_start=1328
  _globals['_WATCHCRYPTOKEYSREQUEST']._serialized_end=1657
  _globals['_WATCHCRYPTOKEYSRESPONSE']._serialized_start=1660
  _globals['_WATCHCRYPTOKEYSRESPONSE']._serialized_end=2010
  _globals['_WATCHCRYPTOKEYSRESPONSE_PAGETOKENCHANGE']._serialized_start=1943
  _globals['_WATCHCRYPTOKEYSRESPONSE_PAGETOKENCHANGE']._serialized_end=2010
  _globals['_DELETECRYPTOKEYREQUEST']._serialized_start=2012
  _globals['_DELETECRYPTOKEYREQUEST']._serialized_end=2050
  _globals['_CRYPTOKEYSERVICE']._serialized_start=2053
  _globals['_CRYPTOKEYSERVICE']._serialized_end=3011
# @@protoc_insertion_point(module_scope)
