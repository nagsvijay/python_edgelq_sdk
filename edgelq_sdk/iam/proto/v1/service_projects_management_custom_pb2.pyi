from edgelq_sdk.common.api import credentials_pb2 as _credentials_pb2
from edgelq_sdk.iam.proto.v1 import common_pb2 as _common_pb2
from edgelq_sdk.iam.proto.v1 import project_pb2 as _project_pb2
from edgelq_sdk.iam.proto.v1 import project_change_pb2 as _project_change_pb2
from edgelq_sdk.iam.proto.v1 import service_account_key_pb2 as _service_account_key_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from goten_sdk.meta_service.proto.v1 import service_pb2 as _service_pb2
from goten_sdk.types import multi_region_policy_pb2 as _multi_region_policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMyServiceProjectsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "order_by", "filter", "field_mask")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    order_by: str
    filter: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListMyServiceProjectsResponse(_message.Message):
    __slots__ = ("projects", "prev_page_token", "next_page_token")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    prev_page_token: str
    next_page_token: str
    def __init__(self, projects: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SetupServiceProjectRequest(_message.Message):
    __slots__ = ("name", "title", "parent_organization", "multi_region_policy", "default_business_tier", "core_edgelq_service_opt_outs", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BUSINESS_TIER_FIELD_NUMBER: _ClassVar[int]
    CORE_EDGELQ_SERVICE_OPT_OUTS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    parent_organization: str
    multi_region_policy: _multi_region_policy_pb2.MultiRegionPolicy
    default_business_tier: _common_pb2.BusinessTier
    core_edgelq_service_opt_outs: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., parent_organization: _Optional[str] = ..., multi_region_policy: _Optional[_Union[_multi_region_policy_pb2.MultiRegionPolicy, _Mapping]] = ..., default_business_tier: _Optional[_Union[_common_pb2.BusinessTier, str]] = ..., core_edgelq_service_opt_outs: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

class ReserveServiceNameRequest(_message.Message):
    __slots__ = ("name", "service", "admin_account", "admin_key", "admin_account_project_role")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ADMIN_KEY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ACCOUNT_PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    service: str
    admin_account: str
    admin_key: _service_account_key_pb2.ServiceAccountKey
    admin_account_project_role: str
    def __init__(self, name: _Optional[str] = ..., service: _Optional[str] = ..., admin_account: _Optional[str] = ..., admin_key: _Optional[_Union[_service_account_key_pb2.ServiceAccountKey, _Mapping]] = ..., admin_account_project_role: _Optional[str] = ...) -> None: ...

class ReserveServiceNameResponse(_message.Message):
    __slots__ = ("ntt_admin_credentials",)
    NTT_ADMIN_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ntt_admin_credentials: _credentials_pb2.ServiceAccount
    def __init__(self, ntt_admin_credentials: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...

class DeleteServiceReservationRequest(_message.Message):
    __slots__ = ("name", "service")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    service: str
    def __init__(self, name: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class ListServiceReservationsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListServiceReservationsResponse(_message.Message):
    __slots__ = ("reservations",)
    class Reservation(_message.Message):
        __slots__ = ("service", "admin_account")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ADMIN_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        service: str
        admin_account: str
        def __init__(self, service: _Optional[str] = ..., admin_account: _Optional[str] = ...) -> None: ...
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    reservations: _containers.RepeatedCompositeFieldContainer[ListServiceReservationsResponse.Reservation]
    def __init__(self, reservations: _Optional[_Iterable[_Union[ListServiceReservationsResponse.Reservation, _Mapping]]] = ...) -> None: ...

class ListProjectServicesRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListProjectServicesResponse(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ...) -> None: ...

class AddRegionalAdminAccountForServicesRequest(_message.Message):
    __slots__ = ("parent", "services", "admin_account", "admin_key", "admin_account_project_role")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ADMIN_KEY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ACCOUNT_PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    services: _containers.RepeatedScalarFieldContainer[str]
    admin_account: str
    admin_key: _service_account_key_pb2.ServiceAccountKey
    admin_account_project_role: str
    def __init__(self, parent: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ..., admin_account: _Optional[str] = ..., admin_key: _Optional[_Union[_service_account_key_pb2.ServiceAccountKey, _Mapping]] = ..., admin_account_project_role: _Optional[str] = ...) -> None: ...

class AddRegionalAdminAccountForServicesResponse(_message.Message):
    __slots__ = ("ntt_admin_credentials",)
    NTT_ADMIN_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ntt_admin_credentials: _credentials_pb2.ServiceAccount
    def __init__(self, ntt_admin_credentials: _Optional[_Union[_credentials_pb2.ServiceAccount, _Mapping]] = ...) -> None: ...
