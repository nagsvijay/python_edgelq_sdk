# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/notification_change.proto
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
    'edgelq-sdk/monitoring/proto/v4/notification_change.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import notification_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_notification__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8edgelq-sdk/monitoring/proto/v4/notification_change.proto\x12\x11ntt.monitoring.v4\x1a\x31\x65\x64gelq-sdk/monitoring/proto/v4/notification.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\x9f\x05\n\x12NotificationChange\x12<\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32+.ntt.monitoring.v4.NotificationChange.AddedH\x00\x12\x42\n\x08modified\x18\x02 \x01(\x0b\x32..ntt.monitoring.v4.NotificationChange.ModifiedH\x00\x12@\n\x07\x63urrent\x18\x04 \x01(\x0b\x32-.ntt.monitoring.v4.NotificationChange.CurrentH\x00\x12@\n\x07removed\x18\x03 \x01(\x0b\x32-.ntt.monitoring.v4.NotificationChange.RemovedH\x00\x1aR\n\x05\x41\x64\x64\x65\x64\x12\x35\n\x0cnotification\x18\x01 \x01(\x0b\x32\x1f.ntt.monitoring.v4.Notification\x12\x12\n\nview_index\x18\x02 \x01(\x05\x1a\xb0\x01\n\x08Modified\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0cnotification\x18\x02 \x01(\x0b\x32\x1f.ntt.monitoring.v4.Notification\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x13previous_view_index\x18\x04 \x01(\x05\x12\x12\n\nview_index\x18\x05 \x01(\x05\x1a@\n\x07\x43urrent\x12\x35\n\x0cnotification\x18\x01 \x01(\x0b\x32\x1f.ntt.monitoring.v4.Notification\x1a+\n\x07Removed\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nview_index\x18\x02 \x01(\x05\x42\r\n\x0b\x63hange_typeB\x87\x01\n\x18\x63om.ntt.monitoring.pb.v4B\x17NotificationChangeProtoP\x00ZPgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/notification;notificationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.notification_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\027NotificationChangeProtoP\000ZPgithub.com/cloudwan/edgelq-sdk/monitoring/resources/v4/notification;notification'
  _globals['_NOTIFICATIONCHANGE']._serialized_start=192
  _globals['_NOTIFICATIONCHANGE']._serialized_end=863
  _globals['_NOTIFICATIONCHANGE_ADDED']._serialized_start=476
  _globals['_NOTIFICATIONCHANGE_ADDED']._serialized_end=558
  _globals['_NOTIFICATIONCHANGE_MODIFIED']._serialized_start=561
  _globals['_NOTIFICATIONCHANGE_MODIFIED']._serialized_end=737
  _globals['_NOTIFICATIONCHANGE_CURRENT']._serialized_start=739
  _globals['_NOTIFICATIONCHANGE_CURRENT']._serialized_end=803
  _globals['_NOTIFICATIONCHANGE_REMOVED']._serialized_start=805
  _globals['_NOTIFICATIONCHANGE_REMOVED']._serialized_end=848
# @@protoc_insertion_point(module_scope)
