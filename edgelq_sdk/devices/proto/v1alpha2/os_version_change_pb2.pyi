from edgelq_sdk.devices.proto.v1alpha2 import os_version_pb2 as _os_version_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OsVersionChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("os_version", "view_index")
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        os_version: _os_version_pb2.OsVersion
        view_index: int
        def __init__(self, os_version: _Optional[_Union[_os_version_pb2.OsVersion, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "os_version", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        os_version: _os_version_pb2.OsVersion
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., os_version: _Optional[_Union[_os_version_pb2.OsVersion, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("os_version",)
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        os_version: _os_version_pb2.OsVersion
        def __init__(self, os_version: _Optional[_Union[_os_version_pb2.OsVersion, _Mapping]] = ...) -> None: ...
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
    added: OsVersionChange.Added
    modified: OsVersionChange.Modified
    current: OsVersionChange.Current
    removed: OsVersionChange.Removed
    def __init__(self, added: _Optional[_Union[OsVersionChange.Added, _Mapping]] = ..., modified: _Optional[_Union[OsVersionChange.Modified, _Mapping]] = ..., current: _Optional[_Union[OsVersionChange.Current, _Mapping]] = ..., removed: _Optional[_Union[OsVersionChange.Removed, _Mapping]] = ...) -> None: ...
