from edgelq_sdk.audit.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.audit.proto.v1 import resource_change_log_pb2 as _resource_change_log_pb2
from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListResourceChangeLogsRequest(_message.Message):
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

class ListResourceChangeLogsResponse(_message.Message):
    __slots__ = ("resource_change_logs", "next_page_token", "execution_errors")
    class ErrorDetails(_message.Message):
        __slots__ = ("region_id",)
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: str
        def __init__(self, region_id: _Optional[str] = ...) -> None: ...
    RESOURCE_CHANGE_LOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    resource_change_logs: _containers.RepeatedCompositeFieldContainer[_resource_change_log_pb2.ResourceChangeLog]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, resource_change_logs: _Optional[_Iterable[_Union[_resource_change_log_pb2.ResourceChangeLog, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class CreatePreCommittedResourceChangeLogsRequest(_message.Message):
    __slots__ = ("request_id", "timestamp", "authentication", "service", "transaction", "changes")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    timestamp: _timestamp_pb2.Timestamp
    authentication: _common_pb2.Authentication
    service: _common_pb2.ServiceData
    transaction: _resource_change_log_pb2.ResourceChangeLog.TransactionInfo
    changes: _containers.RepeatedCompositeFieldContainer[_resource_change_log_pb2.ResourceChangeLog.ResourceChange]
    def __init__(self, request_id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., authentication: _Optional[_Union[_common_pb2.Authentication, _Mapping]] = ..., service: _Optional[_Union[_common_pb2.ServiceData, _Mapping]] = ..., transaction: _Optional[_Union[_resource_change_log_pb2.ResourceChangeLog.TransactionInfo, _Mapping]] = ..., changes: _Optional[_Iterable[_Union[_resource_change_log_pb2.ResourceChangeLog.ResourceChange, _Mapping]]] = ...) -> None: ...

class CreatePreCommittedResourceChangeLogsResponse(_message.Message):
    __slots__ = ("log_keys",)
    LOG_KEYS_FIELD_NUMBER: _ClassVar[int]
    log_keys: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, log_keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SetResourceChangeLogsCommitStateRequest(_message.Message):
    __slots__ = ("log_keys", "service", "timestamp", "tx_result")
    LOG_KEYS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TX_RESULT_FIELD_NUMBER: _ClassVar[int]
    log_keys: _containers.RepeatedScalarFieldContainer[bytes]
    service: _common_pb2.ServiceData
    timestamp: _timestamp_pb2.Timestamp
    tx_result: _resource_change_log_pb2.ResourceChangeLog.TransactionInfo.State
    def __init__(self, log_keys: _Optional[_Iterable[bytes]] = ..., service: _Optional[_Union[_common_pb2.ServiceData, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tx_result: _Optional[_Union[_resource_change_log_pb2.ResourceChangeLog.TransactionInfo.State, str]] = ...) -> None: ...

class SetResourceChangeLogsCommitStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
