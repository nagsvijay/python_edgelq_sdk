from goten_sdk.meta_service.proto.v1 import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegionalPlanAssignment(_message.Message):
    __slots__ = ("plan", "region", "plan_generation")
    PLAN_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PLAN_GENERATION_FIELD_NUMBER: _ClassVar[int]
    plan: str
    region: str
    plan_generation: int
    def __init__(self, plan: _Optional[str] = ..., region: _Optional[str] = ..., plan_generation: _Optional[int] = ...) -> None: ...

class Allowance(_message.Message):
    __slots__ = ("resource", "value", "region")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    value: int
    region: str
    def __init__(self, resource: _Optional[str] = ..., value: _Optional[int] = ..., region: _Optional[str] = ...) -> None: ...
