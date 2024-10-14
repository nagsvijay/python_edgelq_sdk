from edgelq_sdk.audit.proto.v1 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceChangeLog(_message.Message):
    __slots__ = ("name", "scope", "request_id", "timestamp", "authentication", "service", "resource", "transaction")
    class ResourceChange(_message.Message):
        __slots__ = ("name", "type", "action", "updated_fields", "previous", "current", "labels", "pre", "post")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            CREATE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            DELETE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            SPEC_UPDATE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            STATE_UPDATE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            META_UPDATE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
            UPDATE: _ClassVar[ResourceChangeLog.ResourceChange.Action]
        UNDEFINED: ResourceChangeLog.ResourceChange.Action
        CREATE: ResourceChangeLog.ResourceChange.Action
        DELETE: ResourceChangeLog.ResourceChange.Action
        SPEC_UPDATE: ResourceChangeLog.ResourceChange.Action
        STATE_UPDATE: ResourceChangeLog.ResourceChange.Action
        META_UPDATE: ResourceChangeLog.ResourceChange.Action
        UPDATE: ResourceChangeLog.ResourceChange.Action
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        PRE_FIELD_NUMBER: _ClassVar[int]
        POST_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        action: ResourceChangeLog.ResourceChange.Action
        updated_fields: _field_mask_pb2.FieldMask
        previous: _any_pb2.Any
        current: _any_pb2.Any
        labels: _containers.ScalarMap[str, str]
        pre: _common_pb2.ObjectState
        post: _common_pb2.ObjectState
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., action: _Optional[_Union[ResourceChangeLog.ResourceChange.Action, str]] = ..., updated_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., current: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., pre: _Optional[_Union[_common_pb2.ObjectState, _Mapping]] = ..., post: _Optional[_Union[_common_pb2.ObjectState, _Mapping]] = ...) -> None: ...
    class TransactionInfo(_message.Message):
        __slots__ = ("identifier", "try_counter", "state")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[ResourceChangeLog.TransactionInfo.State]
            PRE_COMMITTED: _ClassVar[ResourceChangeLog.TransactionInfo.State]
            COMMITTED: _ClassVar[ResourceChangeLog.TransactionInfo.State]
            ROLLED_BACK: _ClassVar[ResourceChangeLog.TransactionInfo.State]
        UNDEFINED: ResourceChangeLog.TransactionInfo.State
        PRE_COMMITTED: ResourceChangeLog.TransactionInfo.State
        COMMITTED: ResourceChangeLog.TransactionInfo.State
        ROLLED_BACK: ResourceChangeLog.TransactionInfo.State
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        TRY_COUNTER_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        try_counter: int
        state: ResourceChangeLog.TransactionInfo.State
        def __init__(self, identifier: _Optional[str] = ..., try_counter: _Optional[int] = ..., state: _Optional[_Union[ResourceChangeLog.TransactionInfo.State, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    scope: str
    request_id: int
    timestamp: _timestamp_pb2.Timestamp
    authentication: _common_pb2.Authentication
    service: _common_pb2.ServiceData
    resource: ResourceChangeLog.ResourceChange
    transaction: ResourceChangeLog.TransactionInfo
    def __init__(self, name: _Optional[str] = ..., scope: _Optional[str] = ..., request_id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., authentication: _Optional[_Union[_common_pb2.Authentication, _Mapping]] = ..., service: _Optional[_Union[_common_pb2.ServiceData, _Mapping]] = ..., resource: _Optional[_Union[ResourceChangeLog.ResourceChange, _Mapping]] = ..., transaction: _Optional[_Union[ResourceChangeLog.TransactionInfo, _Mapping]] = ...) -> None: ...
