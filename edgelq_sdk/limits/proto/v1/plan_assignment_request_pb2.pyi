from edgelq_sdk.iam.proto.v1 import organization_pb2 as _organization_pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from edgelq_sdk.limits.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.limits.proto.v1 import plan_pb2 as _plan_pb2
from edgelq_sdk.limits.proto.v1 import plan_assignment_pb2 as _plan_assignment_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanAssignmentRequest(_message.Message):
    __slots__ = ("name", "metadata", "request", "service", "approver", "status")
    class Status(_message.Message):
        __slots__ = ("conclusion", "reason")
        class Conclusion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNDEFINED: _ClassVar[PlanAssignmentRequest.Status.Conclusion]
            PENDING: _ClassVar[PlanAssignmentRequest.Status.Conclusion]
            APPROVED: _ClassVar[PlanAssignmentRequest.Status.Conclusion]
            REJECTED: _ClassVar[PlanAssignmentRequest.Status.Conclusion]
        UNDEFINED: PlanAssignmentRequest.Status.Conclusion
        PENDING: PlanAssignmentRequest.Status.Conclusion
        APPROVED: PlanAssignmentRequest.Status.Conclusion
        REJECTED: PlanAssignmentRequest.Status.Conclusion
        CONCLUSION_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        conclusion: PlanAssignmentRequest.Status.Conclusion
        reason: str
        def __init__(self, conclusion: _Optional[_Union[PlanAssignmentRequest.Status.Conclusion, str]] = ..., reason: _Optional[str] = ...) -> None: ...
    class RequestType(_message.Message):
        __slots__ = ("assign", "extend", "unassign")
        class Assign(_message.Message):
            __slots__ = ("plan", "extensions", "region")
            PLAN_FIELD_NUMBER: _ClassVar[int]
            EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
            REGION_FIELD_NUMBER: _ClassVar[int]
            plan: str
            extensions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
            region: str
            def __init__(self, plan: _Optional[str] = ..., extensions: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ..., region: _Optional[str] = ...) -> None: ...
        class Extend(_message.Message):
            __slots__ = ("assignment", "additions")
            ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
            ADDITIONS_FIELD_NUMBER: _ClassVar[int]
            assignment: str
            additions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Allowance]
            def __init__(self, assignment: _Optional[str] = ..., additions: _Optional[_Iterable[_Union[_common_pb2.Allowance, _Mapping]]] = ...) -> None: ...
        class Unassign(_message.Message):
            __slots__ = ("assignment", "region")
            ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
            REGION_FIELD_NUMBER: _ClassVar[int]
            assignment: str
            region: str
            def __init__(self, assignment: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
        ASSIGN_FIELD_NUMBER: _ClassVar[int]
        EXTEND_FIELD_NUMBER: _ClassVar[int]
        UNASSIGN_FIELD_NUMBER: _ClassVar[int]
        assign: PlanAssignmentRequest.RequestType.Assign
        extend: PlanAssignmentRequest.RequestType.Extend
        unassign: PlanAssignmentRequest.RequestType.Unassign
        def __init__(self, assign: _Optional[_Union[PlanAssignmentRequest.RequestType.Assign, _Mapping]] = ..., extend: _Optional[_Union[PlanAssignmentRequest.RequestType.Extend, _Mapping]] = ..., unassign: _Optional[_Union[PlanAssignmentRequest.RequestType.Unassign, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    request: PlanAssignmentRequest.RequestType
    service: str
    approver: str
    status: PlanAssignmentRequest.Status
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., request: _Optional[_Union[PlanAssignmentRequest.RequestType, _Mapping]] = ..., service: _Optional[str] = ..., approver: _Optional[str] = ..., status: _Optional[_Union[PlanAssignmentRequest.Status, _Mapping]] = ...) -> None: ...
