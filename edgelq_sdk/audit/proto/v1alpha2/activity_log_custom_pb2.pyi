from edgelq_sdk.audit.proto.v1alpha2 import activity_log_pb2 as _activity_log_pb2
from edgelq_sdk.audit.proto.v1alpha2 import common_pb2 as _common_pb2
from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListActivityLogsRequest(_message.Message):
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

class ListActivityLogsResponse(_message.Message):
    __slots__ = ("activity_logs", "next_page_token", "execution_errors")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    ACTIVITY_LOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    activity_logs: _containers.RepeatedCompositeFieldContainer[_activity_log_pb2.ActivityLog]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, activity_logs: _Optional[_Iterable[_Union[_activity_log_pb2.ActivityLog, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class CreateActivityLogsRequest(_message.Message):
    __slots__ = ("activity_logs",)
    ACTIVITY_LOGS_FIELD_NUMBER: _ClassVar[int]
    activity_logs: _containers.RepeatedCompositeFieldContainer[_activity_log_pb2.ActivityLog]
    def __init__(self, activity_logs: _Optional[_Iterable[_Union[_activity_log_pb2.ActivityLog, _Mapping]]] = ...) -> None: ...

class CreateActivityLogsResponse(_message.Message):
    __slots__ = ("log_names",)
    LOG_NAMES_FIELD_NUMBER: _ClassVar[int]
    log_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, log_names: _Optional[_Iterable[str]] = ...) -> None: ...
