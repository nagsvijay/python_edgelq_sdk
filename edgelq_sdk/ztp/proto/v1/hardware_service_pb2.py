# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/ztp/proto/v1/hardware_service.proto
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
    'edgelq-sdk/ztp/proto/v1/hardware_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.ztp.proto.v1 import hardware_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_hardware__pb2
from edgelq_sdk.ztp.proto.v1 import hardware_change_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_hardware__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.edgelq-sdk/ztp/proto/v1/hardware_service.proto\x12\nntt.ztp.v1\x1a&edgelq-sdk/ztp/proto/v1/hardware.proto\x1a-edgelq-sdk/ztp/proto/v1/hardware_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"s\n\x12GetHardwareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x80\x01\n\x18\x42\x61tchGetHardwaresRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"U\n\x19\x42\x61tchGetHardwaresResponse\x12\'\n\thardwares\x18\x01 \x03(\x0b\x32\x14.ntt.ztp.v1.Hardware\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xdd\x01\n\x14ListHardwaresRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xa7\x01\n\x15ListHardwaresResponse\x12\'\n\thardwares\x18\x01 \x03(\x0b\x32\x14.ntt.ztp.v1.Hardware\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"u\n\x14WatchHardwareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"C\n\x15WatchHardwareResponse\x12*\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1a.ntt.ztp.v1.HardwareChange\"\xc8\x02\n\x15WatchHardwaresRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xd1\x02\n\x16WatchHardwaresResponse\x12\x34\n\x10hardware_changes\x18\x02 \x03(\x0b\x32\x1a.ntt.ztp.v1.HardwareChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12M\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x32.ntt.ztp.v1.WatchHardwaresResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"O\n\x15\x43reateHardwareRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12&\n\x08hardware\x18\x02 \x01(\x0b\x32\x14.ntt.ztp.v1.Hardware\"\xa3\x02\n\x15UpdateHardwareRequest\x12&\n\x08hardware\x18\x02 \x01(\x0b\x32\x14.ntt.ztp.v1.Hardware\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32%.ntt.ztp.v1.UpdateHardwareRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1a\x66\n\x03\x43\x41S\x12/\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x14.ntt.ztp.v1.Hardware\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"%\n\x15\x44\x65leteHardwareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xcb\x08\n\x0fHardwareService\x12n\n\x0bGetHardware\x12\x1e.ntt.ztp.v1.GetHardwareRequest\x1a\x14.ntt.ztp.v1.Hardware\")\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/hardwares/*}\x12\x80\x01\n\x11\x42\x61tchGetHardwares\x12$.ntt.ztp.v1.BatchGetHardwaresRequest\x1a%.ntt.ztp.v1.BatchGetHardwaresResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/hardwares:batchGet\x12\x7f\n\rListHardwares\x12 .ntt.ztp.v1.ListHardwaresRequest\x1a!.ntt.ztp.v1.ListHardwaresResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/hardwares\x12\x87\x01\n\rWatchHardware\x12 .ntt.ztp.v1.WatchHardwareRequest\x1a!.ntt.ztp.v1.WatchHardwareResponse\"/\x82\xd3\xe4\x93\x02)\"\'/v1/{name=projects/*/hardwares/*}:watch0\x01\x12\x8a\x01\n\x0eWatchHardwares\x12!.ntt.ztp.v1.WatchHardwaresRequest\x1a\".ntt.ztp.v1.WatchHardwaresResponse\"/\x82\xd3\xe4\x93\x02)\"\'/v1/{parent=projects/*}/hardwares:watch0\x01\x12~\n\x0e\x43reateHardware\x12!.ntt.ztp.v1.CreateHardwareRequest\x1a\x14.ntt.ztp.v1.Hardware\"3\x82\xd3\xe4\x93\x02-\"!/v1/{parent=projects/*}/hardwares:\x08hardware\x12\x87\x01\n\x0eUpdateHardware\x12!.ntt.ztp.v1.UpdateHardwareRequest\x1a\x14.ntt.ztp.v1.Hardware\"<\x82\xd3\xe4\x93\x02\x36\x1a*/v1/{hardware.name=projects/*/hardwares/*}:\x08hardware\x12v\n\x0e\x44\x65leteHardware\x12!.ntt.ztp.v1.DeleteHardwareRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/v1/{name=projects/*/hardwares/*}\x1a+\xca\x41\x0eztp.edgelq.com\xd2\x41\x17https://apis.edgelq.comBr\n\x11\x63om.ntt.ztp.pb.v1B\x14HardwareServiceProtoP\x00ZEgithub.com/cloudwan/edgelq-sdk/ztp/client/v1/hardware;hardware_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.ztp.proto.v1.hardware_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.ztp.pb.v1B\024HardwareServiceProtoP\000ZEgithub.com/cloudwan/edgelq-sdk/ztp/client/v1/hardware;hardware_client'
  _globals['_HARDWARESERVICE']._loaded_options = None
  _globals['_HARDWARESERVICE']._serialized_options = b'\312A\016ztp.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_HARDWARESERVICE'].methods_by_name['GetHardware']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['GetHardware']._serialized_options = b'\202\323\344\223\002#\022!/v1/{name=projects/*/hardwares/*}'
  _globals['_HARDWARESERVICE'].methods_by_name['BatchGetHardwares']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['BatchGetHardwares']._serialized_options = b'\202\323\344\223\002\030\022\026/v1/hardwares:batchGet'
  _globals['_HARDWARESERVICE'].methods_by_name['ListHardwares']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['ListHardwares']._serialized_options = b'\202\323\344\223\002#\022!/v1/{parent=projects/*}/hardwares'
  _globals['_HARDWARESERVICE'].methods_by_name['WatchHardware']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['WatchHardware']._serialized_options = b'\202\323\344\223\002)\"\'/v1/{name=projects/*/hardwares/*}:watch'
  _globals['_HARDWARESERVICE'].methods_by_name['WatchHardwares']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['WatchHardwares']._serialized_options = b'\202\323\344\223\002)\"\'/v1/{parent=projects/*}/hardwares:watch'
  _globals['_HARDWARESERVICE'].methods_by_name['CreateHardware']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['CreateHardware']._serialized_options = b'\202\323\344\223\002-\"!/v1/{parent=projects/*}/hardwares:\010hardware'
  _globals['_HARDWARESERVICE'].methods_by_name['UpdateHardware']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['UpdateHardware']._serialized_options = b'\202\323\344\223\0026\032*/v1/{hardware.name=projects/*/hardwares/*}:\010hardware'
  _globals['_HARDWARESERVICE'].methods_by_name['DeleteHardware']._loaded_options = None
  _globals['_HARDWARESERVICE'].methods_by_name['DeleteHardware']._serialized_options = b'\202\323\344\223\002#*!/v1/{name=projects/*/hardwares/*}'
  _globals['_GETHARDWAREREQUEST']._serialized_start=362
  _globals['_GETHARDWAREREQUEST']._serialized_end=477
  _globals['_BATCHGETHARDWARESREQUEST']._serialized_start=480
  _globals['_BATCHGETHARDWARESREQUEST']._serialized_end=608
  _globals['_BATCHGETHARDWARESRESPONSE']._serialized_start=610
  _globals['_BATCHGETHARDWARESRESPONSE']._serialized_end=695
  _globals['_LISTHARDWARESREQUEST']._serialized_start=698
  _globals['_LISTHARDWARESREQUEST']._serialized_end=919
  _globals['_LISTHARDWARESRESPONSE']._serialized_start=922
  _globals['_LISTHARDWARESRESPONSE']._serialized_end=1089
  _globals['_WATCHHARDWAREREQUEST']._serialized_start=1091
  _globals['_WATCHHARDWAREREQUEST']._serialized_end=1208
  _globals['_WATCHHARDWARERESPONSE']._serialized_start=1210
  _globals['_WATCHHARDWARERESPONSE']._serialized_end=1277
  _globals['_WATCHHARDWARESREQUEST']._serialized_start=1280
  _globals['_WATCHHARDWARESREQUEST']._serialized_end=1608
  _globals['_WATCHHARDWARESRESPONSE']._serialized_start=1611
  _globals['_WATCHHARDWARESRESPONSE']._serialized_end=1948
  _globals['_WATCHHARDWARESRESPONSE_PAGETOKENCHANGE']._serialized_start=1881
  _globals['_WATCHHARDWARESRESPONSE_PAGETOKENCHANGE']._serialized_end=1948
  _globals['_CREATEHARDWAREREQUEST']._serialized_start=1950
  _globals['_CREATEHARDWAREREQUEST']._serialized_end=2029
  _globals['_UPDATEHARDWAREREQUEST']._serialized_start=2032
  _globals['_UPDATEHARDWAREREQUEST']._serialized_end=2323
  _globals['_UPDATEHARDWAREREQUEST_CAS']._serialized_start=2221
  _globals['_UPDATEHARDWAREREQUEST_CAS']._serialized_end=2323
  _globals['_DELETEHARDWAREREQUEST']._serialized_start=2325
  _globals['_DELETEHARDWAREREQUEST']._serialized_end=2362
  _globals['_HARDWARESERVICE']._serialized_start=2365
  _globals['_HARDWARESERVICE']._serialized_end=3464
# @@protoc_insertion_point(module_scope)
