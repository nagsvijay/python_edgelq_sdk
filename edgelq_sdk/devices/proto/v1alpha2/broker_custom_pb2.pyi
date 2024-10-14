from edgelq_sdk.devices.proto.v1alpha2 import device_pb2 as _device_pb2
from edgelq_sdk.devices.proto.v1alpha2 import device_change_pb2 as _device_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrokerServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BROKER_SERVICE_UNSPECIFIED: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_SSH_LEGACY: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_SSH: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_TCP_FORWARD_PORT: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_REBOOT: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_SHUTDOWN: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_SCP: _ClassVar[BrokerServiceType]
    BROKER_SERVICE_SCP_LEGACY: _ClassVar[BrokerServiceType]
    BROKER_SYS_LOGS: _ClassVar[BrokerServiceType]
    BROKER_APP_LOGS: _ClassVar[BrokerServiceType]
    BROKER_POD_MANAGEMENT: _ClassVar[BrokerServiceType]
BROKER_SERVICE_UNSPECIFIED: BrokerServiceType
BROKER_SERVICE_SSH_LEGACY: BrokerServiceType
BROKER_SERVICE_SSH: BrokerServiceType
BROKER_SERVICE_TCP_FORWARD_PORT: BrokerServiceType
BROKER_SERVICE_REBOOT: BrokerServiceType
BROKER_SERVICE_SHUTDOWN: BrokerServiceType
BROKER_SERVICE_SCP: BrokerServiceType
BROKER_SERVICE_SCP_LEGACY: BrokerServiceType
BROKER_SYS_LOGS: BrokerServiceType
BROKER_APP_LOGS: BrokerServiceType
BROKER_POD_MANAGEMENT: BrokerServiceType

