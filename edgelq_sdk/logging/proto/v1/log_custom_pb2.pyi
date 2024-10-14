from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from edgelq_sdk.logging.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.logging.proto.v1 import log_pb2 as _log_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListLogsRequest(_message.Message):
    __slots__ = ("parents", "filter", "interval", "page_size", "page_token")
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parents: _containers.RepeatedScalarFieldContainer[str]
    filter: str
    interval: _common_pb2.TimeInterval
    page_size: int
    page_token: str
    def __init__(self, parents: _Optional[_Iterable[str]] = ..., filter: _Optional[str] = ..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListLogsResponse(_message.Message):
    __slots__ = ("logs", "next_page_token", "execution_errors")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    LOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[_log_pb2.Log]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, logs: _Optional[_Iterable[_Union[_log_pb2.Log, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class CreateLogsRequest(_message.Message):
    __slots__ = ("parent", "logs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    logs: _containers.RepeatedCompositeFieldContainer[_log_pb2.Log]
    def __init__(self, parent: _Optional[str] = ..., logs: _Optional[_Iterable[_Union[_log_pb2.Log, _Mapping]]] = ...) -> None: ...

class CreateLogsResponse(_message.Message):
    __slots__ = ("log_names", "failed_logs")
    class LogNamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class CreateError(_message.Message):
        __slots__ = ("logs", "status")
        LOGS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        logs: _containers.RepeatedCompositeFieldContainer[_log_pb2.Log]
        status: _status_pb2.Status
        def __init__(self, logs: _Optional[_Iterable[_Union[_log_pb2.Log, _Mapping]]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    LOG_NAMES_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOGS_FIELD_NUMBER: _ClassVar[int]
    log_names: _containers.ScalarMap[int, str]
    failed_logs: _containers.RepeatedCompositeFieldContainer[CreateLogsResponse.CreateError]
    def __init__(self, log_names: _Optional[_Mapping[int, str]] = ..., failed_logs: _Optional[_Iterable[_Union[CreateLogsResponse.CreateError, _Mapping]]] = ...) -> None: ...
