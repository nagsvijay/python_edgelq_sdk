# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/meta/proto/v1alpha2/resource_service.proto
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
    'edgelq-sdk/meta/proto/v1alpha2/resource_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.meta.proto.v1alpha2 import resource_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_resource__pb2
from edgelq_sdk.meta.proto.v1alpha2 import resource_change_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_resource__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5edgelq-sdk/meta/proto/v1alpha2/resource_service.proto\x12\x11ntt.meta.v1alpha2\x1a-edgelq-sdk/meta/proto/v1alpha2/resource.proto\x1a\x34\x65\x64gelq-sdk/meta/proto/v1alpha2/resource_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"s\n\x12GetResourceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x80\x01\n\x18\x42\x61tchGetResourcesRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"\\\n\x19\x42\x61tchGetResourcesResponse\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.ntt.meta.v1alpha2.Resource\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xdd\x01\n\x14ListResourcesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xae\x01\n\x15ListResourcesResponse\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.ntt.meta.v1alpha2.Resource\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"u\n\x14WatchResourceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"J\n\x15WatchResourceResponse\x12\x31\n\x06\x63hange\x18\x01 \x01(\x0b\x32!.ntt.meta.v1alpha2.ResourceChange\"\xc8\x02\n\x15WatchResourcesRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xdf\x02\n\x16WatchResourcesResponse\x12;\n\x10resource_changes\x18\x02 \x03(\x0b\x32!.ntt.meta.v1alpha2.ResourceChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12T\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x39.ntt.meta.v1alpha2.WatchResourcesResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb0\x06\n\x0fResourceService\x12\x82\x01\n\x0bGetResource\x12%.ntt.meta.v1alpha2.GetResourceRequest\x1a\x1b.ntt.meta.v1alpha2.Resource\"/\x82\xd3\xe4\x93\x02)\x12\'/v1alpha2/{name=services/*/resources/*}\x12\x94\x01\n\x11\x42\x61tchGetResources\x12+.ntt.meta.v1alpha2.BatchGetResourcesRequest\x1a,.ntt.meta.v1alpha2.BatchGetResourcesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha2/resources:batchGet\x12\x93\x01\n\rListResources\x12\'.ntt.meta.v1alpha2.ListResourcesRequest\x1a(.ntt.meta.v1alpha2.ListResourcesResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/v1alpha2/{parent=services/*}/resources\x12\x9b\x01\n\rWatchResource\x12\'.ntt.meta.v1alpha2.WatchResourceRequest\x1a(.ntt.meta.v1alpha2.WatchResourceResponse\"5\x82\xd3\xe4\x93\x02/\"-/v1alpha2/{name=services/*/resources/*}:watch0\x01\x12\x9e\x01\n\x0eWatchResources\x12(.ntt.meta.v1alpha2.WatchResourcesRequest\x1a).ntt.meta.v1alpha2.WatchResourcesResponse\"5\x82\xd3\xe4\x93\x02/\"-/v1alpha2/{parent=services/*}/resources:watch0\x01\x1a,\xca\x41\x0fmeta.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x80\x01\n\x18\x63om.ntt.meta.pb.v1alpha2B\x14ResourceServiceProtoP\x00ZLgithub.com/cloudwan/edgelq-sdk/meta/client/v1alpha2/resource;resource_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.meta.proto.v1alpha2.resource_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.meta.pb.v1alpha2B\024ResourceServiceProtoP\000ZLgithub.com/cloudwan/edgelq-sdk/meta/client/v1alpha2/resource;resource_client'
  _globals['_RESOURCESERVICE']._loaded_options = None
  _globals['_RESOURCESERVICE']._serialized_options = b'\312A\017meta.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_RESOURCESERVICE'].methods_by_name['GetResource']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['GetResource']._serialized_options = b'\202\323\344\223\002)\022\'/v1alpha2/{name=services/*/resources/*}'
  _globals['_RESOURCESERVICE'].methods_by_name['BatchGetResources']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['BatchGetResources']._serialized_options = b'\202\323\344\223\002\036\022\034/v1alpha2/resources:batchGet'
  _globals['_RESOURCESERVICE'].methods_by_name['ListResources']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['ListResources']._serialized_options = b'\202\323\344\223\002)\022\'/v1alpha2/{parent=services/*}/resources'
  _globals['_RESOURCESERVICE'].methods_by_name['WatchResource']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['WatchResource']._serialized_options = b'\202\323\344\223\002/\"-/v1alpha2/{name=services/*/resources/*}:watch'
  _globals['_RESOURCESERVICE'].methods_by_name['WatchResources']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['WatchResources']._serialized_options = b'\202\323\344\223\002/\"-/v1alpha2/{parent=services/*}/resources:watch'
  _globals['_GETRESOURCEREQUEST']._serialized_start=390
  _globals['_GETRESOURCEREQUEST']._serialized_end=505
  _globals['_BATCHGETRESOURCESREQUEST']._serialized_start=508
  _globals['_BATCHGETRESOURCESREQUEST']._serialized_end=636
  _globals['_BATCHGETRESOURCESRESPONSE']._serialized_start=638
  _globals['_BATCHGETRESOURCESRESPONSE']._serialized_end=730
  _globals['_LISTRESOURCESREQUEST']._serialized_start=733
  _globals['_LISTRESOURCESREQUEST']._serialized_end=954
  _globals['_LISTRESOURCESRESPONSE']._serialized_start=957
  _globals['_LISTRESOURCESRESPONSE']._serialized_end=1131
  _globals['_WATCHRESOURCEREQUEST']._serialized_start=1133
  _globals['_WATCHRESOURCEREQUEST']._serialized_end=1250
  _globals['_WATCHRESOURCERESPONSE']._serialized_start=1252
  _globals['_WATCHRESOURCERESPONSE']._serialized_end=1326
  _globals['_WATCHRESOURCESREQUEST']._serialized_start=1329
  _globals['_WATCHRESOURCESREQUEST']._serialized_end=1657
  _globals['_WATCHRESOURCESRESPONSE']._serialized_start=1660
  _globals['_WATCHRESOURCESRESPONSE']._serialized_end=2011
  _globals['_WATCHRESOURCESRESPONSE_PAGETOKENCHANGE']._serialized_start=1944
  _globals['_WATCHRESOURCESRESPONSE_PAGETOKENCHANGE']._serialized_end=2011
  _globals['_RESOURCESERVICE']._serialized_start=2014
  _globals['_RESOURCESERVICE']._serialized_end=2830
# @@protoc_insertion_point(module_scope)
