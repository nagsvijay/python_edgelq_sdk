from edgelq_sdk.devices.proto.v1alpha2 import device_type_pb2 as _device_type_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTypeChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("device_type", "view_index")
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        device_type: _device_type_pb2.DeviceType
        view_index: int
        def __init__(self, device_type: _Optional[_Union[_device_type_pb2.DeviceType, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "device_type", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        device_type: _device_type_pb2.DeviceType
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., device_type: _Optional[_Union[_device_type_pb2.DeviceType, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("device_type",)
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_type: _device_type_pb2.DeviceType
        def __init__(self, device_type: _Optional[_Union[_device_type_pb2.DeviceType, _Mapping]] = ...) -> None: ...
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
    added: DeviceTypeChange.Added
    modified: DeviceTypeChange.Modified
    current: DeviceTypeChange.Current
    removed: DeviceTypeChange.Removed
    def __init__(self, added: _Optional[_Union[DeviceTypeChange.Added, _Mapping]] = ..., modified: _Optional[_Union[DeviceTypeChange.Modified, _Mapping]] = ..., current: _Optional[_Union[DeviceTypeChange.Current, _Mapping]] = ..., removed: _Optional[_Union[DeviceTypeChange.Removed, _Mapping]] = ...) -> None: ...
