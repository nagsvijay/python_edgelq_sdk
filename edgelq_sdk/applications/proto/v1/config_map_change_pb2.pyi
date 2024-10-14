from edgelq_sdk.applications.proto.v1 import config_map_pb2 as _config_map_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigMapChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("config_map", "view_index")
        CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        config_map: _config_map_pb2.ConfigMap
        view_index: int
        def __init__(self, config_map: _Optional[_Union[_config_map_pb2.ConfigMap, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "config_map", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        config_map: _config_map_pb2.ConfigMap
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., config_map: _Optional[_Union[_config_map_pb2.ConfigMap, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("config_map",)
        CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
        config_map: _config_map_pb2.ConfigMap
        def __init__(self, config_map: _Optional[_Union[_config_map_pb2.ConfigMap, _Mapping]] = ...) -> None: ...
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
    added: ConfigMapChange.Added
    modified: ConfigMapChange.Modified
    current: ConfigMapChange.Current
    removed: ConfigMapChange.Removed
    def __init__(self, added: _Optional[_Union[ConfigMapChange.Added, _Mapping]] = ..., modified: _Optional[_Union[ConfigMapChange.Modified, _Mapping]] = ..., current: _Optional[_Union[ConfigMapChange.Current, _Mapping]] = ..., removed: _Optional[_Union[ConfigMapChange.Removed, _Mapping]] = ...) -> None: ...
