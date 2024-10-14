from edgelq_sdk.secrets.proto.v1 import crypto_key_pb2 as _crypto_key_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoKeyChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("crypto_key", "view_index")
        CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        crypto_key: _crypto_key_pb2.CryptoKey
        view_index: int
        def __init__(self, crypto_key: _Optional[_Union[_crypto_key_pb2.CryptoKey, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "crypto_key", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        crypto_key: _crypto_key_pb2.CryptoKey
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., crypto_key: _Optional[_Union[_crypto_key_pb2.CryptoKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("crypto_key",)
        CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
        crypto_key: _crypto_key_pb2.CryptoKey
        def __init__(self, crypto_key: _Optional[_Union[_crypto_key_pb2.CryptoKey, _Mapping]] = ...) -> None: ...
    class Removed(_message.Message):
        __slots__ = ("name", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        view_index: int
        def __init__(self, name: _Optional[str] = ..., view_index: _Optional[int] = ...) -> None: ...
    ADDED_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    added: CryptoKeyChange.Added
    modified: CryptoKeyChange.Modified
    current: CryptoKeyChange.Current
    removed: CryptoKeyChange.Removed
    def __init__(self, added: _Optional[_Union[CryptoKeyChange.Added, _Mapping]] = ..., modified: _Optional[_Union[CryptoKeyChange.Modified, _Mapping]] = ..., current: _Optional[_Union[CryptoKeyChange.Current, _Mapping]] = ..., removed: _Optional[_Union[CryptoKeyChange.Removed, _Mapping]] = ...) -> None: ...
