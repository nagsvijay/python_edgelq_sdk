from edgelq_sdk.iam.proto.v1 import project_invitation_pb2 as _project_invitation_pb2
from edgelq_sdk.iam.proto.v1 import project_invitation_change_pb2 as _project_invitation_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptProjectInvitationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AcceptProjectInvitationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeclineProjectInvitationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeclineProjectInvitationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMyProjectInvitationsRequest(_message.Message):
    __slots__ = ("parent", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListMyProjectInvitationsResponse(_message.Message):
    __slots__ = ("project_invitations",)
    PROJECT_INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    project_invitations: _containers.RepeatedCompositeFieldContainer[_project_invitation_pb2.ProjectInvitation]
    def __init__(self, project_invitations: _Optional[_Iterable[_Union[_project_invitation_pb2.ProjectInvitation, _Mapping]]] = ...) -> None: ...

class ResendProjectInvitationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResendProjectInvitationResponse(_message.Message):
    __slots__ = ("project_invitation",)
    PROJECT_INVITATION_FIELD_NUMBER: _ClassVar[int]
    project_invitation: _project_invitation_pb2.ProjectInvitation
    def __init__(self, project_invitation: _Optional[_Union[_project_invitation_pb2.ProjectInvitation, _Mapping]] = ...) -> None: ...
