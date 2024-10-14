# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/authorization_custom.proto
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
    'edgelq-sdk/iam/proto/v1/authorization_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import condition_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_condition__pb2
from edgelq_sdk.iam.proto.v1 import permission_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_permission__pb2
from edgelq_sdk.iam.proto.v1 import permission_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_permission__change__pb2
from edgelq_sdk.iam.proto.v1 import role_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_role__pb2
from edgelq_sdk.iam.proto.v1 import role_binding_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_role__binding__pb2
from edgelq_sdk.iam.proto.v1 import role_binding_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_role__binding__change__pb2
from edgelq_sdk.iam.proto.v1 import service_account_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2
from edgelq_sdk.iam.proto.v1 import service_account_key_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__key__pb2
from edgelq_sdk.iam.proto.v1 import user_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_user__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2edgelq-sdk/iam/proto/v1/authorization_custom.proto\x12\nntt.iam.v1\x1a\'edgelq-sdk/iam/proto/v1/condition.proto\x1a(edgelq-sdk/iam/proto/v1/permission.proto\x1a/edgelq-sdk/iam/proto/v1/permission_change.proto\x1a\"edgelq-sdk/iam/proto/v1/role.proto\x1a*edgelq-sdk/iam/proto/v1/role_binding.proto\x1a\x31\x65\x64gelq-sdk/iam/proto/v1/role_binding_change.proto\x1a-edgelq-sdk/iam/proto/v1/service_account.proto\x1a\x31\x65\x64gelq-sdk/iam/proto/v1/service_account_key.proto\x1a\"edgelq-sdk/iam/proto/v1/user.proto\x1a google/protobuf/field_mask.proto\x1a\x1agoten-sdk/types/view.proto\"e\n\x13GetPrincipalRequest\x12\x1a\n\x12requesting_service\x18\x01 \x01(\t\x12\x18\n\x10principal_key_id\x18\x02 \x01(\t\x12\x12\n\nauth_token\x18\x04 \x01(\tJ\x04\x08\x03\x10\x04\"\xbf\x01\n\x14GetPrincipalResponse\x12\x10\n\x08json_key\x18\x01 \x01(\t\x12\x1a\n\x12principal_key_type\x18\x02 \x01(\t\x12 \n\x04user\x18\x03 \x01(\x0b\x32\x10.ntt.iam.v1.UserH\x00\x12\x35\n\x0fservice_account\x18\x04 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccountH\x00\x12\x13\n\tanonymous\x18\x05 \x01(\x08H\x00\x42\x0b\n\tprincipal\"V\n\x1cWatchPrincipalUpdatesRequest\x12\x1a\n\x12requesting_service\x18\x01 \x01(\t\x12\x14\n\x0cresume_token\x18\x03 \x01(\tJ\x04\x08\x02\x10\x03\"\xf9\x03\n\x1dWatchPrincipalUpdatesResponse\x12V\n\x12\x63urrent_principals\x18\x01 \x03(\x0b\x32:.ntt.iam.v1.WatchPrincipalUpdatesResponse.CurrentPrincipal\x12V\n\x12removed_principals\x18\x02 \x03(\x0b\x32:.ntt.iam.v1.WatchPrincipalUpdatesResponse.RemovedPrincipal\x12\x12\n\nis_current\x18\x03 \x01(\x08\x12\x10\n\x08is_reset\x18\x04 \x01(\x08\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x1a\xbd\x01\n\x10\x43urrentPrincipal\x12\x18\n\x10principal_key_id\x18\x01 \x01(\t\x12\x10\n\x08json_key\x18\x02 \x01(\t\x12\x1a\n\x12principal_key_type\x18\x03 \x01(\t\x12 \n\x04user\x18\x04 \x01(\x0b\x32\x10.ntt.iam.v1.UserH\x00\x12\x35\n\x0fservice_account\x18\x05 \x01(\x0b\x32\x1a.ntt.iam.v1.ServiceAccountH\x00\x42\x08\n\x06update\x1a,\n\x10RemovedPrincipal\x12\x18\n\x10principal_key_id\x18\x01 \x01(\t\"s\n\x1a\x43heckMyRoleBindingsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12\x35\n\x11\x63ustom_field_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xdb\x01\n\x1b\x43heckMyRoleBindingsResponse\x12R\n\x11resolvable_grants\x18\x01 \x03(\x0b\x32\x37.ntt.iam.v1.CheckMyRoleBindingsResponse.ResolvableGrant\x1ah\n\x0fResolvableGrant\x12-\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x17.ntt.iam.v1.RoleBinding\x12&\n\x06grants\x18\x02 \x03(\x0b\x32\x16.ntt.iam.v1.Role.GrantB\x80\x01\n\x11\x63om.ntt.iam.pb.v1B\x18\x41uthorizationCustomProtoP\x00ZOgithub.com/cloudwan/edgelq-sdk/iam/client/v1/authorization;authorization_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.authorization_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\030AuthorizationCustomProtoP\000ZOgithub.com/cloudwan/edgelq-sdk/iam/client/v1/authorization;authorization_client'
  _globals['_GETPRINCIPALREQUEST']._serialized_start=525
  _globals['_GETPRINCIPALREQUEST']._serialized_end=626
  _globals['_GETPRINCIPALRESPONSE']._serialized_start=629
  _globals['_GETPRINCIPALRESPONSE']._serialized_end=820
  _globals['_WATCHPRINCIPALUPDATESREQUEST']._serialized_start=822
  _globals['_WATCHPRINCIPALUPDATESREQUEST']._serialized_end=908
  _globals['_WATCHPRINCIPALUPDATESRESPONSE']._serialized_start=911
  _globals['_WATCHPRINCIPALUPDATESRESPONSE']._serialized_end=1416
  _globals['_WATCHPRINCIPALUPDATESRESPONSE_CURRENTPRINCIPAL']._serialized_start=1181
  _globals['_WATCHPRINCIPALUPDATESRESPONSE_CURRENTPRINCIPAL']._serialized_end=1370
  _globals['_WATCHPRINCIPALUPDATESRESPONSE_REMOVEDPRINCIPAL']._serialized_start=1372
  _globals['_WATCHPRINCIPALUPDATESRESPONSE_REMOVEDPRINCIPAL']._serialized_end=1416
  _globals['_CHECKMYROLEBINDINGSREQUEST']._serialized_start=1418
  _globals['_CHECKMYROLEBINDINGSREQUEST']._serialized_end=1533
  _globals['_CHECKMYROLEBINDINGSRESPONSE']._serialized_start=1536
  _globals['_CHECKMYROLEBINDINGSRESPONSE']._serialized_end=1755
  _globals['_CHECKMYROLEBINDINGSRESPONSE_RESOLVABLEGRANT']._serialized_start=1651
  _globals['_CHECKMYROLEBINDINGSRESPONSE_RESOLVABLEGRANT']._serialized_end=1755
# @@protoc_insertion_point(module_scope)