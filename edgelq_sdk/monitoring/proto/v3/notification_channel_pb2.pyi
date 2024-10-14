from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannel(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "spec", "state", "description")
    class Spec(_message.Message):
        __slots__ = ("enabled", "type", "email", "slack", "webhook", "notification_language_code")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[NotificationChannel.Spec.Type]
            EMAIL: _ClassVar[NotificationChannel.Spec.Type]
            SLACK: _ClassVar[NotificationChannel.Spec.Type]
            WEBHOOK: _ClassVar[NotificationChannel.Spec.Type]
        TYPE_UNSPECIFIED: NotificationChannel.Spec.Type
        EMAIL: NotificationChannel.Spec.Type
        SLACK: NotificationChannel.Spec.Type
        WEBHOOK: NotificationChannel.Spec.Type
        class Email(_message.Message):
            __slots__ = ("addresses",)
            ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            addresses: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, addresses: _Optional[_Iterable[str]] = ...) -> None: ...
        class Slack(_message.Message):
            __slots__ = ("incoming_webhook",)
            INCOMING_WEBHOOK_FIELD_NUMBER: _ClassVar[int]
            incoming_webhook: str
            def __init__(self, incoming_webhook: _Optional[str] = ...) -> None: ...
        class PagerDuty(_message.Message):
            __slots__ = ("service_key",)
            SERVICE_KEY_FIELD_NUMBER: _ClassVar[int]
            service_key: str
            def __init__(self, service_key: _Optional[str] = ...) -> None: ...
        class Webhook(_message.Message):
            __slots__ = ("url", "headers")
            class Header(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            URL_FIELD_NUMBER: _ClassVar[int]
            HEADERS_FIELD_NUMBER: _ClassVar[int]
            url: str
            headers: _containers.RepeatedCompositeFieldContainer[NotificationChannel.Spec.Webhook.Header]
            def __init__(self, url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[NotificationChannel.Spec.Webhook.Header, _Mapping]]] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        SLACK_FIELD_NUMBER: _ClassVar[int]
        WEBHOOK_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        type: NotificationChannel.Spec.Type
        email: NotificationChannel.Spec.Email
        slack: NotificationChannel.Spec.Slack
        webhook: NotificationChannel.Spec.Webhook
        notification_language_code: str
        def __init__(self, enabled: bool = ..., type: _Optional[_Union[NotificationChannel.Spec.Type, str]] = ..., email: _Optional[_Union[NotificationChannel.Spec.Email, _Mapping]] = ..., slack: _Optional[_Union[NotificationChannel.Spec.Slack, _Mapping]] = ..., webhook: _Optional[_Union[NotificationChannel.Spec.Webhook, _Mapping]] = ..., notification_language_code: _Optional[str] = ...) -> None: ...
    class State(_message.Message):
        __slots__ = ("status", "error")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[NotificationChannel.State.Status]
            ACTIVE: _ClassVar[NotificationChannel.State.Status]
            DISABLED: _ClassVar[NotificationChannel.State.Status]
            ERROR: _ClassVar[NotificationChannel.State.Status]
        STATE_UNSPECIFIED: NotificationChannel.State.Status
        ACTIVE: NotificationChannel.State.Status
        DISABLED: NotificationChannel.State.Status
        ERROR: NotificationChannel.State.Status
        class Error(_message.Message):
            __slots__ = ("time", "message")
            TIME_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            time: _timestamp_pb2.Timestamp
            message: str
            def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        status: NotificationChannel.State.Status
        error: NotificationChannel.State.Error
        def __init__(self, status: _Optional[_Union[NotificationChannel.State.Status, str]] = ..., error: _Optional[_Union[NotificationChannel.State.Error, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    spec: NotificationChannel.Spec
    state: NotificationChannel.State
    description: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., spec: _Optional[_Union[NotificationChannel.Spec, _Mapping]] = ..., state: _Optional[_Union[NotificationChannel.State, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...
