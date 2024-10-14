# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/condition_service.proto
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
    'edgelq-sdk/iam/proto/v1/condition_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import condition_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_condition__pb2
from edgelq_sdk.iam.proto.v1 import condition_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_condition__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/edgelq-sdk/iam/proto/v1/condition_service.proto\x12\nntt.iam.v1\x1a\'edgelq-sdk/iam/proto/v1/condition.proto\x1a.edgelq-sdk/iam/proto/v1/condition_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"t\n\x13GetConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x81\x01\n\x19\x42\x61tchGetConditionsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"X\n\x1a\x42\x61tchGetConditionsResponse\x12)\n\nconditions\x18\x01 \x03(\x0b\x32\x15.ntt.iam.v1.Condition\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xde\x01\n\x15ListConditionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xaa\x01\n\x16ListConditionsResponse\x12)\n\nconditions\x18\x01 \x03(\x0b\x32\x15.ntt.iam.v1.Condition\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"v\n\x15WatchConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"E\n\x16WatchConditionResponse\x12+\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1b.ntt.iam.v1.ConditionChange\"\xc9\x02\n\x16WatchConditionsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xd5\x02\n\x17WatchConditionsResponse\x12\x36\n\x11\x63ondition_changes\x18\x02 \x03(\x0b\x32\x1b.ntt.iam.v1.ConditionChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12N\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x33.ntt.iam.v1.WatchConditionsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"R\n\x16\x43reateConditionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12(\n\tcondition\x18\x02 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\"\xa8\x02\n\x16UpdateConditionRequest\x12(\n\tcondition\x18\x02 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32&.ntt.iam.v1.UpdateConditionRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1ag\n\x03\x43\x41S\x12\x30\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x15.ntt.iam.v1.Condition\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"&\n\x16\x44\x65leteConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x9b\x0f\n\x10\x43onditionService\x12\xe0\x01\n\x0cGetCondition\x12\x1f.ntt.iam.v1.GetConditionRequest\x1a\x15.ntt.iam.v1.Condition\"\x97\x01\x82\xd3\xe4\x93\x02\x90\x01\x12\x17/v1/{name=conditions/*}Z$\x12\"/v1/{name=projects/*/conditions/*}Z)\x12\'/v1/{name=organizations/*/conditions/*}Z$\x12\"/v1/{name=services/*/conditions/*}\x12\x84\x01\n\x12\x42\x61tchGetConditions\x12%.ntt.iam.v1.BatchGetConditionsRequest\x1a&.ntt.iam.v1.BatchGetConditionsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/conditions:batchGet\x12\xe8\x01\n\x0eListConditions\x12!.ntt.iam.v1.ListConditionsRequest\x1a\".ntt.iam.v1.ListConditionsResponse\"\x8e\x01\x82\xd3\xe4\x93\x02\x87\x01\x12\x0e/v1/conditionsZ$\x12\"/v1/{parent=projects/*}/conditionsZ)\x12\'/v1/{parent=organizations/*}/conditionsZ$\x12\"/v1/{parent=services/*}/conditions\x12\x8b\x02\n\x0eWatchCondition\x12!.ntt.iam.v1.WatchConditionRequest\x1a\".ntt.iam.v1.WatchConditionResponse\"\xaf\x01\x82\xd3\xe4\x93\x02\xa8\x01\"\x1d/v1/{name=conditions/*}:watchZ*\"(/v1/{name=projects/*/conditions/*}:watchZ/\"-/v1/{name=organizations/*/conditions/*}:watchZ*\"(/v1/{name=services/*/conditions/*}:watch0\x01\x12\x85\x02\n\x0fWatchConditions\x12\".ntt.iam.v1.WatchConditionsRequest\x1a#.ntt.iam.v1.WatchConditionsResponse\"\xa6\x01\x82\xd3\xe4\x93\x02\x9f\x01\"\x14/v1/conditions:watchZ*\"(/v1/{parent=projects/*}/conditions:watchZ/\"-/v1/{parent=organizations/*}/conditions:watchZ*\"(/v1/{parent=services/*}/conditions:watch0\x01\x12\xe8\x01\n\x0f\x43reateCondition\x12\".ntt.iam.v1.CreateConditionRequest\x1a\x15.ntt.iam.v1.Condition\"\x99\x01\x82\xd3\xe4\x93\x02\x92\x01\"\x0e/v1/conditions:\tconditionZ$\"\"/v1/{parent=projects/*}/conditionsZ)\"\'/v1/{parent=organizations/*}/conditionsZ$\"\"/v1/{parent=services/*}/conditions\x12\x99\x02\n\x0fUpdateCondition\x12\".ntt.iam.v1.UpdateConditionRequest\x1a\x15.ntt.iam.v1.Condition\"\xca\x01\x82\xd3\xe4\x93\x02\xc3\x01\x1a!/v1/{condition.name=conditions/*}:\tconditionZ.\x1a,/v1/{condition.name=projects/*/conditions/*}Z3\x1a\x31/v1/{condition.name=organizations/*/conditions/*}Z.\x1a,/v1/{condition.name=services/*/conditions/*}\x12\xe7\x01\n\x0f\x44\x65leteCondition\x12\".ntt.iam.v1.DeleteConditionRequest\x1a\x16.google.protobuf.Empty\"\x97\x01\x82\xd3\xe4\x93\x02\x90\x01*\x17/v1/{name=conditions/*}Z$*\"/v1/{name=projects/*/conditions/*}Z)*\'/v1/{name=organizations/*/conditions/*}Z$*\"/v1/{name=services/*/conditions/*}\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comBu\n\x11\x63om.ntt.iam.pb.v1B\x15\x43onditionServiceProtoP\x00ZGgithub.com/cloudwan/edgelq-sdk/iam/client/v1/condition;condition_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.condition_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\025ConditionServiceProtoP\000ZGgithub.com/cloudwan/edgelq-sdk/iam/client/v1/condition;condition_client'
  _globals['_CONDITIONSERVICE']._loaded_options = None
  _globals['_CONDITIONSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_CONDITIONSERVICE'].methods_by_name['GetCondition']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['GetCondition']._serialized_options = b'\202\323\344\223\002\220\001\022\027/v1/{name=conditions/*}Z$\022\"/v1/{name=projects/*/conditions/*}Z)\022\'/v1/{name=organizations/*/conditions/*}Z$\022\"/v1/{name=services/*/conditions/*}'
  _globals['_CONDITIONSERVICE'].methods_by_name['BatchGetConditions']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['BatchGetConditions']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/conditions:batchGet'
  _globals['_CONDITIONSERVICE'].methods_by_name['ListConditions']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['ListConditions']._serialized_options = b'\202\323\344\223\002\207\001\022\016/v1/conditionsZ$\022\"/v1/{parent=projects/*}/conditionsZ)\022\'/v1/{parent=organizations/*}/conditionsZ$\022\"/v1/{parent=services/*}/conditions'
  _globals['_CONDITIONSERVICE'].methods_by_name['WatchCondition']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['WatchCondition']._serialized_options = b'\202\323\344\223\002\250\001\"\035/v1/{name=conditions/*}:watchZ*\"(/v1/{name=projects/*/conditions/*}:watchZ/\"-/v1/{name=organizations/*/conditions/*}:watchZ*\"(/v1/{name=services/*/conditions/*}:watch'
  _globals['_CONDITIONSERVICE'].methods_by_name['WatchConditions']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['WatchConditions']._serialized_options = b'\202\323\344\223\002\237\001\"\024/v1/conditions:watchZ*\"(/v1/{parent=projects/*}/conditions:watchZ/\"-/v1/{parent=organizations/*}/conditions:watchZ*\"(/v1/{parent=services/*}/conditions:watch'
  _globals['_CONDITIONSERVICE'].methods_by_name['CreateCondition']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['CreateCondition']._serialized_options = b'\202\323\344\223\002\222\001\"\016/v1/conditions:\tconditionZ$\"\"/v1/{parent=projects/*}/conditionsZ)\"\'/v1/{parent=organizations/*}/conditionsZ$\"\"/v1/{parent=services/*}/conditions'
  _globals['_CONDITIONSERVICE'].methods_by_name['UpdateCondition']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['UpdateCondition']._serialized_options = b'\202\323\344\223\002\303\001\032!/v1/{condition.name=conditions/*}:\tconditionZ.\032,/v1/{condition.name=projects/*/conditions/*}Z3\0321/v1/{condition.name=organizations/*/conditions/*}Z.\032,/v1/{condition.name=services/*/conditions/*}'
  _globals['_CONDITIONSERVICE'].methods_by_name['DeleteCondition']._loaded_options = None
  _globals['_CONDITIONSERVICE'].methods_by_name['DeleteCondition']._serialized_options = b'\202\323\344\223\002\220\001*\027/v1/{name=conditions/*}Z$*\"/v1/{name=projects/*/conditions/*}Z)*\'/v1/{name=organizations/*/conditions/*}Z$*\"/v1/{name=services/*/conditions/*}'
  _globals['_GETCONDITIONREQUEST']._serialized_start=365
  _globals['_GETCONDITIONREQUEST']._serialized_end=481
  _globals['_BATCHGETCONDITIONSREQUEST']._serialized_start=484
  _globals['_BATCHGETCONDITIONSREQUEST']._serialized_end=613
  _globals['_BATCHGETCONDITIONSRESPONSE']._serialized_start=615
  _globals['_BATCHGETCONDITIONSRESPONSE']._serialized_end=703
  _globals['_LISTCONDITIONSREQUEST']._serialized_start=706
  _globals['_LISTCONDITIONSREQUEST']._serialized_end=928
  _globals['_LISTCONDITIONSRESPONSE']._serialized_start=931
  _globals['_LISTCONDITIONSRESPONSE']._serialized_end=1101
  _globals['_WATCHCONDITIONREQUEST']._serialized_start=1103
  _globals['_WATCHCONDITIONREQUEST']._serialized_end=1221
  _globals['_WATCHCONDITIONRESPONSE']._serialized_start=1223
  _globals['_WATCHCONDITIONRESPONSE']._serialized_end=1292
  _globals['_WATCHCONDITIONSREQUEST']._serialized_start=1295
  _globals['_WATCHCONDITIONSREQUEST']._serialized_end=1624
  _globals['_WATCHCONDITIONSRESPONSE']._serialized_start=1627
  _globals['_WATCHCONDITIONSRESPONSE']._serialized_end=1968
  _globals['_WATCHCONDITIONSRESPONSE_PAGETOKENCHANGE']._serialized_start=1901
  _globals['_WATCHCONDITIONSRESPONSE_PAGETOKENCHANGE']._serialized_end=1968
  _globals['_CREATECONDITIONREQUEST']._serialized_start=1970
  _globals['_CREATECONDITIONREQUEST']._serialized_end=2052
  _globals['_UPDATECONDITIONREQUEST']._serialized_start=2055
  _globals['_UPDATECONDITIONREQUEST']._serialized_end=2351
  _globals['_UPDATECONDITIONREQUEST_CAS']._serialized_start=2248
  _globals['_UPDATECONDITIONREQUEST_CAS']._serialized_end=2351
  _globals['_DELETECONDITIONREQUEST']._serialized_start=2353
  _globals['_DELETECONDITIONREQUEST']._serialized_end=2391
  _globals['_CONDITIONSERVICE']._serialized_start=2394
  _globals['_CONDITIONSERVICE']._serialized_end=4341
# @@protoc_insertion_point(module_scope)