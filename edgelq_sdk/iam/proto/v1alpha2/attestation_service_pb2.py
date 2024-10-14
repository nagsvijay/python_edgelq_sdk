# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/attestation_service.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/attestation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import attestation_custom_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_attestation__custom__pb2
from edgelq_sdk.iam.proto.v1alpha2 import attestation_domain_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_attestation__domain__pb2
from edgelq_sdk.iam.proto.v1alpha2 import attestation_domain_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_attestation__domain__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7edgelq-sdk/iam/proto/v1alpha2/attestation_service.proto\x12\x10ntt.iam.v1alpha2\x1a\x36\x65\x64gelq-sdk/iam/proto/v1alpha2/attestation_custom.proto\x1a\x36\x65\x64gelq-sdk/iam/proto/v1alpha2/attestation_domain.proto\x1a=edgelq-sdk/iam/proto/v1alpha2/attestation_domain_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto2\xf4\x01\n\x12\x41ttestationService\x12\xb0\x01\n\x06Verify\x12\x1f.ntt.iam.v1alpha2.VerifyRequest\x1a .ntt.iam.v1alpha2.VerifyResponse\"_\x82\xd3\xe4\x93\x02Y\"W/v1alpha2/{ask_for_challenge.attestation_domain=projects/*/attestationDomains/*}:verify(\x01\x30\x01\x1a+\xca\x41\x0eiam.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x87\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x17\x41ttestationServiceProtoP\x00ZQgithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/attestation;attestation_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.attestation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\027AttestationServiceProtoP\000ZQgithub.com/cloudwan/edgelq-sdk/iam/client/v1alpha2/attestation;attestation_client'
  _globals['_ATTESTATIONSERVICE']._loaded_options = None
  _globals['_ATTESTATIONSERVICE']._serialized_options = b'\312A\016iam.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_ATTESTATIONSERVICE'].methods_by_name['Verify']._loaded_options = None
  _globals['_ATTESTATIONSERVICE'].methods_by_name['Verify']._serialized_options = b'\202\323\344\223\002Y\"W/v1alpha2/{ask_for_challenge.attestation_domain=projects/*/attestationDomains/*}:verify'
  _globals['_ATTESTATIONSERVICE']._serialized_start=466
  _globals['_ATTESTATIONSERVICE']._serialized_end=710
# @@protoc_insertion_point(module_scope)