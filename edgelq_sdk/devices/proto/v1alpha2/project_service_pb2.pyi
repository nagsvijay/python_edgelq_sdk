from edgelq_sdk.devices.proto.v1alpha2 import project_pb2 as _project_pb2
from edgelq_sdk.devices.proto.v1alpha2 import project_change_pb2 as _project_change_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from goten_sdk.types import watch_type_pb2 as _watch_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProjectRequest(_message.Message):
    __slots__ = ("name", "field_mask", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class BatchGetProjectsRequest(_message.Message):
    __slots__ = ("names", "field_mask", "view")
    NAMES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, names: _Optional[_Iterable[str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class BatchGetProjectsResponse(_message.Message):
    __slots__ = ("projects", "missing")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    missing: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, projects: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ..., missing: _Optional[_Iterable[str]] = ...) -> None: ...

class ListProjectsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "order_by", "filter", "field_mask", "view", "include_paging_info")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAGING_INFO_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    order_by: str
    filter: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    include_paging_info: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., include_paging_info: bool = ...) -> None: ...

class ListProjectsResponse(_message.Message):
    __slots__ = ("projects", "prev_page_token", "next_page_token", "current_offset", "total_results_count")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    prev_page_token: str
    next_page_token: str
    current_offset: int
    total_results_count: int
    def __init__(self, projects: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ..., current_offset: _Optional[int] = ..., total_results_count: _Optional[int] = ...) -> None: ...

class WatchProjectRequest(_message.Message):
    __slots__ = ("name", "field_mask", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...

class WatchProjectResponse(_message.Message):
    __slots__ = ("change",)
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    change: _project_change_pb2.ProjectChange
    def __init__(self, change: _Optional[_Union[_project_change_pb2.ProjectChange, _Mapping]] = ...) -> None: ...

class WatchProjectsRequest(_message.Message):
    __slots__ = ("type", "page_size", "page_token", "order_by", "resume_token", "starting_time", "filter", "field_mask", "view", "max_chunk_size")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STARTING_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    type: _watch_type_pb2.WatchType
    page_size: int
    page_token: str
    order_by: str
    resume_token: str
    starting_time: _timestamp_pb2.Timestamp
    filter: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    max_chunk_size: int
    def __init__(self, type: _Optional[_Union[_watch_type_pb2.WatchType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., resume_token: _Optional[str] = ..., starting_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ..., max_chunk_size: _Optional[int] = ...) -> None: ...

class WatchProjectsResponse(_message.Message):
    __slots__ = ("project_changes", "is_current", "page_token_change", "resume_token", "snapshot_size", "is_soft_reset", "is_hard_reset")
    class PageTokenChange(_message.Message):
        __slots__ = ("prev_page_token", "next_page_token")
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        prev_page_token: str
        next_page_token: str
        def __init__(self, prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    PROJECT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_SOFT_RESET_FIELD_NUMBER: _ClassVar[int]
    IS_HARD_RESET_FIELD_NUMBER: _ClassVar[int]
    project_changes: _containers.RepeatedCompositeFieldContainer[_project_change_pb2.ProjectChange]
    is_current: bool
    page_token_change: WatchProjectsResponse.PageTokenChange
    resume_token: str
    snapshot_size: int
    is_soft_reset: bool
    is_hard_reset: bool
    def __init__(self, project_changes: _Optional[_Iterable[_Union[_project_change_pb2.ProjectChange, _Mapping]]] = ..., is_current: bool = ..., page_token_change: _Optional[_Union[WatchProjectsResponse.PageTokenChange, _Mapping]] = ..., resume_token: _Optional[str] = ..., snapshot_size: _Optional[int] = ..., is_soft_reset: bool = ..., is_hard_reset: bool = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ("project", "update_mask", "cas", "allow_missing")
    class CAS(_message.Message):
        __slots__ = ("conditional_state", "field_mask")
        CONDITIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        conditional_state: _project_pb2.Project
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, conditional_state: _Optional[_Union[_project_pb2.Project, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CAS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    update_mask: _field_mask_pb2.FieldMask
    cas: UpdateProjectRequest.CAS
    allow_missing: bool
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cas: _Optional[_Union[UpdateProjectRequest.CAS, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
