from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_pb2 as _plan_assignment_pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_change_pb2 as _plan_assignment_change_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MigratePlanAssignmentRequest(_message.Message):
    __slots__ = ("plan_assignment",)
    PLAN_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    plan_assignment: _plan_assignment_pb2.PlanAssignment
    def __init__(self, plan_assignment: _Optional[_Union[_plan_assignment_pb2.PlanAssignment, _Mapping]] = ...) -> None: ...
