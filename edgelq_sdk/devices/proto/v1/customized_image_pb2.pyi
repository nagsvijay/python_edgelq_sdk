from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomizedImage(_message.Message):
    __slots__ = ("name", "metadata", "spec", "status")
    class Spec(_message.Message):
        __slots__ = ("version", "device_type", "provisioning_policy", "install_ai_accelerator", "password", "encryption", "encryption_password", "disk_mapping", "network_agent", "ntp", "http_proxy", "https_proxy", "no_proxy")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_POLICY_FIELD_NUMBER: _ClassVar[int]
        INSTALL_AI_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        DISK_MAPPING_FIELD_NUMBER: _ClassVar[int]
        NETWORK_AGENT_FIELD_NUMBER: _ClassVar[int]
        NTP_FIELD_NUMBER: _ClassVar[int]
        HTTP_PROXY_FIELD_NUMBER: _ClassVar[int]
        HTTPS_PROXY_FIELD_NUMBER: _ClassVar[int]
        NO_PROXY_FIELD_NUMBER: _ClassVar[int]
        version: str
        device_type: str
        provisioning_policy: str
        install_ai_accelerator: bool
        password: str
        encryption: bool
        encryption_password: str
        disk_mapping: str
        network_agent: str
        ntp: str
        http_proxy: str
        https_proxy: str
        no_proxy: str
        def __init__(self, version: _Optional[str] = ..., device_type: _Optional[str] = ..., provisioning_policy: _Optional[str] = ..., install_ai_accelerator: bool = ..., password: _Optional[str] = ..., encryption: bool = ..., encryption_password: _Optional[str] = ..., disk_mapping: _Optional[str] = ..., network_agent: _Optional[str] = ..., ntp: _Optional[str] = ..., http_proxy: _Optional[str] = ..., https_proxy: _Optional[str] = ..., no_proxy: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("state", "log", "file")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[CustomizedImage.Status.State]
            IN_PROGRESS: _ClassVar[CustomizedImage.Status.State]
            ERROR: _ClassVar[CustomizedImage.Status.State]
            READY: _ClassVar[CustomizedImage.Status.State]
        STATE_UNSPECIFIED: CustomizedImage.Status.State
        IN_PROGRESS: CustomizedImage.Status.State
        ERROR: CustomizedImage.Status.State
        READY: CustomizedImage.Status.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        LOG_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        state: CustomizedImage.Status.State
        log: str
        file: str
        def __init__(self, state: _Optional[_Union[CustomizedImage.Status.State, str]] = ..., log: _Optional[str] = ..., file: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    spec: CustomizedImage.Spec
    status: CustomizedImage.Status
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[CustomizedImage.Spec, _Mapping]] = ..., status: _Optional[_Union[CustomizedImage.Status, _Mapping]] = ...) -> None: ...
