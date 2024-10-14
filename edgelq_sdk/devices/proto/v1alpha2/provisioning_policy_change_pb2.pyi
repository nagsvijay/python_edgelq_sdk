from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_pb2 as _provisioning_policy_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisioningPolicyChange(_message.Message):
    __slots__ = ("added", "modified", "current", "removed")
    class Added(_message.Message):
        __slots__ = ("provisioning_policy", "view_index")
        PROVISIONING_POLICY_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        provisioning_policy: _provisioning_policy_pb2.ProvisioningPolicy
        view_index: int
        def __init__(self, provisioning_policy: _Optional[_Union[_provisioning_policy_pb2.ProvisioningPolicy, _Mapping]] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Modified(_message.Message):
        __slots__ = ("name", "provisioning_policy", "field_mask", "previous_view_index", "view_index")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_POLICY_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
        name: str
        provisioning_policy: _provisioning_policy_pb2.ProvisioningPolicy
        field_mask: _field_mask_pb2.FieldMask
        previous_view_index: int
        view_index: int
        def __init__(self, name: _Optional[str] = ..., provisioning_policy: _Optional[_Union[_provisioning_policy_pb2.ProvisioningPolicy, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., previous_view_index: _Optional[int] = ..., view_index: _Optional[int] = ...) -> None: ...
    class Current(_message.Message):
        __slots__ = ("provisioning_policy",)
        PROVISIONING_POLICY_FIELD_NUMBER: _ClassVar[int]
        provisioning_policy: _provisioning_policy_pb2.ProvisioningPolicy
        def __init__(self, provisioning_policy: _Optional[_Union[_provisioning_policy_pb2.ProvisioningPolicy, _Mapping]] = ...) -> None: ...
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
    added: ProvisioningPolicyChange.Added
    modified: ProvisioningPolicyChange.Modified
    current: ProvisioningPolicyChange.Current
    removed: ProvisioningPolicyChange.Removed
    def __init__(self, added: _Optional[_Union[ProvisioningPolicyChange.Added, _Mapping]] = ..., modified: _Optional[_Union[ProvisioningPolicyChange.Modified, _Mapping]] = ..., current: _Optional[_Union[ProvisioningPolicyChange.Current, _Mapping]] = ..., removed: _Optional[_Union[ProvisioningPolicyChange.Removed, _Mapping]] = ...) -> None: ...
