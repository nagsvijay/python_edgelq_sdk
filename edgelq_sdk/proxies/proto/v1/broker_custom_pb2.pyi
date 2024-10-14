from edgelq_sdk.proxies.proto.v1 import project_pb2 as _project_pb2
from edgelq_sdk.proxies.proto.v1 import project_change_pb2 as _project_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectRequest(_message.Message):
    __slots__ = ("open_request", "resume_request", "ack", "data", "close", "error", "ping")
    class OpenRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "provider_name", "name", "service", "arg")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        provider_name: str
        name: str
        service: str
        arg: bytes
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., provider_name: _Optional[str] = ..., name: _Optional[str] = ..., service: _Optional[str] = ..., arg: _Optional[bytes] = ...) -> None: ...
    class ResumeRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "provider_name", "name", "session_id", "channel_id", "last_message_id")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        provider_name: str
        name: str
        session_id: int
        channel_id: int
        last_message_id: int
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., provider_name: _Optional[str] = ..., name: _Optional[str] = ..., session_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., last_message_id: _Optional[int] = ...) -> None: ...
    OPEN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESUME_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    open_request: ConnectRequest.OpenRequest
    resume_request: ConnectRequest.ResumeRequest
    ack: Ack
    data: Data
    close: Close
    error: Error
    ping: Ping
    def __init__(self, open_request: _Optional[_Union[ConnectRequest.OpenRequest, _Mapping]] = ..., resume_request: _Optional[_Union[ConnectRequest.ResumeRequest, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ("open_response", "resume_response", "channel_open_error", "ack", "data", "close", "error", "pong")
    class OpenResponse(_message.Message):
        __slots__ = ("session_id", "channel_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        channel_id: int
        def __init__(self, session_id: _Optional[int] = ..., channel_id: _Optional[int] = ...) -> None: ...
    class ResumeResponse(_message.Message):
        __slots__ = ("session_id", "channel_id", "last_message_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        channel_id: int
        last_message_id: int
        def __init__(self, session_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., last_message_id: _Optional[int] = ...) -> None: ...
    class ChannelOpenError(_message.Message):
        __slots__ = ("channel_id", "message")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        message: str
        def __init__(self, channel_id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
    OPEN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESUME_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OPEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    open_response: ConnectResponse.OpenResponse
    resume_response: ConnectResponse.ResumeResponse
    channel_open_error: ConnectResponse.ChannelOpenError
    ack: Ack
    data: Data
    close: Close
    error: Error
    pong: Pong
    def __init__(self, open_response: _Optional[_Union[ConnectResponse.OpenResponse, _Mapping]] = ..., resume_response: _Optional[_Union[ConnectResponse.ResumeResponse, _Mapping]] = ..., channel_open_error: _Optional[_Union[ConnectResponse.ChannelOpenError, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ...) -> None: ...

class ListenRequest(_message.Message):
    __slots__ = ("open_request", "resume_request", "channel_open_error", "ping")
    class OpenRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "name")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        name: str
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class ResumeRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "name", "session_id")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        name: str
        session_id: int
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., name: _Optional[str] = ..., session_id: _Optional[int] = ...) -> None: ...
    class ChannelOpenError(_message.Message):
        __slots__ = ("channel_id", "message")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        message: str
        def __init__(self, channel_id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
    OPEN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESUME_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OPEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    open_request: ListenRequest.OpenRequest
    resume_request: ListenRequest.ResumeRequest
    channel_open_error: ListenRequest.ChannelOpenError
    ping: Ping
    def __init__(self, open_request: _Optional[_Union[ListenRequest.OpenRequest, _Mapping]] = ..., resume_request: _Optional[_Union[ListenRequest.ResumeRequest, _Mapping]] = ..., channel_open_error: _Optional[_Union[ListenRequest.ChannelOpenError, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class ListenResponse(_message.Message):
    __slots__ = ("listening", "open_channel_response", "resume_channel_response", "pong")
    class Listening(_message.Message):
        __slots__ = ("session_id",)
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        def __init__(self, session_id: _Optional[int] = ...) -> None: ...
    class OpenChannelResponse(_message.Message):
        __slots__ = ("channel_id", "service", "arg")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        service: str
        arg: bytes
        def __init__(self, channel_id: _Optional[int] = ..., service: _Optional[str] = ..., arg: _Optional[bytes] = ...) -> None: ...
    class ResumeChannelResponse(_message.Message):
        __slots__ = ("channel_id", "service", "arg", "last_message_id")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        service: str
        arg: bytes
        last_message_id: int
        def __init__(self, channel_id: _Optional[int] = ..., service: _Optional[str] = ..., arg: _Optional[bytes] = ..., last_message_id: _Optional[int] = ...) -> None: ...
    LISTENING_FIELD_NUMBER: _ClassVar[int]
    OPEN_CHANNEL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESUME_CHANNEL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    listening: ListenResponse.Listening
    open_channel_response: ListenResponse.OpenChannelResponse
    resume_channel_response: ListenResponse.ResumeChannelResponse
    pong: Pong
    def __init__(self, listening: _Optional[_Union[ListenResponse.Listening, _Mapping]] = ..., open_channel_response: _Optional[_Union[ListenResponse.OpenChannelResponse, _Mapping]] = ..., resume_channel_response: _Optional[_Union[ListenResponse.ResumeChannelResponse, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ...) -> None: ...

class AcceptRequest(_message.Message):
    __slots__ = ("open_request", "resume_request", "data", "ack", "close", "error", "ping")
    class OpenRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "name", "session_id", "channel_id")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        name: str
        session_id: int
        channel_id: int
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., name: _Optional[str] = ..., session_id: _Optional[int] = ..., channel_id: _Optional[int] = ...) -> None: ...
    class ResumeRequest(_message.Message):
        __slots__ = ("project", "region_id", "service_domain", "name", "session_id", "channel_id", "last_message_id")
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        project: str
        region_id: str
        service_domain: str
        name: str
        session_id: int
        channel_id: int
        last_message_id: int
        def __init__(self, project: _Optional[str] = ..., region_id: _Optional[str] = ..., service_domain: _Optional[str] = ..., name: _Optional[str] = ..., session_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., last_message_id: _Optional[int] = ...) -> None: ...
    OPEN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESUME_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    open_request: AcceptRequest.OpenRequest
    resume_request: AcceptRequest.ResumeRequest
    data: Data
    ack: Ack
    close: Close
    error: Error
    ping: Ping
    def __init__(self, open_request: _Optional[_Union[AcceptRequest.OpenRequest, _Mapping]] = ..., resume_request: _Optional[_Union[AcceptRequest.ResumeRequest, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class AcceptResponse(_message.Message):
    __slots__ = ("data", "ack", "close", "error", "pong")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    data: Data
    ack: Ack
    close: Close
    error: Error
    pong: Pong
    def __init__(self, data: _Optional[_Union[Data, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Pong(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Data(_message.Message):
    __slots__ = ("id", "bytes", "ack_required")
    ID_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    ACK_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    id: int
    bytes: bytes
    ack_required: bool
    def __init__(self, id: _Optional[int] = ..., bytes: _Optional[bytes] = ..., ack_required: bool = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Close(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    message: str
    def __init__(self, id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
