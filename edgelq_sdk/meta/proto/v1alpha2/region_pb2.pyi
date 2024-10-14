from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Region(_message.Message):
    __slots__ = ("name", "title", "domain", "location", "is_default", "connectivity_scores", "metadata")
    class RegionLocation(_message.Message):
        __slots__ = ("continent", "country", "agglomeration", "city", "cloud")
        CONTINENT_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        AGGLOMERATION_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        CLOUD_FIELD_NUMBER: _ClassVar[int]
        continent: str
        country: str
        agglomeration: str
        city: str
        cloud: str
        def __init__(self, continent: _Optional[str] = ..., country: _Optional[str] = ..., agglomeration: _Optional[str] = ..., city: _Optional[str] = ..., cloud: _Optional[str] = ...) -> None: ...
    class RegionConnectivityPreference(_message.Message):
        __slots__ = ("dest", "score")
        DEST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        dest: str
        score: int
        def __init__(self, dest: _Optional[str] = ..., score: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_SCORES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    domain: str
    location: Region.RegionLocation
    is_default: bool
    connectivity_scores: _containers.RepeatedCompositeFieldContainer[Region.RegionConnectivityPreference]
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., domain: _Optional[str] = ..., location: _Optional[_Union[Region.RegionLocation, _Mapping]] = ..., is_default: bool = ..., connectivity_scores: _Optional[_Iterable[_Union[Region.RegionConnectivityPreference, _Mapping]]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
