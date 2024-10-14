# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/attestation_custom.proto
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
    'edgelq-sdk/iam/proto/v1/attestation_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import attestation_domain_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_attestation__domain__pb2
from edgelq_sdk.iam.proto.v1 import attestation_domain_change_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_attestation__domain__change__pb2
from edgelq_sdk.iam.proto.v1 import common_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0edgelq-sdk/iam/proto/v1/attestation_custom.proto\x12\nntt.iam.v1\x1a\x30\x65\x64gelq-sdk/iam/proto/v1/attestation_domain.proto\x1a\x37\x65\x64gelq-sdk/iam/proto/v1/attestation_domain_change.proto\x1a$edgelq-sdk/iam/proto/v1/common.proto\"\x90\x06\n\rVerifyRequest\x12\x46\n\x11\x61sk_for_challenge\x18\x01 \x01(\x0b\x32).ntt.iam.v1.VerifyRequest.AskForChallengeH\x00\x12I\n\x12\x63hallenge_response\x18\x02 \x01(\x0b\x32+.ntt.iam.v1.VerifyRequest.ChallengeResponseH\x00\x1a\x87\x03\n\x0f\x41skForChallenge\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x1a\n\x12\x61ttestation_domain\x18\x02 \x01(\t\x12+\n\x0btpm_version\x18\x03 \x01(\x0e\x32\x16.ntt.iam.v1.TpmVersion\x12\r\n\x05\x65kpub\x18\x04 \x01(\x0c\x12\x0e\n\x06\x65kcert\x18\x05 \x01(\x0c\x12\x11\n\tekcerturl\x18\x06 \x01(\t\x12\r\n\x05\x61kpub\x18\x07 \x01(\x0c\x12\x15\n\rcreation_data\x18\x08 \x01(\x0c\x12\x0e\n\x06\x61ttest\x18\t \x01(\x0c\x12\x11\n\tsignature\x18\n \x01(\x0c\x12S\n\x10\x63hallenge_format\x18\x0b \x01(\x0e\x32\x39.ntt.iam.v1.VerifyRequest.AskForChallenge.ChallengeFormat\"J\n\x0f\x43hallengeFormat\x12\x14\n\x10TPM20_CREDENTIAL\x10\x00\x12\x10\n\x0cTPM12_EKBLOB\x10\x01\x12\x0f\n\x0bTSPI_EKBLOB\x10\x02\x1a\xda\x01\n\x11\x43hallengeResponse\x12&\n\x1e\x61k_activation_decrypted_secret\x18\x01 \x01(\x0c\x12\x41\n\x06quotes\x18\x02 \x03(\x0b\x32\x31.ntt.iam.v1.VerifyRequest.ChallengeResponse.Quote\x12\x1d\n\x04pcrs\x18\x03 \x03(\x0b\x32\x0f.ntt.iam.v1.PCR\x12\x10\n\x08\x65ventlog\x18\x04 \x01(\x0c\x1a)\n\x05Quote\x12\r\n\x05quote\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42\x05\n\x03msg\"\xce\x02\n\x0eVerifyResponse\x12\x39\n\tchallenge\x18\x01 \x01(\x0b\x32$.ntt.iam.v1.VerifyResponse.ChallengeH\x00\x12R\n\x16\x61ttestation_successful\x18\x02 \x01(\x0b\x32\x30.ntt.iam.v1.VerifyResponse.AttestationSuccessfulH\x00\x1ar\n\tChallenge\x12\"\n\x1aplatform_attestation_nonce\x18\x01 \x01(\x0c\x12\x1f\n\x17\x63red_encrypted_by_ekpub\x18\x02 \x01(\x0c\x12 \n\x18secret_encrypted_by_cred\x18\x03 \x01(\x0c\x1a\x32\n\x15\x41ttestationSuccessful\x12\x19\n\x11\x61ttestation_token\x18\x01 \x01(\tB\x05\n\x03msgBz\n\x11\x63om.ntt.iam.pb.v1B\x16\x41ttestationCustomProtoP\x00ZKgithub.com/cloudwan/edgelq-sdk/iam/client/v1/attestation;attestation_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.attestation_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\026AttestationCustomProtoP\000ZKgithub.com/cloudwan/edgelq-sdk/iam/client/v1/attestation;attestation_client'
  _globals['_VERIFYREQUEST']._serialized_start=210
  _globals['_VERIFYREQUEST']._serialized_end=994
  _globals['_VERIFYREQUEST_ASKFORCHALLENGE']._serialized_start=375
  _globals['_VERIFYREQUEST_ASKFORCHALLENGE']._serialized_end=766
  _globals['_VERIFYREQUEST_ASKFORCHALLENGE_CHALLENGEFORMAT']._serialized_start=692
  _globals['_VERIFYREQUEST_ASKFORCHALLENGE_CHALLENGEFORMAT']._serialized_end=766
  _globals['_VERIFYREQUEST_CHALLENGERESPONSE']._serialized_start=769
  _globals['_VERIFYREQUEST_CHALLENGERESPONSE']._serialized_end=987
  _globals['_VERIFYREQUEST_CHALLENGERESPONSE_QUOTE']._serialized_start=946
  _globals['_VERIFYREQUEST_CHALLENGERESPONSE_QUOTE']._serialized_end=987
  _globals['_VERIFYRESPONSE']._serialized_start=997
  _globals['_VERIFYRESPONSE']._serialized_end=1331
  _globals['_VERIFYRESPONSE_CHALLENGE']._serialized_start=1158
  _globals['_VERIFYRESPONSE_CHALLENGE']._serialized_end=1272
  _globals['_VERIFYRESPONSE_ATTESTATIONSUCCESSFUL']._serialized_start=1274
  _globals['_VERIFYRESPONSE_ATTESTATIONSUCCESSFUL']._serialized_end=1324
# @@protoc_insertion_point(module_scope)