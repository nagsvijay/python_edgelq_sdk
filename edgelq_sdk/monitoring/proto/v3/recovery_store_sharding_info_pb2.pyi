from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecoveryStoreShardingInfo(_message.Message):
    __slots__ = ("name", "validity_period", "spec", "metadata")
    class ValidityPeriod(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class ShardingSpec(_message.Message):
        __slots__ = ("ts_blob_period", "shards_count")
        TS_BLOB_PERIOD_FIELD_NUMBER: _ClassVar[int]
        SHARDS_COUNT_FIELD_NUMBER: _ClassVar[int]
        ts_blob_period: _duration_pb2.Duration
        shards_count: int
        def __init__(self, ts_blob_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., shards_count: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    validity_period: RecoveryStoreShardingInfo.ValidityPeriod
    spec: RecoveryStoreShardingInfo.ShardingSpec
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., validity_period: _Optional[_Union[RecoveryStoreShardingInfo.ValidityPeriod, _Mapping]] = ..., spec: _Optional[_Union[RecoveryStoreShardingInfo.ShardingSpec, _Mapping]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
