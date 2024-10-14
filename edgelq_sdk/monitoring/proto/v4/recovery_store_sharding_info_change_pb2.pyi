from edgelq_sdk.monitoring.proto.v4 import recovery_store_sharding_info_pb2 as _recovery_store_sharding_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecoveryStoreShardingInfoChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("recovery_store_sharding_info", "view_index")
        RECOVERY_STORE_SHARDING_INFO_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        recovery_store_sharding_info: _recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo
        view_index: int
        def __init__(self, recovery_store_sharding_info: _Optional[_Union[_recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "recovery_store_sharding_info", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_STORE_SHARDING_INFO_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        recovery_store_sharding_info: _recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., recovery_store_sharding_info: _Optional[_Union[_recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("recovery_store_sharding_info",)
        RECOVERY_STORE_SHARDING_INFO_FIELD_NUMBER: _ClassVar[int]
        recovery_store_sharding_info: _recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo
        def __init__(self, recovery_store_sharding_info: _Optional[_Union[_recovery_store_sharding_info_pb2.RecoveryStoreShardingInfo, _Mapping]] = ...) -> None: ...
    class Removed(_message.Message):
        __slots__ = ("name", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        view_index: int
        def __init__(self, name: _Optional[str] = ..., view_index: _Optional[int] = ...) -> None: ...
    ADDED_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    added: RecoveryStoreShardingInfoChange.Added
    modified: RecoveryStoreShardingInfoChange.Modified
    current: RecoveryStoreShardingInfoChange.Current
    removed: RecoveryStoreShardingInfoChange.Removed
    def __init__(self, added: _Optional[_Union[RecoveryStoreShardingInfoChange.Added, _Mapping]] = ..., modified: _Optional[_Union[RecoveryStoreShardingInfoChange.Modified, _Mapping]] = ..., current: _Optional[_Union[RecoveryStoreShardingInfoChange.Current, _Mapping]] = ..., removed: _Optional[_Union[RecoveryStoreShardingInfoChange.Removed, _Mapping]] = ...) -> None: ...
