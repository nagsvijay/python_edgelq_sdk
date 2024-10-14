from edgelq_sdk.iam.proto.v1 import condition_pb2 as _condition_pb2
from edgelq_sdk.iam.proto.v1 import role_pb2 as _role_pb2
from edgelq_sdk.iam.proto.v1 import role_binding_pb2 as _role_binding_pb2
from edgelq_sdk.iam.proto.v1 import service_account_pb2 as _service_account_pb2
from edgelq_sdk.iam.proto.v1 import user_pb2 as _user_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ("user", "service_account")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user: str
    service_account: str
    def __init__(self, user: _Optional[str] = ..., service_account: _Optional[str] = ...) -> None: ...

class Invitation(_message.Message):
    __slots__ = ("invitee_email", "inviter_actor", "inviter_full_name", "inviter_email", "language_code", "binding_roles", "expiration_date", "extras", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Invitation.State]
        PENDING: _ClassVar[Invitation.State]
        ACCEPTED: _ClassVar[Invitation.State]
        DECLINED: _ClassVar[Invitation.State]
        EXPIRED: _ClassVar[Invitation.State]
    STATE_UNSPECIFIED: Invitation.State
    PENDING: Invitation.State
    ACCEPTED: Invitation.State
    DECLINED: Invitation.State
    EXPIRED: Invitation.State
    class ExtrasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BindingRole(_message.Message):
        __slots__ = ("role", "executable_conditions", "scope_params")
        ROLE_FIELD_NUMBER: _ClassVar[int]
        EXECUTABLE_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        SCOPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        role: str
        executable_conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ExecutableCondition]
        scope_params: _containers.RepeatedCompositeFieldContainer[_role_pb2.ScopeParam]
        def __init__(self, role: _Optional[str] = ..., executable_conditions: _Optional[_Iterable[_Union[_condition_pb2.ExecutableCondition, _Mapping]]] = ..., scope_params: _Optional[_Iterable[_Union[_role_pb2.ScopeParam, _Mapping]]] = ...) -> None: ...
    INVITEE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    INVITER_ACTOR_FIELD_NUMBER: _ClassVar[int]
    INVITER_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    BINDING_ROLES_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    invitee_email: str
    inviter_actor: Actor
    inviter_full_name: str
    inviter_email: str
    language_code: str
    binding_roles: _containers.RepeatedCompositeFieldContainer[Invitation.BindingRole]
    expiration_date: _timestamp_pb2.Timestamp
    extras: _containers.ScalarMap[str, str]
    state: Invitation.State
    def __init__(self, invitee_email: _Optional[str] = ..., inviter_actor: _Optional[_Union[Actor, _Mapping]] = ..., inviter_full_name: _Optional[str] = ..., inviter_email: _Optional[str] = ..., language_code: _Optional[str] = ..., binding_roles: _Optional[_Iterable[_Union[Invitation.BindingRole, _Mapping]]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., extras: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[Invitation.State, str]] = ...) -> None: ...
