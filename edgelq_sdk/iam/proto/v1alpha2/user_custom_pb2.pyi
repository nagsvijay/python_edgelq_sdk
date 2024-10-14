from edgelq_sdk.iam.proto.v1alpha2 import user_pb2 as _user_pb2
from edgelq_sdk.iam.proto.v1alpha2 import user_change_pb2 as _user_change_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserByEmailRequest(_message.Message):
    __slots__ = ("email", "field_mask", "view", "skip_cache")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    email: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    skip_cache: bool
    def __init__(self, email: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., skip_cache: bool = ...) -> None: ...

class BatchGetUsersByEmailRequest(_message.Message):
    __slots__ = ("emails", "field_mask", "view", "skip_cache")
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    emails: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    skip_cache: bool
    def __init__(self, emails: _Optional[_Iterable[str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., skip_cache: bool = ...) -> None: ...

class BatchGetUsersByEmailResponse(_message.Message):
    __slots__ = ("users", "missing")
    USERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    missing: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., missing: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMySettingsRequest(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMySettingsResponse(_message.Message):
    __slots__ = ("settings",)
    class SettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.ScalarMap[str, str]
    def __init__(self, settings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SetMySettingsRequest(_message.Message):
    __slots__ = ("settings",)
    class SettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.ScalarMap[str, str]
    def __init__(self, settings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RefreshUserFromIdTokenRequest(_message.Message):
    __slots__ = ("id_token",)
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    def __init__(self, id_token: _Optional[str] = ...) -> None: ...

class RefreshUserFromIdTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResendVerificationEmailRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsUserVerifiedRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetMFAIfRecoveryKeyUsedRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetUsersNameInAuth0Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
