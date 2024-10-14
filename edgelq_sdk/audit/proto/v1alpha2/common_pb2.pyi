from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Authentication(_message.Message):
    __slots__ = ("principal", "principal_type")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    principal: str
    principal_type: str
    def __init__(self, principal: _Optional[str] = ..., principal_type: _Optional[str] = ...) -> None: ...

class Authorization(_message.Message):
    __slots__ = ("granted_permissions", "denied_permissions")
    GRANTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DENIED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    granted_permissions: _containers.RepeatedScalarFieldContainer[str]
    denied_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, granted_permissions: _Optional[_Iterable[str]] = ..., denied_permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class ServiceData(_message.Message):
    __slots__ = ("name", "region_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    region_id: str
    def __init__(self, name: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class ObjectState(_message.Message):
    __slots__ = ("data", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    data: _any_pb2.Any
    labels: _containers.ScalarMap[str, str]
    def __init__(self, data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LabelDescriptor(_message.Message):
    __slots__ = ("key", "versions")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    key: str
    versions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., versions: _Optional[_Iterable[str]] = ...) -> None: ...

class LabelKeySet(_message.Message):
    __slots__ = ("label_keys", "versions")
    LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    label_keys: _containers.RepeatedScalarFieldContainer[str]
    versions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, label_keys: _Optional[_Iterable[str]] = ..., versions: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeInterval(_message.Message):
    __slots__ = ("end_time", "start_time")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
