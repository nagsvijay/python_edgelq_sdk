# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: edgelq-sdk/monitoring/proto/v4/bucket_service.proto
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
    'edgelq-sdk/monitoring/proto/v4/bucket_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgelq_sdk.monitoring.proto.v4 import bucket_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_bucket__pb2
from edgelq_sdk.monitoring.proto.v4 import bucket_change_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v4_dot_bucket__change__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from goten_sdk.types import view_pb2 as goten__sdk_dot_types_dot_view__pb2
from goten_sdk.types import watch_type_pb2 as goten__sdk_dot_types_dot_watch__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3edgelq-sdk/monitoring/proto/v4/bucket_service.proto\x12\x11ntt.monitoring.v4\x1a+edgelq-sdk/monitoring/proto/v4/bucket.proto\x1a\x32\x65\x64gelq-sdk/monitoring/proto/v4/bucket_change.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoten-sdk/types/view.proto\x1a goten-sdk/types/watch_type.proto\"q\n\x10GetBucketRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"~\n\x16\x42\x61tchGetBucketsRequest\x12\r\n\x05names\x18\x02 \x03(\t\x12.\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.ViewJ\x04\x08\x01\x10\x02\"V\n\x17\x42\x61tchGetBucketsResponse\x12*\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x19.ntt.monitoring.v4.Bucket\x12\x0f\n\x07missing\x18\x02 \x03(\t\"\xdb\x01\n\x12ListBucketsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x07 \x01(\x0e\x32\x11.goten.types.View\x12\x1b\n\x13include_paging_info\x18\x08 \x01(\x08\"\xa8\x01\n\x13ListBucketsResponse\x12*\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x19.ntt.monitoring.v4.Bucket\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\x12\x16\n\x0e\x63urrent_offset\x18\x05 \x01(\x05\x12\x1b\n\x13total_results_count\x18\x06 \x01(\x05\"s\n\x12WatchBucketRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x04 \x01(\x0e\x32\x11.goten.types.View\"F\n\x13WatchBucketResponse\x12/\n\x06\x63hange\x18\x01 \x01(\x0b\x32\x1f.ntt.monitoring.v4.BucketChange\"\xc6\x02\n\x13WatchBucketsRequest\x12$\n\x04type\x18\t \x01(\x0e\x32\x16.goten.types.WatchType\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x14\n\x0cresume_token\x18\n \x01(\t\x12\x31\n\rstarting_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1f\n\x04view\x18\x08 \x01(\x0e\x32\x11.goten.types.View\x12\x16\n\x0emax_chunk_size\x18\x0b \x01(\x05\"\xd7\x02\n\x14WatchBucketsResponse\x12\x37\n\x0e\x62ucket_changes\x18\x02 \x03(\x0b\x32\x1f.ntt.monitoring.v4.BucketChange\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12R\n\x11page_token_change\x18\x03 \x01(\x0b\x32\x37.ntt.monitoring.v4.WatchBucketsResponse.PageTokenChange\x12\x14\n\x0cresume_token\x18\x05 \x01(\t\x12\x15\n\rsnapshot_size\x18\x06 \x01(\x03\x12\x15\n\ris_soft_reset\x18\x07 \x01(\x08\x12\x15\n\ris_hard_reset\x18\x08 \x01(\x08\x1a\x43\n\x0fPageTokenChange\x12\x17\n\x0fprev_page_token\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"P\n\x13\x43reateBucketRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12)\n\x06\x62ucket\x18\x02 \x01(\x0b\x32\x19.ntt.monitoring.v4.Bucket\"\xae\x02\n\x13UpdateBucketRequest\x12)\n\x06\x62ucket\x18\x02 \x01(\x0b\x32\x19.ntt.monitoring.v4.Bucket\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x37\n\x03\x63\x61s\x18\x04 \x01(\x0b\x32*.ntt.monitoring.v4.UpdateBucketRequest.CAS\x12\x15\n\rallow_missing\x18\x05 \x01(\x08\x1ak\n\x03\x43\x41S\x12\x34\n\x11\x63onditional_state\x18\x01 \x01(\x0b\x32\x19.ntt.monitoring.v4.Bucket\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"#\n\x13\x44\x65leteBucketRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xbe\t\n\rBucketService\x12~\n\tGetBucket\x12#.ntt.monitoring.v4.GetBucketRequest\x1a\x19.ntt.monitoring.v4.Bucket\"1\x82\xd3\xe4\x93\x02+\x12)/v4/{name=projects/*/regions/*/buckets/*}\x12\x86\x01\n\x0f\x42\x61tchGetBuckets\x12).ntt.monitoring.v4.BatchGetBucketsRequest\x1a*.ntt.monitoring.v4.BatchGetBucketsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v4/buckets:batchGet\x12\x8f\x01\n\x0bListBuckets\x12%.ntt.monitoring.v4.ListBucketsRequest\x1a&.ntt.monitoring.v4.ListBucketsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/v4/{parent=projects/*/regions/*}/buckets\x12\x97\x01\n\x0bWatchBucket\x12%.ntt.monitoring.v4.WatchBucketRequest\x1a&.ntt.monitoring.v4.WatchBucketResponse\"7\x82\xd3\xe4\x93\x02\x31\"//v4/{name=projects/*/regions/*/buckets/*}:watch0\x01\x12\x9a\x01\n\x0cWatchBuckets\x12&.ntt.monitoring.v4.WatchBucketsRequest\x1a\'.ntt.monitoring.v4.WatchBucketsResponse\"7\x82\xd3\xe4\x93\x02\x31\"//v4/{parent=projects/*/regions/*}/buckets:watch0\x01\x12\x8c\x01\n\x0c\x43reateBucket\x12&.ntt.monitoring.v4.CreateBucketRequest\x1a\x19.ntt.monitoring.v4.Bucket\"9\x82\xd3\xe4\x93\x02\x33\")/v4/{parent=projects/*/regions/*}/buckets:\x06\x62ucket\x12\x93\x01\n\x0cUpdateBucket\x12&.ntt.monitoring.v4.UpdateBucketRequest\x1a\x19.ntt.monitoring.v4.Bucket\"@\x82\xd3\xe4\x93\x02:\x1a\x30/v4/{bucket.name=projects/*/regions/*/buckets/*}:\x06\x62ucket\x12\x81\x01\n\x0c\x44\x65leteBucket\x12&.ntt.monitoring.v4.DeleteBucketRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/v4/{name=projects/*/regions/*/buckets/*}\x1a\x32\xca\x41\x15monitoring.edgelq.com\xd2\x41\x17https://apis.edgelq.comBz\n\x18\x63om.ntt.monitoring.pb.v4B\x12\x42ucketServiceProtoP\x00ZHgithub.com/cloudwan/edgelq-sdk/monitoring/client/v4/bucket;bucket_clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgelq_sdk.monitoring.proto.v4.bucket_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.ntt.monitoring.pb.v4B\022BucketServiceProtoP\000ZHgithub.com/cloudwan/edgelq-sdk/monitoring/client/v4/bucket;bucket_client'
  _globals['_BUCKETSERVICE']._loaded_options = None
  _globals['_BUCKETSERVICE']._serialized_options = b'\312A\025monitoring.edgelq.com\322A\027https://apis.edgelq.com'
  _globals['_BUCKETSERVICE'].methods_by_name['GetBucket']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['GetBucket']._serialized_options = b'\202\323\344\223\002+\022)/v4/{name=projects/*/regions/*/buckets/*}'
  _globals['_BUCKETSERVICE'].methods_by_name['BatchGetBuckets']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['BatchGetBuckets']._serialized_options = b'\202\323\344\223\002\026\022\024/v4/buckets:batchGet'
  _globals['_BUCKETSERVICE'].methods_by_name['ListBuckets']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['ListBuckets']._serialized_options = b'\202\323\344\223\002+\022)/v4/{parent=projects/*/regions/*}/buckets'
  _globals['_BUCKETSERVICE'].methods_by_name['WatchBucket']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['WatchBucket']._serialized_options = b'\202\323\344\223\0021\"//v4/{name=projects/*/regions/*/buckets/*}:watch'
  _globals['_BUCKETSERVICE'].methods_by_name['WatchBuckets']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['WatchBuckets']._serialized_options = b'\202\323\344\223\0021\"//v4/{parent=projects/*/regions/*}/buckets:watch'
  _globals['_BUCKETSERVICE'].methods_by_name['CreateBucket']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['CreateBucket']._serialized_options = b'\202\323\344\223\0023\")/v4/{parent=projects/*/regions/*}/buckets:\006bucket'
  _globals['_BUCKETSERVICE'].methods_by_name['UpdateBucket']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['UpdateBucket']._serialized_options = b'\202\323\344\223\002:\0320/v4/{bucket.name=projects/*/regions/*/buckets/*}:\006bucket'
  _globals['_BUCKETSERVICE'].methods_by_name['DeleteBucket']._loaded_options = None
  _globals['_BUCKETSERVICE'].methods_by_name['DeleteBucket']._serialized_options = b'\202\323\344\223\002+*)/v4/{name=projects/*/regions/*/buckets/*}'
  _globals['_GETBUCKETREQUEST']._serialized_start=384
  _globals['_GETBUCKETREQUEST']._serialized_end=497
  _globals['_BATCHGETBUCKETSREQUEST']._serialized_start=499
  _globals['_BATCHGETBUCKETSREQUEST']._serialized_end=625
  _globals['_BATCHGETBUCKETSRESPONSE']._serialized_start=627
  _globals['_BATCHGETBUCKETSRESPONSE']._serialized_end=713
  _globals['_LISTBUCKETSREQUEST']._serialized_start=716
  _globals['_LISTBUCKETSREQUEST']._serialized_end=935
  _globals['_LISTBUCKETSRESPONSE']._serialized_start=938
  _globals['_LISTBUCKETSRESPONSE']._serialized_end=1106
  _globals['_WATCHBUCKETREQUEST']._serialized_start=1108
  _globals['_WATCHBUCKETREQUEST']._serialized_end=1223
  _globals['_WATCHBUCKETRESPONSE']._serialized_start=1225
  _globals['_WATCHBUCKETRESPONSE']._serialized_end=1295
  _globals['_WATCHBUCKETSREQUEST']._serialized_start=1298
  _globals['_WATCHBUCKETSREQUEST']._serialized_end=1624
  _globals['_WATCHBUCKETSRESPONSE']._serialized_start=1627
  _globals['_WATCHBUCKETSRESPONSE']._serialized_end=1970
  _globals['_WATCHBUCKETSRESPONSE_PAGETOKENCHANGE']._serialized_start=1903
  _globals['_WATCHBUCKETSRESPONSE_PAGETOKENCHANGE']._serialized_end=1970
  _globals['_CREATEBUCKETREQUEST']._serialized_start=1972
  _globals['_CREATEBUCKETREQUEST']._serialized_end=2052
  _globals['_UPDATEBUCKETREQUEST']._serialized_start=2055
  _globals['_UPDATEBUCKETREQUEST']._serialized_end=2357
  _globals['_UPDATEBUCKETREQUEST_CAS']._serialized_start=2250
  _globals['_UPDATEBUCKETREQUEST_CAS']._serialized_end=2357
  _globals['_DELETEBUCKETREQUEST']._serialized_start=2359
  _globals['_DELETEBUCKETREQUEST']._serialized_end=2394
  _globals['_BUCKETSERVICE']._serialized_start=2397
  _globals['_BUCKETSERVICE']._serialized_end=3611
# @@protoc_insertion_point(module_scope)
