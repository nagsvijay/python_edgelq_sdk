# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/applications/proto/v1alpha2/distribution_change.proto
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
    'edgelq-sdk/applications/proto/v1alpha2/distribution_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.applications.proto.v1alpha2 import distribution_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_distribution__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@edgelq-sdk/applications/proto/v1alpha2/distribution_change.proto\x12\x19ntt.applications.v1alpha2\x1a\x39\x65\x64gelq-sdk/applications/proto/v1alpha2/distribution.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\xd7\x05\n\x12\x44istributionChange\x12\x44\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\x33.ntt.applications.v1alpha2.DistributionChange.AddedH\x00\x12J\n\x08modified\x18\x02 \x01(\x0b\x32\x36.ntt.applications.v1alpha2.DistributionChange.ModifiedH\x00\x12H\n\x07\x63urrent\x18\x04 \x01(\x0b\x32\x35.ntt.applications.v1alpha2.DistributionChange.CurrentH\x00\x12H\n\x07removed\x18\x03 \x01(\x0b\x32\x35.ntt.applications.v1alpha2.DistributionChange.RemovedH\x00\x1aZ\n\x05\x41\x64\x64\x65\x64\x12=\n\x0c\x64istribution\x18\x01 \x01(\x0b\x32\'.ntt.applications.v1alpha2.Distribution\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xb8\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x0c\x64istribution\x18\x02 \x01(\x0b\x32\'.ntt.applications.v1alpha2.Distribution\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1aH\n\x07\x43urrent\x12=\n\x0c\x64istribution\x18\x01 \x01(\x0b\x32\'.ntt.applications.v1alpha2.Distribution\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x97\x01\n com.ntt.applications.pb.v1alpha2B\x17\x44istributionChangeProtoP\x00ZXgithub.com/cloudwan/edgelq-sdk/applications/resources/v1alpha2/distribution;distributionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.applications.proto.v1alpha2.distribution_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.ntt.applications.pb.v1alpha2B\027DistributionChangeProtoP\000ZXgithub.com/cloudwan/edgelq-sdk/applications/resources/v1alpha2/distribution;distribution'
  _globals['_DISTRIBUTIONCHANGE']._serialized_start=216
  _globals['_DISTRIBUTIONCHANGE']._serialized_end=943
  _globals['_DISTRIBUTIONCHANGE_ADDED']._serialized_start=532
  _globals['_DISTRIBUTIONCHANGE_ADDED']._serialized_end=622
  _globals['_DISTRIBUTIONCHANGE_MODIFIED']._serialized_start=625
  _globals['_DISTRIBUTIONCHANGE_MODIFIED']._serialized_end=809
  _globals['_DISTRIBUTIONCHANGE_CURRENT']._serialized_start=811
  _globals['_DISTRIBUTIONCHANGE_CURRENT']._serialized_end=883
  _globals['_DISTRIBUTIONCHANGE_REMOVED']._serialized_start=885
  _globals['_DISTRIBUTIONCHANGE_REMOVED']._serialized_end=928
# @@protoc_insertion_point(module_scope)