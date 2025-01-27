# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/proxies/proto/v1alpha2/broker_custom.proto
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
    'edgelq-sdk/proxies/proto/v1alpha2/broker_custom.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.proxies.proto.v1alpha2 import project_pb2 as edgelq__sdk_dot_proxies_dot_proto_dot_v1alpha2_dot_project__pb2
from edgelq_sdk.proxies.proto.v1alpha2 import project_change_pb2 as edgelq__sdk_dot_proxies_dot_proto_dot_v1alpha2_dot_project__change__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5edgelq-sdk/proxies/proto/v1alpha2/broker_custom.proto\x12\x14ntt.proxies.v1alpha2\x1a/edgelq-sdk/proxies/proto/v1alpha2/project.proto\x1a\x36\x65\x64gelq-sdk/proxies/proto/v1alpha2/project_change.proto\"\xa3\x05\n\x0e\x43onnectRequest\x12H\n\x0copen_request\x18\x01 \x01(\x0b\x32\x30.ntt.proxies.v1alpha2.ConnectRequest.OpenRequestH\x00\x12L\n\x0eresume_request\x18\x02 \x01(\x0b\x32\x32.ntt.proxies.v1alpha2.ConnectRequest.ResumeRequestH\x00\x12(\n\x03\x61\x63k\x18\x03 \x01(\x0b\x32\x19.ntt.proxies.v1alpha2.AckH\x00\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.DataH\x00\x12,\n\x05\x63lose\x18\x05 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.CloseH\x00\x12,\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.ErrorH\x00\x12*\n\x04ping\x18\x07 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PingH\x00\x1at\n\x0bOpenRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rprovider_name\x18\x03 \x01(\t\x12\x0f\n\x07service\x18\x04 \x01(\t\x12\x0b\n\x03\x61rg\x18\x05 \x01(\x0c\x1a\x99\x01\n\rResumeRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rprovider_name\x18\x03 \x01(\t\x12\x12\n\nsession_id\x18\x04 \x01(\x04\x12\x12\n\nchannel_id\x18\x05 \x01(\x04\x12\x17\n\x0flast_message_id\x18\x06 \x01(\x04\x42\t\n\x07message\"\xb2\x05\n\x0f\x43onnectResponse\x12K\n\ropen_response\x18\x01 \x01(\x0b\x32\x32.ntt.proxies.v1alpha2.ConnectResponse.OpenResponseH\x00\x12O\n\x0fresume_response\x18\x02 \x01(\x0b\x32\x34.ntt.proxies.v1alpha2.ConnectResponse.ResumeResponseH\x00\x12T\n\x12\x63hannel_open_error\x18\x03 \x01(\x0b\x32\x36.ntt.proxies.v1alpha2.ConnectResponse.ChannelOpenErrorH\x00\x12(\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\x19.ntt.proxies.v1alpha2.AckH\x00\x12*\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.DataH\x00\x12,\n\x05\x63lose\x18\x06 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.CloseH\x00\x12,\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.ErrorH\x00\x12*\n\x04pong\x18\x08 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PongH\x00\x1a\x36\n\x0cOpenResponse\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x12\n\nchannel_id\x18\x02 \x01(\x04\x1aQ\n\x0eResumeResponse\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x12\n\nchannel_id\x18\x02 \x01(\x04\x12\x17\n\x0flast_message_id\x18\x04 \x01(\x04\x1a\x37\n\x10\x43hannelOpenError\x12\x12\n\nchannel_id\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\tB\t\n\x07message\"\x81\x04\n\rListenRequest\x12G\n\x0copen_request\x18\x01 \x01(\x0b\x32/.ntt.proxies.v1alpha2.ListenRequest.OpenRequestH\x00\x12K\n\x0eresume_request\x18\x02 \x01(\x0b\x32\x31.ntt.proxies.v1alpha2.ListenRequest.ResumeRequestH\x00\x12R\n\x12\x63hannel_open_error\x18\x03 \x01(\x0b\x32\x34.ntt.proxies.v1alpha2.ListenRequest.ChannelOpenErrorH\x00\x12*\n\x04ping\x18\x04 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PingH\x00\x1a?\n\x0bOpenRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1aU\n\rResumeRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\x04\x1a\x37\n\x10\x43hannelOpenError\x12\x12\n\nchannel_id\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\tB\t\n\x07message\"\x94\x04\n\x0eListenResponse\x12\x43\n\tlistening\x18\x01 \x01(\x0b\x32..ntt.proxies.v1alpha2.ListenResponse.ListeningH\x00\x12Y\n\x15open_channel_response\x18\x02 \x01(\x0b\x32\x38.ntt.proxies.v1alpha2.ListenResponse.OpenChannelResponseH\x00\x12]\n\x17resume_channel_response\x18\x03 \x01(\x0b\x32:.ntt.proxies.v1alpha2.ListenResponse.ResumeChannelResponseH\x00\x12*\n\x04pong\x18\x04 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PongH\x00\x1a\x1f\n\tListening\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x1aG\n\x13OpenChannelResponse\x12\x12\n\nchannel_id\x18\x01 \x01(\x04\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0b\n\x03\x61rg\x18\x03 \x01(\x0c\x1a\x62\n\x15ResumeChannelResponse\x12\x12\n\nchannel_id\x18\x01 \x01(\x04\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0b\n\x03\x61rg\x18\x03 \x01(\x0c\x12\x17\n\x0flast_message_id\x18\x04 \x01(\x04\x42\t\n\x07message\"\xfc\x04\n\rAcceptRequest\x12G\n\x0copen_request\x18\x01 \x01(\x0b\x32/.ntt.proxies.v1alpha2.AcceptRequest.OpenRequestH\x00\x12K\n\x0eresume_request\x18\x02 \x01(\x0b\x32\x31.ntt.proxies.v1alpha2.AcceptRequest.ResumeRequestH\x00\x12*\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.DataH\x00\x12(\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\x19.ntt.proxies.v1alpha2.AckH\x00\x12,\n\x05\x63lose\x18\x05 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.CloseH\x00\x12,\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.ErrorH\x00\x12*\n\x04ping\x18\x07 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PingH\x00\x1ag\n\x0bOpenRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\x04\x12\x12\n\nchannel_id\x18\x04 \x01(\x04\x1a\x82\x01\n\rResumeRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\x04\x12\x12\n\nchannel_id\x18\x04 \x01(\x04\x12\x17\n\x0flast_message_id\x18\x05 \x01(\x04\x42\t\n\x07message\"\xf9\x01\n\x0e\x41\x63\x63\x65ptResponse\x12*\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.DataH\x00\x12(\n\x03\x61\x63k\x18\x02 \x01(\x0b\x32\x19.ntt.proxies.v1alpha2.AckH\x00\x12,\n\x05\x63lose\x18\x03 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.CloseH\x00\x12,\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1b.ntt.proxies.v1alpha2.ErrorH\x00\x12*\n\x04pong\x18\x05 \x01(\x0b\x32\x1a.ntt.proxies.v1alpha2.PongH\x00\x42\t\n\x07message\"\x06\n\x04Ping\"\x06\n\x04Pong\"7\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05\x62ytes\x18\x02 \x01(\x0c\x12\x14\n\x0c\x61\x63k_required\x18\x03 \x01(\x08\"\x11\n\x03\x41\x63k\x12\n\n\x02id\x18\x01 \x01(\x04\"\x13\n\x05\x43lose\x12\n\n\x02id\x18\x01 \x01(\x04\"$\n\x05\x45rror\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\tB\x7f\n\x1b\x63om.ntt.proxies.pb.v1alpha2B\x11\x42rokerCustomProtoP\x00ZKgithub.com/cloudwan/edgelq-sdk/proxies/client/v1alpha2/broker;broker_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.proxies.proto.v1alpha2.broker_custom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.ntt.proxies.pb.v1alpha2B\021BrokerCustomProtoP\000ZKgithub.com/cloudwan/edgelq-sdk/proxies/client/v1alpha2/broker;broker_client'
  _globals['_CONNECTREQUEST']._serialized_start=185
  _globals['_CONNECTREQUEST']._serialized_end=860
  _globals['_CONNECTREQUEST_OPENREQUEST']._serialized_start=577
  _globals['_CONNECTREQUEST_OPENREQUEST']._serialized_end=693
  _globals['_CONNECTREQUEST_RESUMEREQUEST']._serialized_start=696
  _globals['_CONNECTREQUEST_RESUMEREQUEST']._serialized_end=849
  _globals['_CONNECTRESPONSE']._serialized_start=863
  _globals['_CONNECTRESPONSE']._serialized_end=1553
  _globals['_CONNECTRESPONSE_OPENRESPONSE']._serialized_start=1348
  _globals['_CONNECTRESPONSE_OPENRESPONSE']._serialized_end=1402
  _globals['_CONNECTRESPONSE_RESUMERESPONSE']._serialized_start=1404
  _globals['_CONNECTRESPONSE_RESUMERESPONSE']._serialized_end=1485
  _globals['_CONNECTRESPONSE_CHANNELOPENERROR']._serialized_start=1487
  _globals['_CONNECTRESPONSE_CHANNELOPENERROR']._serialized_end=1542
  _globals['_LISTENREQUEST']._serialized_start=1556
  _globals['_LISTENREQUEST']._serialized_end=2069
  _globals['_LISTENREQUEST_OPENREQUEST']._serialized_start=1851
  _globals['_LISTENREQUEST_OPENREQUEST']._serialized_end=1914
  _globals['_LISTENREQUEST_RESUMEREQUEST']._serialized_start=1916
  _globals['_LISTENREQUEST_RESUMEREQUEST']._serialized_end=2001
  _globals['_LISTENREQUEST_CHANNELOPENERROR']._serialized_start=1487
  _globals['_LISTENREQUEST_CHANNELOPENERROR']._serialized_end=1542
  _globals['_LISTENRESPONSE']._serialized_start=2072
  _globals['_LISTENRESPONSE']._serialized_end=2604
  _globals['_LISTENRESPONSE_LISTENING']._serialized_start=2389
  _globals['_LISTENRESPONSE_LISTENING']._serialized_end=2420
  _globals['_LISTENRESPONSE_OPENCHANNELRESPONSE']._serialized_start=2422
  _globals['_LISTENRESPONSE_OPENCHANNELRESPONSE']._serialized_end=2493
  _globals['_LISTENRESPONSE_RESUMECHANNELRESPONSE']._serialized_start=2495
  _globals['_LISTENRESPONSE_RESUMECHANNELRESPONSE']._serialized_end=2593
  _globals['_ACCEPTREQUEST']._serialized_start=2607
  _globals['_ACCEPTREQUEST']._serialized_end=3243
  _globals['_ACCEPTREQUEST_OPENREQUEST']._serialized_start=2996
  _globals['_ACCEPTREQUEST_OPENREQUEST']._serialized_end=3099
  _globals['_ACCEPTREQUEST_RESUMEREQUEST']._serialized_start=3102
  _globals['_ACCEPTREQUEST_RESUMEREQUEST']._serialized_end=3232
  _globals['_ACCEPTRESPONSE']._serialized_start=3246
  _globals['_ACCEPTRESPONSE']._serialized_end=3495
  _globals['_PING']._serialized_start=3497
  _globals['_PING']._serialized_end=3503
  _globals['_PONG']._serialized_start=3505
  _globals['_PONG']._serialized_end=3511
  _globals['_DATA']._serialized_start=3513
  _globals['_DATA']._serialized_end=3568
  _globals['_ACK']._serialized_start=3570
  _globals['_ACK']._serialized_end=3587
  _globals['_CLOSE']._serialized_start=3589
  _globals['_CLOSE']._serialized_end=3608
  _globals['_ERROR']._serialized_start=3610
  _globals['_ERROR']._serialized_end=3646
# @@protoc_insertion_point(module_scope)
