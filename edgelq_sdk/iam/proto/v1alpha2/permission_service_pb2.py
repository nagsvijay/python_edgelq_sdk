# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/permission_service.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/permission_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import permission_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_permission__pb2
from edgelq_sdk.iam.proto.v1alpha2 import permission_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_permission__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/iam/proto/v1alpha2/permission_service.proto\x12\x10ntt.iam.v1alpha2\x1a.edgelq-sdk/iam/proto/v1alpha2/permission.proto\x1a\x35\x65\x64gelq-sdk/iam/proto/v1alpha2/permission_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"u\n\x14GetPermissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x82\x01\n\x1a\x42\x61tchGetPermissionsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"a\n\x1b\x42\x61tchGetPermissionsResponse\x12\x31\n\x0bpermissions\x18\x01 \x03(\x0b\x32\x1c.ntt.iam.v1alpha2.Permission\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xcf\x01\n\x16ListPermissionsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xb3\x01\n\x17ListPermissionsResponse\x12\x31\n\x0bpermissions\x18\x01 \x03(\x0b\x32\x1c.ntt.iam.v1alpha2.Permission\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"w\n\x16WatchPermissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"M\n\x17WatchPermissionResponse\x12\x32\n\x06\x63hange\x18\x01 \x01(\x0b\x32\".ntt.iam.v1alpha2.PermissionChange\"\xba\x02\n\x17WatchPermissionsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xe5\x02\n\x18WatchPermissionsResponse\x12>\n\x12permission_changes\x18\x02 \x03(\x0b\x32\".ntt.iam.v1alpha2.PermissionChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12U\n\x11page_token_change\x18\x03 \x01(\x0b\x32:.ntt.iam.v1alpha2.WatchPermissionsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"K\n\x17\x43reatePermissionRequest\x12\x30\n\npermission\x18\x02 \x01(\x0b\x32\x1c.ntt.iam.v1alpha2.Permission\"\xbf\x02\n\x17UpdatePermissionRequest\x12\x30\n\npermission\x18\x02 \x01(\x0b\x32\x1c.ntt.iam.v1alpha2.Permission\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12:\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32-.ntt.iam.v1alpha2.UpdatePermissionRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1an\n\x03\x43\x41S\x12\x37\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1c.ntt.iam.v1alpha2.Permission\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\'\n\x17\x44\x65letePermissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xb5\t\n\x11PermissionService\x12}\n\rGetPermission\x12&.ntt.iam.v1alpha2.GetPermissionRequest\x1a\x1c.ntt.iam.v1alpha2.Permission\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1alpha2/{name=permissions/*}\x12\x9a\x01\n\x13\x42\x61tchGetPermissions\x12,.ntt.iam.v1alpha2.BatchGetPermissionsRequest\x1a-.ntt.iam.v1alpha2.BatchGetPermissionsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1alpha2/permissions:batchGet\x12\x85\x01\n\x0fListPermissions\x12(.ntt.iam.v1alpha2.ListPermissionsRequest\x1a).ntt.iam.v1alpha2.ListPermissionsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha2/permissions\x12\x96\x01\n\x0fWatchPermission\x12(.ntt.iam.v1alpha2.WatchPermissionRequest\x1a).ntt.iam.v1alpha2.WatchPermissionResponse\",\x82\xd3\xe4\x93\x02&\"$/v1alpha2/{name=permissions/*}:watch0\x01\x12\x90\x01\n\x10WatchPermissions\x12).ntt.iam.v1alpha2.WatchPermissionsRequest\x1a*.ntt.iam.v1alpha2.WatchPermissionsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/v1alpha2/permissions:watch0\x01\x12\x86\x01\n\x10\x43reatePermission\x12).ntt.iam.v1alpha2.CreatePermissionRequest\x1a\x1c.ntt.iam.v1alpha2.Permission\")\x82\xd3\xe4\x93\x02#\"\x15/v1alpha2/permissions:\npermission\x12\x9a\x01\n\x10UpdatePermission\x12).ntt.iam.v1alpha2.UpdatePermissionRequest\x1a\x1c.ntt.iam.v1alpha2.Permission\"=\x82\xd3\xe4\x93\x02\x37\x1a)/v1alpha2/{permission.name=permissions/*}:\npermission\x12}\n\x10\x44\x65letePermission\x12).ntt.iam.v1alpha2.DeletePermissionRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02 *\x1e/v1alpha2/{name=permissions/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x84\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x16PermissionServiceProtoP\x00ZOgithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/permission;permission_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.permission_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\026PermissionServiceProtoP\000ZOgithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/permission;permission_client'
  _globals['_PERMISSIONSERVICE']._loaded_options = None
  _globals['_PERMISSIONSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._serialized_options = b'\202\323\344\223\002 \022\036/v1alpha2/{name=permissions/*}'
  _globals['_PERMISSIONSERVICE'].methods_by_name['BatchGetPermissions']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['BatchGetPermissions']._serialized_options = b'\202\323\344\223\002 \022\036/v1alpha2/permissions:batchGet'
  _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._serialized_options = b'\202\323\344\223\002\027\022\025/v1alpha2/permissions'
  _globals['_PERMISSIONSERVICE'].methods_by_name['WatchPermission']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['WatchPermission']._serialized_options = b'\202\323\344\223\002&\"$/v1alpha2/{name=permissions/*}:watch'
  _globals['_PERMISSIONSERVICE'].methods_by_name['WatchPermissions']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['WatchPermissions']._serialized_options = b'\202\323\344\223\002\035\"\033/v1alpha2/permissions:watch'
  _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._serialized_options = b'\202\323\344\223\002#\"\025/v1alpha2/permissions:\npermission'
  _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._serialized_options = b'\202\323\344\223\0027\032)/v1alpha2/{permission.name=permissions/*}:\npermission'
  _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._loaded_options = None
  _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._serialized_options = b'\202\323\344\223\002 *\036/v1alpha2/{name=permissions/*}'
  _globals['_GETPERMISSIONREQUEST']._serialized_start=392
  _globals['_GETPERMISSIONREQUEST']._serialized_end=509
  _globals['_BATCHGETPERMISSIONSREQUEST']._serialized_start=512
  _globals['_BATCHGETPERMISSIONSREQUEST']._serialized_end=642
  _globals['_BATCHGETPERMISSIONSRESPONSE']._serialized_start=644
  _globals['_BATCHGETPERMISSIONSRESPONSE']._serialized_end=741
  _globals['_LISTPERMISSIONSREQUEST']._serialized_start=744
  _globals['_LISTPERMISSIONSREQUEST']._serialized_end=951
  _globals['_LISTPERMISSIONSRESPONSE']._serialized_start=954
  _globals['_LISTPERMISSIONSRESPONSE']._serialized_end=1133
  _globals['_WATCHPERMISSIONREQUEST']._serialized_start=1135
  _globals['_WATCHPERMISSIONREQUEST']._serialized_end=1254
  _globals['_WATCHPERMISSIONRESPONSE']._serialized_start=1256
  _globals['_WATCHPERMISSIONRESPONSE']._serialized_end=1333
  _globals['_WATCHPERMISSIONSREQUEST']._serialized_start=1336
  _globals['_WATCHPERMISSIONSREQUEST']._serialized_end=1650
  _globals['_WATCHPERMISSIONSRESPONSE']._serialized_start=1653
  _globals['_WATCHPERMISSIONSRESPONSE']._serialized_end=2010
  _globals['_WATCHPERMISSIONSRESPONSE_PAGETOKENCHANGE']._serialized_start=1943
  _globals['_WATCHPERMISSIONSRESPONSE_PAGETOKENCHANGE']._serialized_end=2010
  _globals['_CREATEPERMISSIONREQUEST']._serialized_start=2012
  _globals['_CREATEPERMISSIONREQUEST']._serialized_end=2087
  _globals['_UPDATEPERMISSIONREQUEST']._serialized_start=2090
  _globals['_UPDATEPERMISSIONREQUEST']._serialized_end=2409
  _globals['_UPDATEPERMISSIONREQUEST_CAS']._serialized_start=2299
  _globals['_UPDATEPERMISSIONREQUEST_CAS']._serialized_end=2409
  _globals['_DELETEPERMISSIONREQUEST']._serialized_start=2411
  _globals['_DELETEPERMISSIONREQUEST']._serialized_end=2450
  _globals['_PERMISSIONSERVICE']._serialized_start=2453
  _globals['_PERMISSIONSERVICE']._serialized_end=3658
# @@protoc_insertion_point(module_scope)
