from edgelq_sdk.monitoring.proto.v4 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Notification(_message.Message):
    __slots__ = ("name", "metadata", "alerting_policy", "alerts", "state")
    class State(_message.Message):
        __slots__ = ("is_resolved", "notification_state", "incident_notify_attempts_done", "resolution_notify_attempts_done", "alerts_lifetime", "resolution_notification_state", "lifecycle_completed")
        class NotificationState(_message.Message):
            __slots__ = ("notification_channel", "status", "error", "provider_data", "notify_attempts")
            class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[Notification.State.NotificationState.Status]
                PENDING: _ClassVar[Notification.State.NotificationState.Status]
                FAILED: _ClassVar[Notification.State.NotificationState.Status]
                SUPPRESSED: _ClassVar[Notification.State.NotificationState.Status]
                SENT: _ClassVar[Notification.State.NotificationState.Status]
                DELIVERED: _ClassVar[Notification.State.NotificationState.Status]
                ACKNOWLEDGED: _ClassVar[Notification.State.NotificationState.Status]
                UNACKNOWLEDGED: _ClassVar[Notification.State.NotificationState.Status]
            UNKNOWN: Notification.State.NotificationState.Status
            PENDING: Notification.State.NotificationState.Status
            FAILED: Notification.State.NotificationState.Status
            SUPPRESSED: Notification.State.NotificationState.Status
            SENT: Notification.State.NotificationState.Status
            DELIVERED: Notification.State.NotificationState.Status
            ACKNOWLEDGED: Notification.State.NotificationState.Status
            UNACKNOWLEDGED: Notification.State.NotificationState.Status
            class ProviderData(_message.Message):
                __slots__ = ("slack", "pager_duty")
                class Slack(_message.Message):
                    __slots__ = ("ts",)
                    TS_FIELD_NUMBER: _ClassVar[int]
                    ts: str
                    def __init__(self, ts: _Optional[str] = ...) -> None: ...
                class PagerDuty(_message.Message):
                    __slots__ = ("incident_key",)
                    INCIDENT_KEY_FIELD_NUMBER: _ClassVar[int]
                    incident_key: str
                    def __init__(self, incident_key: _Optional[str] = ...) -> None: ...
                SLACK_FIELD_NUMBER: _ClassVar[int]
                PAGER_DUTY_FIELD_NUMBER: _ClassVar[int]
                slack: Notification.State.NotificationState.ProviderData.Slack
                pager_duty: Notification.State.NotificationState.ProviderData.PagerDuty
                def __init__(self, slack: _Optional[_Union[Notification.State.NotificationState.ProviderData.Slack, _Mapping]] = ..., pager_duty: _Optional[_Union[Notification.State.NotificationState.ProviderData.PagerDuty, _Mapping]] = ...) -> None: ...
            NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            ERROR_FIELD_NUMBER: _ClassVar[int]
            PROVIDER_DATA_FIELD_NUMBER: _ClassVar[int]
            NOTIFY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            notification_channel: str
            status: Notification.State.NotificationState.Status
            error: str
            provider_data: Notification.State.NotificationState.ProviderData
            notify_attempts: int
            def __init__(self, notification_channel: _Optional[str] = ..., status: _Optional[_Union[Notification.State.NotificationState.Status, str]] = ..., error: _Optional[str] = ..., provider_data: _Optional[_Union[Notification.State.NotificationState.ProviderData, _Mapping]] = ..., notify_attempts: _Optional[int] = ...) -> None: ...
        IS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        INCIDENT_NOTIFY_ATTEMPTS_DONE_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_NOTIFY_ATTEMPTS_DONE_FIELD_NUMBER: _ClassVar[int]
        ALERTS_LIFETIME_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_NOTIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        LIFECYCLE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        is_resolved: bool
        notification_state: _containers.RepeatedCompositeFieldContainer[Notification.State.NotificationState]
        incident_notify_attempts_done: bool
        resolution_notify_attempts_done: bool
        alerts_lifetime: _common_pb2.TimeRange
        resolution_notification_state: _containers.RepeatedCompositeFieldContainer[Notification.State.NotificationState]
        lifecycle_completed: bool
        def __init__(self, is_resolved: bool = ..., notification_state: _Optional[_Iterable[_Union[Notification.State.NotificationState, _Mapping]]] = ..., incident_notify_attempts_done: bool = ..., resolution_notify_attempts_done: bool = ..., alerts_lifetime: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., resolution_notification_state: _Optional[_Iterable[_Union[Notification.State.NotificationState, _Mapping]]] = ..., lifecycle_completed: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALERTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    alerting_policy: str
    alerts: _containers.RepeatedScalarFieldContainer[str]
    state: Notification.State
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., alerting_policy: _Optional[str] = ..., alerts: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[Notification.State, _Mapping]] = ...) -> None: ...
