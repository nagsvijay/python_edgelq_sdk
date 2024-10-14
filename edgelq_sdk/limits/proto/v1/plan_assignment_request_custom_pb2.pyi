from edgelq_sdk.iam.proto.v1 import organization_pb2 as _organization_pb2
from edgelq_sdk.limits.proto.v1 import accepted_plan_pb2 as _accepted_plan_pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_request_pb2 as _plan_assignment_request_pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_request_change_pb2 as _plan_assignment_request_change_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.types import view_pb2 as _view_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptPlanAssignmentRequest(_message.Message):
    __slots__ = ("name", "approver")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    name: str
    approver: str
    def __init__(self, name: _Optional[str] = ..., approver: _Optional[str] = ...) -> None: ...

class AcceptPlanAssignmentResponse(_message.Message):
    __slots__ = ("accepted_plan",)
    ACCEPTED_PLAN_FIELD_NUMBER: _ClassVar[int]
    accepted_plan: _accepted_plan_pb2.AcceptedPlan
    def __init__(self, accepted_plan: _Optional[_Union[_accepted_plan_pb2.AcceptedPlan, _Mapping]] = ...) -> None: ...

class DeclinePlanAssignmentRequest(_message.Message):
    __slots__ = ("name", "approver", "reason")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    approver: str
    reason: str
    def __init__(self, name: _Optional[str] = ..., approver: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeclinePlanAssignmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListApproverPlanAssignmentRequestsRequest(_message.Message):
    __slots__ = ("approver", "page_size", "page_token", "order_by", "filter", "field_mask", "view")
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    approver: str
    page_size: int
    page_token: str
    order_by: str
    filter: str
    field_mask: _field_mask_pb2.FieldMask
    view: _view_pb2.View
    def __init__(self, approver: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., view: _Optional[_Union[_view_pb2.View, str]] = ...) -> None: ...
