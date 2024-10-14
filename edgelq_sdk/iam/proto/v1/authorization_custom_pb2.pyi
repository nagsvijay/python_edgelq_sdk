from edgelq_sdk.iam.proto.v1 import condition_pb2 as _condition_pb2
from edgelq_sdk.iam.proto.v1 import permission_pb2 as _permission_pb2
from edgelq_sdk.iam.proto.v1 import permission_change_pb2 as _permission_change_pb2
from edgelq_sdk.iam.proto.v1 import role_pb2 as _role_pb2
from edgelq_sdk.iam.proto.v1 import role_binding_pb2 as _role_binding_pb2
from edgelq_sdk.iam.proto.v1 import role_binding_change_pb2 as _role_binding_change_pb2
from edgelq_sdk.iam.proto.v1 import service_account_pb2 as _service_account_pb2
from edgelq_sdk.iam.proto.v1 import service_account_key_pb2 as _service_account_key_pb2
from edgelq_sdk.iam.proto.v1 import user_pb2 as _user_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPrincipalRequest(_message.Message):
    __slots__ = ("requesting_service", "principal_key_id", "auth_token")
    REQUESTING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    requesting_service: str
    principal_key_id: str
    auth_token: str
    def __init__(self, requesting_service: _Optional[str] = ..., principal_key_id: _Optional[str] = ..., auth_token: _Optional[str] = ...) -> None: ...

class GetPrincipalResponse(_message.Message):
    __slots__ = ("json_key", "principal_key_type", "user", "service_account", "anonymous")
    JSON_KEY_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    json_key: str
    principal_key_type: str
    user: _user_pb2.User
    service_account: _service_account_pb2.ServiceAccount
    anonymous: bool
    def __init__(self, json_key: _Optional[str] = ..., principal_key_type: _Optional[str] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ..., anonymous: bool = ...) -> None: ...

class WatchPrincipalUpdatesRequest(_message.Message):
    __slots__ = ("requesting_service", "resume_token")
    REQUESTING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    requesting_service: str
    resume_token: str
    def __init__(self, requesting_service: _Optional[str] = ..., resume_token: _Optional[str] = ...) -> None: ...

class WatchPrincipalUpdatesResponse(_message.Message):
    __slots__ = ("current_principals", "removed_principals", "is_current", "is_reset", "resume_token")
    class CurrentPrincipal(_message.Message):
        __slots__ = ("principal_key_id", "json_key", "principal_key_type", "user", "service_account")
        PRINCIPAL_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        JSON_KEY_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        principal_key_id: str
        json_key: str
        principal_key_type: str
        user: _user_pb2.User
        service_account: _service_account_pb2.ServiceAccount
        def __init__(self, principal_key_id: _Optional[str] = ..., json_key: _Optional[str] = ..., principal_key_type: _Optional[str] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., service_account: _Optional[_Union[_service_account_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...
    class RemovedPrincipal(_message.Message):
        __slots__ = ("principal_key_id",)
        PRINCIPAL_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        principal_key_id: str
        def __init__(self, principal_key_id: _Optional[str] = ...) -> None: ...
    CURRENT_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    IS_RESET_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    current_principals: _containers.RepeatedCompositeFieldContainer[WatchPrincipalUpdatesResponse.CurrentPrincipal]
    removed_principals: _containers.RepeatedCompositeFieldContainer[WatchPrincipalUpdatesResponse.RemovedPrincipal]
    is_current: bool
    is_reset: bool
    resume_token: str
    def __init__(self, current_principals: _Optional[_Iterable[_Union[WatchPrincipalUpdatesResponse.CurrentPrincipal, _Mapping]]] = ..., removed_principals: _Optional[_Iterable[_Union[WatchPrincipalUpdatesResponse.RemovedPrincipal, _Mapping]]] = ..., is_current: bool = ..., is_reset: bool = ..., resume_token: _Optional[str] = ...) -> None: ...

class CheckMyRoleBindingsRequest(_message.Message):
    __slots__ = ("parent", "filter", "custom_field_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    custom_field_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., custom_field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CheckMyRoleBindingsResponse(_message.Message):
    __slots__ = ("resolvable_grants",)
    class ResolvableGrant(_message.Message):
        __slots__ = ("role_binding", "grants")
        ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
        GRANTS_FIELD_NUMBER: _ClassVar[int]
        role_binding: _role_binding_pb2.RoleBinding
        grants: _containers.RepeatedCompositeFieldContainer[_role_pb2.Role.Grant]
        def __init__(self, role_binding: _Optional[_Union[_role_binding_pb2.RoleBinding, _Mapping]] = ..., grants: _Optional[_Iterable[_Union[_role_pb2.Role.Grant, _Mapping]]] = ...) -> None: ...
    RESOLVABLE_GRANTS_FIELD_NUMBER: _ClassVar[int]
    resolvable_grants: _containers.RepeatedCompositeFieldContainer[CheckMyRoleBindingsResponse.ResolvableGrant]
    def __init__(self, resolvable_grants: _Optional[_Iterable[_Union[CheckMyRoleBindingsResponse.ResolvableGrant, _Mapping]]] = ...) -> None: ...
