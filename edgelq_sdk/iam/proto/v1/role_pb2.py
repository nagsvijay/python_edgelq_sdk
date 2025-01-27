# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/iam/proto/v1/role.proto
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
    'edgelq-sdk/iam/proto/v1/role.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.iam.proto.v1 import condition_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_condition__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from goten_sdk.types import meta_pb2 as goten__sdk_dot_types_dot_meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"edgelq-sdk/iam/proto/v1/role.proto\x12\nntt.iam.v1\x1a\'edgelq-sdk/iam/proto/v1/condition.proto\x1a\x19google/api/resource.proto\x1a\x1agoten-sdk/types/meta.proto\"\xe2\x07\n\x04Role\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08metadata\x18\x04 \x01(\x0b\x32\x11.goten.types.Meta\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12+\n\x08\x63\x61tegory\x18\n \x01(\x0e\x32\x19.ntt.iam.v1.Role.Category\x12\x35\n\x0cscope_params\x18\x03 \x03(\x0b\x32\x1f.ntt.iam.v1.Role.ScopeParamType\x12&\n\x06grants\x18\x05 \x03(\x0b\x32\x16.ntt.iam.v1.Role.Grant\x12\x15\n\rowned_objects\x18\x06 \x03(\t\x12\x10\n\x08services\x18\x07 \x03(\t\x12\x1a\n\x12rb_spec_generation\x18\x08 \x01(\x03\x1a\x8b\x01\n\x0eScopeParamType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x04type\x18\x02 \x01(\x0e\x32$.ntt.iam.v1.Role.ScopeParamType.Type\"7\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x14\n\x10\x41RRAY_OF_STRINGS\x10\x02\x1a\xb1\x02\n\x05Grant\x12\x11\n\tsub_scope\x18\x01 \x01(\t\x12\x13\n\x0bpermissions\x18\x02 \x03(\t\x12H\n\x19resource_field_conditions\x18\x03 \x03(\x0b\x32%.ntt.iam.v1.Role.Grant.FieldCondition\x12G\n\x18request_field_conditions\x18\x04 \x03(\x0b\x32%.ntt.iam.v1.Role.Grant.FieldCondition\x12>\n\x15\x65xecutable_conditions\x18\x05 \x03(\x0b\x32\x1f.ntt.iam.v1.ExecutableCondition\x1a-\n\x0e\x46ieldCondition\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"`\n\x08\x43\x61tegory\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0c\n\x08INTERNAL\x10\x02\x12\t\n\x05OWNER\x10\x03\x12\x0b\n\x07SERVICE\x10\x04\x12\t\n\x05\x41GENT\x10\x05\x12\x08\n\x04USER\x10\x06:\x86\x01\xea\x41\x82\x01\n\x13iam.edgelq.com/Role\x12\x1fservices/{service}/roles/{role}\x12\x1fprojects/{project}/roles/{role}\x12)organizations/{organization}/roles/{role}\"\x9b\x03\n\nScopeParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x06string\x18\x02 \x01(\x0b\x32\".ntt.iam.v1.ScopeParam.StringValueH\x00\x12=\n\x07strings\x18\x03 \x01(\x0b\x32*.ntt.iam.v1.ScopeParam.ArrayOfStringsValueH\x00\x12\x36\n\nvalue_from\x18\x04 \x01(\x0b\x32 .ntt.iam.v1.ScopeParam.FromValueH\x00\x1a\x1c\n\x0bStringValue\x12\r\n\x05value\x18\x01 \x01(\t\x1a%\n\x13\x41rrayOfStringsValue\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a\x83\x01\n\tFromValue\x12\x37\n\x06source\x18\x01 \x01(\x0e\x32\'.ntt.iam.v1.ScopeParam.FromValue.Source\x12\x0c\n\x04path\x18\x02 \x01(\t\"/\n\x06Source\x12\r\n\tUNDEFINED\x10\x00\x12\x16\n\x12PRINCIPAL_METADATA\x10\x01\x42\x07\n\x05valueB[\n\x11\x63om.ntt.iam.pb.v1B\tRoleProtoP\x01Z9github.com/cloudwan/edgelq-sdk/iam/resources/v1/role;roleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.iam.proto.v1.role_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.ntt.iam.pb.v1B\tRoleProtoP\001Z9github.com/cloudwan/edgelq-sdk/iam/resources/v1/role;role'
  _globals['_ROLE']._loaded_options = None
  _globals['_ROLE']._serialized_options = b'\352A\202\001\n\023iam.edgelq.com/Role\022\037services/{service}/roles/{role}\022\037projects/{project}/roles/{role}\022)organizations/{organization}/roles/{role}'
  _globals['_ROLE']._serialized_start=147
  _globals['_ROLE']._serialized_end=1141
  _globals['_ROLE_SCOPEPARAMTYPE']._serialized_start=459
  _globals['_ROLE_SCOPEPARAMTYPE']._serialized_end=598
  _globals['_ROLE_SCOPEPARAMTYPE_TYPE']._serialized_start=543
  _globals['_ROLE_SCOPEPARAMTYPE_TYPE']._serialized_end=598
  _globals['_ROLE_GRANT']._serialized_start=601
  _globals['_ROLE_GRANT']._serialized_end=906
  _globals['_ROLE_GRANT_FIELDCONDITION']._serialized_start=861
  _globals['_ROLE_GRANT_FIELDCONDITION']._serialized_end=906
  _globals['_ROLE_CATEGORY']._serialized_start=908
  _globals['_ROLE_CATEGORY']._serialized_end=1004
  _globals['_SCOPEPARAM']._serialized_start=1144
  _globals['_SCOPEPARAM']._serialized_end=1555
  _globals['_SCOPEPARAM_STRINGVALUE']._serialized_start=1345
  _globals['_SCOPEPARAM_STRINGVALUE']._serialized_end=1373
  _globals['_SCOPEPARAM_ARRAYOFSTRINGSVALUE']._serialized_start=1375
  _globals['_SCOPEPARAM_ARRAYOFSTRINGSVALUE']._serialized_end=1412
  _globals['_SCOPEPARAM_FROMVALUE']._serialized_start=1415
  _globals['_SCOPEPARAM_FROMVALUE']._serialized_end=1546
  _globals['_SCOPEPARAM_FROMVALUE_SOURCE']._serialized_start=1499
  _globals['_SCOPEPARAM_FROMVALUE_SOURCE']._serialized_end=1546
# @@protoc_insertion_point(module_scope)
