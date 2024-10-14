# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/attestation_domain.proto
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
    'edgelq-sdk/iam/proto/v1/attestation_domain.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_common__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0edgelq-sdk/iam/proto/v1/attestation_domain.proto\x12\nntt.iam.v1\x1a$edgelq-sdk/iam/proto/v1/common.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xb8\x04\n\x11\x41ttestationDomain\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x08metadata\x18\x01 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x36\n.insecure_skip_manufacturer_ekcert_verification\x18\x04 \x01(\x08\x12\x36\n\x08policies\x18\x05 \x03(\x0b\x32$.ntt.iam.v1.AttestationDomain.Policy\x12\x42\n\x0f\x65nrollment_list\x18\x06 \x03(\x0b\x32).ntt.iam.v1.AttestationDomain.EnrolledKey\x1a\x8e\x01\n\x06Policy\x12&\n\x1emanufacturer_root_ca_certs_pem\x18\x01 \x01(\t\x12\x1a\n\x12require_enrollment\x18\x02 \x01(\x08\x12\x18\n\x10verify_event_log\x18\x03 \x01(\x08\x12&\n\rexpected_pcrs\x18\x04 \x03(\x0b\x32\x0f.ntt.iam.v1.PCR\x1a\x32\n\x0b\x45nrolledKey\x12\x12\n\npubkey_pem\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t:a\xea\x41^\n iam.edgelq.com/AttestationDomain\x12:projects/{project}/attestationDomains/{attestation_domain}B\x84\x01\n\x11\x63om.ntt.iam.pb.v1B\x16\x41ttestationDomainProtoP\x01ZUgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/attestation_domain;attestation_domainb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.attestation_domain_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\026AttestationDomainProtoP\001ZUgithub.com/cloudwan/edgelq-sdk/iam/resources/v1/attestation_domain;attestation_domain'
  _globals['_ATTESTATIONDOMAIN']._loaded_options = None
  _globals['_ATTESTATIONDOMAIN']._serialized_options = b'\352A^\n iam.edgelq.com/AttestationDomain\022:projects/{project}/attestationDomains/{attestation_domain}'
  _globals['_ATTESTATIONDOMAIN']._serialized_start=158
  _globals['_ATTESTATIONDOMAIN']._serialized_end=726
  _globals['_ATTESTATIONDOMAIN_POLICY']._serialized_start=433
  _globals['_ATTESTATIONDOMAIN_POLICY']._serialized_end=575
  _globals['_ATTESTATIONDOMAIN_ENROLLEDKEY']._serialized_start=577
  _globals['_ATTESTATIONDOMAIN_ENROLLEDKEY']._serialized_end=627
# @@protoc_insertion_point(module_scope)