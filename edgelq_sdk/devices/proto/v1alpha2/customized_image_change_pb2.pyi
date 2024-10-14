from edgelq_sdk.devices.proto.v1alpha2 import customized_image_pb2 as _customized_image_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomizedImageChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("customized_image", "view_index")
        CUSTOMIZED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        customized_image: _customized_image_pb2.CustomizedImage
        view_index: int
        def __init__(self, customized_image: _Optional[_Union[_customized_image_pb2.CustomizedImage, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "customized_image", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        CUSTOMIZED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        customized_image: _customized_image_pb2.CustomizedImage
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., customized_image: _Optional[_Union[_customized_image_pb2.CustomizedImage, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("customized_image",)
        CUSTOMIZED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        customized_image: _customized_image_pb2.CustomizedImage
        def __init__(self, customized_image: _Optional[_Union[_customized_image_pb2.CustomizedImage, _Mapping]] = ...) -> None: ...
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
    added: CustomizedImageChange.Added
    modified: CustomizedImageChange.Modified
    current: CustomizedImageChange.Current
    removed: CustomizedImageChange.Removed
    def __init__(self, added: _Optional[_Union[CustomizedImageChange.Added, _Mapping]] = ..., modified: _Optional[_Union[CustomizedImageChange.Modified, _Mapping]] = ..., current: _Optional[_Union[CustomizedImageChange.Current, _Mapping]] = ..., removed: _Optional[_Union[CustomizedImageChange.Removed, _Mapping]] = ...) -> None: ...