# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/service_account_service.proto
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
    'edgelq-sdk/iam/proto/v1/service_account_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import service_account_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2
from edgelq_sdk.iam.proto.v1 import service_account_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5edgelq-sdk/iam/proto/v1/service_account_service.proto\x12\nntt.iam.v1\x1a-edgelq-sdk/iam/proto/v1/service_account.proto\x1a\x34\x65\x64gelq-sdk/iam/proto/v1/service_account_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"y\n\x18GetServiceAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x86\x01\n\x1e\x42\x61tchGetServiceAccountsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"h\n\x1f\x42\x61tchGetServiceAccountsResponse\x12\x34\n\x10service_accounts\x18\x01 \x03(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xe3\x01\n\x1aListServiceAccountsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xba\x01\n\x1bListServiceAccountsResponse\x12\x34\n\x10service_accounts\x18\x01 \x03(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"{\n\x1aWatchServiceAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"O\n\x1bWatchServiceAccountResponse\x12\x30\n\x06\x63hange\x18\x01 \x01(\x0b\x32 .ntt.iam.v1.ServiceAccountChange\"\xce\x02\n\x1bWatchServiceAccountsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xea\x02\n\x1cWatchServiceAccountsResponse\x12\x41\n\x17service_account_changes\x18\x02 \x03(\x0b\x32 .ntt.iam.v1.ServiceAccountChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12S\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x38.ntt.iam.v1.WatchServiceAccountsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"b\n\x1b\x43reateServiceAccountRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x33\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\"\xc2\x02\n\x1bUpdateServiceAccountRequest\x12\x33\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x38\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32+.ntt.iam.v1.UpdateServiceAccountRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1al\n\x03\x43\x41S\x12\x35\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccount\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"+\n\x1b\x44\x65leteServiceAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xea\n\n\x15ServiceAccountService\x12\x90\x01\n\x11GetServiceAccount\x12$.ntt.iam.v1.GetServiceAccountRequest\x1a\x1a.ntt.iam.v1.ServiceAccount\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/{name=projects/*/regions/*/serviceAccounts/*}\x12\x98\x01\n\x17\x42\x61tchGetServiceAccounts\x12*.ntt.iam.v1.BatchGetServiceAccountsRequest\x1a+.ntt.iam.v1.BatchGetServiceAccountsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/serviceAccounts:batchGet\x12\xa1\x01\n\x13ListServiceAccounts\x12&.ntt.iam.v1.ListServiceAccountsRequest\x1a\'.ntt.iam.v1.ListServiceAccountsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/{parent=projects/*/regions/*}/serviceAccounts\x12\xa9\x01\n\x13WatchServiceAccount\x12&.ntt.iam.v1.WatchServiceAccountRequest\x1a\'.ntt.iam.v1.WatchServiceAccountResponse\"?\x82\xd3\xe4\x93\x02\x39\"7/v1/{name=projects/*/regions/*/serviceAccounts/*}:watch0\x01\x12\xac\x01\n\x14WatchServiceAccounts\x12\'.ntt.iam.v1.WatchServiceAccountsRequest\x1a(.ntt.iam.v1.WatchServiceAccountsResponse\"?\x82\xd3\xe4\x93\x02\x39\"7/v1/{parent=projects/*/regions/*}/serviceAccounts:watch0\x01\x12\xa7\x01\n\x14\x43reateServiceAccount\x12\'.ntt.iam.v1.CreateServiceAccountRequest\x1a\x1a.ntt.iam.v1.ServiceAccount\"J\x82\xd3\xe4\x93\x02\x44\"1/v1/{parent=projects/*/regions/*}/serviceAccounts:\x0fservice_account\x12\xb7\x01\n\x14UpdateServiceAccount\x12\'.ntt.iam.v1.UpdateServiceAccountRequest\x1a\x1a.ntt.iam.v1.ServiceAccount\"Z\x82\xd3\xe4\x93\x02T\x1a\x41/v1/{service_account.name=projects/*/regions/*/serviceAccounts/*}:\x0fservice_account\x12\x92\x01\n\x14\x44\x65leteServiceAccount\x12\'.ntt.iam.v1.DeleteServiceAccountRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v1/{name=projects/*/regions/*/serviceAccounts/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x86\x01\n\x11\x63om.ntt.iam.pb.v1B\x1aServiceAccountServiceProtoP\x00ZSgithub.com/cloudwan/edgelq-sdk/iam/client/v1/service_account;service_account_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.service_account_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\032ServiceAccountServiceProtoP\000ZSgithub.com/cloudwan/edgelq-sdk/iam/client/v1/service_account;service_account_client'
  _globals['_SERVICEACCOUNTSERVICE']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccount']._serialized_options = b'\202\323\344\223\0023\0221/v1/{name=projects/*/regions/*/serviceAccounts/*}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['BatchGetServiceAccounts']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['BatchGetServiceAccounts']._serialized_options = b'\202\323\344\223\002\036\022\034/v1/serviceAccounts:batchGet'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['ListServiceAccounts']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['ListServiceAccounts']._serialized_options = b'\202\323\344\223\0023\0221/v1/{parent=projects/*/regions/*}/serviceAccounts'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['WatchServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['WatchServiceAccount']._serialized_options = b'\202\323\344\223\0029\"7/v1/{name=projects/*/regions/*/serviceAccounts/*}:watch'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['WatchServiceAccounts']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['WatchServiceAccounts']._serialized_options = b'\202\323\344\223\0029\"7/v1/{parent=projects/*/regions/*}/serviceAccounts:watch'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._serialized_options = b'\202\323\344\223\002D\"1/v1/{parent=projects/*/regions/*}/serviceAccounts:\017service_account'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['UpdateServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['UpdateServiceAccount']._serialized_options = b'\202\323\344\223\002T\032A/v1/{service_account.name=projects/*/regions/*/serviceAccounts/*}:\017service_account'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._serialized_options = b'\202\323\344\223\0023*1/v1/{name=projects/*/regions/*/serviceAccounts/*}'
  _globals['_GETSERVICEACCOUNTREQUEST']._serialized_start=383
  _globals['_GETSERVICEACCOUNTREQUEST']._serialized_end=504
  _globals['_BATCHGETSERVICEACCOUNTSREQUEST']._serialized_start=507
  _globals['_BATCHGETSERVICEACCOUNTSREQUEST']._serialized_end=641
  _globals['_BATCHGETSERVICEACCOUNTSRESPONSE']._serialized_start=643
  _globals['_BATCHGETSERVICEACCOUNTSRESPONSE']._serialized_end=747
  _globals['_LISTSERVICEACCOUNTSREQUEST']._serialized_start=750
  _globals['_LISTSERVICEACCOUNTSREQUEST']._serialized_end=977
  _globals['_LISTSERVICEACCOUNTSRESPONSE']._serialized_start=980
  _globals['_LISTSERVICEACCOUNTSRESPONSE']._serialized_end=1166
  _globals['_WATCHSERVICEACCOUNTREQUEST']._serialized_start=1168
  _globals['_WATCHSERVICEACCOUNTREQUEST']._serialized_end=1291
  _globals['_WATCHSERVICEACCOUNTRESPONSE']._serialized_start=1293
  _globals['_WATCHSERVICEACCOUNTRESPONSE']._serialized_end=1372
  _globals['_WATCHSERVICEACCOUNTSREQUEST']._serialized_start=1375
  _globals['_WATCHSERVICEACCOUNTSREQUEST']._serialized_end=1709
  _globals['_WATCHSERVICEACCOUNTSRESPONSE']._serialized_start=1712
  _globals['_WATCHSERVICEACCOUNTSRESPONSE']._serialized_end=2074
  _globals['_WATCHSERVICEACCOUNTSRESPONSE_PAGETOKENCHANGE']._serialized_start=2007
  _globals['_WATCHSERVICEACCOUNTSRESPONSE_PAGETOKENCHANGE']._serialized_end=2074
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_start=2076
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_end=2174
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_start=2177
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_end=2499
  _globals['_UPDATESERVICEACCOUNTREQUEST_CAS']._serialized_start=2391
  _globals['_UPDATESERVICEACCOUNTREQUEST_CAS']._serialized_end=2499
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_start=2501
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_end=2544
  _globals['_SERVICEACCOUNTSERVICE']._serialized_start=2547
  _globals['_SERVICEACCOUNTSERVICE']._serialized_end=3933
# @@protoc_insertion_point(module_scope)