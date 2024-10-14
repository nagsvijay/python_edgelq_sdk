from edgelq_sdk.meta.proto.v1alpha2 import deployment_pb2 as _deployment_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("deployment", "view_index")
        DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        deployment: _deployment_pb2.Deployment
        view_index: int
        def __init__(self, deployment: _Optional[_Union[_deployment_pb2.Deployment, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "deployment", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        deployment: _deployment_pb2.Deployment
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., deployment: _Optional[_Union[_deployment_pb2.Deployment, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("deployment",)
        DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        deployment: _deployment_pb2.Deployment
        def __init__(self, deployment: _Optional[_Union[_deployment_pb2.Deployment, _Mapping]] = ...) -> None: ...
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
    added: DeploymentChange.Added
    modified: DeploymentChange.Modified
    current: DeploymentChange.Current
    removed: DeploymentChange.Removed
    def __init__(self, added: _Optional[_Union[DeploymentChange.Added, _Mapping]] = ..., modified: _Optional[_Union[DeploymentChange.Modified, _Mapping]] = ..., current: _Optional[_Union[DeploymentChange.Current, _Mapping]] = ..., removed: _Optional[_Union[DeploymentChange.Removed, _Mapping]] = ...) -> None: ...
