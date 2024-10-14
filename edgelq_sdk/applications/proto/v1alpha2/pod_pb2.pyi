from edgelq_sdk.applications.proto.v1alpha2 import common_pb2 as _common_pb2
from edgelq_sdk.devices.proto.v1alpha2 import device_pb2 as _device_pb2
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

class Pod(_message.Message):
    __slots__ = ("name", "display_name", "metadata", "spec", "distribution", "status")
    class Status(_message.Message):
        __slots__ = ("phase", "container_statuses", "error")
        class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PHASE_UNSPECIFIED: _ClassVar[Pod.Status.Phase]
            PENDING: _ClassVar[Pod.Status.Phase]
            RUNNING: _ClassVar[Pod.Status.Phase]
            SUCCEEDED: _ClassVar[Pod.Status.Phase]
            FAILED: _ClassVar[Pod.Status.Phase]
            UNKNOWN: _ClassVar[Pod.Status.Phase]
        PHASE_UNSPECIFIED: Pod.Status.Phase
        PENDING: Pod.Status.Phase
        RUNNING: Pod.Status.Phase
        SUCCEEDED: Pod.Status.Phase
        FAILED: Pod.Status.Phase
        UNKNOWN: Pod.Status.Phase
        class Container(_message.Message):
            __slots__ = ("name", "state", "waiting", "running", "terminated")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[Pod.Status.Container.State]
                WAITING: _ClassVar[Pod.Status.Container.State]
                RUNNING: _ClassVar[Pod.Status.Container.State]
                TERMINATED: _ClassVar[Pod.Status.Container.State]
                UNKNOWN: _ClassVar[Pod.Status.Container.State]
            STATE_UNSPECIFIED: Pod.Status.Container.State
            WAITING: Pod.Status.Container.State
            RUNNING: Pod.Status.Container.State
            TERMINATED: Pod.Status.Container.State
            UNKNOWN: Pod.Status.Container.State
            class StateWaiting(_message.Message):
                __slots__ = ("reason", "message")
                REASON_FIELD_NUMBER: _ClassVar[int]
                MESSAGE_FIELD_NUMBER: _ClassVar[int]
                reason: str
                message: str
                def __init__(self, reason: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
            class StateRunning(_message.Message):
                __slots__ = ("started_at",)
                STARTED_AT_FIELD_NUMBER: _ClassVar[int]
                started_at: _timestamp_pb2.Timestamp
                def __init__(self, started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
            class StateTerminated(_message.Message):
                __slots__ = ("exit_code", "signal", "reason", "message", "started_at", "finished_at", "container_id")
                EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
                SIGNAL_FIELD_NUMBER: _ClassVar[int]
                REASON_FIELD_NUMBER: _ClassVar[int]
                MESSAGE_FIELD_NUMBER: _ClassVar[int]
                STARTED_AT_FIELD_NUMBER: _ClassVar[int]
                FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
                CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
                exit_code: int
                signal: int
                reason: str
                message: str
                started_at: _timestamp_pb2.Timestamp
                finished_at: _timestamp_pb2.Timestamp
                container_id: str
                def __init__(self, exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., reason: _Optional[str] = ..., message: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., container_id: _Optional[str] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            WAITING_FIELD_NUMBER: _ClassVar[int]
            RUNNING_FIELD_NUMBER: _ClassVar[int]
            TERMINATED_FIELD_NUMBER: _ClassVar[int]
            name: str
            state: Pod.Status.Container.State
            waiting: Pod.Status.Container.StateWaiting
            running: Pod.Status.Container.StateRunning
            terminated: Pod.Status.Container.StateTerminated
            def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Pod.Status.Container.State, str]] = ..., waiting: _Optional[_Union[Pod.Status.Container.StateWaiting, _Mapping]] = ..., running: _Optional[_Union[Pod.Status.Container.StateRunning, _Mapping]] = ..., terminated: _Optional[_Union[Pod.Status.Container.StateTerminated, _Mapping]] = ...) -> None: ...
        PHASE_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_STATUSES_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        phase: Pod.Status.Phase
        container_statuses: _containers.RepeatedCompositeFieldContainer[Pod.Status.Container]
        error: str
        def __init__(self, phase: _Optional[_Union[Pod.Status.Phase, str]] = ..., container_statuses: _Optional[_Iterable[_Union[Pod.Status.Container, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metadata: _meta_pb2.Meta
    spec: _common_pb2.PodSpec
    distribution: str
    status: Pod.Status
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[_common_pb2.PodSpec, _Mapping]] = ..., distribution: _Optional[str] = ..., status: _Optional[_Union[Pod.Status, _Mapping]] = ...) -> None: ...
