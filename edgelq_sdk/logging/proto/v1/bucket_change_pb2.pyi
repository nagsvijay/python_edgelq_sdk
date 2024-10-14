from edgelq_sdk.logging.proto.v1 import bucket_pb2 as _bucket_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BucketChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("bucket", "view_index")
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        bucket: _bucket_pb2.Bucket
        view_index: int
        def __init__(self, bucket: _Optional[_Union[_bucket_pb2.Bucket, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "bucket", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        bucket: _bucket_pb2.Bucket
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., bucket: _Optional[_Union[_bucket_pb2.Bucket, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("bucket",)
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        bucket: _bucket_pb2.Bucket
        def __init__(self, bucket: _Optional[_Union[_bucket_pb2.Bucket, _Mapping]] = ...) -> None: ...
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
    added: BucketChange.Added
    modified: BucketChange.Modified
    current: BucketChange.Current
    removed: BucketChange.Removed
    def __init__(self, added: _Optional[_Union[BucketChange.Added, _Mapping]] = ..., modified: _Optional[_Union[BucketChange.Modified, _Mapping]] = ..., current: _Optional[_Union[BucketChange.Current, _Mapping]] = ..., removed: _Optional[_Union[BucketChange.Removed, _Mapping]] = ...) -> None: ...
