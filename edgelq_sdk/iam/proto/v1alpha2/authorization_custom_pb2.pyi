from edgelq_sdk.iam.proto.v1alpha2 import condition_pb2 as _condition_pb2
from edgelq_sdk.iam.proto.v1alpha2 import permission_pb2 as _permission_pb2
from edgelq_sdk.iam.proto.v1alpha2 import permission_change_pb2 as _permission_change_pb2
from edgelq_sdk.iam.proto.v1alpha2 import role_pb2 as _role_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Check(_message.Message):
    __slots__ = ("object", "permissions")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    object: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class ConditionalGrant(_message.Message):
    __slots__ = ("permissions", "condition_bindings")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    condition_bindings: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ConditionBinding]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ..., condition_bindings: _Optional[_Iterable[_Union[_condition_pb2.ConditionBinding, _Mapping]]] = ...) -> None: ...

class CheckResult(_message.Message):
    __slots__ = ("object", "granted_permissions", "conditionally_granted_permissions")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GRANTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONALLY_GRANTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    object: str
    granted_permissions: _containers.RepeatedScalarFieldContainer[str]
    conditionally_granted_permissions: _containers.RepeatedCompositeFieldContainer[ConditionalGrant]
    def __init__(self, object: _Optional[str] = ..., granted_permissions: _Optional[_Iterable[str]] = ..., conditionally_granted_permissions: _Optional[_Iterable[_Union[ConditionalGrant, _Mapping]]] = ...) -> None: ...

class CheckPermissionsRequest(_message.Message):
    __slots__ = ("member", "checks", "skip_cache")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    member: str
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    skip_cache: bool
    def __init__(self, member: _Optional[str] = ..., checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ..., skip_cache: bool = ...) -> None: ...

class CheckPermissionsResponse(_message.Message):
    __slots__ = ("check_results",)
    CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    check_results: _containers.RepeatedCompositeFieldContainer[CheckResult]
    def __init__(self, check_results: _Optional[_Iterable[_Union[CheckResult, _Mapping]]] = ...) -> None: ...

class CheckMyPermissionsRequest(_message.Message):
    __slots__ = ("checks", "skip_cache")
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    skip_cache: bool
    def __init__(self, checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ..., skip_cache: bool = ...) -> None: ...

class CheckMyPermissionsResponse(_message.Message):
    __slots__ = ("check_results",)
    CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    check_results: _containers.RepeatedCompositeFieldContainer[CheckResult]
    def __init__(self, check_results: _Optional[_Iterable[_Union[CheckResult, _Mapping]]] = ...) -> None: ...

class CheckMyRolesRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: str
    def __init__(self, object: _Optional[str] = ...) -> None: ...

class CheckMyRolesResponse(_message.Message):
    __slots__ = ("object", "granted_roles", "conditionally_granted_roles")
    class ConditionalGrant(_message.Message):
        __slots__ = ("role", "condition_bindings")
        ROLE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_BINDINGS_FIELD_NUMBER: _ClassVar[int]
        role: str
        condition_bindings: _containers.RepeatedCompositeFieldContainer[_condition_pb2.ConditionBinding]
        def __init__(self, role: _Optional[str] = ..., condition_bindings: _Optional[_Iterable[_Union[_condition_pb2.ConditionBinding, _Mapping]]] = ...) -> None: ...
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GRANTED_ROLES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONALLY_GRANTED_ROLES_FIELD_NUMBER: _ClassVar[int]
    object: str
    granted_roles: _containers.RepeatedScalarFieldContainer[str]
    conditionally_granted_roles: _containers.RepeatedCompositeFieldContainer[CheckMyRolesResponse.ConditionalGrant]
    def __init__(self, object: _Optional[str] = ..., granted_roles: _Optional[_Iterable[str]] = ..., conditionally_granted_roles: _Optional[_Iterable[_Union[CheckMyRolesResponse.ConditionalGrant, _Mapping]]] = ...) -> None: ...
