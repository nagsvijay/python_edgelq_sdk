# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/provisioning_approval_request_service.proto
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
    'edgelq-sdk/devices/proto/v1/provisioning_approval_request_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__approval__request__pb2
from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__approval__request__change__pb2
from edgelq_sdk.devices.proto.v1 import provisioning_approval_request_custom_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_provisioning__approval__request__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGedgelq-sdk/devices/proto/v1/provisioning_approval_request_service.proto\x12\x0entt.devices.v1\x1a?edgelq-sdk/devices/proto/v1/provisioning_approval_request.proto\x1a\x46\x65\x64gelq-sdk/devices/proto/v1/provisioning_approval_request_change.proto\x1a\x46\x65\x64gelq-sdk/devices/proto/v1/provisioning_approval_request_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"\x86\x01\n%GetProvisioningApprovalRequestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x93\x01\n+BatchGetProvisioningApprovalRequestsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"\x94\x01\n,BatchGetProvisioningApprovalRequestsResponse\x12S\n\x1eprovisioning_approval_requests\x18\x01 \x03(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xf0\x01\n\'ListProvisioningApprovalRequestsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xe6\x01\n(ListProvisioningApprovalRequestsResponse\x12S\n\x1eprovisioning_approval_requests\x18\x01 \x03(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"\x88\x01\n\'WatchProvisioningApprovalRequestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"m\n(WatchProvisioningApprovalRequestResponse\x12\x41\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x31.ntt.devices.v1.ProvisioningApprovalRequestChange\"\xdb\x02\n(WatchProvisioningApprovalRequestsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xa7\x03\n)WatchProvisioningApprovalRequestsResponse\x12`\n%provisioning_approval_request_changes\x18\x02 \x03(\x0b\x32\x31.ntt.devices.v1.ProvisioningApprovalRequestChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\x64\n\x11page_token_change\x18\x03 \x01(\x0b\x32I.ntt.devices.v1.WatchProvisioningApprovalRequestsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8e\x01\n(CreateProvisioningApprovalRequestRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12R\n\x1dprovisioning_approval_request\x18\x02 \x01(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\"\x90\x03\n(UpdateProvisioningApprovalRequestRequest\x12R\n\x1dprovisioning_approval_request\x18\x02 \x01(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12I\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32<.ntt.devices.v1.UpdateProvisioningApprovalRequestRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1a}\n\x03\x43\x41S\x12\x46\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32+.ntt.devices.v1.ProvisioningApprovalRequest\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"8\n(DeleteProvisioningApprovalRequestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xb3\x12\n\"ProvisioningApprovalRequestService\x12\xe3\x01\n\x1eGetProvisioningApprovalRequest\x12\x35.ntt.devices.v1.GetProvisioningApprovalRequestRequest\x1a+.ntt.devices.v1.ProvisioningApprovalRequest\"]\x82\xd3\xe4\x93\x02W\x12U/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}\x12\xd4\x01\n$BatchGetProvisioningApprovalRequests\x12;.ntt.devices.v1.BatchGetProvisioningApprovalRequestsRequest\x1a<.ntt.devices.v1.BatchGetProvisioningApprovalRequestsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/v1/provisioningApprovalRequests:batchGet\x12\xf4\x01\n ListProvisioningApprovalRequests\x12\x37.ntt.devices.v1.ListProvisioningApprovalRequestsRequest\x1a\x38.ntt.devices.v1.ListProvisioningApprovalRequestsResponse\"]\x82\xd3\xe4\x93\x02W\x12U/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests\x12\xfc\x01\n WatchProvisioningApprovalRequest\x12\x37.ntt.devices.v1.WatchProvisioningApprovalRequestRequest\x1a\x38.ntt.devices.v1.WatchProvisioningApprovalRequestResponse\"c\x82\xd3\xe4\x93\x02]\"[/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:watch0\x01\x12\xff\x01\n!WatchProvisioningApprovalRequests\x12\x38.ntt.devices.v1.WatchProvisioningApprovalRequestsRequest\x1a\x39.ntt.devices.v1.WatchProvisioningApprovalRequestsResponse\"c\x82\xd3\xe4\x93\x02]\"[/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests:watch0\x01\x12\x88\x02\n!CreateProvisioningApprovalRequest\x12\x38.ntt.devices.v1.CreateProvisioningApprovalRequestRequest\x1a+.ntt.devices.v1.ProvisioningApprovalRequest\"|\x82\xd3\xe4\x93\x02v\"U/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests:\x1dprovisioning_approval_request\x12\xa8\x02\n!UpdateProvisioningApprovalRequest\x12\x38.ntt.devices.v1.UpdateProvisioningApprovalRequestRequest\x1a+.ntt.devices.v1.ProvisioningApprovalRequest\"\x9b\x01\x82\xd3\xe4\x93\x02\x94\x01\x1as/v1/{provisioning_approval_request.name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:\x1dprovisioning_approval_request\x12\xd4\x01\n!DeleteProvisioningApprovalRequest\x12\x38.ntt.devices.v1.DeleteProvisioningApprovalRequestRequest\x1a\x16.google.protobuf.Empty\"]\x82\xd3\xe4\x93\x02W*U/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}\x12\x99\x02\n!ProvisionDeviceForApprovedRequest\x12\x38.ntt.devices.v1.ProvisionDeviceForApprovedRequestRequest\x1a\x39.ntt.devices.v1.ProvisionDeviceForApprovedRequestResponse\"\x7f\x82\xd3\xe4\x93\x02y\"w/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:provisionDeviceForApprovedRequest\x1a/\xca\x41\x12\x64\x65vices.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\xb7\x01\n\x15\x63om.ntt.devices.pb.v1B\'ProvisioningApprovalRequestServiceProtoP\x00Zsgithub.com/cloudwan/edgelq-sdk/devices/client/v1/provisioning_approval_request;provisioning_approval_request_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.provisioning_approval_request_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\'ProvisioningApprovalRequestServiceProtoP\000Zsgithub.com/cloudwan/edgelq-sdk/devices/client/v1/provisioning_approval_request;provisioning_approval_request_client'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE']._serialized_options = b'\312A\022devices.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['GetProvisioningApprovalRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['GetProvisioningApprovalRequest']._serialized_options = b'\202\323\344\223\002W\022U/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['BatchGetProvisioningApprovalRequests']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['BatchGetProvisioningApprovalRequests']._serialized_options = b'\202\323\344\223\002+\022)/v1/provisioningApprovalRequests:batchGet'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['ListProvisioningApprovalRequests']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['ListProvisioningApprovalRequests']._serialized_options = b'\202\323\344\223\002W\022U/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['WatchProvisioningApprovalRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['WatchProvisioningApprovalRequest']._serialized_options = b'\202\323\344\223\002]\"[/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:watch'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['WatchProvisioningApprovalRequests']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['WatchProvisioningApprovalRequests']._serialized_options = b'\202\323\344\223\002]\"[/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests:watch'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['CreateProvisioningApprovalRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['CreateProvisioningApprovalRequest']._serialized_options = b'\202\323\344\223\002v\"U/v1/{parent=projects/*/regions/*/provisioningPolicies/*}/provisioningApprovalRequests:\035provisioning_approval_request'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['UpdateProvisioningApprovalRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['UpdateProvisioningApprovalRequest']._serialized_options = b'\202\323\344\223\002\224\001\032s/v1/{provisioning_approval_request.name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:\035provisioning_approval_request'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['DeleteProvisioningApprovalRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['DeleteProvisioningApprovalRequest']._serialized_options = b'\202\323\344\223\002W*U/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}'
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['ProvisionDeviceForApprovedRequest']._loaded_options = None
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE'].methods_by_name['ProvisionDeviceForApprovedRequest']._serialized_options = b'\202\323\344\223\002y\"w/v1/{name=projects/*/regions/*/provisioningPolicies/*/provisioningApprovalRequests/*}:provisionDeviceForApprovedRequest'
  _globals['_GETPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_start=514
  _globals['_GETPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_end=648
  _globals['_BATCHGETPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_start=651
  _globals['_BATCHGETPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_end=798
  _globals['_BATCHGETPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_start=801
  _globals['_BATCHGETPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_end=949
  _globals['_LISTPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_start=952
  _globals['_LISTPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_end=1192
  _globals['_LISTPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_start=1195
  _globals['_LISTPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_end=1425
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_start=1428
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_end=1564
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTRESPONSE']._serialized_start=1566
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTRESPONSE']._serialized_end=1675
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_start=1678
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSREQUEST']._serialized_end=2025
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_start=2028
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSRESPONSE']._serialized_end=2451
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSRESPONSE_PAGETOKENCHANGE']._serialized_start=2384
  _globals['_WATCHPROVISIONINGAPPROVALREQUESTSRESPONSE_PAGETOKENCHANGE']._serialized_end=2451
  _globals['_CREATEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_start=2454
  _globals['_CREATEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_end=2596
  _globals['_UPDATEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_start=2599
  _globals['_UPDATEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_end=2999
  _globals['_UPDATEPROVISIONINGAPPROVALREQUESTREQUEST_CAS']._serialized_start=2874
  _globals['_UPDATEPROVISIONINGAPPROVALREQUESTREQUEST_CAS']._serialized_end=2999
  _globals['_DELETEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_start=3001
  _globals['_DELETEPROVISIONINGAPPROVALREQUESTREQUEST']._serialized_end=3057
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE']._serialized_start=3060
  _globals['_PROVISIONINGAPPROVALREQUESTSERVICE']._serialized_end=5415
# @@protoc_insertion_point(module_scope)