from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccountKey(_message.Message):
    __slots__ = ("name", "display_name", "public_key_data", "private_key_data", "api_key", "algorithm", "valid_not_before", "valid_not_after", "metadata")
    class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_ALGORITHM_UNSPECIFIED: _ClassVar[ServiceAccountKey.Algorithm]
        RSA_1024: _ClassVar[ServiceAccountKey.Algorithm]
        RSA_2048: _ClassVar[ServiceAccountKey.Algorithm]
        RSA_4096: _ClassVar[ServiceAccountKey.Algorithm]
        API_KEY: _ClassVar[ServiceAccountKey.Algorithm]
    KEY_ALGORITHM_UNSPECIFIED: ServiceAccountKey.Algorithm
    RSA_1024: ServiceAccountKey.Algorithm
    RSA_2048: ServiceAccountKey.Algorithm
    RSA_4096: ServiceAccountKey.Algorithm
    API_KEY: ServiceAccountKey.Algorithm
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    VALID_NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    VALID_NOT_AFTER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    public_key_data: str
    private_key_data: str
    api_key: str
    algorithm: ServiceAccountKey.Algorithm
    valid_not_before: _timestamp_pb2.Timestamp
    valid_not_after: _timestamp_pb2.Timestamp
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., public_key_data: _Optional[str] = ..., private_key_data: _Optional[str] = ..., api_key: _Optional[str] = ..., algorithm: _Optional[_Union[ServiceAccountKey.Algorithm, str]] = ..., valid_not_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_not_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
