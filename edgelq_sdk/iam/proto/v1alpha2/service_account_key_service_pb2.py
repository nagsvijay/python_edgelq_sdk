# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/service_account_key_service.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/service_account_key_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import service_account_key_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_service__account__key__pb2
from edgelq_sdk.iam.proto.v1alpha2 import service_account_key_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_service__account__key__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?edgelq-sdk/iam/proto/v1alpha2/service_account_key_service.proto\x12\x10ntt.iam.v1alpha2\x1a\x37\x65\x64gelq-sdk/iam/proto/v1alpha2/service_account_key.proto\x1a>edgelq-sdk/iam/proto/v1alpha2/service_account_key_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"|\n\x1bGetServiceAccountKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x89\x01\n!BatchGetServiceAccountKeysRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"x\n\"BatchGetServiceAccountKeysResponse\x12\x41\n\x14service_account_keys\x18\x01 \x03(\x0b\x32#.ntt.iam.v1alpha2.ServiceAccountKey\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe6\x01\n\x1dListServiceAccountKeysRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xca\x01\n\x1eListServiceAccountKeysResponse\x12\x41\n\x14service_account_keys\x18\x01 \x03(\x0b\x32#.ntt.iam.v1alpha2.ServiceAccountKey\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"~\n\x1dWatchServiceAccountKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"[\n\x1eWatchServiceAccountKeyResponse\x12\x39\n\x06\x63hange\x18\x01 \x01(\x0b\x32).ntt.iam.v1alpha2.ServiceAccountKeyChange\"\xd1\x02\n\x1eWatchServiceAccountKeysRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\x83\x03\n\x1fWatchServiceAccountKeysResponse\x12N\n\x1bservice_account_key_changes\x18\x02 \x03(\x0b\x32).ntt.iam.v1alpha2.ServiceAccountKeyChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\\\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x41.ntt.iam.v1alpha2.WatchServiceAccountKeysResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"r\n\x1e\x43reateServiceAccountKeyRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x13service_account_key\x18\x02 \x01(\x0b\x32#.ntt.iam.v1alpha2.ServiceAccountKey\"\xe4\x02\n\x1eUpdateServiceAccountKeyRequest\x12@\n\x13service_account_key\x18\x02 \x01(\x0b\x32#.ntt.iam.v1alpha2.ServiceAccountKey\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x41\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\x34.ntt.iam.v1alpha2.UpdateServiceAccountKeyRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1au\n\x03\x43\x41S\x12>\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32#.ntt.iam.v1alpha2.ServiceAccountKey\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\".\n\x1e\x44\x65leteServiceAccountKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xde\r\n\x18ServiceAccountKeyService\x12\xc0\x01\n\x14GetServiceAccountKey\x12-.ntt.iam.v1alpha2.GetServiceAccountKeyRequest\x1a#.ntt.iam.v1alpha2.ServiceAccountKey\"T\x82\xd3\xe4\x93\x02N\x12L/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}\x12\xb6\x01\n\x1a\x42\x61tchGetServiceAccountKeys\x12\x33.ntt.iam.v1alpha2.BatchGetServiceAccountKeysRequest\x1a\x34.ntt.iam.v1alpha2.BatchGetServiceAccountKeysResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1alpha2/serviceAccountKeys:batchGet\x12\xd1\x01\n\x16ListServiceAccountKeys\x12/.ntt.iam.v1alpha2.ListServiceAccountKeysRequest\x1a\x30.ntt.iam.v1alpha2.ListServiceAccountKeysResponse\"T\x82\xd3\xe4\x93\x02N\x12L/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys\x12\xd9\x01\n\x16WatchServiceAccountKey\x12/.ntt.iam.v1alpha2.WatchServiceAccountKeyRequest\x1a\x30.ntt.iam.v1alpha2.WatchServiceAccountKeyResponse\"Z\x82\xd3\xe4\x93\x02T\"R/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}:watch0\x01\x12\xdc\x01\n\x17WatchServiceAccountKeys\x12\x30.ntt.iam.v1alpha2.WatchServiceAccountKeysRequest\x1a\x31.ntt.iam.v1alpha2.WatchServiceAccountKeysResponse\"Z\x82\xd3\xe4\x93\x02T\"R/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys:watch0\x01\x12\xdb\x01\n\x17\x43reateServiceAccountKey\x12\x30.ntt.iam.v1alpha2.CreateServiceAccountKeyRequest\x1a#.ntt.iam.v1alpha2.ServiceAccountKey\"i\x82\xd3\xe4\x93\x02\x63\"L/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys:\x13service_account_key\x12\xef\x01\n\x17UpdateServiceAccountKey\x12\x30.ntt.iam.v1alpha2.UpdateServiceAccountKeyRequest\x1a#.ntt.iam.v1alpha2.ServiceAccountKey\"}\x82\xd3\xe4\x93\x02w\x1a`/v1alpha2/{service_account_key.name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}:\x13service_account_key\x12\xb9\x01\n\x17\x44\x65leteServiceAccountKey\x12\x30.ntt.iam.v1alpha2.DeleteServiceAccountKeyRequest\x1a\x16.google.protobuf.Empty\"T\x82\xd3\xe4\x93\x02N*L/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x9d\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x1dServiceAccountKeyServiceProtoP\x00Zagithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/service_account_key;service_account_key_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.service_account_key_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\035ServiceAccountKeyServiceProtoP\000Zagithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/service_account_key;service_account_key_client'
  _globals['_SERVICEACCOUNTKEYSERVICE']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['GetServiceAccountKey']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['GetServiceAccountKey']._serialized_options = b'\202\323\344\223\002N\022L/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['BatchGetServiceAccountKeys']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['BatchGetServiceAccountKeys']._serialized_options = b'\202\323\344\223\002\'\022%/v1alpha2/serviceAccountKeys:batchGet'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['ListServiceAccountKeys']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['ListServiceAccountKeys']._serialized_options = b'\202\323\344\223\002N\022L/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['WatchServiceAccountKey']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['WatchServiceAccountKey']._serialized_options = b'\202\323\344\223\002T\"R/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}:watch'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['WatchServiceAccountKeys']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['WatchServiceAccountKeys']._serialized_options = b'\202\323\344\223\002T\"R/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys:watch'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['CreateServiceAccountKey']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['CreateServiceAccountKey']._serialized_options = b'\202\323\344\223\002c\"L/v1alpha2/{parent=projects/*/regions/*/serviceAccounts/*}/serviceAccountKeys:\023service_account_key'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['UpdateServiceAccountKey']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['UpdateServiceAccountKey']._serialized_options = b'\202\323\344\223\002w\032`/v1alpha2/{service_account_key.name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}:\023service_account_key'
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['DeleteServiceAccountKey']._loaded_options = None
  _globals['_SERVICEACCOUNTKEYSERVICE'].methods_by_name['DeleteServiceAccountKey']._serialized_options = b'\202\323\344\223\002N*L/v1alpha2/{name=projects/*/regions/*/serviceAccounts/*/serviceAccountKeys/*}'
  _globals['_GETSERVICEACCOUNTKEYREQUEST']._serialized_start=419
  _globals['_GETSERVICEACCOUNTKEYREQUEST']._serialized_end=543
  _globals['_BATCHGETSERVICEACCOUNTKEYSREQUEST']._serialized_start=546
  _globals['_BATCHGETSERVICEACCOUNTKEYSREQUEST']._serialized_end=683
  _globals['_BATCHGETSERVICEACCOUNTKEYSRESPONSE']._serialized_start=685
  _globals['_BATCHGETSERVICEACCOUNTKEYSRESPONSE']._serialized_end=805
  _globals['_LISTSERVICEACCOUNTKEYSREQUEST']._serialized_start=808
  _globals['_LISTSERVICEACCOUNTKEYSREQUEST']._serialized_end=1038
  _globals['_LISTSERVICEACCOUNTKEYSRESPONSE']._serialized_start=1041
  _globals['_LISTSERVICEACCOUNTKEYSRESPONSE']._serialized_end=1243
  _globals['_WATCHSERVICEACCOUNTKEYREQUEST']._serialized_start=1245
  _globals['_WATCHSERVICEACCOUNTKEYREQUEST']._serialized_end=1371
  _globals['_WATCHSERVICEACCOUNTKEYRESPONSE']._serialized_start=1373
  _globals['_WATCHSERVICEACCOUNTKEYRESPONSE']._serialized_end=1464
  _globals['_WATCHSERVICEACCOUNTKEYSREQUEST']._serialized_start=1467
  _globals['_WATCHSERVICEACCOUNTKEYSREQUEST']._serialized_end=1804
  _globals['_WATCHSERVICEACCOUNTKEYSRESPONSE']._serialized_start=1807
  _globals['_WATCHSERVICEACCOUNTKEYSRESPONSE']._serialized_end=2194
  _globals['_WATCHSERVICEACCOUNTKEYSRESPONSE_PAGETOKENCHANGE']._serialized_start=2127
  _globals['_WATCHSERVICEACCOUNTKEYSRESPONSE_PAGETOKENCHANGE']._serialized_end=2194
  _globals['_CREATESERVICEACCOUNTKEYREQUEST']._serialized_start=2196
  _globals['_CREATESERVICEACCOUNTKEYREQUEST']._serialized_end=2310
  _globals['_UPDATESERVICEACCOUNTKEYREQUEST']._serialized_start=2313
  _globals['_UPDATESERVICEACCOUNTKEYREQUEST']._serialized_end=2669
  _globals['_UPDATESERVICEACCOUNTKEYREQUEST_CAS']._serialized_start=2552
  _globals['_UPDATESERVICEACCOUNTKEYREQUEST_CAS']._serialized_end=2669
  _globals['_DELETESERVICEACCOUNTKEYREQUEST']._serialized_start=2671
  _globals['_DELETESERVICEACCOUNTKEYREQUEST']._serialized_end=2717
  _globals['_SERVICEACCOUNTKEYSERVICE']._serialized_start=2720
  _globals['_SERVICEACCOUNTKEYSERVICE']._serialized_end=4478
# @@protoc_insertion_point(module_scope)
