# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1alpha2/attestation_domain.proto
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
    'edgelq-sdk/iam/proto/v1alpha2/attestation_domain.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/iam/proto/v1alpha2/attestation_domain.proto\x12\x10ntt.iam.v1alpha2\x1a*edgelq-sdk/iam/proto/v1alpha2/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xca\x04\n\x11\x41ttestationDomain\x12#\n\x08metadata\x18\x01 \x01(\x0b\x32\x11.goten.types.Meta\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x36\n.insecure_skip_manufacturer_ekcert_verification\x18\x04 \x01(\x08\x12<\n\x08policies\x18\x05 \x03(\x0b\x32*.ntt.iam.v1alpha2.AttestationDomain.Policy\x12H\n\x0f\x65nrollment_list\x18\x06 \x03(\x0b\x32/.ntt.iam.v1alpha2.AttestationDomain.EnrolledKey\x1a\x94\x01\n\x06Policy\x12&\n\x1emanufacturer_root_ca_certs_pem\x18\x01 \x01(\t\x12\x1a\n\x12require_enrollment\x18\x02 \x01(\x08\x12\x18\n\x10verify_event_log\x18\x03 \x01(\x08\x12,\n\rexpected_pcrs\x18\x04 \x03(\x0b\x32\x15.ntt.iam.v1alpha2.PCR\x1a\x32\n\x0b\x45nrolledKey\x12\x12\n\npubkey_pem\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t:a\xea\x41^\n iam.edgelq.com/AttestationDomain\x12:projects/{project}/attestationDomains/{attestation_domain}B\x90\x01\n\x17\x63om.ntt.iam.pb.v1alpha2B\x16\x41ttestationDomainProtoP\x01Z[github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/attestation_domain;attestation_domainb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1alpha2.attestation_domain_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ntt.iam.pb.v1alpha2B\026AttestationDomainProtoP\001Z[github.com/cloudwan/edgelq-sdk/iam/resources/v1alpha2/attestation_domain;attestation_domain'
  _globals['_ATTESTATIONDOMAIN']._loaded_options = None
  _globals['_ATTESTATIONDOMAIN']._serialized_options = b'\352A^\n iam.edgelq.com/AttestationDomain\022:projects/{project}/attestationDomains/{attestation_domain}'
  _globals['_ATTESTATIONDOMAIN']._serialized_start=176
  _globals['_ATTESTATIONDOMAIN']._serialized_end=762
  _globals['_ATTESTATIONDOMAIN_POLICY']._serialized_start=463
  _globals['_ATTESTATIONDOMAIN_POLICY']._serialized_end=611
  _globals['_ATTESTATIONDOMAIN_ENROLLEDKEY']._serialized_start=613
  _globals['_ATTESTATIONDOMAIN_ENROLLEDKEY']._serialized_end=663
# @@protoc_insertion_point(module_scope)
