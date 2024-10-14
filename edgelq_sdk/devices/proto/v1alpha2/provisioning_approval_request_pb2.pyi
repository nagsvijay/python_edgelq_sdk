from google.api import resource_pb2 as _resource_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisioningApprovalRequest(_message.Message):
    __slots__ = ("name", "spec", "status", "metadata")
    class Spec(_message.Message):
        __slots__ = ("conclusion", "service_account")
        class Conclusion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONCLUSION_NOT_SPECIFIED: _ClassVar[ProvisioningApprovalRequest.Spec.Conclusion]
            APPROVED: _ClassVar[ProvisioningApprovalRequest.Spec.Conclusion]
            REVOKED: _ClassVar[ProvisioningApprovalRequest.Spec.Conclusion]
        CONCLUSION_NOT_SPECIFIED: ProvisioningApprovalRequest.Spec.Conclusion
        APPROVED: ProvisioningApprovalRequest.Spec.Conclusion
        REVOKED: ProvisioningApprovalRequest.Spec.Conclusion
        CONCLUSION_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        conclusion: ProvisioningApprovalRequest.Spec.Conclusion
        service_account: str
        def __init__(self, conclusion: _Optional[_Union[ProvisioningApprovalRequest.Spec.Conclusion, str]] = ..., service_account: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    spec: ProvisioningApprovalRequest.Spec
    status: ProvisioningApprovalRequest.Status
    metadata: _meta_pb2.Meta
    def __init__(self, name: _Optional[str] = ..., spec: _Optional[_Union[ProvisioningApprovalRequest.Spec, _Mapping]] = ..., status: _Optional[_Union[ProvisioningApprovalRequest.Status, _Mapping]] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
