# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/applications/proto/v1/applications.proto
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
    'edgelq-sdk/applications/proto/v1/applications.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.applications.proto.v1 import config_map_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_config__map__pb2
from edgelq_sdk.applications.proto.v1 import config_map_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_config__map__service__pb2
from edgelq_sdk.applications.proto.v1 import distribution_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2
from edgelq_sdk.applications.proto.v1 import distribution_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2
from edgelq_sdk.applications.proto.v1 import pod_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2
from edgelq_sdk.applications.proto.v1 import pod_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2
from edgelq_sdk.applications.proto.v1 import project_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_project__pb2
from edgelq_sdk.applications.proto.v1 import project_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_project__service__pb2
from edgelq_sdk.devices.proto.v1 import devices_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_devices__pb2
from edgelq_sdk.secrets.proto.v1 import secrets_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secrets__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3edgelq-sdk/applications/proto/v1/applications.proto\x12\x13ntt.applications.v1\x1a\x31\x65\x64gelq-sdk/applications/proto/v1/config_map.proto\x1a\x39\x65\x64gelq-sdk/applications/proto/v1/config_map_service.proto\x1a\x33\x65\x64gelq-sdk/applications/proto/v1/distribution.proto\x1a;edgelq-sdk/applications/proto/v1/distribution_service.proto\x1a*edgelq-sdk/applications/proto/v1/pod.proto\x1a\x32\x65\x64gelq-sdk/applications/proto/v1/pod_service.proto\x1a.edgelq-sdk/applications/proto/v1/project.proto\x1a\x36\x65\x64gelq-sdk/applications/proto/v1/project_service.proto\x1a)edgelq-sdk/devices/proto/v1/devices.proto\x1a)edgelq-sdk/secrets/proto/v1/secrets.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.protoB\x89\x01\n\x1a\x63om.ntt.applications.pb.v1B\x11\x41pplicationsProtoP\x01ZVgithub.com/cloudwan/edgelq-sdk/applications/client/v1/applications;applications_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.applications.proto.v1.applications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ntt.applications.pb.v1B\021ApplicationsProtoP\001ZVgithub.com/cloudwan/edgelq-sdk/applications/client/v1/applications;applications_client'
# @@protoc_insertion_point(module_scope)
