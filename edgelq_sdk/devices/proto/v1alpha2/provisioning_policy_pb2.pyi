from edgelq_sdk.devices.proto.v1alpha2 import device_pb2 as _device_pb2
from edgelq_sdk.iam.proto.v1alpha2 import condition_pb2 as _condition_pb2
from edgelq_sdk.iam.proto.v1alpha2 import role_pb2 as _role_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisioningPolicy(_message.Message):
    __slots__ = ("name", "display_name", "spec", "status", "metadata")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[ProvisioningPolicy.Mode]
        UNATTENDED: _ClassVar[ProvisioningPolicy.Mode]
        MANUAL_APPROVAL: _ClassVar[ProvisioningPolicy.Mode]
    MODE_UNSPECIFIED: ProvisioningPolicy.Mode
    UNATTENDED: ProvisioningPolicy.Mode
    MANUAL_APPROVAL: ProvisioningPolicy.Mode
    class Spec(_message.Message):
        __slots__ = ("mode", "service_account", "device_name_format", "labels", "template", "identity_field_paths", "role", "condition")
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class Template(_message.Message):
            __slots__ = ("metadata", "spec", "public_listing_spec")
            METADATA_FIELD_NUMBER: _ClassVar[int]
            SPEC_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_LISTING_SPEC_FIELD_NUMBER: _ClassVar[int]
            metadata: _meta_pb2.Meta
            spec: _device_pb2.Device.Spec
            public_listing_spec: _device_pb2.Device.PublicListingSpec
            def __init__(self, metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[_device_pb2.Device.Spec, _Mapping]] = ..., public_listing_spec: _Optional[_Union[_device_pb2.Device.PublicListingSpec, _Mapping]] = ...) -> None: ...
        MODE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        IDENTITY_FIELD_PATHS_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        mode: ProvisioningPolicy.Mode
        service_account: str
        device_name_format: str
        labels: _containers.ScalarMap[str, str]
        template: ProvisioningPolicy.Spec.Template
        identity_field_paths: _containers.RepeatedScalarFieldContainer[str]
        role: str
        condition: str
        def __init__(self, mode: _Optional[_Union[ProvisioningPolicy.Mode, str]] = ..., service_account: _Optional[str] = ..., device_name_format: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., template: _Optional[_Union[ProvisioningPolicy.Spec.Template, _Mapping]] = ..., identity_field_paths: _Optional[_Iterable[str]] = ..., role: _Optional[str] = ..., condition: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    spec: ProvisioningPolicy.Spec
    status: ProvisioningPolicy.Status
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., spec: _Optional[_Union[ProvisioningPolicy.Spec, _Mapping]] = ..., status: _Optional[_Union[ProvisioningPolicy.Status, _Mapping]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
