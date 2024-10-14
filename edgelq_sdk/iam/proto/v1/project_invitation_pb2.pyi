from edgelq_sdk.iam.proto.v1 import invitation_pb2 as _invitation_pb2
from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectInvitation(_message.Message):
    __slots__ = ("name", "metadata", "project_display_name", "invitation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    project_display_name: str
    invitation: _invitation_pb2.Invitation
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., project_display_name: _Optional[str] = ..., invitation: _Optional[_Union[_invitation_pb2.Invitation, _Mapping]] = ...) -> None: ...
