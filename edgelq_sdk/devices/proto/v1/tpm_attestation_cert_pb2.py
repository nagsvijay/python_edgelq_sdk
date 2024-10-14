# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/devices/proto/v1/tpm_attestation_cert.proto
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
    'edgelq-sdk/devices/proto/v1/tpm_attestation_cert.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/devices/proto/v1/tpm_attestation_cert.proto\x12\x0entt.devices.v1\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\x82\x03\n\x12TpmAttestationCert\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x02 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12 \n\x18tpm_manufacturer_ca_cert\x18\x06 \x01(\t\x12\x1d\n\x15idevid_issuer_ca_cert\x18\x07 \x01(\t\x12\x1d\n\x15ldevid_issuer_ca_cert\x18\x08 \x01(\t:\x96\x01\xea\x41\x92\x01\n%devices.edgelq.com/TpmAttestationCert\x12*tpmAttestationCerts/{tpm_attestation_cert}\x12=projects/{project}/tpmAttestationCerts/{tpm_attestation_cert}B\x91\x01\n\x15\x63om.ntt.devices.pb.v1B\x17TpmAttestationCertProtoP\x01Z]github.com/cloudwan/edgelq-sdk/devices/resources/v1/tpm_attestation_cert;tpm_attestation_certb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.devices.proto.v1.tpm_attestation_cert_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ntt.devices.pb.v1B\027TpmAttestationCertProtoP\001Z]github.com/cloudwan/edgelq-sdk/devices/resources/v1/tpm_attestation_cert;tpm_attestation_cert'
  _globals['_TPMATTESTATIONCERT']._loaded_options = None
  _globals['_TPMATTESTATIONCERT']._serialized_options = b'\352A\222\001\n%devices.edgelq.com/TpmAttestationCert\022*tpmAttestationCerts/{tpm_attestation_cert}\022=projects/{project}/tpmAttestationCerts/{tpm_attestation_cert}'
  _globals['_TPMATTESTATIONCERT']._serialized_start=130
  _globals['_TPMATTESTATIONCERT']._serialized_end=516
# @@protoc_insertion_point(module_scope)
