# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/meta/proto/v1alpha2/deployment_change.proto
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
    'edgelq-sdk/meta/proto/v1alpha2/deployment_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.meta.proto.v1alpha2 import deployment_pb2 as edgelq__sdk_dot_meta_dot_proto_dot_v1alpha2_dot_deployment__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/meta/proto/v1alpha2/deployment_change.proto\x12\x11ntt.meta.v1alpha2\x1a/edgelq-sdk/meta/proto/v1alpha2/deployment.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\x89\x05\n\x10\x44\x65ploymentChange\x12:\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32).ntt.meta.v1alpha2.DeploymentChange.AddedH\x00\x12@\n\x08modified\x18\x02 \x01(\x0b\x32,.ntt.meta.v1alpha2.DeploymentChange.ModifiedH\x00\x12>\n\x07\x63urrent\x18\x04 \x01(\x0b\x32+.ntt.meta.v1alpha2.DeploymentChange.CurrentH\x00\x12>\n\x07removed\x18\x03 \x01(\x0b\x32+.ntt.meta.v1alpha2.DeploymentChange.RemovedH\x00\x1aN\n\x05\x41\x64\x64\x65\x64\x12\x31\n\ndeployment\x18\x01 \x01(\x0b\x32\x1d.ntt.meta.v1alpha2.Deployment\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xac\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\ndeployment\x18\x02 \x01(\x0b\x32\x1d.ntt.meta.v1alpha2.Deployment\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a<\n\x07\x43urrent\x12\x31\n\ndeployment\x18\x01 \x01(\x0b\x32\x1d.ntt.meta.v1alpha2.Deployment\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x81\x01\n\x18\x63om.ntt.meta.pb.v1alpha2B\x15\x44\x65ploymentChangeProtoP\x00ZLgithub.com/cloudwan/edgelq-sdk/meta/resources/v1alpha2/deployment;deploymentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.meta.proto.v1alpha2.deployment_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.meta.pb.v1alpha2B\025DeploymentChangeProtoP\000ZLgithub.com/cloudwan/edgelq-sdk/meta/resources/v1alpha2/deployment;deployment'
  _globals['_DEPLOYMENTCHANGE']._serialized_start=188
  _globals['_DEPLOYMENTCHANGE']._serialized_end=837
  _globals['_DEPLOYMENTCHANGE_ADDED']._serialized_start=462
  _globals['_DEPLOYMENTCHANGE_ADDED']._serialized_end=540
  _globals['_DEPLOYMENTCHANGE_MODIFIED']._serialized_start=543
  _globals['_DEPLOYMENTCHANGE_MODIFIED']._serialized_end=715
  _globals['_DEPLOYMENTCHANGE_CURRENT']._serialized_start=717
  _globals['_DEPLOYMENTCHANGE_CURRENT']._serialized_end=777
  _globals['_DEPLOYMENTCHANGE_REMOVED']._serialized_start=779
  _globals['_DEPLOYMENTCHANGE_REMOVED']._serialized_end=822
# @@protoc_insertion_point(module_scope)
