# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v3/project_service.proto
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
    'edgelq-sdk/monitoring/proto/v3/project_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v3 import project_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_project__pb2
from edgelq_sdk.monitoring.proto.v3 import project_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_project__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4edgelq-sdk/monitoring/proto/v3/project_service.proto\x12\x11ntt.monitoring.v3\x1a,edgelq-sdk/monitoring/proto/v3/project.proto\x1a\x33\x65\x64gelq-sdk/monitoring/proto/v3/project_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"r\n\x11GetProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x7f\n\x17\x42\x61tchGetProjectsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"Y\n\x18\x42\x61tchGetProjectsResponse\x12,\n\x08projects\x18\x01 \x03(\x0b\x32\x1a.ntt.monitoring.v3.Project\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xcc\x01\n\x13ListProjectsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xab\x01\n\x14ListProjectsResponse\x12,\n\x08projects\x18\x01 \x03(\x0b\x32\x1a.ntt.monitoring.v3.Project\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"t\n\x13WatchProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"H\n\x14WatchProjectResponse\x12\x30\n\x06\x63hange\x18\x01 \x01(\x0b\x32 .ntt.monitoring.v3.ProjectChange\"\xb7\x02\n\x14WatchProjectsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xdb\x02\n\x15WatchProjectsResponse\x12\x39\n\x0fproject_changes\x18\x02 \x03(\x0b\x32 .ntt.monitoring.v3.ProjectChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12S\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x38.ntt.monitoring.v3.WatchProjectsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"C\n\x14\x43reateProjectRequest\x12+\n\x07project\x18\x02 \x01(\x0b\x32\x1a.ntt.monitoring.v3.Project\"\xb3\x02\n\x14UpdateProjectRequest\x12+\n\x07project\x18\x02 \x01(\x0b\x32\x1a.ntt.monitoring.v3.Project\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x38\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32+.ntt.monitoring.v3.UpdateProjectRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1al\n\x03\x43\x41S\x12\x35\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x1a.ntt.monitoring.v3.Project\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xb0\x08\n\x0eProjectService\x12m\n\nGetProject\x12$.ntt.monitoring.v3.GetProjectRequest\x1a\x1a.ntt.monitoring.v3.Project\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v3/{name=projects/*}\x12\x8a\x01\n\x10\x42\x61tchGetProjects\x12*.ntt.monitoring.v3.BatchGetProjectsRequest\x1a+.ntt.monitoring.v3.BatchGetProjectsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v3/projects:batchGet\x12u\n\x0cListProjects\x12&.ntt.monitoring.v3.ListProjectsRequest\x1a\'.ntt.monitoring.v3.ListProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v3/projects\x12\x86\x01\n\x0cWatchProject\x12&.ntt.monitoring.v3.WatchProjectRequest\x1a\'.ntt.monitoring.v3.WatchProjectResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/v3/{name=projects/*}:watch0\x01\x12\x80\x01\n\rWatchProjects\x12\'.ntt.monitoring.v3.WatchProjectsRequest\x1a(.ntt.monitoring.v3.WatchProjectsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x12/v3/projects:watch0\x01\x12s\n\rCreateProject\x12\'.ntt.monitoring.v3.CreateProjectRequest\x1a\x1a.ntt.monitoring.v3.Project\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0c/v3/projects:\x07project\x12\x84\x01\n\rUpdateProject\x12\'.ntt.monitoring.v3.UpdateProjectRequest\x1a\x1a.ntt.monitoring.v3.Project\".\x82\xd3\xe4\x93\x02(\x1a\x1d/v3/{project.name=projects/*}:\x07project\x12o\n\rDeleteProject\x12\'.ntt.monitoring.v3.DeleteProjectRequest\x1a\x16.google.protobuf.Empty\"\x1d\x82\xd3\xe4\x93\x02\x17*\x15/v3/{name=projects/*}\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comB}\n\x18\x63om.ntt.monitoring.pb.v3B\x13ProjectServiceProtoP\x00ZJgithub.com/cloudwan/edgelq-sdk/monitoring/client/v3/project;project_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v3.project_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v3B\023ProjectServiceProtoP\000ZJgithub.com/cloudwan/edgelq-sdk/monitoring/client/v3/project;project_client'
  _globals['_PROJECTSERVICE']._loaded_options = None
  _globals['_PROJECTSERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\027\022\025/v3/{name=projects/*}'
  _globals['_PROJECTSERVICE'].methods_by_name['BatchGetProjects']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['BatchGetProjects']._serialized_options = b'\202\323\344\223\002\027\022\025/v3/projects:batchGet'
  _globals['_PROJECTSERVICE'].methods_by_name['ListProjects']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['ListProjects']._serialized_options = b'\202\323\344\223\002\016\022\014/v3/projects'
  _globals['_PROJECTSERVICE'].methods_by_name['WatchProject']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['WatchProject']._serialized_options = b'\202\323\344\223\002\035\"\033/v3/{name=projects/*}:watch'
  _globals['_PROJECTSERVICE'].methods_by_name['WatchProjects']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['WatchProjects']._serialized_options = b'\202\323\344\223\002\024\"\022/v3/projects:watch'
  _globals['_PROJECTSERVICE'].methods_by_name['CreateProject']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\027\"\014/v3/projects:\007project'
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProject']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProject']._serialized_options = b'\202\323\344\223\002(\032\035/v3/{project.name=projects/*}:\007project'
  _globals['_PROJECTSERVICE'].methods_by_name['DeleteProject']._loaded_options = None
  _globals['_PROJECTSERVICE'].methods_by_name['DeleteProject']._serialized_options = b'\202\323\344\223\002\027*\025/v3/{name=projects/*}'
  _globals['_GETPROJECTREQUEST']._serialized_start=387
  _globals['_GETPROJECTREQUEST']._serialized_end=501
  _globals['_BATCHGETPROJECTSREQUEST']._serialized_start=503
  _globals['_BATCHGETPROJECTSREQUEST']._serialized_end=630
  _globals['_BATCHGETPROJECTSRESPONSE']._serialized_start=632
  _globals['_BATCHGETPROJECTSRESPONSE']._serialized_end=721
  _globals['_LISTPROJECTSREQUEST']._serialized_start=724
  _globals['_LISTPROJECTSREQUEST']._serialized_end=928
  _globals['_LISTPROJECTSRESPONSE']._serialized_start=931
  _globals['_LISTPROJECTSRESPONSE']._serialized_end=1102
  _globals['_WATCHPROJECTREQUEST']._serialized_start=1104
  _globals['_WATCHPROJECTREQUEST']._serialized_end=1220
  _globals['_WATCHPROJECTRESPONSE']._serialized_start=1222
  _globals['_WATCHPROJECTRESPONSE']._serialized_end=1294
  _globals['_WATCHPROJECTSREQUEST']._serialized_start=1297
  _globals['_WATCHPROJECTSREQUEST']._serialized_end=1608
  _globals['_WATCHPROJECTSRESPONSE']._serialized_start=1611
  _globals['_WATCHPROJECTSRESPONSE']._serialized_end=1958
  _globals['_WATCHPROJECTSRESPONSE_PAGETOKENCHANGE']._serialized_start=1891
  _globals['_WATCHPROJECTSRESPONSE_PAGETOKENCHANGE']._serialized_end=1958
  _globals['_CREATEPROJECTREQUEST']._serialized_start=1960
  _globals['_CREATEPROJECTREQUEST']._serialized_end=2027
  _globals['_UPDATEPROJECTREQUEST']._serialized_start=2030
  _globals['_UPDATEPROJECTREQUEST']._serialized_end=2337
  _globals['_UPDATEPROJECTREQUEST_CAS']._serialized_start=2229
  _globals['_UPDATEPROJECTREQUEST_CAS']._serialized_end=2337
  _globals['_DELETEPROJECTREQUEST']._serialized_start=2339
  _globals['_DELETEPROJECTREQUEST']._serialized_end=2375
  _globals['_PROJECTSERVICE']._serialized_start=2378
  _globals['_PROJECTSERVICE']._serialized_end=3450
# @@protoc_insertion_point(module_scope)