class ListenForConnectionsRequest(_message.Message):
    __slots__ = ("register_listener", "channel_open_error", "keep_alive")
    class RegisterListener(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: str
        def __init__(self, device: _Optional[str] = ...) -> None: ...
    class ChannelOpenError(_message.Message):
        __slots__ = ("channel", "message")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        channel: str
        message: str
        def __init__(self, channel: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    class KeepAlive(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    REGISTER_LISTENER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OPEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    register_listener: ListenForConnectionsRequest.RegisterListener
    channel_open_error: ListenForConnectionsRequest.ChannelOpenError
    keep_alive: ListenForConnectionsRequest.KeepAlive
    def __init__(self, register_listener: _Optional[_Union[ListenForConnectionsRequest.RegisterListener, _Mapping]] = ..., channel_open_error: _Optional[_Union[ListenForConnectionsRequest.ChannelOpenError, _Mapping]] = ..., keep_alive: _Optional[_Union[ListenForConnectionsRequest.KeepAlive, _Mapping]] = ...) -> None: ...

class ListenForConnectionsResponse(_message.Message):
    __slots__ = ("channel_requested", "keep_alive")
    class ChannelRequested(_message.Message):
        __slots__ = ("channel", "service", "arg")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        channel: str
        service: BrokerServiceType
        arg: str
        def __init__(self, channel: _Optional[str] = ..., service: _Optional[_Union[BrokerServiceType, str]] = ..., arg: _Optional[str] = ...) -> None: ...
    class KeepAlive(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CHANNEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    channel_requested: ListenForConnectionsResponse.ChannelRequested
    keep_alive: ListenForConnectionsResponse.KeepAlive
    def __init__(self, channel_requested: _Optional[_Union[ListenForConnectionsResponse.ChannelRequested, _Mapping]] = ..., keep_alive: _Optional[_Union[ListenForConnectionsResponse.KeepAlive, _Mapping]] = ...) -> None: ...

class OpenConnectionChannelSocketRequest(_message.Message):
    __slots__ = ("register_socket", "data", "error", "ack")
    class RegisterSocket(_message.Message):
        __slots__ = ("device", "channel")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        device: str
        channel: str
        def __init__(self, device: _Optional[str] = ..., channel: _Optional[str] = ...) -> None: ...
    REGISTER_SOCKET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    register_socket: OpenConnectionChannelSocketRequest.RegisterSocket
    data: bytes
    error: bytes
    ack: Ack
    def __init__(self, register_socket: _Optional[_Union[OpenConnectionChannelSocketRequest.RegisterSocket, _Mapping]] = ..., data: _Optional[bytes] = ..., error: _Optional[bytes] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ...) -> None: ...

class OpenConnectionChannelSocketResponse(_message.Message):
    __slots__ = ("data", "ack")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    ack: Ack
    def __init__(self, data: _Optional[bytes] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ...) -> None: ...

class ConnectToDeviceRequest(_message.Message):
    __slots__ = ("open_request", "data", "ack", "keep_alive")
    class OpenRequest(_message.Message):
        __slots__ = ("device", "service", "arg")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        device: str
        service: BrokerServiceType
        arg: str
        def __init__(self, device: _Optional[str] = ..., service: _Optional[_Union[BrokerServiceType, str]] = ..., arg: _Optional[str] = ...) -> None: ...
    class KeepAlive(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    OPEN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    open_request: ConnectToDeviceRequest.OpenRequest
    data: bytes
    ack: Ack
    keep_alive: ConnectToDeviceRequest.KeepAlive
    def __init__(self, open_request: _Optional[_Union[ConnectToDeviceRequest.OpenRequest, _Mapping]] = ..., data: _Optional[bytes] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., keep_alive: _Optional[_Union[ConnectToDeviceRequest.KeepAlive, _Mapping]] = ...) -> None: ...

class ConnectToDeviceResponse(_message.Message):
    __slots__ = ("open_response", "data", "error", "ack")
    class OpenResponse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    OPEN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    open_response: ConnectToDeviceResponse.OpenResponse
    data: bytes
    error: bytes
    ack: Ack
    def __init__(self, open_response: _Optional[_Union[ConnectToDeviceResponse.OpenResponse, _Mapping]] = ..., data: _Optional[bytes] = ..., error: _Optional[bytes] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ("processed",)
    PROCESSED_FIELD_NUMBER: _ClassVar[int]
    processed: int
    def __init__(self, processed: _Optional[int] = ...) -> None: ...

class SSHService(_message.Message):
    __slots__ = ()
    class Hello(_message.Message):
        __slots__ = ("user", "command", "env")
        class EnvEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        USER_FIELD_NUMBER: _ClassVar[int]
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        user: str
        command: _containers.RepeatedScalarFieldContainer[str]
        env: _containers.ScalarMap[str, str]
        def __init__(self, user: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., env: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class TerminalSize(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class ClientOut(_message.Message):
        __slots__ = ("data", "ssh_hello", "ssh_resize_terminal")
        DATA_FIELD_NUMBER: _ClassVar[int]
        SSH_HELLO_FIELD_NUMBER: _ClassVar[int]
        SSH_RESIZE_TERMINAL_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        ssh_hello: SSHService.Hello
        ssh_resize_terminal: SSHService.TerminalSize
        def __init__(self, data: _Optional[bytes] = ..., ssh_hello: _Optional[_Union[SSHService.Hello, _Mapping]] = ..., ssh_resize_terminal: _Optional[_Union[SSHService.TerminalSize, _Mapping]] = ...) -> None: ...
    class ClientIn(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class SCPService(_message.Message):
    __slots__ = ("dir", "file", "eot", "config")
    class Configure(_message.Message):
        __slots__ = ("recursive", "direction", "path")
        class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DOWNLOAD: _ClassVar[SCPService.Configure.Direction]
            UPLOAD: _ClassVar[SCPService.Configure.Direction]
        DOWNLOAD: SCPService.Configure.Direction
        UPLOAD: SCPService.Configure.Direction
        RECURSIVE_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        recursive: bool
        direction: SCPService.Configure.Direction
        path: str
        def __init__(self, recursive: bool = ..., direction: _Optional[_Union[SCPService.Configure.Direction, str]] = ..., path: _Optional[str] = ...) -> None: ...
    class CreateDirectory(_message.Message):
        __slots__ = ("path", "mode")
        PATH_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        path: str
        mode: int
        def __init__(self, path: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...
    class CreateFile(_message.Message):
        __slots__ = ("init", "data", "eof")
        class Initialize(_message.Message):
            __slots__ = ("path", "mode", "size")
            PATH_FIELD_NUMBER: _ClassVar[int]
            MODE_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            path: str
            mode: int
            size: int
            def __init__(self, path: _Optional[str] = ..., mode: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
        INIT_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        EOF_FIELD_NUMBER: _ClassVar[int]
        init: SCPService.CreateFile.Initialize
        data: bytes
        eof: bool
        def __init__(self, init: _Optional[_Union[SCPService.CreateFile.Initialize, _Mapping]] = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...
    DIR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    EOT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    dir: SCPService.CreateDirectory
    file: SCPService.CreateFile
    eot: bool
    config: SCPService.Configure
    def __init__(self, dir: _Optional[_Union[SCPService.CreateDirectory, _Mapping]] = ..., file: _Optional[_Union[SCPService.CreateFile, _Mapping]] = ..., eot: bool = ..., config: _Optional[_Union[SCPService.Configure, _Mapping]] = ...) -> None: ...

class LogsService(_message.Message):
    __slots__ = ()
    class ToDevice(_message.Message):
        __slots__ = ("follow", "lines", "source")
        FOLLOW_FIELD_NUMBER: _ClassVar[int]
        LINES_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        follow: bool
        lines: int
        source: str
        def __init__(self, follow: bool = ..., lines: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...
    class ToClient(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class PodManagementService(_message.Message):
    __slots__ = ("command", "pod", "service")
    class PodState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PodManagementService.PodState]
        START: _ClassVar[PodManagementService.PodState]
        STOP: _ClassVar[PodManagementService.PodState]
        RESTART: _ClassVar[PodManagementService.PodState]
    UNSPECIFIED: PodManagementService.PodState
    START: PodManagementService.PodState
    STOP: PodManagementService.PodState
    RESTART: PodManagementService.PodState
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    command: PodManagementService.PodState
    pod: str
    service: str
    def __init__(self, command: _Optional[_Union[PodManagementService.PodState, str]] = ..., pod: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class SystemStateService(_message.Message):
    __slots__ = ()
    class SystemState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SystemStateService.SystemState]
        SHUTDOWN: _ClassVar[SystemStateService.SystemState]
        REBOOT: _ClassVar[SystemStateService.SystemState]
    UNSPECIFIED: SystemStateService.SystemState
    SHUTDOWN: SystemStateService.SystemState
    REBOOT: SystemStateService.SystemState
    def __init__(self) -> None: ...
