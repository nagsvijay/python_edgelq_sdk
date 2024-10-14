from edgelq_sdk.limits.proto.v1alpha2 import accepted_plan_pb2 as _accepted_plan_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptedPlanChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("accepted_plan", "view_index")
        ACCEPTED_PLAN_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        accepted_plan: _accepted_plan_pb2.AcceptedPlan
        view_index: int
        def __init__(self, accepted_plan: _Optional[_Union[_accepted_plan_pb2.AcceptedPlan, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "accepted_plan", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ACCEPTED_PLAN_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        accepted_plan: _accepted_plan_pb2.AcceptedPlan
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., accepted_plan: _Optional[_Union[_accepted_plan_pb2.AcceptedPlan, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("accepted_plan",)
        ACCEPTED_PLAN_FIELD_NUMBER: _ClassVar[int]
        accepted_plan: _accepted_plan_pb2.AcceptedPlan
        def __init__(self, accepted_plan: _Optional[_Union[_accepted_plan_pb2.AcceptedPlan, _Mapping]] = ...) -> None: ...
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
    added: AcceptedPlanChange.Added
    modified: AcceptedPlanChange.Modified
    current: AcceptedPlanChange.Current
    removed: AcceptedPlanChange.Removed
    def __init__(self, added: _Optional[_Union[AcceptedPlanChange.Added, _Mapping]] = ..., modified: _Optional[_Union[AcceptedPlanChange.Modified, _Mapping]] = ..., current: _Optional[_Union[AcceptedPlanChange.Current, _Mapping]] = ..., removed: _Optional[_Union[AcceptedPlanChange.Removed, _Mapping]] = ...) -> None: ...
