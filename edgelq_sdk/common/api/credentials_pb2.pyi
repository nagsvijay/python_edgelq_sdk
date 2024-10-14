from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("user", "service_account")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user: User
    service_account: ServiceAccount
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("email", "access_token", "token_type", "refresh_token", "expiry")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    email: str
    access_token: str
    token_type: str
    refresh_token: str
    expiry: _timestamp_pb2.Timestamp
    def __init__(self, email: _Optional[str] = ..., access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ("type", "client_email", "private_key_id", "private_key")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    type: str
    client_email: str
    private_key_id: str
    private_key: str
    def __init__(self, type: _Optional[str] = ..., client_email: _Optional[str] = ..., private_key_id: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...
