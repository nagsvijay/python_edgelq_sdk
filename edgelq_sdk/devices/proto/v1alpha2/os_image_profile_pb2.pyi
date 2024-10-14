from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OsImageProfile(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "device_type", "install_ai_accelerator", "encryption", "disk_mapping", "network_agent", "ntp", "http_proxy", "https_proxy", "no_proxy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_AI_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    DISK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_AGENT_FIELD_NUMBER: _ClassVar[int]
    NTP_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROXY_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PROXY_FIELD_NUMBER: _ClassVar[int]
    NO_PROXY_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    device_type: str
    install_ai_accelerator: bool
    encryption: bool
    disk_mapping: str
    network_agent: str
    ntp: str
    http_proxy: str
    https_proxy: str
    no_proxy: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., device_type: _Optional[str] = ..., install_ai_accelerator: bool = ..., encryption: bool = ..., disk_mapping: _Optional[str] = ..., network_agent: _Optional[str] = ..., ntp: _Optional[str] = ..., http_proxy: _Optional[str] = ..., https_proxy: _Optional[str] = ..., no_proxy: _Optional[str] = ...) -> None: ...
