from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LabelDescriptor(_message.Message):
    __slots__ = ("key", "description")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    key: str
    description: str
    def __init__(self, key: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class LabelKeySet(_message.Message):
    __slots__ = ("label_keys",)
    LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    label_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, label_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeInterval(_message.Message):
    __slots__ = ("end_time", "start_time")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
