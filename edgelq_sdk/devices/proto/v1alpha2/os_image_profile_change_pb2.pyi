from edgelq_sdk.devices.proto.v1alpha2 import os_image_profile_pb2 as _os_image_profile_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OsImageProfileChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("os_image_profile", "view_index")
        OS_IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        os_image_profile: _os_image_profile_pb2.OsImageProfile
        view_index: int
        def __init__(self, os_image_profile: _Optional[_Union[_os_image_profile_pb2.OsImageProfile, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "os_image_profile", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        OS_IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        os_image_profile: _os_image_profile_pb2.OsImageProfile
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., os_image_profile: _Optional[_Union[_os_image_profile_pb2.OsImageProfile, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("os_image_profile",)
        OS_IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
        os_image_profile: _os_image_profile_pb2.OsImageProfile
        def __init__(self, os_image_profile: _Optional[_Union[_os_image_profile_pb2.OsImageProfile, _Mapping]] = ...) -> None: ...
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
    added: OsImageProfileChange.Added
    modified: OsImageProfileChange.Modified
    current: OsImageProfileChange.Current
    removed: OsImageProfileChange.Removed
    def __init__(self, added: _Optional[_Union[OsImageProfileChange.Added, _Mapping]] = ..., modified: _Optional[_Union[OsImageProfileChange.Modified, _Mapping]] = ..., current: _Optional[_Union[OsImageProfileChange.Current, _Mapping]] = ..., removed: _Optional[_Union[OsImageProfileChange.Removed, _Mapping]] = ...) -> None: ...
