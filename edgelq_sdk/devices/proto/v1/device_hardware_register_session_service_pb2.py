# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/device_hardware_register_session_service.proto
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
    'edgelq-sdk/devices/proto/v1/device_hardware_register_session_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.devices.proto.v1 import device_hardware_register_session_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__hardware__register__session__pb2
from edgelq_sdk.devices.proto.v1 import device_hardware_register_session_change_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__hardware__register__session__change__pb2
from edgelq_sdk.devices.proto.v1 import device_hardware_register_session_custom_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__hardware__register__session__custom__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJedgelq-sdk/devices/proto/v1/device_hardware_register_session_service.proto\x12\x0entt.devices.v1\x1a\x42\x65\x64gelq-sdk/devices/proto/v1/device_hardware_register_session.proto\x1aIedgelq-sdk/devices/proto/v1/device_hardware_register_session_change.proto\x1aIedgelq-sdk/devices/proto/v1/device_hardware_register_session_custom.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"\x88\x01\n\'GetDeviceHardwareRegisterSessionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x95\x01\n-BatchGetDeviceHardwareRegisterSessionsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"\x9b\x01\n.BatchGetDeviceHardwareRegisterSessionsResponse\x12X\n!device_hardware_register_sessions\x18\x01 \x03(\x0b\x32-.ntt.devices.v1.DeviceHardwareRegisterSession\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xf2\x01\n)ListDeviceHardwareRegisterSessionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xed\x01\n*ListDeviceHardwareRegisterSessionsResponse\x12X\n!device_hardware_register_sessions\x18\x01 \x03(\x0b\x32-.ntt.devices.v1.DeviceHardwareRegisterSession\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"\x8a\x01\n)WatchDeviceHardwareRegisterSessionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"q\n*WatchDeviceHardwareRegisterSessionResponse\x12\x43\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x33.ntt.devices.v1.DeviceHardwareRegisterSessionChange\"\xdd\x02\n*WatchDeviceHardwareRegisterSessionsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xb0\x03\n+WatchDeviceHardwareRegisterSessionsResponse\x12\x65\n(device_hardware_register_session_changes\x18\x02 \x03(\x0b\x32\x33.ntt.devices.v1.DeviceHardwareRegisterSessionChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\x66\n\x11page_token_change\x18\x03 \x01(\x0b\x32K.ntt.devices.v1.WatchDeviceHardwareRegisterSessionsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x95\x01\n*CreateDeviceHardwareRegisterSessionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12W\n device_hardware_register_session\x18\x02 \x01(\x0b\x32-.ntt.devices.v1.DeviceHardwareRegisterSession\"\x9b\x03\n*UpdateDeviceHardwareRegisterSessionRequest\x12W\n device_hardware_register_session\x18\x02 \x01(\x0b\x32-.ntt.devices.v1.DeviceHardwareRegisterSession\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12K\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32>.ntt.devices.v1.UpdateDeviceHardwareRegisterSessionRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1a\x7f\n\x03\x43\x41S\x12H\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32-.ntt.devices.v1.DeviceHardwareRegisterSession\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\":\n*DeleteDeviceHardwareRegisterSessionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x8a\x14\n$DeviceHardwareRegisterSessionService\x12\xd4\x01\n GetDeviceHardwareRegisterSession\x12\x37.ntt.devices.v1.GetDeviceHardwareRegisterSessionRequest\x1a-.ntt.devices.v1.DeviceHardwareRegisterSession\"H\x82\xd3\xe4\x93\x02\x42\x12@/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}\x12\xdc\x01\n&BatchGetDeviceHardwareRegisterSessions\x12=.ntt.devices.v1.BatchGetDeviceHardwareRegisterSessionsRequest\x1a>.ntt.devices.v1.BatchGetDeviceHardwareRegisterSessionsResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v1/deviceHardwareRegisterSessions:batchGet\x12\xe5\x01\n\"ListDeviceHardwareRegisterSessions\x12\x39.ntt.devices.v1.ListDeviceHardwareRegisterSessionsRequest\x1a:.ntt.devices.v1.ListDeviceHardwareRegisterSessionsResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions\x12\xed\x01\n\"WatchDeviceHardwareRegisterSession\x12\x39.ntt.devices.v1.WatchDeviceHardwareRegisterSessionRequest\x1a:.ntt.devices.v1.WatchDeviceHardwareRegisterSessionResponse\"N\x82\xd3\xe4\x93\x02H\"F/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}:watch0\x01\x12\xf0\x01\n#WatchDeviceHardwareRegisterSessions\x12:.ntt.devices.v1.WatchDeviceHardwareRegisterSessionsRequest\x1a;.ntt.devices.v1.WatchDeviceHardwareRegisterSessionsResponse\"N\x82\xd3\xe4\x93\x02H\"F/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions:watch0\x01\x12\xfc\x01\n#CreateDeviceHardwareRegisterSession\x12:.ntt.devices.v1.CreateDeviceHardwareRegisterSessionRequest\x1a-.ntt.devices.v1.DeviceHardwareRegisterSession\"j\x82\xd3\xe4\x93\x02\x64\"@/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions: device_hardware_register_session\x12\x9f\x02\n#UpdateDeviceHardwareRegisterSession\x12:.ntt.devices.v1.UpdateDeviceHardwareRegisterSessionRequest\x1a-.ntt.devices.v1.DeviceHardwareRegisterSession\"\x8c\x01\x82\xd3\xe4\x93\x02\x85\x01\x1a\x61/v1/{device_hardware_register_session.name=projects/*/regions/*/deviceHardwareRegisterSessions/*}: device_hardware_register_session\x12\xc3\x01\n#DeleteDeviceHardwareRegisterSession\x12:.ntt.devices.v1.DeleteDeviceHardwareRegisterSessionRequest\x1a\x16.google.protobuf.Empty\"H\x82\xd3\xe4\x93\x02\x42*@/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}\x12\x86\x02\n)GetDeviceHardwareRegisterSessionFromToken\x12@.ntt.devices.v1.GetDeviceHardwareRegisterSessionFromTokenRequest\x1a\x41.ntt.devices.v1.GetDeviceHardwareRegisterSessionFromTokenResponse\"T\x82\xd3\xe4\x93\x02N\x12L/v1/deviceHardwareRegisterSessions:getDeviceHardwareRegisterSessionFromToken\x12\xa2\x01\n\x10RegisterHardware\x12\'.ntt.devices.v1.RegisterHardwareRequest\x1a(.ntt.devices.v1.RegisterHardwareResponse\";\x82\xd3\xe4\x93\x02\x35\"3/v1/deviceHardwareRegisterSessions:registerHardware\x12\x9a\x01\n\x0eHardwareStatus\x12%.ntt.devices.v1.HardwareStatusRequest\x1a&.ntt.devices.v1.HardwareStatusResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/deviceHardwareRegisterSessions:hardwareStatus\x1a/\xca\x41\x12\x64\x65vices.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\xbf\x01\n\x15\x63om.ntt.devices.pb.v1B)DeviceHardwareRegisterSessionServiceProtoP\x00Zygithub.com/cloudwan/edgelq-sdk/devices/client/v1/device_hardware_register_session;device_hardware_register_session_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.device_hardware_register_session_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B)DeviceHardwareRegisterSessionServiceProtoP\000Zygithub.com/cloudwan/edgelq-sdk/devices/client/v1/device_hardware_register_session;device_hardware_register_session_client'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE']._serialized_options = b'\312A\022devices.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['GetDeviceHardwareRegisterSession']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['GetDeviceHardwareRegisterSession']._serialized_options = b'\202\323\344\223\002B\022@/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['BatchGetDeviceHardwareRegisterSessions']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['BatchGetDeviceHardwareRegisterSessions']._serialized_options = b'\202\323\344\223\002-\022+/v1/deviceHardwareRegisterSessions:batchGet'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['ListDeviceHardwareRegisterSessions']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['ListDeviceHardwareRegisterSessions']._serialized_options = b'\202\323\344\223\002B\022@/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['WatchDeviceHardwareRegisterSession']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['WatchDeviceHardwareRegisterSession']._serialized_options = b'\202\323\344\223\002H\"F/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}:watch'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['WatchDeviceHardwareRegisterSessions']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['WatchDeviceHardwareRegisterSessions']._serialized_options = b'\202\323\344\223\002H\"F/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions:watch'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['CreateDeviceHardwareRegisterSession']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['CreateDeviceHardwareRegisterSession']._serialized_options = b'\202\323\344\223\002d\"@/v1/{parent=projects/*/regions/*}/deviceHardwareRegisterSessions: device_hardware_register_session'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['UpdateDeviceHardwareRegisterSession']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['UpdateDeviceHardwareRegisterSession']._serialized_options = b'\202\323\344\223\002\205\001\032a/v1/{device_hardware_register_session.name=projects/*/regions/*/deviceHardwareRegisterSessions/*}: device_hardware_register_session'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['DeleteDeviceHardwareRegisterSession']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['DeleteDeviceHardwareRegisterSession']._serialized_options = b'\202\323\344\223\002B*@/v1/{name=projects/*/regions/*/deviceHardwareRegisterSessions/*}'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['GetDeviceHardwareRegisterSessionFromToken']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['GetDeviceHardwareRegisterSessionFromToken']._serialized_options = b'\202\323\344\223\002N\022L/v1/deviceHardwareRegisterSessions:getDeviceHardwareRegisterSessionFromToken'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['RegisterHardware']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['RegisterHardware']._serialized_options = b'\202\323\344\223\0025\"3/v1/deviceHardwareRegisterSessions:registerHardware'
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['HardwareStatus']._loaded_options = None
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE'].methods_by_name['HardwareStatus']._serialized_options = b'\202\323\344\223\0023\0221/v1/deviceHardwareRegisterSessions:hardwareStatus'
  _globals['_GETDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_start=526
  _globals['_GETDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_end=662
  _globals['_BATCHGETDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_start=665
  _globals['_BATCHGETDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_end=814
  _globals['_BATCHGETDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_start=817
  _globals['_BATCHGETDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_end=972
  _globals['_LISTDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_start=975
  _globals['_LISTDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_end=1217
  _globals['_LISTDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_start=1220
  _globals['_LISTDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_end=1457
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_start=1460
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_end=1598
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONRESPONSE']._serialized_start=1600
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONRESPONSE']._serialized_end=1713
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_start=1716
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSREQUEST']._serialized_end=2065
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_start=2068
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSRESPONSE']._serialized_end=2500
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSRESPONSE_PAGETOKENCHANGE']._serialized_start=2433
  _globals['_WATCHDEVICEHARDWAREREGISTERSESSIONSRESPONSE_PAGETOKENCHANGE']._serialized_end=2500
  _globals['_CREATEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_start=2503
  _globals['_CREATEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_end=2652
  _globals['_UPDATEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_start=2655
  _globals['_UPDATEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_end=3066
  _globals['_UPDATEDEVICEHARDWAREREGISTERSESSIONREQUEST_CAS']._serialized_start=2939
  _globals['_UPDATEDEVICEHARDWAREREGISTERSESSIONREQUEST_CAS']._serialized_end=3066
  _globals['_DELETEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_start=3068
  _globals['_DELETEDEVICEHARDWAREREGISTERSESSIONREQUEST']._serialized_end=3126
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE']._serialized_start=3129
  _globals['_DEVICEHARDWAREREGISTERSESSIONSERVICE']._serialized_end=5699
# @@protoc_insertion_point(module_scope)