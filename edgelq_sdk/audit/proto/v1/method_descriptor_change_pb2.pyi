from edgelq_sdk.audit.proto.v1 import method_descriptor_pb2 as _method_descriptor_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MethodDescriptorChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("method_descriptor", "view_index")
        METHOD_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        method_descriptor: _method_descriptor_pb2.MethodDescriptor
        view_index: int
        def __init__(self, method_descriptor: _Optional[_Union[_method_descriptor_pb2.MethodDescriptor, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "method_descriptor", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        method_descriptor: _method_descriptor_pb2.MethodDescriptor
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., method_descriptor: _Optional[_Union[_method_descriptor_pb2.MethodDescriptor, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("method_descriptor",)
        METHOD_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        method_descriptor: _method_descriptor_pb2.MethodDescriptor
        def __init__(self, method_descriptor: _Optional[_Union[_method_descriptor_pb2.MethodDescriptor, _Mapping]] = ...) -> None: ...
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
    added: MethodDescriptorChange.Added
    modified: MethodDescriptorChange.Modified
    current: MethodDescriptorChange.Current
    removed: MethodDescriptorChange.Removed
    def __init__(self, added: _Optional[_Union[MethodDescriptorChange.Added, _Mapping]] = ..., modified: _Optional[_Union[MethodDescriptorChange.Modified, _Mapping]] = ..., current: _Optional[_Union[MethodDescriptorChange.Current, _Mapping]] = ..., removed: _Optional[_Union[MethodDescriptorChange.Removed, _Mapping]] = ...) -> None: ...
