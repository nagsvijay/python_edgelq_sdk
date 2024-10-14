from edgelq_sdk.audit.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.common.rpc import status_pb2 as _status_pb2
from edgelq_sdk.iam.proto.v1 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityLog(_message.Message):
    __slots__ = ("name", "scope", "request_id", "authentication", "authorization", "service", "method", "request_metadata", "request_routing", "resource", "category", "labels", "events")
    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Undefined: _ClassVar[ActivityLog.Category]
        Operation: _ClassVar[ActivityLog.Category]
        Creation: _ClassVar[ActivityLog.Category]
        Deletion: _ClassVar[ActivityLog.Category]
        SpecUpdate: _ClassVar[ActivityLog.Category]
        StateUpdate: _ClassVar[ActivityLog.Category]
        MetaUpdate: _ClassVar[ActivityLog.Category]
        Internal: _ClassVar[ActivityLog.Category]
        Rejected: _ClassVar[ActivityLog.Category]
        ClientError: _ClassVar[ActivityLog.Category]
        ServerError: _ClassVar[ActivityLog.Category]
        Read: _ClassVar[ActivityLog.Category]
    Undefined: ActivityLog.Category
    Operation: ActivityLog.Category
    Creation: ActivityLog.Category
    Deletion: ActivityLog.Category
    SpecUpdate: ActivityLog.Category
    StateUpdate: ActivityLog.Category
    MetaUpdate: ActivityLog.Category
    Internal: ActivityLog.Category
    Rejected: ActivityLog.Category
    ClientError: ActivityLog.Category
    ServerError: ActivityLog.Category
    Read: ActivityLog.Category
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ("client_message", "server_message", "exit", "regional_server_message", "regional_exit")
        class ClientMsgEvent(_message.Message):
            __slots__ = ("data", "time")
            DATA_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            data: _any_pb2.Any
            time: _timestamp_pb2.Timestamp
            def __init__(self, data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class RegionalServerMsgEvent(_message.Message):
            __slots__ = ("data", "time", "region_id")
            DATA_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            REGION_ID_FIELD_NUMBER: _ClassVar[int]
            data: _any_pb2.Any
            time: _timestamp_pb2.Timestamp
            region_id: str
            def __init__(self, data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., region_id: _Optional[str] = ...) -> None: ...
        class ServerMsgEvent(_message.Message):
            __slots__ = ("data", "time")
            DATA_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            data: _any_pb2.Any
            time: _timestamp_pb2.Timestamp
            def __init__(self, data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class RegionalExitEvent(_message.Message):
            __slots__ = ("status", "time", "region_id")
            STATUS_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            REGION_ID_FIELD_NUMBER: _ClassVar[int]
            status: _status_pb2.Status
            time: _timestamp_pb2.Timestamp
            region_id: str
            def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., region_id: _Optional[str] = ...) -> None: ...
        class ExitEvent(_message.Message):
            __slots__ = ("status", "time")
            STATUS_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            status: _status_pb2.Status
            time: _timestamp_pb2.Timestamp
            def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        CLIENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EXIT_FIELD_NUMBER: _ClassVar[int]
        REGIONAL_SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REGIONAL_EXIT_FIELD_NUMBER: _ClassVar[int]
        client_message: ActivityLog.Event.ClientMsgEvent
        server_message: ActivityLog.Event.ServerMsgEvent
        exit: ActivityLog.Event.ExitEvent
        regional_server_message: ActivityLog.Event.RegionalServerMsgEvent
        regional_exit: ActivityLog.Event.RegionalServerMsgEvent
        def __init__(self, client_message: _Optional[_Union[ActivityLog.Event.ClientMsgEvent, _Mapping]] = ..., server_message: _Optional[_Union[ActivityLog.Event.ServerMsgEvent, _Mapping]] = ..., exit: _Optional[_Union[ActivityLog.Event.ExitEvent, _Mapping]] = ..., regional_server_message: _Optional[_Union[ActivityLog.Event.RegionalServerMsgEvent, _Mapping]] = ..., regional_exit: _Optional[_Union[ActivityLog.Event.RegionalServerMsgEvent, _Mapping]] = ...) -> None: ...
    class Method(_message.Message):
        __slots__ = ("type", "version")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        type: str
        version: str
        def __init__(self, type: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
    class RequestMetadata(_message.Message):
        __slots__ = ("ip_address", "user_agent")
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        USER_AGENT_FIELD_NUMBER: _ClassVar[int]
        ip_address: str
        user_agent: str
        def __init__(self, ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ...) -> None: ...
    class RequestRouting(_message.Message):
        __slots__ = ("via_region", "dest_regions")
        VIA_REGION_FIELD_NUMBER: _ClassVar[int]
        DEST_REGIONS_FIELD_NUMBER: _ClassVar[int]
        via_region: str
        dest_regions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, via_region: _Optional[str] = ..., dest_regions: _Optional[_Iterable[str]] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ("name", "difference")
        class Difference(_message.Message):
            __slots__ = ("fields", "before", "after")
            FIELDS_FIELD_NUMBER: _ClassVar[int]
            BEFORE_FIELD_NUMBER: _ClassVar[int]
            AFTER_FIELD_NUMBER: _ClassVar[int]
            fields: _field_mask_pb2.FieldMask
            before: _any_pb2.Any
            after: _any_pb2.Any
            def __init__(self, fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., before: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., after: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
        name: str
        difference: ActivityLog.Resource.Difference
        def __init__(self, name: _Optional[str] = ..., difference: _Optional[_Union[ActivityLog.Resource.Difference, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ROUTING_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    scope: str
    request_id: int
    authentication: _common_pb2.Authentication
    authorization: _common_pb2.Authorization
    service: _common_pb2.ServiceData
    method: ActivityLog.Method
    request_metadata: ActivityLog.RequestMetadata
    request_routing: ActivityLog.RequestRouting
    resource: ActivityLog.Resource
    category: ActivityLog.Category
    labels: _containers.ScalarMap[str, str]
    events: _containers.RepeatedCompositeFieldContainer[ActivityLog.Event]
    def __init__(self, name: _Optional[str] = ..., scope: _Optional[str] = ..., request_id: _Optional[int] = ..., authentication: _Optional[_Union[_common_pb2.Authentication, _Mapping]] = ..., authorization: _Optional[_Union[_common_pb2.Authorization, _Mapping]] = ..., service: _Optional[_Union[_common_pb2.ServiceData, _Mapping]] = ..., method: _Optional[_Union[ActivityLog.Method, _Mapping]] = ..., request_metadata: _Optional[_Union[ActivityLog.RequestMetadata, _Mapping]] = ..., request_routing: _Optional[_Union[ActivityLog.RequestRouting, _Mapping]] = ..., resource: _Optional[_Union[ActivityLog.Resource, _Mapping]] = ..., category: _Optional[_Union[ActivityLog.Category, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., events: _Optional[_Iterable[_Union[ActivityLog.Event, _Mapping]]] = ...) -> None: ...
