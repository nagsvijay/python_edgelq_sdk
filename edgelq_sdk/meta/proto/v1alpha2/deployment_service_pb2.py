# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/meta/proto/v1alpha2/deployment_service.proto
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
    'edgelq-sdk/meta/proto/v1alpha2/deployment_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.meta.proto.v1alpha2 import deployment_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_deployment__pb2
from edgelq_sdk.meta.proto.v1alpha2 import deployment_change_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_deployment__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/meta/proto/v1alpha2/deployment_service.proto\x12\x11ntt.meta.v1alpha2\x1a/edgelq-sdk/meta/proto/v1alpha2/deployment.proto\x1a\x36\x65\x64gelq-sdk/meta/proto/v1alpha2/deployment_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"u\n\x14GetDeploymentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"\x82\x01\n\x1a\x42\x61tchGetDeploymentsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"b\n\x1b\x42\x61tchGetDeploymentsResponse\x12\x32\n\x0b\x64\x65ployments\x18\x01 \x03(\x0b\x32\x1d.ntt.meta.v1alpha2.Deployment\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xdf\x01\n\x16ListDeploymentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xb4\x01\n\x17ListDeploymentsResponse\x12\x32\n\x0b\x64\x65ployments\x18\x01 \x03(\x0b\x32\x1d.ntt.meta.v1alpha2.Deployment\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"w\n\x16WatchDeploymentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"N\n\x17WatchDeploymentResponse\x12\x33\n\x06\x63hange\x18\x01 \x01(\x0b\x32#.ntt.meta.v1alpha2.DeploymentChange\"\xca\x02\n\x17WatchDeploymentsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xe7\x02\n\x18WatchDeploymentsResponse\x12?\n\x12\x64\x65ployment_changes\x18\x02 \x03(\x0b\x32#.ntt.meta.v1alpha2.DeploymentChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12V\n\x11page_token_change\x18\x03 \x01(\x0b\x32;.ntt.meta.v1alpha2.WatchDeploymentsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd6\x06\n\x11\x44\x65ploymentService\x12\x89\x01\n\rGetDeployment\x12\'.ntt.meta.v1alpha2.GetDeploymentRequest\x1a\x1d.ntt.meta.v1alpha2.Deployment\"0\x82\xd3\xe4\x93\x02*\x12(/v1alpha2/{name=regions/*/deployments/*}\x12\x9c\x01\n\x13\x42\x61tchGetDeployments\x12-.ntt.meta.v1alpha2.BatchGetDeploymentsRequest\x1a..ntt.meta.v1alpha2.BatchGetDeploymentsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1alpha2/deployments:batchGet\x12\x9a\x01\n\x0fListDeployments\x12).ntt.meta.v1alpha2.ListDeploymentsRequest\x1a*.ntt.meta.v1alpha2.ListDeploymentsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/v1alpha2/{parent=regions/*}/deployments\x12\xa2\x01\n\x0fWatchDeployment\x12).ntt.meta.v1alpha2.WatchDeploymentRequest\x1a*.ntt.meta.v1alpha2.WatchDeploymentResponse\"6\x82\xd3\xe4\x93\x02\x30\"./v1alpha2/{name=regions/*/deployments/*}:watch0\x01\x12\xa5\x01\n\x10WatchDeployments\x12*.ntt.meta.v1alpha2.WatchDeploymentsRequest\x1a+.ntt.meta.v1alpha2.WatchDeploymentsResponse\"6\x82\xd3\xe4\x93\x02\x30\"./v1alpha2/{parent=regions/*}/deployments:watch0\x01\x1a,\xca\x41\x0fmeta.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x86\x01\n\x18\x63om.ntt.meta.pb.v1alpha2B\x16\x44\x65ploymentServiceProtoP\x00ZPgithub.com/cloudwan/edgelq-sdk/meta/client/v1alpha2/deployment;deployment_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.meta.proto.v1alpha2.deployment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.meta.pb.v1alpha2B\026DeploymentServiceProtoP\000ZPgithub.com/cloudwan/edgelq-sdk/meta/client/v1alpha2/deployment;deployment_client'
  _globals['_DEPLOYMENTSERVICE']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE']._serialized_options = b'\312A\017meta.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['GetDeployment']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['GetDeployment']._serialized_options = b'\202\323\344\223\002*\022(/v1alpha2/{name=regions/*/deployments/*}'
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['BatchGetDeployments']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['BatchGetDeployments']._serialized_options = b'\202\323\344\223\002 \022\036/v1alpha2/deployments:batchGet'
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['ListDeployments']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['ListDeployments']._serialized_options = b'\202\323\344\223\002*\022(/v1alpha2/{parent=regions/*}/deployments'
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['WatchDeployment']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['WatchDeployment']._serialized_options = b'\202\323\344\223\0020\"./v1alpha2/{name=regions/*/deployments/*}:watch'
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['WatchDeployments']._loaded_options = None
  _globals['_DEPLOYMENTSERVICE'].methods_by_name['WatchDeployments']._serialized_options = b'\202\323\344\223\0020\"./v1alpha2/{parent=regions/*}/deployments:watch'
  _globals['_GETDEPLOYMENTREQUEST']._serialized_start=396
  _globals['_GETDEPLOYMENTREQUEST']._serialized_end=513
  _globals['_BATCHGETDEPLOYMENTSREQUEST']._serialized_start=516
  _globals['_BATCHGETDEPLOYMENTSREQUEST']._serialized_end=646
  _globals['_BATCHGETDEPLOYMENTSRESPONSE']._serialized_start=648
  _globals['_BATCHGETDEPLOYMENTSRESPONSE']._serialized_end=746
  _globals['_LISTDEPLOYMENTSREQUEST']._serialized_start=749
  _globals['_LISTDEPLOYMENTSREQUEST']._serialized_end=972
  _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_start=975
  _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_end=1155
  _globals['_WATCHDEPLOYMENTREQUEST']._serialized_start=1157
  _globals['_WATCHDEPLOYMENTREQUEST']._serialized_end=1276
  _globals['_WATCHDEPLOYMENTRESPONSE']._serialized_start=1278
  _globals['_WATCHDEPLOYMENTRESPONSE']._serialized_end=1356
  _globals['_WATCHDEPLOYMENTSREQUEST']._serialized_start=1359
  _globals['_WATCHDEPLOYMENTSREQUEST']._serialized_end=1689
  _globals['_WATCHDEPLOYMENTSRESPONSE']._serialized_start=1692
  _globals['_WATCHDEPLOYMENTSRESPONSE']._serialized_end=2051
  _globals['_WATCHDEPLOYMENTSRESPONSE_PAGETOKENCHANGE']._serialized_start=1984
  _globals['_WATCHDEPLOYMENTSRESPONSE_PAGETOKENCHANGE']._serialized_end=2051
  _globals['_DEPLOYMENTSERVICE']._serialized_start=2054
  _globals['_DEPLOYMENTSERVICE']._serialized_end=2908
# @@protoc_insertion_point(module_scope)
