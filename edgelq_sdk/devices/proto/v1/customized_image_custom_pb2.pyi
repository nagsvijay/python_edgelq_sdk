from edgelq_sdk.devices.proto.v1 import customized_image_pb2 as _customized_image_pb2
from edgelq_sdk.devices.proto.v1 import customized_image_change_pb2 as _customized_image_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestUrlRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RequestUrlResponse(_message.Message):
    __slots__ = ("url", "headers")
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    url: str
    headers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, url: _Optional[str] = ..., headers: _Optional[_Iterable[str]] = ...) -> None: ...
