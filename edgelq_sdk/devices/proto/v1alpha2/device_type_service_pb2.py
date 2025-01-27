# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1alpha2/device_type_service.proto
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
    'edgelq-sdk/devices/proto/v1alpha2/device_type_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1alpha2 import device_type_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_device__type__pb2
from edgelq_sdk.devices.proto.v1alpha2 import device_type_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_device__type__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;edgelq-sdk/devices/proto/v1alpha2/device_type_service.proto\x12\x14ntt.devices.v1alpha2\x1a\x33\x65\x64gelq-sdk/devices/proto/v1alpha2/device_type.proto\x1a:edgelq-sdk/devices/proto/v1alpha2/device_type_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"u\n\x14GetDeviceTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x82\x01\n\x1a\x42\x61tchGetDeviceTypesRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"f\n\x1b\x42\x61tchGetDeviceTypesResponse\x12\x36\n\x0c\x64\x65vice_types\x18\x01 \x03(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xcf\x01\n\x16ListDeviceTypesRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xb8\x01\n\x17ListDeviceTypesResponse\x12\x36\n\x0c\x64\x65vice_types\x18\x01 \x03(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"w\n\x16WatchDeviceTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"Q\n\x17WatchDeviceTypeResponse\x12\x36\n\x06\x63hange\x18\x01 \x01(\x0b\x32&.ntt.devices.v1alpha2.DeviceTypeChange\"\xba\x02\n\x17WatchDeviceTypesRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xee\x02\n\x18WatchDeviceTypesResponse\x12\x43\n\x13\x64\x65vice_type_changes\x18\x02 \x03(\x0b\x32&.ntt.devices.v1alpha2.DeviceTypeChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12Y\n\x11page_token_change\x18\x03 \x01(\x0b\x32>.ntt.devices.v1alpha2.WatchDeviceTypesResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"P\n\x17\x43reateDeviceTypeRequest\x12\x35\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\"\xcc\x02\n\x17UpdateDeviceTypeRequest\x12\x35\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12>\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32\x31.ntt.devices.v1alpha2.UpdateDeviceTypeRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1ar\n\x03\x43\x41S\x12;\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32 .ntt.devices.v1alpha2.DeviceType\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\'\n\x17\x44\x65leteDeviceTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xfa\t\n\x11\x44\x65viceTypeService\x12\x85\x01\n\rGetDeviceType\x12*.ntt.devices.v1alpha2.GetDeviceTypeRequest\x1a .ntt.devices.v1alpha2.DeviceType\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1alpha2/{name=deviceTypes/*}\x12\xa2\x01\n\x13\x42\x61tchGetDeviceTypes\x12\x30.ntt.devices.v1alpha2.BatchGetDeviceTypesRequest\x1a\x31.ntt.devices.v1alpha2.BatchGetDeviceTypesResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1alpha2/deviceTypes:batchGet\x12\x8d\x01\n\x0fListDeviceTypes\x12,.ntt.devices.v1alpha2.ListDeviceTypesRequest\x1a-.ntt.devices.v1alpha2.ListDeviceTypesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha2/deviceTypes\x12\x9e\x01\n\x0fWatchDeviceType\x12,.ntt.devices.v1alpha2.WatchDeviceTypeRequest\x1a-.ntt.devices.v1alpha2.WatchDeviceTypeResponse\",\x82\xd3\xe4\x93\x02&\"$/v1alpha2/{name=deviceTypes/*}:watch0\x01\x12\x98\x01\n\x10WatchDeviceTypes\x12-.ntt.devices.v1alpha2.WatchDeviceTypesRequest\x1a..ntt.devices.v1alpha2.WatchDeviceTypesResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/v1alpha2/deviceTypes:watch0\x01\x12\x8f\x01\n\x10\x43reateDeviceType\x12-.ntt.devices.v1alpha2.CreateDeviceTypeRequest\x1a .ntt.devices.v1alpha2.DeviceType\"*\x82\xd3\xe4\x93\x02$\"\x15/v1alpha2/deviceTypes:\x0b\x64\x65vice_type\x12\xa4\x01\n\x10UpdateDeviceType\x12-.ntt.devices.v1alpha2.UpdateDeviceTypeRequest\x1a .ntt.devices.v1alpha2.DeviceType\"?\x82\xd3\xe4\x93\x02\x39\x1a*/v1alpha2/{device_type.name=deviceTypes/*}:\x0b\x64\x65vice_type\x12\x81\x01\n\x10\x44\x65leteDeviceType\x12-.ntt.devices.v1alpha2.DeleteDeviceTypeRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02 *\x1e/v1alpha2/{name=deviceTypes/*}\x1a/\xca\x41\x12\x64\x65vices.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x8e\x01\n\x1b\x63om.ntt.devices.pb.v1alpha2B\x16\x44\x65viceTypeServiceProtoP\x00ZUgithub.com/cloudwan/edgelq-sdk/devices/client/v1alpha2/device_type;device_type_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1alpha2.device_type_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.devices.pb.v1alpha2B\026DeviceTypeServiceProtoP\000ZUgithub.com/cloudwan/edgelq-sdk/devices/client/v1alpha2/device_type;device_type_client'
  _globals['_DEVICETYPESERVICE']._loaded_options = None
  _globals['_DEVICETYPESERVICE']._serialized_options = b'\312A\022devices.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_DEVICETYPESERVICE'].methods_by_name['GetDeviceType']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['GetDeviceType']._serialized_options = b'\202\323\344\223\002 \022\036/v1alpha2/{name=deviceTypes/*}'
  _globals['_DEVICETYPESERVICE'].methods_by_name['BatchGetDeviceTypes']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['BatchGetDeviceTypes']._serialized_options = b'\202\323\344\223\002 \022\036/v1alpha2/deviceTypes:batchGet'
  _globals['_DEVICETYPESERVICE'].methods_by_name['ListDeviceTypes']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['ListDeviceTypes']._serialized_options = b'\202\323\344\223\002\027\022\025/v1alpha2/deviceTypes'
  _globals['_DEVICETYPESERVICE'].methods_by_name['WatchDeviceType']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['WatchDeviceType']._serialized_options = b'\202\323\344\223\002&\"$/v1alpha2/{name=deviceTypes/*}:watch'
  _globals['_DEVICETYPESERVICE'].methods_by_name['WatchDeviceTypes']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['WatchDeviceTypes']._serialized_options = b'\202\323\344\223\002\035\"\033/v1alpha2/deviceTypes:watch'
  _globals['_DEVICETYPESERVICE'].methods_by_name['CreateDeviceType']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['CreateDeviceType']._serialized_options = b'\202\323\344\223\002$\"\025/v1alpha2/deviceTypes:\013device_type'
  _globals['_DEVICETYPESERVICE'].methods_by_name['UpdateDeviceType']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['UpdateDeviceType']._serialized_options = b'\202\323\344\223\0029\032*/v1alpha2/{device_type.name=deviceTypes/*}:\013device_type'
  _globals['_DEVICETYPESERVICE'].methods_by_name['DeleteDeviceType']._loaded_options = None
  _globals['_DEVICETYPESERVICE'].methods_by_name['DeleteDeviceType']._serialized_options = b'\202\323\344\223\002 *\036/v1alpha2/{name=deviceTypes/*}'
  _globals['_GETDEVICETYPEREQUEST']._serialized_start=411
  _globals['_GETDEVICETYPEREQUEST']._serialized_end=528
  _globals['_BATCHGETDEVICETYPESREQUEST']._serialized_start=531
  _globals['_BATCHGETDEVICETYPESREQUEST']._serialized_end=661
  _globals['_BATCHGETDEVICETYPESRESPONSE']._serialized_start=663
  _globals['_BATCHGETDEVICETYPESRESPONSE']._serialized_end=765
  _globals['_LISTDEVICETYPESREQUEST']._serialized_start=768
  _globals['_LISTDEVICETYPESREQUEST']._serialized_end=975
  _globals['_LISTDEVICETYPESRESPONSE']._serialized_start=978
  _globals['_LISTDEVICETYPESRESPONSE']._serialized_end=1162
  _globals['_WATCHDEVICETYPEREQUEST']._serialized_start=1164
  _globals['_WATCHDEVICETYPEREQUEST']._serialized_end=1283
  _globals['_WATCHDEVICETYPERESPONSE']._serialized_start=1285
  _globals['_WATCHDEVICETYPERESPONSE']._serialized_end=1366
  _globals['_WATCHDEVICETYPESREQUEST']._serialized_start=1369
  _globals['_WATCHDEVICETYPESREQUEST']._serialized_end=1683
  _globals['_WATCHDEVICETYPESRESPONSE']._serialized_start=1686
  _globals['_WATCHDEVICETYPESRESPONSE']._serialized_end=2052
  _globals['_WATCHDEVICETYPESRESPONSE_PAGETOKENCHANGE']._serialized_start=1985
  _globals['_WATCHDEVICETYPESRESPONSE_PAGETOKENCHANGE']._serialized_end=2052
  _globals['_CREATEDEVICETYPEREQUEST']._serialized_start=2054
  _globals['_CREATEDEVICETYPEREQUEST']._serialized_end=2134
  _globals['_UPDATEDEVICETYPEREQUEST']._serialized_start=2137
  _globals['_UPDATEDEVICETYPEREQUEST']._serialized_end=2469
  _globals['_UPDATEDEVICETYPEREQUEST_CAS']._serialized_start=2355
  _globals['_UPDATEDEVICETYPEREQUEST_CAS']._serialized_end=2469
  _globals['_DELETEDEVICETYPEREQUEST']._serialized_start=2471
  _globals['_DELETEDEVICETYPEREQUEST']._serialized_end=2510
  _globals['_DEVICETYPESERVICE']._serialized_start=2513
  _globals['_DEVICETYPESERVICE']._serialized_end=3787
# @@protoc_insertion_point(module_scope)
