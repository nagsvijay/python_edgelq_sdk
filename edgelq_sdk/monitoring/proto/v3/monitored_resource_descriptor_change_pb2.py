# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v3/monitored_resource_descriptor_change.proto
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
    'edgelq-sdk/monitoring/proto/v3/monitored_resource_descriptor_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v3 import monitored_resource_descriptor_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_monitored__resource__descriptor__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIedgelq-sdk/monitoring/proto/v3/monitored_resource_descriptor_change.proto\x12\x11ntt.monitoring.v3\x1a\x42\x65\x64gelq-sdk/monitoring/proto/v3/monitored_resource_descriptor.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xca\x06\n!MonitoredResourceDescriptorChange\x12K\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32:.ntt.monitoring.v3.MonitoredResourceDescriptorChange.AddedH\x00\x12Q\n\x08modified\x18\x02 \x01(\x0b\x32=.ntt.monitoring.v3.MonitoredResourceDescriptorChange.ModifiedH\x00\x12O\n\x07\x63urrent\x18\x04 \x01(\x0b\x32<.ntt.monitoring.v3.MonitoredResourceDescriptorChange.CurrentH\x00\x12O\n\x07removed\x18\x03 \x01(\x0b\x32<.ntt.monitoring.v3.MonitoredResourceDescriptorChange.RemovedH\x00\x1ar\n\x05\x41\x64\x64\x65\x64\x12U\n\x1dmonitored_resource_descriptor\x18\x01 \x01(\x0b\x32..ntt.monitoring.v3.MonitoredResourceDescriptor\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xd0\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12U\n\x1dmonitored_resource_descriptor\x18\x02 \x01(\x0b\x32..ntt.monitoring.v3.MonitoredResourceDescriptor\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a`\n\x07\x43urrent\x12U\n\x1dmonitored_resource_descriptor\x18\x01 \x01(\x0b\x32..ntt.monitoring.v3.MonitoredResourceDescriptor\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\xb8\x01\n\x18\x63om.ntt.monitoring.pb.v3B&MonitoredResourceDescriptorChangeProtoP\x00Zrgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v3/monitored_resource_descriptor;monitored_resource_descriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v3.monitored_resource_descriptor_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v3B&MonitoredResourceDescriptorChangeProtoP\000Zrgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v3/monitored_resource_descriptor;monitored_resource_descriptor'
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE']._serialized_start=226
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE']._serialized_end=1068
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_ADDED']._serialized_start=585
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_ADDED']._serialized_end=699
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_MODIFIED']._serialized_start=702
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_MODIFIED']._serialized_end=910
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_CURRENT']._serialized_start=912
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_CURRENT']._serialized_end=1008
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_REMOVED']._serialized_start=1010
  _globals['_MONITOREDRESOURCEDESCRIPTORCHANGE_REMOVED']._serialized_end=1053
# @@protoc_insertion_point(module_scope)
