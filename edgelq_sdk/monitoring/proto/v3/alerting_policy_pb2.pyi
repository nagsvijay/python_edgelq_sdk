from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertingPolicy(_message.Message):
    __slots__ = ("name", "metadata", "display_name", "description", "documentation", "spec", "state")
    class Documentation(_message.Message):
        __slots__ = ("content", "mime_type")
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        content: str
        mime_type: str
        def __init__(self, content: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...
    class Spec(_message.Message):
        __slots__ = ("enabled", "condition_combiner", "notification")
        class ConditionsCombiner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OR: _ClassVar[AlertingPolicy.Spec.ConditionsCombiner]
            AND: _ClassVar[AlertingPolicy.Spec.ConditionsCombiner]
        OR: AlertingPolicy.Spec.ConditionsCombiner
        AND: AlertingPolicy.Spec.ConditionsCombiner
        class Notification(_message.Message):
            __slots__ = ("enabled", "channels")
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            CHANNELS_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            channels: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, enabled: bool = ..., channels: _Optional[_Iterable[str]] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONDITION_COMBINER_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        condition_combiner: AlertingPolicy.Spec.ConditionsCombiner
        notification: AlertingPolicy.Spec.Notification
        def __init__(self, enabled: bool = ..., condition_combiner: _Optional[_Union[AlertingPolicy.Spec.ConditionsCombiner, str]] = ..., notification: _Optional[_Union[AlertingPolicy.Spec.Notification, _Mapping]] = ...) -> None: ...
    class State(_message.Message):
        __slots__ = ("active_alerts_count",)
        ACTIVE_ALERTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        active_alerts_count: int
        def __init__(self, active_alerts_count: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    display_name: str
    description: str
    documentation: AlertingPolicy.Documentation
    spec: AlertingPolicy.Spec
    state: AlertingPolicy.State
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., documentation: _Optional[_Union[AlertingPolicy.Documentation, _Mapping]] = ..., spec: _Optional[_Union[AlertingPolicy.Spec, _Mapping]] = ..., state: _Optional[_Union[AlertingPolicy.State, _Mapping]] = ...) -> None: ...
