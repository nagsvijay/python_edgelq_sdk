# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/proxies/proto/v1alpha2/broker_service.proto
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
    'edgelq-sdk/proxies/proto/v1alpha2/broker_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.proxies.proto.v1alpha2 import broker_custom_pb2 as edgelq__sdk_dot_proxies_dot_proto_dot_v1alpha2_dot_broker__custom__pb2
from edgelq_sdk.proxies.proto.v1alpha2 import project_pb2 as edgelq__sdk_dot_proxies_dot_proto_dot_v1alpha2_dot_project__pb2
from edgelq_sdk.proxies.proto.v1alpha2 import project_change_pb2 as edgelq__sdk_dot_proxies_dot_proto_dot_v1alpha2_dot_project__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6edgelq-sdk/proxies/proto/v1alpha2/broker_service.proto\x12\x14ntt.proxies.v1alpha2\x1a\x35\x65\x64gelq-sdk/proxies/proto/v1alpha2/broker_custom.proto\x1a/edgelq-sdk/proxies/proto/v1alpha2/project.proto\x1a\x36\x65\x64gelq-sdk/proxies/proto/v1alpha2/project_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto2\x9d\x03\n\rBrokerService\x12u\n\x07\x43onnect\x12$.ntt.proxies.v1alpha2.ConnectRequest\x1a%.ntt.proxies.v1alpha2.ConnectResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/v1alpha2:connect(\x01\x30\x01\x12q\n\x06Listen\x12#.ntt.proxies.v1alpha2.ListenRequest\x1a$.ntt.proxies.v1alpha2.ListenResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/v1alpha2:listen(\x01\x30\x01\x12q\n\x06\x41\x63\x63\x65pt\x12#.ntt.proxies.v1alpha2.AcceptRequest\x1a$.ntt.proxies.v1alpha2.AcceptResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/v1alpha2:accept(\x01\x30\x01\x1a/\xca\x41\x12proxies.edgelq.com\xd2\x41\x17https://apis.edgelq.comB\x80\x01\n\x1b\x63om.ntt.proxies.pb.v1alpha2B\x12\x42rokerServiceProtoP\x00ZKgithub.com/cloudwan/edgelq-sdk/proxies/client/v1alpha2/broker;broker_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.proxies.proto.v1alpha2.broker_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.proxies.pb.v1alpha2B\022BrokerServiceProtoP\000ZKgithub.com/cloudwan/edgelq-sdk/proxies/client/v1alpha2/broker;broker_client'
  _globals['_BROKERSERVICE']._loaded_options = None
  _globals['_BROKERSERVICE']._serialized_options = b'\312A\022proxies.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_BROKERSERVICE'].methods_by_name['Connect']._loaded_options = None
  _globals['_BROKERSERVICE'].methods_by_name['Connect']._serialized_options = b'\202\323\344\223\002\023\"\021/v1alpha2:connect'
  _globals['_BROKERSERVICE'].methods_by_name['Listen']._loaded_options = None
  _globals['_BROKERSERVICE'].methods_by_name['Listen']._serialized_options = b'\202\323\344\223\002\022\"\020/v1alpha2:listen'
  _globals['_BROKERSERVICE'].methods_by_name['Accept']._loaded_options = None
  _globals['_BROKERSERVICE'].methods_by_name['Accept']._serialized_options = b'\202\323\344\223\002\022\"\020/v1alpha2:accept'
  _globals['_BROKERSERVICE']._serialized_start=454
  _globals['_BROKERSERVICE']._serialized_end=867
# @@protoc_insertion_point(module_scope)
