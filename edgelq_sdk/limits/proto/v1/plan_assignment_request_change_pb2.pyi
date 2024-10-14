from edgelq_sdk.limits.proto.v1 import plan_assignment_request_pb2 as _plan_assignment_request_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanAssignmentRequestChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("plan_assignment_request", "view_index")
        PLAN_ASSIGNMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        plan_assignment_request: _plan_assignment_request_pb2.PlanAssignmentRequest
        view_index: int
        def __init__(self, plan_assignment_request: _Optional[_Union[_plan_assignment_request_pb2.PlanAssignmentRequest, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "plan_assignment_request", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLAN_ASSIGNMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        plan_assignment_request: _plan_assignment_request_pb2.PlanAssignmentRequest
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., plan_assignment_request: _Optional[_Union[_plan_assignment_request_pb2.PlanAssignmentRequest, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("plan_assignment_request",)
        PLAN_ASSIGNMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
        plan_assignment_request: _plan_assignment_request_pb2.PlanAssignmentRequest
        def __init__(self, plan_assignment_request: _Optional[_Union[_plan_assignment_request_pb2.PlanAssignmentRequest, _Mapping]] = ...) -> None: ...
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
    added: PlanAssignmentRequestChange.Added
    modified: PlanAssignmentRequestChange.Modified
    current: PlanAssignmentRequestChange.Current
    removed: PlanAssignmentRequestChange.Removed
    def __init__(self, added: _Optional[_Union[PlanAssignmentRequestChange.Added, _Mapping]] = ..., modified: _Optional[_Union[PlanAssignmentRequestChange.Modified, _Mapping]] = ..., current: _Optional[_Union[PlanAssignmentRequestChange.Current, _Mapping]] = ..., removed: _Optional[_Union[PlanAssignmentRequestChange.Removed, _Mapping]] = ...) -> None: ...
