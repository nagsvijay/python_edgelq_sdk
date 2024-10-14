from edgelq_sdk.iam.proto.v1 import organization_invitation_pb2 as _organization_invitation_pb2
from edgelq_sdk.iam.proto.v1 import organization_invitation_change_pb2 as _organization_invitation_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptOrganizationInvitationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AcceptOrganizationInvitationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeclineOrganizationInvitationRequest(_message.Message):
    __slots__ = ("name", "filter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    def __init__(self, name: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class DeclineOrganizationInvitationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMyOrganizationInvitationsRequest(_message.Message):
    __slots__ = ("parent", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListMyOrganizationInvitationsResponse(_message.Message):
    __slots__ = ("organization_invitations",)
    ORGANIZATION_INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    organization_invitations: _containers.RepeatedCompositeFieldContainer[_organization_invitation_pb2.OrganizationInvitation]
    def __init__(self, organization_invitations: _Optional[_Iterable[_Union[_organization_invitation_pb2.OrganizationInvitation, _Mapping]]] = ...) -> None: ...
