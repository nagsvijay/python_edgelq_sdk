# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/secrets/proto/v1alpha2/secret_service.proto
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
    'edgelq-sdk/secrets/proto/v1alpha2/secret_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.secrets.proto.v1alpha2 import secret_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1alpha2_dot_secret__pb2
from edgelq_sdk.secrets.proto.v1alpha2 import secret_change_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1alpha2_dot_secret__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/secrets/proto/v1alpha2/secret_service.proto\x12\x14ntt.secrets.v1alpha2\x1a.edgelq-sdk/secrets/proto/v1alpha2/secret.proto\x1a\x35\x65\x64gelq-sdk/secrets/proto/v1alpha2/secret_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"q\n\x10GetSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"~\n\x16\x42\x61tchGetSecretsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"Y\n\x17\x42\x61tchGetSecretsResponse\x12-\n\x07secrets\x18\x01 \x03(\x0b\x32\x1c.ntt.secrets.v1alpha2.Secret\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xdb\x01\n\x12ListSecretsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xab\x01\n\x13ListSecretsResponse\x12-\n\x07secrets\x18\x01 \x03(\x0b\x32\x1c.ntt.secrets.v1alpha2.Secret\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"s\n\x12WatchSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"I\n\x13WatchSecretResponse\x12\x32\n\x06\x63hange\x18\x01 \x01(\x0b\x32\".ntt.secrets.v1alpha2.SecretChange\"\xc6\x02\n\x13WatchSecretsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xdd\x02\n\x14WatchSecretsResponse\x12:\n\x0esecret_changes\x18\x02 \x03(\x0b\x32\".ntt.secrets.v1alpha2.SecretChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12U\n\x11page_token_change\x18\x03 \x01(\x0b\x32:.ntt.secrets.v1alpha2.WatchSecretsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"S\n\x13\x43reateSecretRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12,\n\x06secret\x18\x02 \x01(\x0b\x32\x1c.ntt.secrets.v1alpha2.Secret\"\xb7\x02\n\x13UpdateSecretRequest\x12,\n\x06secret\x18\x02 \x01(\x0b\x32\x1c.ntt.secrets.v1alpha2.Secret\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12:\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32-.ntt.secrets.v1alpha2.UpdateSecretRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1an\n\x03\x43\x41S\x12\x37\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1c.ntt.secrets.v1alpha2.Secret\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"#\n\x13\x44\x65leteSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xd3\t\n\rSecretService\x12\x80\x01\n\tGetSecret\x12&.ntt.secrets.v1alpha2.GetSecretRequest\x1a\x1c.ntt.secrets.v1alpha2.Secret\"-\x82\xd3\xe4\x93\x02\'\x12%/v1alpha2/{name=projects/*/secrets/*}\x12\x92\x01\n\x0f\x42\x61tchGetSecrets\x12,.ntt.secrets.v1alpha2.BatchGetSecretsRequest\x1a-.ntt.secrets.v1alpha2.BatchGetSecretsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha2/secrets:batchGet\x12\x91\x01\n\x0bListSecrets\x12(.ntt.secrets.v1alpha2.ListSecretsRequest\x1a).ntt.secrets.v1alpha2.ListSecretsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1alpha2/{parent=projects/*}/secrets\x12\x99\x01\n\x0bWatchSecret\x12(.ntt.secrets.v1alpha2.WatchSecretRequest\x1a).ntt.secrets.v1alpha2.WatchSecretResponse\"3\x82\xd3\xe4\x93\x02-\"+/v1alpha2/{name=projects/*/secrets/*}:watch0\x01\x12\x9c\x01\n\x0cWatchSecrets\x12).ntt.secrets.v1alpha2.WatchSecretsRequest\x1a*.ntt.secrets.v1alpha2.WatchSecretsResponse\"3\x82\xd3\xe4\x93\x02-\"+/v1alpha2/{parent=projects/*}/secrets:watch0\x01\x12\x8e\x01\n\x0c\x43reateSecret\x12).ntt.secrets.v1alpha2.CreateSecretRequest\x1a\x1c.ntt.secrets.v1alpha2.Secret\"5\x82\xd3\xe4\x93\x02/\"%/v1alpha2/{parent=projects/*}/secrets:\x06secret\x12\x95\x01\n\x0cUpdateSecret\x12).ntt.secrets.v1alpha2.UpdateSecretRequest\x1a\x1c.ntt.secrets.v1alpha2.Secret\"<\x82\xd3\xe4\x93\x02\x36\x1a,/v1alpha2/{secret.name=projects/*/secrets/*}:\x06secret\x12\x80\x01\n\x0c\x44\x65leteSecret\x12).ntt.secrets.v1alpha2.DeleteSecretRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'*%/v1alpha2/{name=projects/*/secrets/*}\x1a/\xca\x41\x12secrets.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x80\x01\n\x1b\x63om.ntt.secrets.pb.v1alpha2B\x12SecretServiceProtoP\x00ZKgithub.com/cloudwan/edgelq-sdk/secrets/client/v1alpha2/secret;secret_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.secrets.proto.v1alpha2.secret_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.secrets.pb.v1alpha2B\022SecretServiceProtoP\000ZKgithub.com/cloudwan/edgelq-sdk/secrets/client/v1alpha2/secret;secret_client'
  _globals['_SECRETSERVICE']._loaded_options = None
  _globals['_SECRETSERVICE']._serialized_options = b'\312A\022secrets.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_SECRETSERVICE'].methods_by_name['GetSecret']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['GetSecret']._serialized_options = b'\202\323\344\223\002\'\022%/v1alpha2/{name=projects/*/secrets/*}'
  _globals['_SECRETSERVICE'].methods_by_name['BatchGetSecrets']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['BatchGetSecrets']._serialized_options = b'\202\323\344\223\002\034\022\032/v1alpha2/secrets:batchGet'
  _globals['_SECRETSERVICE'].methods_by_name['ListSecrets']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['ListSecrets']._serialized_options = b'\202\323\344\223\002\'\022%/v1alpha2/{parent=projects/*}/secrets'
  _globals['_SECRETSERVICE'].methods_by_name['WatchSecret']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['WatchSecret']._serialized_options = b'\202\323\344\223\002-\"+/v1alpha2/{name=projects/*/secrets/*}:watch'
  _globals['_SECRETSERVICE'].methods_by_name['WatchSecrets']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['WatchSecrets']._serialized_options = b'\202\323\344\223\002-\"+/v1alpha2/{parent=projects/*}/secrets:watch'
  _globals['_SECRETSERVICE'].methods_by_name['CreateSecret']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['CreateSecret']._serialized_options = b'\202\323\344\223\002/\"%/v1alpha2/{parent=projects/*}/secrets:\006secret'
  _globals['_SECRETSERVICE'].methods_by_name['UpdateSecret']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['UpdateSecret']._serialized_options = b'\202\323\344\223\0026\032,/v1alpha2/{secret.name=projects/*/secrets/*}:\006secret'
  _globals['_SECRETSERVICE'].methods_by_name['DeleteSecret']._loaded_options = None
  _globals['_SECRETSERVICE'].methods_by_name['DeleteSecret']._serialized_options = b'\202\323\344\223\002\'*%/v1alpha2/{name=projects/*/secrets/*}'
  _globals['_GETSECRETREQUEST']._serialized_start=396
  _globals['_GETSECRETREQUEST']._serialized_end=509
  _globals['_BATCHGETSECRETSREQUEST']._serialized_start=511
  _globals['_BATCHGETSECRETSREQUEST']._serialized_end=637
  _globals['_BATCHGETSECRETSRESPONSE']._serialized_start=639
  _globals['_BATCHGETSECRETSRESPONSE']._serialized_end=728
  _globals['_LISTSECRETSREQUEST']._serialized_start=731
  _globals['_LISTSECRETSREQUEST']._serialized_end=950
  _globals['_LISTSECRETSRESPONSE']._serialized_start=953
  _globals['_LISTSECRETSRESPONSE']._serialized_end=1124
  _globals['_WATCHSECRETREQUEST']._serialized_start=1126
  _globals['_WATCHSECRETREQUEST']._serialized_end=1241
  _globals['_WATCHSECRETRESPONSE']._serialized_start=1243
  _globals['_WATCHSECRETRESPONSE']._serialized_end=1316
  _globals['_WATCHSECRETSREQUEST']._serialized_start=1319
  _globals['_WATCHSECRETSREQUEST']._serialized_end=1645
  _globals['_WATCHSECRETSRESPONSE']._serialized_start=1648
  _globals['_WATCHSECRETSRESPONSE']._serialized_end=1997
  _globals['_WATCHSECRETSRESPONSE_PAGETOKENCHANGE']._serialized_start=1930
  _globals['_WATCHSECRETSRESPONSE_PAGETOKENCHANGE']._serialized_end=1997
  _globals['_CREATESECRETREQUEST']._serialized_start=1999
  _globals['_CREATESECRETREQUEST']._serialized_end=2082
  _globals['_UPDATESECRETREQUEST']._serialized_start=2085
  _globals['_UPDATESECRETREQUEST']._serialized_end=2396
  _globals['_UPDATESECRETREQUEST_CAS']._serialized_start=2286
  _globals['_UPDATESECRETREQUEST_CAS']._serialized_end=2396
  _globals['_DELETESECRETREQUEST']._serialized_start=2398
  _globals['_DELETESECRETREQUEST']._serialized_end=2433
  _globals['_SECRETSERVICE']._serialized_start=2436
  _globals['_SECRETSERVICE']._serialized_end=3671
# @@protoc_insertion_point(module_scope)