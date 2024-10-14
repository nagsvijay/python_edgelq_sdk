from edgelq_sdk.devices.proto.v1 import device_pb2 as _device_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PodSpec(_message.Message):
    __slots__ = ("node", "containers", "host_network", "restart_policy", "image_pull_secrets", "volumes", "compose", "host_volume_mounts")
    class RestartPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTART_POLICY_UNSPECIFIED: _ClassVar[PodSpec.RestartPolicy]
        ALWAYS: _ClassVar[PodSpec.RestartPolicy]
        ON_FAILURE: _ClassVar[PodSpec.RestartPolicy]
        NEVER: _ClassVar[PodSpec.RestartPolicy]
    RESTART_POLICY_UNSPECIFIED: PodSpec.RestartPolicy
    ALWAYS: PodSpec.RestartPolicy
    ON_FAILURE: PodSpec.RestartPolicy
    NEVER: PodSpec.RestartPolicy
    class Container(_message.Message):
        __slots__ = ("args", "command", "env", "image", "image_pull_policy", "name", "resources", "security_context", "volume_mounts", "envFrom")
        class ResourceRequirements(_message.Message):
            __slots__ = ("limits", "requests")
            class LimitsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int
                def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
            class RequestsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int
                def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
            LIMITS_FIELD_NUMBER: _ClassVar[int]
            REQUESTS_FIELD_NUMBER: _ClassVar[int]
            limits: _containers.ScalarMap[str, int]
            requests: _containers.ScalarMap[str, int]
            def __init__(self, limits: _Optional[_Mapping[str, int]] = ..., requests: _Optional[_Mapping[str, int]] = ...) -> None: ...
        ARGS_FIELD_NUMBER: _ClassVar[int]
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_PULL_POLICY_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        VOLUME_MOUNTS_FIELD_NUMBER: _ClassVar[int]
        ENVFROM_FIELD_NUMBER: _ClassVar[int]
        args: _containers.RepeatedScalarFieldContainer[str]
        command: _containers.RepeatedScalarFieldContainer[str]
        env: _containers.RepeatedCompositeFieldContainer[EnvVar]
        image: str
        image_pull_policy: str
        name: str
        resources: PodSpec.Container.ResourceRequirements
        security_context: SecurityContext
        volume_mounts: _containers.RepeatedCompositeFieldContainer[VolumeMount]
        envFrom: EnvFromSource
        def __init__(self, args: _Optional[_Iterable[str]] = ..., command: _Optional[_Iterable[str]] = ..., env: _Optional[_Iterable[_Union[EnvVar, _Mapping]]] = ..., image: _Optional[str] = ..., image_pull_policy: _Optional[str] = ..., name: _Optional[str] = ..., resources: _Optional[_Union[PodSpec.Container.ResourceRequirements, _Mapping]] = ..., security_context: _Optional[_Union[SecurityContext, _Mapping]] = ..., volume_mounts: _Optional[_Iterable[_Union[VolumeMount, _Mapping]]] = ..., envFrom: _Optional[_Union[EnvFromSource, _Mapping]] = ...) -> None: ...
    NODE_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    HOST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    RESTART_POLICY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PULL_SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    COMPOSE_FIELD_NUMBER: _ClassVar[int]
    HOST_VOLUME_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    node: str
    containers: _containers.RepeatedCompositeFieldContainer[PodSpec.Container]
    host_network: bool
    restart_policy: PodSpec.RestartPolicy
    image_pull_secrets: _containers.RepeatedCompositeFieldContainer[LocalObjectReferenceSecret]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    compose: str
    host_volume_mounts: _containers.RepeatedCompositeFieldContainer[VolumeMount]
    def __init__(self, node: _Optional[str] = ..., containers: _Optional[_Iterable[_Union[PodSpec.Container, _Mapping]]] = ..., host_network: bool = ..., restart_policy: _Optional[_Union[PodSpec.RestartPolicy, str]] = ..., image_pull_secrets: _Optional[_Iterable[_Union[LocalObjectReferenceSecret, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., compose: _Optional[str] = ..., host_volume_mounts: _Optional[_Iterable[_Union[VolumeMount, _Mapping]]] = ...) -> None: ...

class EnvFromSource(_message.Message):
    __slots__ = ("prefix", "config_map_ref", "secret_ref")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MAP_REF_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    config_map_ref: ConfigMapEnvSource
    secret_ref: SecretEnvSource
    def __init__(self, prefix: _Optional[str] = ..., config_map_ref: _Optional[_Union[ConfigMapEnvSource, _Mapping]] = ..., secret_ref: _Optional[_Union[SecretEnvSource, _Mapping]] = ...) -> None: ...

class EnvVar(_message.Message):
    __slots__ = ("name", "value", "value_from")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FROM_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    value_from: EnvVarSource
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., value_from: _Optional[_Union[EnvVarSource, _Mapping]] = ...) -> None: ...

class ConfigMapEnvSource(_message.Message):
    __slots__ = ("name", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    optional: bool
    def __init__(self, name: _Optional[str] = ..., optional: bool = ...) -> None: ...

class SecretEnvSource(_message.Message):
    __slots__ = ("name", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    optional: bool
    def __init__(self, name: _Optional[str] = ..., optional: bool = ...) -> None: ...

class EnvVarSource(_message.Message):
    __slots__ = ("config_map_key_ref", "secret_key_ref")
    CONFIG_MAP_KEY_REF_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_REF_FIELD_NUMBER: _ClassVar[int]
    config_map_key_ref: ConfigMapKeySelector
    secret_key_ref: SecretKeySelector
    def __init__(self, config_map_key_ref: _Optional[_Union[ConfigMapKeySelector, _Mapping]] = ..., secret_key_ref: _Optional[_Union[SecretKeySelector, _Mapping]] = ...) -> None: ...

class ConfigMapKeySelector(_message.Message):
    __slots__ = ("name", "key", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    optional: bool
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., optional: bool = ...) -> None: ...

class SecretKeySelector(_message.Message):
    __slots__ = ("name", "key", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    optional: bool
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., optional: bool = ...) -> None: ...

class LocalObjectReferenceSecret(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SecurityContext(_message.Message):
    __slots__ = ("privileged",)
    PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    privileged: bool
    def __init__(self, privileged: bool = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("name", "host_path", "secret", "config_map")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_PATH_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
    name: str
    host_path: HostPathVolumeSource
    secret: SecretVolumeSource
    config_map: ConfigMapVolumeSource
    def __init__(self, name: _Optional[str] = ..., host_path: _Optional[_Union[HostPathVolumeSource, _Mapping]] = ..., secret: _Optional[_Union[SecretVolumeSource, _Mapping]] = ..., config_map: _Optional[_Union[ConfigMapVolumeSource, _Mapping]] = ...) -> None: ...

class VolumeMount(_message.Message):
    __slots__ = ("name", "read_only", "mount_path", "sub_path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    SUB_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_only: bool
    mount_path: str
    sub_path: str
    def __init__(self, name: _Optional[str] = ..., read_only: bool = ..., mount_path: _Optional[str] = ..., sub_path: _Optional[str] = ...) -> None: ...

class HostPathVolumeSource(_message.Message):
    __slots__ = ("path", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[HostPathVolumeSource.Type]
        DIRECTORY_OR_CREATE: _ClassVar[HostPathVolumeSource.Type]
        DIRECTORY: _ClassVar[HostPathVolumeSource.Type]
        FILE_OR_CREATE: _ClassVar[HostPathVolumeSource.Type]
        FILE: _ClassVar[HostPathVolumeSource.Type]
        SOCKET: _ClassVar[HostPathVolumeSource.Type]
        CHAR_DEVICE: _ClassVar[HostPathVolumeSource.Type]
        BLOCK_DEVICE: _ClassVar[HostPathVolumeSource.Type]
    TYPE_UNSPECIFIED: HostPathVolumeSource.Type
    DIRECTORY_OR_CREATE: HostPathVolumeSource.Type
    DIRECTORY: HostPathVolumeSource.Type
    FILE_OR_CREATE: HostPathVolumeSource.Type
    FILE: HostPathVolumeSource.Type
    SOCKET: HostPathVolumeSource.Type
    CHAR_DEVICE: HostPathVolumeSource.Type
    BLOCK_DEVICE: HostPathVolumeSource.Type
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    path: str
    type: HostPathVolumeSource.Type
    def __init__(self, path: _Optional[str] = ..., type: _Optional[_Union[HostPathVolumeSource.Type, str]] = ...) -> None: ...

class SecretVolumeSource(_message.Message):
    __slots__ = ("secret_name", "items", "default_mode", "optional")
    SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    secret_name: str
    items: _containers.RepeatedCompositeFieldContainer[KeyToPath]
    default_mode: int
    optional: bool
    def __init__(self, secret_name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[KeyToPath, _Mapping]]] = ..., default_mode: _Optional[int] = ..., optional: bool = ...) -> None: ...

class KeyToPath(_message.Message):
    __slots__ = ("key", "path", "mode")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    key: str
    path: str
    mode: int
    def __init__(self, key: _Optional[str] = ..., path: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...

class ConfigMapVolumeSource(_message.Message):
    __slots__ = ("name", "items", "default_mode", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    items: _containers.RepeatedCompositeFieldContainer[KeyToPath]
    default_mode: int
    optional: bool
    def __init__(self, name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[KeyToPath, _Mapping]]] = ..., default_mode: _Optional[int] = ..., optional: bool = ...) -> None: ...
