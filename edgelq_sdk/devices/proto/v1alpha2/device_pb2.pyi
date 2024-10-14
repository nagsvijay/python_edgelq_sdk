from edgelq_sdk.iam.proto.v1alpha2 import common_pb2 as _common_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from goten_sdk.types import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ("name", "metadata", "spec", "status", "public_listing_spec", "display_name")
    class Spec(_message.Message):
        __slots__ = ("service_account", "os_version", "netplan_config", "netplan_api_config_mode", "os_image_url", "ssh_config", "attestation_config", "disable_device_discovery", "logging_config", "proxy_config", "location")
        class NetworkConfigMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MERGE: _ClassVar[Device.Spec.NetworkConfigMode]
            REPLACE: _ClassVar[Device.Spec.NetworkConfigMode]
        MERGE: Device.Spec.NetworkConfigMode
        REPLACE: Device.Spec.NetworkConfigMode
        class NetworkingConfig(_message.Message):
            __slots__ = ("version", "renderer", "ethernets", "wifis", "bridges", "bonds", "tunnels", "vlans", "modems")
            class EthernetsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.EthOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.EthOpts, _Mapping]] = ...) -> None: ...
            class WifisEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.WifiOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.WifiOpts, _Mapping]] = ...) -> None: ...
            class BridgesEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.BridgesOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.BridgesOpts, _Mapping]] = ...) -> None: ...
            class BondsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.BondsOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.BondsOpts, _Mapping]] = ...) -> None: ...
            class TunnelsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.TunnelsOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.TunnelsOpts, _Mapping]] = ...) -> None: ...
            class VlansEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.VlansOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.VlansOpts, _Mapping]] = ...) -> None: ...
            class ModemsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Spec.NetworkingConfig.ModemOpts
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.ModemOpts, _Mapping]] = ...) -> None: ...
            class CommonOpts(_message.Message):
                __slots__ = ()
                class DHCPOverrides(_message.Message):
                    __slots__ = ("use_dns", "use_ntp", "send_hostname", "use_hostname", "use_mtu", "hostname", "use_routes", "route_metric")
                    USE_DNS_FIELD_NUMBER: _ClassVar[int]
                    USE_NTP_FIELD_NUMBER: _ClassVar[int]
                    SEND_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
                    USE_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
                    USE_MTU_FIELD_NUMBER: _ClassVar[int]
                    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
                    USE_ROUTES_FIELD_NUMBER: _ClassVar[int]
                    ROUTE_METRIC_FIELD_NUMBER: _ClassVar[int]
                    use_dns: bool
                    use_ntp: bool
                    send_hostname: bool
                    use_hostname: bool
                    use_mtu: bool
                    hostname: str
                    use_routes: bool
                    route_metric: int
                    def __init__(self, use_dns: bool = ..., use_ntp: bool = ..., send_hostname: bool = ..., use_hostname: bool = ..., use_mtu: bool = ..., hostname: _Optional[str] = ..., use_routes: bool = ..., route_metric: _Optional[int] = ...) -> None: ...
                class Nameservers(_message.Message):
                    __slots__ = ("search", "addresses")
                    SEARCH_FIELD_NUMBER: _ClassVar[int]
                    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                    search: _containers.RepeatedScalarFieldContainer[str]
                    addresses: _containers.RepeatedScalarFieldContainer[str]
                    def __init__(self, search: _Optional[_Iterable[str]] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...
                class Routes(_message.Message):
                    __slots__ = ("to", "via", "on_link", "metric", "type", "scope", "table")
                    FROM_FIELD_NUMBER: _ClassVar[int]
                    TO_FIELD_NUMBER: _ClassVar[int]
                    VIA_FIELD_NUMBER: _ClassVar[int]
                    ON_LINK_FIELD_NUMBER: _ClassVar[int]
                    METRIC_FIELD_NUMBER: _ClassVar[int]
                    TYPE_FIELD_NUMBER: _ClassVar[int]
                    SCOPE_FIELD_NUMBER: _ClassVar[int]
                    TABLE_FIELD_NUMBER: _ClassVar[int]
                    to: str
                    via: str
                    on_link: bool
                    metric: int
                    type: str
                    scope: str
                    table: int
                    def __init__(self, to: _Optional[str] = ..., via: _Optional[str] = ..., on_link: bool = ..., metric: _Optional[int] = ..., type: _Optional[str] = ..., scope: _Optional[str] = ..., table: _Optional[int] = ..., **kwargs) -> None: ...
                class RoutingPolicy(_message.Message):
                    __slots__ = ("to", "table", "priority", "mark", "type_of_service")
                    FROM_FIELD_NUMBER: _ClassVar[int]
                    TO_FIELD_NUMBER: _ClassVar[int]
                    TABLE_FIELD_NUMBER: _ClassVar[int]
                    PRIORITY_FIELD_NUMBER: _ClassVar[int]
                    MARK_FIELD_NUMBER: _ClassVar[int]
                    TYPE_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
                    to: str
                    table: int
                    priority: int
                    mark: int
                    type_of_service: int
                    def __init__(self, to: _Optional[str] = ..., table: _Optional[int] = ..., priority: _Optional[int] = ..., mark: _Optional[int] = ..., type_of_service: _Optional[int] = ..., **kwargs) -> None: ...
                class Auth(_message.Message):
                    __slots__ = ("key_management", "password", "method", "identity", "anonymous_identity", "ca_certificate", "client_certificate", "client_key", "client_key_password", "phase2_auth")
                    KEY_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
                    PASSWORD_FIELD_NUMBER: _ClassVar[int]
                    METHOD_FIELD_NUMBER: _ClassVar[int]
                    IDENTITY_FIELD_NUMBER: _ClassVar[int]
                    ANONYMOUS_IDENTITY_FIELD_NUMBER: _ClassVar[int]
                    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
                    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
                    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
                    CLIENT_KEY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
                    PHASE2_AUTH_FIELD_NUMBER: _ClassVar[int]
                    key_management: str
                    password: str
                    method: str
                    identity: str
                    anonymous_identity: str
                    ca_certificate: str
                    client_certificate: str
                    client_key: str
                    client_key_password: str
                    phase2_auth: str
                    def __init__(self, key_management: _Optional[str] = ..., password: _Optional[str] = ..., method: _Optional[str] = ..., identity: _Optional[str] = ..., anonymous_identity: _Optional[str] = ..., ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ..., client_key_password: _Optional[str] = ..., phase2_auth: _Optional[str] = ...) -> None: ...
                def __init__(self) -> None: ...
            class EthOpts(_message.Message):
                __slots__ = ("match", "set_name", "wakeonlan", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                class Match(_message.Message):
                    __slots__ = ("name", "macaddress", "driver")
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                    DRIVER_FIELD_NUMBER: _ClassVar[int]
                    name: str
                    macaddress: str
                    driver: str
                    def __init__(self, name: _Optional[str] = ..., macaddress: _Optional[str] = ..., driver: _Optional[str] = ...) -> None: ...
                MATCH_FIELD_NUMBER: _ClassVar[int]
                SET_NAME_FIELD_NUMBER: _ClassVar[int]
                WAKEONLAN_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                match: Device.Spec.NetworkingConfig.EthOpts.Match
                set_name: str
                wakeonlan: bool
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, match: _Optional[_Union[Device.Spec.NetworkingConfig.EthOpts.Match, _Mapping]] = ..., set_name: _Optional[str] = ..., wakeonlan: bool = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class WifiOpts(_message.Message):
                __slots__ = ("match", "set_name", "wakeonlan", "access_points", "wakeonwlan", "regulatory_domain", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                class AccessPointsEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: Device.Spec.NetworkingConfig.WifiOpts.AccessPoint
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Spec.NetworkingConfig.WifiOpts.AccessPoint, _Mapping]] = ...) -> None: ...
                class Match(_message.Message):
                    __slots__ = ("name", "macaddress", "driver")
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                    DRIVER_FIELD_NUMBER: _ClassVar[int]
                    name: str
                    macaddress: str
                    driver: str
                    def __init__(self, name: _Optional[str] = ..., macaddress: _Optional[str] = ..., driver: _Optional[str] = ...) -> None: ...
                class AccessPoint(_message.Message):
                    __slots__ = ("password", "mode", "bssid", "band", "channel", "hidden", "auth")
                    PASSWORD_FIELD_NUMBER: _ClassVar[int]
                    MODE_FIELD_NUMBER: _ClassVar[int]
                    BSSID_FIELD_NUMBER: _ClassVar[int]
                    BAND_FIELD_NUMBER: _ClassVar[int]
                    CHANNEL_FIELD_NUMBER: _ClassVar[int]
                    HIDDEN_FIELD_NUMBER: _ClassVar[int]
                    AUTH_FIELD_NUMBER: _ClassVar[int]
                    password: str
                    mode: str
                    bssid: str
                    band: str
                    channel: str
                    hidden: str
                    auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                    def __init__(self, password: _Optional[str] = ..., mode: _Optional[str] = ..., bssid: _Optional[str] = ..., band: _Optional[str] = ..., channel: _Optional[str] = ..., hidden: _Optional[str] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ...) -> None: ...
                MATCH_FIELD_NUMBER: _ClassVar[int]
                SET_NAME_FIELD_NUMBER: _ClassVar[int]
                WAKEONLAN_FIELD_NUMBER: _ClassVar[int]
                ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
                WAKEONWLAN_FIELD_NUMBER: _ClassVar[int]
                REGULATORY_DOMAIN_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                match: Device.Spec.NetworkingConfig.WifiOpts.Match
                set_name: str
                wakeonlan: bool
                access_points: _containers.MessageMap[str, Device.Spec.NetworkingConfig.WifiOpts.AccessPoint]
                wakeonwlan: _containers.RepeatedScalarFieldContainer[str]
                regulatory_domain: str
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, match: _Optional[_Union[Device.Spec.NetworkingConfig.WifiOpts.Match, _Mapping]] = ..., set_name: _Optional[str] = ..., wakeonlan: bool = ..., access_points: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.WifiOpts.AccessPoint]] = ..., wakeonwlan: _Optional[_Iterable[str]] = ..., regulatory_domain: _Optional[str] = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class BridgesOpts(_message.Message):
                __slots__ = ("interfaces", "parameters", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                class Parameters(_message.Message):
                    __slots__ = ("ageing_time", "priority", "port_priority", "forward_delay", "hello_time", "max_age", "path_cost", "stp")
                    AGEING_TIME_FIELD_NUMBER: _ClassVar[int]
                    PRIORITY_FIELD_NUMBER: _ClassVar[int]
                    PORT_PRIORITY_FIELD_NUMBER: _ClassVar[int]
                    FORWARD_DELAY_FIELD_NUMBER: _ClassVar[int]
                    HELLO_TIME_FIELD_NUMBER: _ClassVar[int]
                    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
                    PATH_COST_FIELD_NUMBER: _ClassVar[int]
                    STP_FIELD_NUMBER: _ClassVar[int]
                    ageing_time: int
                    priority: int
                    port_priority: int
                    forward_delay: int
                    hello_time: int
                    max_age: int
                    path_cost: int
                    stp: bool
                    def __init__(self, ageing_time: _Optional[int] = ..., priority: _Optional[int] = ..., port_priority: _Optional[int] = ..., forward_delay: _Optional[int] = ..., hello_time: _Optional[int] = ..., max_age: _Optional[int] = ..., path_cost: _Optional[int] = ..., stp: bool = ...) -> None: ...
                INTERFACES_FIELD_NUMBER: _ClassVar[int]
                PARAMETERS_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                interfaces: _containers.RepeatedScalarFieldContainer[str]
                parameters: Device.Spec.NetworkingConfig.BridgesOpts.Parameters
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, interfaces: _Optional[_Iterable[str]] = ..., parameters: _Optional[_Union[Device.Spec.NetworkingConfig.BridgesOpts.Parameters, _Mapping]] = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class BondsOpts(_message.Message):
                __slots__ = ("interfaces", "parameters", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                class Parameters(_message.Message):
                    __slots__ = ("mode", "lacp_rate", "mii_monitor_interval", "min_links", "transmit_hash_policy", "ad_select", "all_slaves_active", "arp_ip_targets", "arp_validate", "arp_all_targets", "up_delay", "fail_over_mac_policy", "gratuitous_arp", "packets_per_slave", "primary_reselect_policy", "resend_igmp", "learn_packet_interval", "primary")
                    MODE_FIELD_NUMBER: _ClassVar[int]
                    LACP_RATE_FIELD_NUMBER: _ClassVar[int]
                    MII_MONITOR_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                    MIN_LINKS_FIELD_NUMBER: _ClassVar[int]
                    TRANSMIT_HASH_POLICY_FIELD_NUMBER: _ClassVar[int]
                    AD_SELECT_FIELD_NUMBER: _ClassVar[int]
                    ALL_SLAVES_ACTIVE_FIELD_NUMBER: _ClassVar[int]
                    ARP_IP_TARGETS_FIELD_NUMBER: _ClassVar[int]
                    ARP_VALIDATE_FIELD_NUMBER: _ClassVar[int]
                    ARP_ALL_TARGETS_FIELD_NUMBER: _ClassVar[int]
                    UP_DELAY_FIELD_NUMBER: _ClassVar[int]
                    FAIL_OVER_MAC_POLICY_FIELD_NUMBER: _ClassVar[int]
                    GRATUITOUS_ARP_FIELD_NUMBER: _ClassVar[int]
                    PACKETS_PER_SLAVE_FIELD_NUMBER: _ClassVar[int]
                    PRIMARY_RESELECT_POLICY_FIELD_NUMBER: _ClassVar[int]
                    RESEND_IGMP_FIELD_NUMBER: _ClassVar[int]
                    LEARN_PACKET_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                    PRIMARY_FIELD_NUMBER: _ClassVar[int]
                    mode: str
                    lacp_rate: int
                    mii_monitor_interval: int
                    min_links: int
                    transmit_hash_policy: int
                    ad_select: int
                    all_slaves_active: int
                    arp_ip_targets: bool
                    arp_validate: str
                    arp_all_targets: str
                    up_delay: str
                    fail_over_mac_policy: str
                    gratuitous_arp: int
                    packets_per_slave: str
                    primary_reselect_policy: str
                    resend_igmp: str
                    learn_packet_interval: str
                    primary: str
                    def __init__(self, mode: _Optional[str] = ..., lacp_rate: _Optional[int] = ..., mii_monitor_interval: _Optional[int] = ..., min_links: _Optional[int] = ..., transmit_hash_policy: _Optional[int] = ..., ad_select: _Optional[int] = ..., all_slaves_active: _Optional[int] = ..., arp_ip_targets: bool = ..., arp_validate: _Optional[str] = ..., arp_all_targets: _Optional[str] = ..., up_delay: _Optional[str] = ..., fail_over_mac_policy: _Optional[str] = ..., gratuitous_arp: _Optional[int] = ..., packets_per_slave: _Optional[str] = ..., primary_reselect_policy: _Optional[str] = ..., resend_igmp: _Optional[str] = ..., learn_packet_interval: _Optional[str] = ..., primary: _Optional[str] = ...) -> None: ...
                INTERFACES_FIELD_NUMBER: _ClassVar[int]
                PARAMETERS_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                interfaces: _containers.RepeatedScalarFieldContainer[str]
                parameters: Device.Spec.NetworkingConfig.BondsOpts.Parameters
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, interfaces: _Optional[_Iterable[str]] = ..., parameters: _Optional[_Union[Device.Spec.NetworkingConfig.BondsOpts.Parameters, _Mapping]] = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class TunnelsOpts(_message.Message):
                __slots__ = ("mode", "local", "remote", "key", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                class Key(_message.Message):
                    __slots__ = ("input", "output")
                    INPUT_FIELD_NUMBER: _ClassVar[int]
                    OUTPUT_FIELD_NUMBER: _ClassVar[int]
                    input: int
                    output: int
                    def __init__(self, input: _Optional[int] = ..., output: _Optional[int] = ...) -> None: ...
                MODE_FIELD_NUMBER: _ClassVar[int]
                LOCAL_FIELD_NUMBER: _ClassVar[int]
                REMOTE_FIELD_NUMBER: _ClassVar[int]
                KEY_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                mode: str
                local: str
                remote: str
                key: int
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, mode: _Optional[str] = ..., local: _Optional[str] = ..., remote: _Optional[str] = ..., key: _Optional[int] = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class VlansOpts(_message.Message):
                __slots__ = ("id", "link", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                ID_FIELD_NUMBER: _ClassVar[int]
                LINK_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                id: int
                link: str
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, id: _Optional[int] = ..., link: _Optional[str] = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            class ModemOpts(_message.Message):
                __slots__ = ("apn", "username", "password", "number", "network_id", "device_id", "pin", "sim_id", "sim_operator_id", "auto_config", "renderer", "dhcp4", "dhcp6", "ipv6_privacy", "link_local", "critical", "dhcp_identifier", "dhcp4_overrides", "dhcp6_overrides", "accept_ra", "addresses", "nameservers", "macaddress", "mtu", "optional", "optional_addresses", "routes", "routing_policy", "auth", "gateway4", "gateway6")
                APN_FIELD_NUMBER: _ClassVar[int]
                USERNAME_FIELD_NUMBER: _ClassVar[int]
                PASSWORD_FIELD_NUMBER: _ClassVar[int]
                NUMBER_FIELD_NUMBER: _ClassVar[int]
                NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
                DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
                PIN_FIELD_NUMBER: _ClassVar[int]
                SIM_ID_FIELD_NUMBER: _ClassVar[int]
                SIM_OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
                AUTO_CONFIG_FIELD_NUMBER: _ClassVar[int]
                RENDERER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_FIELD_NUMBER: _ClassVar[int]
                DHCP6_FIELD_NUMBER: _ClassVar[int]
                IPV6_PRIVACY_FIELD_NUMBER: _ClassVar[int]
                LINK_LOCAL_FIELD_NUMBER: _ClassVar[int]
                CRITICAL_FIELD_NUMBER: _ClassVar[int]
                DHCP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DHCP4_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                DHCP6_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
                ACCEPT_RA_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
                MACADDRESS_FIELD_NUMBER: _ClassVar[int]
                MTU_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                ROUTES_FIELD_NUMBER: _ClassVar[int]
                ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                GATEWAY4_FIELD_NUMBER: _ClassVar[int]
                GATEWAY6_FIELD_NUMBER: _ClassVar[int]
                apn: str
                username: str
                password: str
                number: str
                network_id: str
                device_id: str
                pin: str
                sim_id: str
                sim_operator_id: str
                auto_config: bool
                renderer: str
                dhcp4: bool
                dhcp6: bool
                ipv6_privacy: bool
                link_local: _containers.RepeatedScalarFieldContainer[str]
                critical: bool
                dhcp_identifier: str
                dhcp4_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                dhcp6_overrides: Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides
                accept_ra: bool
                addresses: _containers.RepeatedScalarFieldContainer[str]
                nameservers: Device.Spec.NetworkingConfig.CommonOpts.Nameservers
                macaddress: str
                mtu: int
                optional: bool
                optional_addresses: _containers.RepeatedScalarFieldContainer[str]
                routes: _containers.RepeatedCompositeFieldContainer[Device.Spec.NetworkingConfig.CommonOpts.Routes]
                routing_policy: Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy
                auth: Device.Spec.NetworkingConfig.CommonOpts.Auth
                gateway4: str
                gateway6: str
                def __init__(self, apn: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., number: _Optional[str] = ..., network_id: _Optional[str] = ..., device_id: _Optional[str] = ..., pin: _Optional[str] = ..., sim_id: _Optional[str] = ..., sim_operator_id: _Optional[str] = ..., auto_config: bool = ..., renderer: _Optional[str] = ..., dhcp4: bool = ..., dhcp6: bool = ..., ipv6_privacy: bool = ..., link_local: _Optional[_Iterable[str]] = ..., critical: bool = ..., dhcp_identifier: _Optional[str] = ..., dhcp4_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., dhcp6_overrides: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.DHCPOverrides, _Mapping]] = ..., accept_ra: bool = ..., addresses: _Optional[_Iterable[str]] = ..., nameservers: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Nameservers, _Mapping]] = ..., macaddress: _Optional[str] = ..., mtu: _Optional[int] = ..., optional: bool = ..., optional_addresses: _Optional[_Iterable[str]] = ..., routes: _Optional[_Iterable[_Union[Device.Spec.NetworkingConfig.CommonOpts.Routes, _Mapping]]] = ..., routing_policy: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.RoutingPolicy, _Mapping]] = ..., auth: _Optional[_Union[Device.Spec.NetworkingConfig.CommonOpts.Auth, _Mapping]] = ..., gateway4: _Optional[str] = ..., gateway6: _Optional[str] = ...) -> None: ...
            VERSION_FIELD_NUMBER: _ClassVar[int]
            RENDERER_FIELD_NUMBER: _ClassVar[int]
            ETHERNETS_FIELD_NUMBER: _ClassVar[int]
            WIFIS_FIELD_NUMBER: _ClassVar[int]
            BRIDGES_FIELD_NUMBER: _ClassVar[int]
            BONDS_FIELD_NUMBER: _ClassVar[int]
            TUNNELS_FIELD_NUMBER: _ClassVar[int]
            VLANS_FIELD_NUMBER: _ClassVar[int]
            MODEMS_FIELD_NUMBER: _ClassVar[int]
            version: int
            renderer: str
            ethernets: _containers.MessageMap[str, Device.Spec.NetworkingConfig.EthOpts]
            wifis: _containers.MessageMap[str, Device.Spec.NetworkingConfig.WifiOpts]
            bridges: _containers.MessageMap[str, Device.Spec.NetworkingConfig.BridgesOpts]
            bonds: _containers.MessageMap[str, Device.Spec.NetworkingConfig.BondsOpts]
            tunnels: _containers.MessageMap[str, Device.Spec.NetworkingConfig.TunnelsOpts]
            vlans: _containers.MessageMap[str, Device.Spec.NetworkingConfig.VlansOpts]
            modems: _containers.MessageMap[str, Device.Spec.NetworkingConfig.ModemOpts]
            def __init__(self, version: _Optional[int] = ..., renderer: _Optional[str] = ..., ethernets: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.EthOpts]] = ..., wifis: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.WifiOpts]] = ..., bridges: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.BridgesOpts]] = ..., bonds: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.BondsOpts]] = ..., tunnels: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.TunnelsOpts]] = ..., vlans: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.VlansOpts]] = ..., modems: _Optional[_Mapping[str, Device.Spec.NetworkingConfig.ModemOpts]] = ...) -> None: ...
        class NetplanConfig(_message.Message):
            __slots__ = ("network",)
            NETWORK_FIELD_NUMBER: _ClassVar[int]
            network: Device.Spec.NetworkingConfig
            def __init__(self, network: _Optional[_Union[Device.Spec.NetworkingConfig, _Mapping]] = ...) -> None: ...
        class SSHConfig(_message.Message):
            __slots__ = ("disable_ssh_server", "disable_ssh_password", "ssh_authorized", "ip_allow_list", "ip_deny_list", "reject_period", "disable_ssh_authkey")
            class AuthKey(_message.Message):
                __slots__ = ("ssha_key", "cert_authority", "command", "environment", "no_agent_forwarding", "no_port_forwarding", "no_pty", "no_user_rc", "no_x11_forwarding", "permitopen", "principals", "tunnel", "restrict")
                SSHA_KEY_FIELD_NUMBER: _ClassVar[int]
                CERT_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
                COMMAND_FIELD_NUMBER: _ClassVar[int]
                ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
                FROM_FIELD_NUMBER: _ClassVar[int]
                NO_AGENT_FORWARDING_FIELD_NUMBER: _ClassVar[int]
                NO_PORT_FORWARDING_FIELD_NUMBER: _ClassVar[int]
                NO_PTY_FIELD_NUMBER: _ClassVar[int]
                NO_USER_RC_FIELD_NUMBER: _ClassVar[int]
                NO_X11_FORWARDING_FIELD_NUMBER: _ClassVar[int]
                PERMITOPEN_FIELD_NUMBER: _ClassVar[int]
                PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
                TUNNEL_FIELD_NUMBER: _ClassVar[int]
                RESTRICT_FIELD_NUMBER: _ClassVar[int]
                ssha_key: str
                cert_authority: bool
                command: str
                environment: str
                no_agent_forwarding: bool
                no_port_forwarding: bool
                no_pty: bool
                no_user_rc: bool
                no_x11_forwarding: bool
                permitopen: str
                principals: str
                tunnel: str
                restrict: bool
                def __init__(self, ssha_key: _Optional[str] = ..., cert_authority: bool = ..., command: _Optional[str] = ..., environment: _Optional[str] = ..., no_agent_forwarding: bool = ..., no_port_forwarding: bool = ..., no_pty: bool = ..., no_user_rc: bool = ..., no_x11_forwarding: bool = ..., permitopen: _Optional[str] = ..., principals: _Optional[str] = ..., tunnel: _Optional[str] = ..., restrict: bool = ..., **kwargs) -> None: ...
            DISABLE_SSH_SERVER_FIELD_NUMBER: _ClassVar[int]
            DISABLE_SSH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            SSH_AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
            IP_ALLOW_LIST_FIELD_NUMBER: _ClassVar[int]
            IP_DENY_LIST_FIELD_NUMBER: _ClassVar[int]
            REJECT_PERIOD_FIELD_NUMBER: _ClassVar[int]
            DISABLE_SSH_AUTHKEY_FIELD_NUMBER: _ClassVar[int]
            disable_ssh_server: bool
            disable_ssh_password: bool
            ssh_authorized: _containers.RepeatedCompositeFieldContainer[Device.Spec.SSHConfig.AuthKey]
            ip_allow_list: _containers.RepeatedScalarFieldContainer[str]
            ip_deny_list: _containers.RepeatedScalarFieldContainer[str]
            reject_period: _duration_pb2.Duration
            disable_ssh_authkey: bool
            def __init__(self, disable_ssh_server: bool = ..., disable_ssh_password: bool = ..., ssh_authorized: _Optional[_Iterable[_Union[Device.Spec.SSHConfig.AuthKey, _Mapping]]] = ..., ip_allow_list: _Optional[_Iterable[str]] = ..., ip_deny_list: _Optional[_Iterable[str]] = ..., reject_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., disable_ssh_authkey: bool = ...) -> None: ...
        class AttestationConfig(_message.Message):
            __slots__ = ("attestation_expected", "attestation_domain", "insecure_use_tpm_simulator_seed")
            ATTESTATION_EXPECTED_FIELD_NUMBER: _ClassVar[int]
            ATTESTATION_DOMAIN_FIELD_NUMBER: _ClassVar[int]
            INSECURE_USE_TPM_SIMULATOR_SEED_FIELD_NUMBER: _ClassVar[int]
            attestation_expected: bool
            attestation_domain: str
            insecure_use_tpm_simulator_seed: int
            def __init__(self, attestation_expected: bool = ..., attestation_domain: _Optional[str] = ..., insecure_use_tpm_simulator_seed: _Optional[int] = ...) -> None: ...
        class LoggingConfig(_message.Message):
            __slots__ = ("priority", "units", "enable_journal_export")
            PRIORITY_FIELD_NUMBER: _ClassVar[int]
            UNITS_FIELD_NUMBER: _ClassVar[int]
            ENABLE_JOURNAL_EXPORT_FIELD_NUMBER: _ClassVar[int]
            priority: int
            units: _containers.RepeatedScalarFieldContainer[str]
            enable_journal_export: bool
            def __init__(self, priority: _Optional[int] = ..., units: _Optional[_Iterable[str]] = ..., enable_journal_export: bool = ...) -> None: ...
        class ProxyConfig(_message.Message):
            __slots__ = ("http_proxy", "https_proxy", "no_proxy", "proxy_interfaces")
            HTTP_PROXY_FIELD_NUMBER: _ClassVar[int]
            HTTPS_PROXY_FIELD_NUMBER: _ClassVar[int]
            NO_PROXY_FIELD_NUMBER: _ClassVar[int]
            PROXY_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            http_proxy: str
            https_proxy: str
            no_proxy: str
            proxy_interfaces: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, http_proxy: _Optional[str] = ..., https_proxy: _Optional[str] = ..., no_proxy: _Optional[str] = ..., proxy_interfaces: _Optional[_Iterable[str]] = ...) -> None: ...
        class Location(_message.Message):
            __slots__ = ("address", "placement")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PLACEMENT_FIELD_NUMBER: _ClassVar[int]
            address: str
            placement: str
            def __init__(self, address: _Optional[str] = ..., placement: _Optional[str] = ...) -> None: ...
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        NETPLAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NETPLAN_API_CONFIG_MODE_FIELD_NUMBER: _ClassVar[int]
        OS_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ATTESTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DISABLE_DEVICE_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
        LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        service_account: str
        os_version: str
        netplan_config: Device.Spec.NetplanConfig
        netplan_api_config_mode: Device.Spec.NetworkConfigMode
        os_image_url: str
        ssh_config: Device.Spec.SSHConfig
        attestation_config: Device.Spec.AttestationConfig
        disable_device_discovery: bool
        logging_config: Device.Spec.LoggingConfig
        proxy_config: Device.Spec.ProxyConfig
        location: Device.Spec.Location
        def __init__(self, service_account: _Optional[str] = ..., os_version: _Optional[str] = ..., netplan_config: _Optional[_Union[Device.Spec.NetplanConfig, _Mapping]] = ..., netplan_api_config_mode: _Optional[_Union[Device.Spec.NetworkConfigMode, str]] = ..., os_image_url: _Optional[str] = ..., ssh_config: _Optional[_Union[Device.Spec.SSHConfig, _Mapping]] = ..., attestation_config: _Optional[_Union[Device.Spec.AttestationConfig, _Mapping]] = ..., disable_device_discovery: bool = ..., logging_config: _Optional[_Union[Device.Spec.LoggingConfig, _Mapping]] = ..., proxy_config: _Optional[_Union[Device.Spec.ProxyConfig, _Mapping]] = ..., location: _Optional[_Union[Device.Spec.Location, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("addresses", "conditions", "network_config_state", "proxy_config_status", "device_info", "attestation_status", "normalized_address")
        class Address(_message.Message):
            __slots__ = ("address", "type")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            address: str
            type: str
            def __init__(self, address: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
        class Condition(_message.Message):
            __slots__ = ("message", "reason", "status", "type", "last_heart_beat_time", "last_transition_time")
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            REASON_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            LAST_HEART_BEAT_TIME_FIELD_NUMBER: _ClassVar[int]
            LAST_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
            message: str
            reason: str
            status: str
            type: str
            last_heart_beat_time: _timestamp_pb2.Timestamp
            last_transition_time: _timestamp_pb2.Timestamp
            def __init__(self, message: _Optional[str] = ..., reason: _Optional[str] = ..., status: _Optional[str] = ..., type: _Optional[str] = ..., last_heart_beat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_transition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class NetworkConfigState(_message.Message):
            __slots__ = ("active_network_config_source", "desired_network_config_source", "desired_network_config_error", "default_config", "active_config", "desired_config")
            class NetworkConfigSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
                DEFAULT_CONFIG: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
                API_CONFIG: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
                MERGED_DEFAULT_AND_API_CONFIG: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
                PREVIOUS_MERGED_DEFAULT_AND_API_CONFIG: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
                PREVIOUS_API_CONFIG: _ClassVar[Device.Status.NetworkConfigState.NetworkConfigSource]
            UNKNOWN: Device.Status.NetworkConfigState.NetworkConfigSource
            DEFAULT_CONFIG: Device.Status.NetworkConfigState.NetworkConfigSource
            API_CONFIG: Device.Status.NetworkConfigState.NetworkConfigSource
            MERGED_DEFAULT_AND_API_CONFIG: Device.Status.NetworkConfigState.NetworkConfigSource
            PREVIOUS_MERGED_DEFAULT_AND_API_CONFIG: Device.Status.NetworkConfigState.NetworkConfigSource
            PREVIOUS_API_CONFIG: Device.Status.NetworkConfigState.NetworkConfigSource
            ACTIVE_NETWORK_CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
            DESIRED_NETWORK_CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
            DESIRED_NETWORK_CONFIG_ERROR_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            DESIRED_CONFIG_FIELD_NUMBER: _ClassVar[int]
            active_network_config_source: Device.Status.NetworkConfigState.NetworkConfigSource
            desired_network_config_source: Device.Status.NetworkConfigState.NetworkConfigSource
            desired_network_config_error: str
            default_config: Device.Spec.NetplanConfig
            active_config: Device.Spec.NetplanConfig
            desired_config: Device.Spec.NetplanConfig
            def __init__(self, active_network_config_source: _Optional[_Union[Device.Status.NetworkConfigState.NetworkConfigSource, str]] = ..., desired_network_config_source: _Optional[_Union[Device.Status.NetworkConfigState.NetworkConfigSource, str]] = ..., desired_network_config_error: _Optional[str] = ..., default_config: _Optional[_Union[Device.Spec.NetplanConfig, _Mapping]] = ..., active_config: _Optional[_Union[Device.Spec.NetplanConfig, _Mapping]] = ..., desired_config: _Optional[_Union[Device.Spec.NetplanConfig, _Mapping]] = ...) -> None: ...
        class ProxyConfigStatus(_message.Message):
            __slots__ = ("active_config_source", "desired_config_source", "proxy_config_error", "default_config", "active_config", "api_config")
            class ProxyConfigSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_CONFIG: _ClassVar[Device.Status.ProxyConfigStatus.ProxyConfigSource]
                DEFAULT_CONFIG: _ClassVar[Device.Status.ProxyConfigStatus.ProxyConfigSource]
                API_CONFIG: _ClassVar[Device.Status.ProxyConfigStatus.ProxyConfigSource]
            NO_CONFIG: Device.Status.ProxyConfigStatus.ProxyConfigSource
            DEFAULT_CONFIG: Device.Status.ProxyConfigStatus.ProxyConfigSource
            API_CONFIG: Device.Status.ProxyConfigStatus.ProxyConfigSource
            ACTIVE_CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
            DESIRED_CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
            PROXY_CONFIG_ERROR_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            API_CONFIG_FIELD_NUMBER: _ClassVar[int]
            active_config_source: Device.Status.ProxyConfigStatus.ProxyConfigSource
            desired_config_source: Device.Status.ProxyConfigStatus.ProxyConfigSource
            proxy_config_error: str
            default_config: Device.Spec.ProxyConfig
            active_config: Device.Spec.ProxyConfig
            api_config: Device.Spec.ProxyConfig
            def __init__(self, active_config_source: _Optional[_Union[Device.Status.ProxyConfigStatus.ProxyConfigSource, str]] = ..., desired_config_source: _Optional[_Union[Device.Status.ProxyConfigStatus.ProxyConfigSource, str]] = ..., proxy_config_error: _Optional[str] = ..., default_config: _Optional[_Union[Device.Spec.ProxyConfig, _Mapping]] = ..., active_config: _Optional[_Union[Device.Spec.ProxyConfig, _Mapping]] = ..., api_config: _Optional[_Union[Device.Spec.ProxyConfig, _Mapping]] = ...) -> None: ...
        class DeviceInfo(_message.Message):
            __slots__ = ("architecture", "operating_system", "kernel_version", "os_image", "container_runtime_version", "os_version", "driver", "hardware_information", "network_interfaces", "control_plane_interface_info")
            class NetworkInterfacesEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Device.Status.DeviceInfo.NetworkInterface
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Status.DeviceInfo.NetworkInterface, _Mapping]] = ...) -> None: ...
            class HardwareInformation(_message.Message):
                __slots__ = ("os", "bios", "system", "cpu", "block", "network", "gpu", "memory_info", "hailo_info", "nvidia_info", "modem_status")
                class Capability(_message.Message):
                    __slots__ = ("name", "description")
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                    name: str
                    description: str
                    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
                class OS(_message.Message):
                    __slots__ = ("operating_system", "kernel_version", "os_image", "container_runtime_version")
                    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
                    KERNEL_VERSION_FIELD_NUMBER: _ClassVar[int]
                    OS_IMAGE_FIELD_NUMBER: _ClassVar[int]
                    CONTAINER_RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
                    operating_system: str
                    kernel_version: str
                    os_image: str
                    container_runtime_version: str
                    def __init__(self, operating_system: _Optional[str] = ..., kernel_version: _Optional[str] = ..., os_image: _Optional[str] = ..., container_runtime_version: _Optional[str] = ...) -> None: ...
                class BIOS(_message.Message):
                    __slots__ = ("vendor", "bios_version", "release_date")
                    VENDOR_FIELD_NUMBER: _ClassVar[int]
                    BIOS_VERSION_FIELD_NUMBER: _ClassVar[int]
                    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
                    vendor: str
                    bios_version: str
                    release_date: str
                    def __init__(self, vendor: _Optional[str] = ..., bios_version: _Optional[str] = ..., release_date: _Optional[str] = ...) -> None: ...
                class System(_message.Message):
                    __slots__ = ("manufacturer", "product_name", "version", "serial_number", "configuration")
                    class Configuration(_message.Message):
                        __slots__ = ("chassis", "uuid", "sku_number", "family")
                        CHASSIS_FIELD_NUMBER: _ClassVar[int]
                        UUID_FIELD_NUMBER: _ClassVar[int]
                        SKU_NUMBER_FIELD_NUMBER: _ClassVar[int]
                        FAMILY_FIELD_NUMBER: _ClassVar[int]
                        chassis: str
                        uuid: str
                        sku_number: str
                        family: str
                        def __init__(self, chassis: _Optional[str] = ..., uuid: _Optional[str] = ..., sku_number: _Optional[str] = ..., family: _Optional[str] = ...) -> None: ...
                    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
                    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
                    VERSION_FIELD_NUMBER: _ClassVar[int]
                    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
                    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
                    manufacturer: str
                    product_name: str
                    version: str
                    serial_number: str
                    configuration: Device.Status.DeviceInfo.HardwareInformation.System.Configuration
                    def __init__(self, manufacturer: _Optional[str] = ..., product_name: _Optional[str] = ..., version: _Optional[str] = ..., serial_number: _Optional[str] = ..., configuration: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.System.Configuration, _Mapping]] = ...) -> None: ...
                class CPU(_message.Message):
                    __slots__ = ("processors",)
                    class Processor(_message.Message):
                        __slots__ = ("vendor", "model", "capabilities", "num_threads", "num_cores", "num_enabled_cores", "name", "serial", "frequency_mhz", "max_frequency_mhz", "cache_info", "driver", "latency", "clock")
                        class Cache(_message.Message):
                            __slots__ = ("type", "size_bytes")
                            TYPE_FIELD_NUMBER: _ClassVar[int]
                            SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                            type: str
                            size_bytes: int
                            def __init__(self, type: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...
                        VENDOR_FIELD_NUMBER: _ClassVar[int]
                        MODEL_FIELD_NUMBER: _ClassVar[int]
                        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
                        NUM_THREADS_FIELD_NUMBER: _ClassVar[int]
                        NUM_CORES_FIELD_NUMBER: _ClassVar[int]
                        NUM_ENABLED_CORES_FIELD_NUMBER: _ClassVar[int]
                        NAME_FIELD_NUMBER: _ClassVar[int]
                        SERIAL_FIELD_NUMBER: _ClassVar[int]
                        FREQUENCY_MHZ_FIELD_NUMBER: _ClassVar[int]
                        MAX_FREQUENCY_MHZ_FIELD_NUMBER: _ClassVar[int]
                        CACHE_INFO_FIELD_NUMBER: _ClassVar[int]
                        DRIVER_FIELD_NUMBER: _ClassVar[int]
                        LATENCY_FIELD_NUMBER: _ClassVar[int]
                        CLOCK_FIELD_NUMBER: _ClassVar[int]
                        vendor: str
                        model: str
                        capabilities: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.Capability]
                        num_threads: int
                        num_cores: int
                        num_enabled_cores: int
                        name: str
                        serial: str
                        frequency_mhz: int
                        max_frequency_mhz: int
                        cache_info: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.CPU.Processor.Cache]
                        driver: str
                        latency: int
                        clock: int
                        def __init__(self, vendor: _Optional[str] = ..., model: _Optional[str] = ..., capabilities: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.Capability, _Mapping]]] = ..., num_threads: _Optional[int] = ..., num_cores: _Optional[int] = ..., num_enabled_cores: _Optional[int] = ..., name: _Optional[str] = ..., serial: _Optional[str] = ..., frequency_mhz: _Optional[int] = ..., max_frequency_mhz: _Optional[int] = ..., cache_info: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.CPU.Processor.Cache, _Mapping]]] = ..., driver: _Optional[str] = ..., latency: _Optional[int] = ..., clock: _Optional[int] = ...) -> None: ...
                    PROCESSORS_FIELD_NUMBER: _ClassVar[int]
                    processors: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.CPU.Processor]
                    def __init__(self, processors: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.CPU.Processor, _Mapping]]] = ...) -> None: ...
                class Block(_message.Message):
                    __slots__ = ("disks",)
                    class Disk(_message.Message):
                        __slots__ = ("name", "size_bytes", "drive_type", "vendor", "model", "serial_number", "wwn", "partitions")
                        class Partition(_message.Message):
                            __slots__ = ("name", "size_bytes", "mount_point", "type")
                            NAME_FIELD_NUMBER: _ClassVar[int]
                            SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                            MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
                            TYPE_FIELD_NUMBER: _ClassVar[int]
                            name: str
                            size_bytes: int
                            mount_point: str
                            type: str
                            def __init__(self, name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., mount_point: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
                        NAME_FIELD_NUMBER: _ClassVar[int]
                        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
                        VENDOR_FIELD_NUMBER: _ClassVar[int]
                        MODEL_FIELD_NUMBER: _ClassVar[int]
                        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
                        WWN_FIELD_NUMBER: _ClassVar[int]
                        PARTITIONS_FIELD_NUMBER: _ClassVar[int]
                        name: str
                        size_bytes: int
                        drive_type: str
                        vendor: str
                        model: str
                        serial_number: str
                        wwn: str
                        partitions: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.Block.Disk.Partition]
                        def __init__(self, name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., drive_type: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., serial_number: _Optional[str] = ..., wwn: _Optional[str] = ..., partitions: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.Block.Disk.Partition, _Mapping]]] = ...) -> None: ...
                    DISKS_FIELD_NUMBER: _ClassVar[int]
                    disks: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.Block.Disk]
                    def __init__(self, disks: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.Block.Disk, _Mapping]]] = ...) -> None: ...
                class Network(_message.Message):
                    __slots__ = ("nics",)
                    class NIC(_message.Message):
                        __slots__ = ("name", "mac_address", "virtual", "description", "product_name", "vendor", "subvendor", "setting")
                        class SettingEntry(_message.Message):
                            __slots__ = ("key", "value")
                            KEY_FIELD_NUMBER: _ClassVar[int]
                            VALUE_FIELD_NUMBER: _ClassVar[int]
                            key: str
                            value: str
                            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                        NAME_FIELD_NUMBER: _ClassVar[int]
                        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
                        VIRTUAL_FIELD_NUMBER: _ClassVar[int]
                        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
                        VENDOR_FIELD_NUMBER: _ClassVar[int]
                        SUBVENDOR_FIELD_NUMBER: _ClassVar[int]
                        SETTING_FIELD_NUMBER: _ClassVar[int]
                        name: str
                        mac_address: str
                        virtual: bool
                        description: str
                        product_name: str
                        vendor: str
                        subvendor: str
                        setting: _containers.ScalarMap[str, str]
                        def __init__(self, name: _Optional[str] = ..., mac_address: _Optional[str] = ..., virtual: bool = ..., description: _Optional[str] = ..., product_name: _Optional[str] = ..., vendor: _Optional[str] = ..., subvendor: _Optional[str] = ..., setting: _Optional[_Mapping[str, str]] = ...) -> None: ...
                    NICS_FIELD_NUMBER: _ClassVar[int]
                    nics: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.Network.NIC]
                    def __init__(self, nics: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.Network.NIC, _Mapping]]] = ...) -> None: ...
                class GPU(_message.Message):
                    __slots__ = ("graphic_cards",)
                    class GraphicCard(_message.Message):
                        __slots__ = ("index", "device")
                        INDEX_FIELD_NUMBER: _ClassVar[int]
                        DEVICE_FIELD_NUMBER: _ClassVar[int]
                        index: int
                        device: Device.Status.DeviceInfo.HardwareInformation.PCIDevice
                        def __init__(self, index: _Optional[int] = ..., device: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.PCIDevice, _Mapping]] = ...) -> None: ...
                    GRAPHIC_CARDS_FIELD_NUMBER: _ClassVar[int]
                    graphic_cards: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.GPU.GraphicCard]
                    def __init__(self, graphic_cards: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.GPU.GraphicCard, _Mapping]]] = ...) -> None: ...
                class PCIDevice(_message.Message):
                    __slots__ = ("address", "vendor", "product", "name", "subvendor")
                    ADDRESS_FIELD_NUMBER: _ClassVar[int]
                    VENDOR_FIELD_NUMBER: _ClassVar[int]
                    PRODUCT_FIELD_NUMBER: _ClassVar[int]
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    SUBVENDOR_FIELD_NUMBER: _ClassVar[int]
                    address: str
                    vendor: str
                    product: str
                    name: str
                    subvendor: str
                    def __init__(self, address: _Optional[str] = ..., vendor: _Optional[str] = ..., product: _Optional[str] = ..., name: _Optional[str] = ..., subvendor: _Optional[str] = ...) -> None: ...
                class MemoryInfo(_message.Message):
                    __slots__ = ("memory",)
                    class Memory(_message.Message):
                        __slots__ = ("description", "size_bytes", "memory_banks")
                        class MemoryBank(_message.Message):
                            __slots__ = ("description", "product", "vendor", "serial", "slot", "size_bytes", "frequency_hz", "width_bits")
                            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                            PRODUCT_FIELD_NUMBER: _ClassVar[int]
                            VENDOR_FIELD_NUMBER: _ClassVar[int]
                            SERIAL_FIELD_NUMBER: _ClassVar[int]
                            SLOT_FIELD_NUMBER: _ClassVar[int]
                            SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                            FREQUENCY_HZ_FIELD_NUMBER: _ClassVar[int]
                            WIDTH_BITS_FIELD_NUMBER: _ClassVar[int]
                            description: str
                            product: str
                            vendor: str
                            serial: str
                            slot: str
                            size_bytes: int
                            frequency_hz: int
                            width_bits: int
                            def __init__(self, description: _Optional[str] = ..., product: _Optional[str] = ..., vendor: _Optional[str] = ..., serial: _Optional[str] = ..., slot: _Optional[str] = ..., size_bytes: _Optional[int] = ..., frequency_hz: _Optional[int] = ..., width_bits: _Optional[int] = ...) -> None: ...
                        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                        MEMORY_BANKS_FIELD_NUMBER: _ClassVar[int]
                        description: str
                        size_bytes: int
                        memory_banks: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.MemoryInfo.Memory.MemoryBank]
                        def __init__(self, description: _Optional[str] = ..., size_bytes: _Optional[int] = ..., memory_banks: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.MemoryInfo.Memory.MemoryBank, _Mapping]]] = ...) -> None: ...
                    MEMORY_FIELD_NUMBER: _ClassVar[int]
                    memory: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.MemoryInfo.Memory]
                    def __init__(self, memory: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.MemoryInfo.Memory, _Mapping]]] = ...) -> None: ...
                class HailoInfo(_message.Message):
                    __slots__ = ("status", "cli_version", "modules")
                    class HailoModuleInfo(_message.Message):
                        __slots__ = ("dev_id", "control_proto_version", "firmware_version", "logger_version", "board_name", "serial_number", "part_number", "product_name", "neural_network_core_clock_rate")
                        DEV_ID_FIELD_NUMBER: _ClassVar[int]
                        CONTROL_PROTO_VERSION_FIELD_NUMBER: _ClassVar[int]
                        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
                        LOGGER_VERSION_FIELD_NUMBER: _ClassVar[int]
                        BOARD_NAME_FIELD_NUMBER: _ClassVar[int]
                        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
                        PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
                        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
                        NEURAL_NETWORK_CORE_CLOCK_RATE_FIELD_NUMBER: _ClassVar[int]
                        dev_id: str
                        control_proto_version: str
                        firmware_version: str
                        logger_version: str
                        board_name: str
                        serial_number: str
                        part_number: str
                        product_name: str
                        neural_network_core_clock_rate: str
                        def __init__(self, dev_id: _Optional[str] = ..., control_proto_version: _Optional[str] = ..., firmware_version: _Optional[str] = ..., logger_version: _Optional[str] = ..., board_name: _Optional[str] = ..., serial_number: _Optional[str] = ..., part_number: _Optional[str] = ..., product_name: _Optional[str] = ..., neural_network_core_clock_rate: _Optional[str] = ...) -> None: ...
                    STATUS_FIELD_NUMBER: _ClassVar[int]
                    CLI_VERSION_FIELD_NUMBER: _ClassVar[int]
                    MODULES_FIELD_NUMBER: _ClassVar[int]
                    status: str
                    cli_version: str
                    modules: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.HailoInfo.HailoModuleInfo]
                    def __init__(self, status: _Optional[str] = ..., cli_version: _Optional[str] = ..., modules: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.HailoInfo.HailoModuleInfo, _Mapping]]] = ...) -> None: ...
                class NvidiaInfo(_message.Message):
                    __slots__ = ("status", "driver_version", "cuda_version", "gpus")
                    class GpuInfo(_message.Message):
                        __slots__ = ("id", "product_name")
                        ID_FIELD_NUMBER: _ClassVar[int]
                        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
                        id: str
                        product_name: str
                        def __init__(self, id: _Optional[str] = ..., product_name: _Optional[str] = ...) -> None: ...
                    STATUS_FIELD_NUMBER: _ClassVar[int]
                    DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
                    CUDA_VERSION_FIELD_NUMBER: _ClassVar[int]
                    GPUS_FIELD_NUMBER: _ClassVar[int]
                    status: str
                    driver_version: str
                    cuda_version: str
                    gpus: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.NvidiaInfo.GpuInfo]
                    def __init__(self, status: _Optional[str] = ..., driver_version: _Optional[str] = ..., cuda_version: _Optional[str] = ..., gpus: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.NvidiaInfo.GpuInfo, _Mapping]]] = ...) -> None: ...
                class ModemStatus(_message.Message):
                    __slots__ = ("modem",)
                    class RegistrationSettings(_message.Message):
                        __slots__ = ("drx_cycle", "mico_mode")
                        DRX_CYCLE_FIELD_NUMBER: _ClassVar[int]
                        MICO_MODE_FIELD_NUMBER: _ClassVar[int]
                        drx_cycle: str
                        mico_mode: str
                        def __init__(self, drx_cycle: _Optional[str] = ..., mico_mode: _Optional[str] = ...) -> None: ...
                    class FiveGNr(_message.Message):
                        __slots__ = ("registration_settings",)
                        REGISTRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
                        registration_settings: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.RegistrationSettings
                        def __init__(self, registration_settings: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.RegistrationSettings, _Mapping]] = ...) -> None: ...
                    class Settings(_message.Message):
                        __slots__ = ("apn", "ip_type", "password", "user")
                        APN_FIELD_NUMBER: _ClassVar[int]
                        IP_TYPE_FIELD_NUMBER: _ClassVar[int]
                        PASSWORD_FIELD_NUMBER: _ClassVar[int]
                        USER_FIELD_NUMBER: _ClassVar[int]
                        apn: str
                        ip_type: str
                        password: str
                        user: str
                        def __init__(self, apn: _Optional[str] = ..., ip_type: _Optional[str] = ..., password: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...
                    class InitialBearer(_message.Message):
                        __slots__ = ("dbus_path", "settings")
                        DBUS_PATH_FIELD_NUMBER: _ClassVar[int]
                        SETTINGS_FIELD_NUMBER: _ClassVar[int]
                        dbus_path: str
                        settings: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Settings
                        def __init__(self, dbus_path: _Optional[str] = ..., settings: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Settings, _Mapping]] = ...) -> None: ...
                    class Eps(_message.Message):
                        __slots__ = ("initial_bearer", "ue_mode_operation")
                        INITIAL_BEARER_FIELD_NUMBER: _ClassVar[int]
                        UE_MODE_OPERATION_FIELD_NUMBER: _ClassVar[int]
                        initial_bearer: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.InitialBearer
                        ue_mode_operation: str
                        def __init__(self, initial_bearer: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.InitialBearer, _Mapping]] = ..., ue_mode_operation: _Optional[str] = ...) -> None: ...
                    class ThreeGpp(_message.Message):
                        __slots__ = ("fiveg_nr", "enabled_locks", "eps", "imei", "operator_code", "operator_name", "packet_service_state", "pco", "registration_state")
                        FIVEG_NR_FIELD_NUMBER: _ClassVar[int]
                        ENABLED_LOCKS_FIELD_NUMBER: _ClassVar[int]
                        EPS_FIELD_NUMBER: _ClassVar[int]
                        IMEI_FIELD_NUMBER: _ClassVar[int]
                        OPERATOR_CODE_FIELD_NUMBER: _ClassVar[int]
                        OPERATOR_NAME_FIELD_NUMBER: _ClassVar[int]
                        PACKET_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
                        PCO_FIELD_NUMBER: _ClassVar[int]
                        REGISTRATION_STATE_FIELD_NUMBER: _ClassVar[int]
                        fiveg_nr: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.FiveGNr
                        enabled_locks: _containers.RepeatedScalarFieldContainer[str]
                        eps: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Eps
                        imei: str
                        operator_code: str
                        operator_name: str
                        packet_service_state: str
                        pco: str
                        registration_state: str
                        def __init__(self, fiveg_nr: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.FiveGNr, _Mapping]] = ..., enabled_locks: _Optional[_Iterable[str]] = ..., eps: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Eps, _Mapping]] = ..., imei: _Optional[str] = ..., operator_code: _Optional[str] = ..., operator_name: _Optional[str] = ..., packet_service_state: _Optional[str] = ..., pco: _Optional[str] = ..., registration_state: _Optional[str] = ...) -> None: ...
                    class Cdma(_message.Message):
                        __slots__ = ("activation_state", "cdma1x_registration_state", "esn", "evdo_registration_state", "meid", "nid", "sid")
                        ACTIVATION_STATE_FIELD_NUMBER: _ClassVar[int]
                        CDMA1X_REGISTRATION_STATE_FIELD_NUMBER: _ClassVar[int]
                        ESN_FIELD_NUMBER: _ClassVar[int]
                        EVDO_REGISTRATION_STATE_FIELD_NUMBER: _ClassVar[int]
                        MEID_FIELD_NUMBER: _ClassVar[int]
                        NID_FIELD_NUMBER: _ClassVar[int]
                        SID_FIELD_NUMBER: _ClassVar[int]
                        activation_state: str
                        cdma1x_registration_state: str
                        esn: str
                        evdo_registration_state: str
                        meid: str
                        nid: str
                        sid: str
                        def __init__(self, activation_state: _Optional[str] = ..., cdma1x_registration_state: _Optional[str] = ..., esn: _Optional[str] = ..., evdo_registration_state: _Optional[str] = ..., meid: _Optional[str] = ..., nid: _Optional[str] = ..., sid: _Optional[str] = ...) -> None: ...
                    class SignalQuality(_message.Message):
                        __slots__ = ("recent", "value")
                        RECENT_FIELD_NUMBER: _ClassVar[int]
                        VALUE_FIELD_NUMBER: _ClassVar[int]
                        recent: str
                        value: str
                        def __init__(self, recent: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                    class Generic(_message.Message):
                        __slots__ = ("access_technologies", "bearers", "carrier_configuration", "carrier_configuration_revision", "current_bands", "current_capabilities", "current_modes", "device", "device_identifier", "drivers", "equipment_identifier", "hardware_revision", "manufacturer", "model", "own_numbers", "plugin", "ports", "power_state", "primary_port", "primary_sim_slot", "revision", "signal_quality", "sim", "sim_slots", "state", "state_failed_reason", "supported_bands", "supported_capabilities", "supported_ip_families", "supported_modes", "unlock_required", "unlock_retries")
                        ACCESS_TECHNOLOGIES_FIELD_NUMBER: _ClassVar[int]
                        BEARERS_FIELD_NUMBER: _ClassVar[int]
                        CARRIER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
                        CARRIER_CONFIGURATION_REVISION_FIELD_NUMBER: _ClassVar[int]
                        CURRENT_BANDS_FIELD_NUMBER: _ClassVar[int]
                        CURRENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
                        CURRENT_MODES_FIELD_NUMBER: _ClassVar[int]
                        DEVICE_FIELD_NUMBER: _ClassVar[int]
                        DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                        DRIVERS_FIELD_NUMBER: _ClassVar[int]
                        EQUIPMENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                        HARDWARE_REVISION_FIELD_NUMBER: _ClassVar[int]
                        MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
                        MODEL_FIELD_NUMBER: _ClassVar[int]
                        OWN_NUMBERS_FIELD_NUMBER: _ClassVar[int]
                        PLUGIN_FIELD_NUMBER: _ClassVar[int]
                        PORTS_FIELD_NUMBER: _ClassVar[int]
                        POWER_STATE_FIELD_NUMBER: _ClassVar[int]
                        PRIMARY_PORT_FIELD_NUMBER: _ClassVar[int]
                        PRIMARY_SIM_SLOT_FIELD_NUMBER: _ClassVar[int]
                        REVISION_FIELD_NUMBER: _ClassVar[int]
                        SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
                        SIM_FIELD_NUMBER: _ClassVar[int]
                        SIM_SLOTS_FIELD_NUMBER: _ClassVar[int]
                        STATE_FIELD_NUMBER: _ClassVar[int]
                        STATE_FAILED_REASON_FIELD_NUMBER: _ClassVar[int]
                        SUPPORTED_BANDS_FIELD_NUMBER: _ClassVar[int]
                        SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
                        SUPPORTED_IP_FAMILIES_FIELD_NUMBER: _ClassVar[int]
                        SUPPORTED_MODES_FIELD_NUMBER: _ClassVar[int]
                        UNLOCK_REQUIRED_FIELD_NUMBER: _ClassVar[int]
                        UNLOCK_RETRIES_FIELD_NUMBER: _ClassVar[int]
                        access_technologies: _containers.RepeatedScalarFieldContainer[str]
                        bearers: _containers.RepeatedScalarFieldContainer[str]
                        carrier_configuration: str
                        carrier_configuration_revision: str
                        current_bands: _containers.RepeatedScalarFieldContainer[str]
                        current_capabilities: _containers.RepeatedScalarFieldContainer[str]
                        current_modes: str
                        device: str
                        device_identifier: str
                        drivers: _containers.RepeatedScalarFieldContainer[str]
                        equipment_identifier: str
                        hardware_revision: str
                        manufacturer: str
                        model: str
                        own_numbers: _containers.RepeatedScalarFieldContainer[str]
                        plugin: str
                        ports: _containers.RepeatedScalarFieldContainer[str]
                        power_state: str
                        primary_port: str
                        primary_sim_slot: str
                        revision: str
                        signal_quality: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalQuality
                        sim: str
                        sim_slots: _containers.RepeatedScalarFieldContainer[str]
                        state: str
                        state_failed_reason: str
                        supported_bands: _containers.RepeatedScalarFieldContainer[str]
                        supported_capabilities: _containers.RepeatedScalarFieldContainer[str]
                        supported_ip_families: _containers.RepeatedScalarFieldContainer[str]
                        supported_modes: _containers.RepeatedScalarFieldContainer[str]
                        unlock_required: str
                        unlock_retries: _containers.RepeatedScalarFieldContainer[str]
                        def __init__(self, access_technologies: _Optional[_Iterable[str]] = ..., bearers: _Optional[_Iterable[str]] = ..., carrier_configuration: _Optional[str] = ..., carrier_configuration_revision: _Optional[str] = ..., current_bands: _Optional[_Iterable[str]] = ..., current_capabilities: _Optional[_Iterable[str]] = ..., current_modes: _Optional[str] = ..., device: _Optional[str] = ..., device_identifier: _Optional[str] = ..., drivers: _Optional[_Iterable[str]] = ..., equipment_identifier: _Optional[str] = ..., hardware_revision: _Optional[str] = ..., manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., own_numbers: _Optional[_Iterable[str]] = ..., plugin: _Optional[str] = ..., ports: _Optional[_Iterable[str]] = ..., power_state: _Optional[str] = ..., primary_port: _Optional[str] = ..., primary_sim_slot: _Optional[str] = ..., revision: _Optional[str] = ..., signal_quality: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalQuality, _Mapping]] = ..., sim: _Optional[str] = ..., sim_slots: _Optional[_Iterable[str]] = ..., state: _Optional[str] = ..., state_failed_reason: _Optional[str] = ..., supported_bands: _Optional[_Iterable[str]] = ..., supported_capabilities: _Optional[_Iterable[str]] = ..., supported_ip_families: _Optional[_Iterable[str]] = ..., supported_modes: _Optional[_Iterable[str]] = ..., unlock_required: _Optional[str] = ..., unlock_retries: _Optional[_Iterable[str]] = ...) -> None: ...
                    class Signal5g(_message.Message):
                        __slots__ = ("error_rate", "rsrp", "rsrq", "snr")
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSRP_FIELD_NUMBER: _ClassVar[int]
                        RSRQ_FIELD_NUMBER: _ClassVar[int]
                        SNR_FIELD_NUMBER: _ClassVar[int]
                        error_rate: str
                        rsrp: str
                        rsrq: str
                        snr: str
                        def __init__(self, error_rate: _Optional[str] = ..., rsrp: _Optional[str] = ..., rsrq: _Optional[str] = ..., snr: _Optional[str] = ...) -> None: ...
                    class SignalCdma1x(_message.Message):
                        __slots__ = ("ecio", "error_rate", "rssi")
                        ECIO_FIELD_NUMBER: _ClassVar[int]
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        ecio: str
                        error_rate: str
                        rssi: str
                        def __init__(self, ecio: _Optional[str] = ..., error_rate: _Optional[str] = ..., rssi: _Optional[str] = ...) -> None: ...
                    class SignalEvdo(_message.Message):
                        __slots__ = ("ecio", "error_rate", "io", "rssi", "sinr")
                        ECIO_FIELD_NUMBER: _ClassVar[int]
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        IO_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        SINR_FIELD_NUMBER: _ClassVar[int]
                        ecio: str
                        error_rate: str
                        io: str
                        rssi: str
                        sinr: str
                        def __init__(self, ecio: _Optional[str] = ..., error_rate: _Optional[str] = ..., io: _Optional[str] = ..., rssi: _Optional[str] = ..., sinr: _Optional[str] = ...) -> None: ...
                    class SignalGsm(_message.Message):
                        __slots__ = ("error_rate", "rssi")
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        error_rate: str
                        rssi: str
                        def __init__(self, error_rate: _Optional[str] = ..., rssi: _Optional[str] = ...) -> None: ...
                    class SignalLte(_message.Message):
                        __slots__ = ("error_rate", "rsrp", "rsrq", "rssi", "snr")
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSRP_FIELD_NUMBER: _ClassVar[int]
                        RSRQ_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        SNR_FIELD_NUMBER: _ClassVar[int]
                        error_rate: str
                        rsrp: str
                        rsrq: str
                        rssi: str
                        snr: str
                        def __init__(self, error_rate: _Optional[str] = ..., rsrp: _Optional[str] = ..., rsrq: _Optional[str] = ..., rssi: _Optional[str] = ..., snr: _Optional[str] = ...) -> None: ...
                    class SignalRefresh(_message.Message):
                        __slots__ = ("rate",)
                        RATE_FIELD_NUMBER: _ClassVar[int]
                        rate: str
                        def __init__(self, rate: _Optional[str] = ...) -> None: ...
                    class SignalThreshold(_message.Message):
                        __slots__ = ("error_rate", "rssi")
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        error_rate: str
                        rssi: str
                        def __init__(self, error_rate: _Optional[str] = ..., rssi: _Optional[str] = ...) -> None: ...
                    class SignalUmts(_message.Message):
                        __slots__ = ("ecio", "error_rate", "rscp", "rssi")
                        ECIO_FIELD_NUMBER: _ClassVar[int]
                        ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
                        RSCP_FIELD_NUMBER: _ClassVar[int]
                        RSSI_FIELD_NUMBER: _ClassVar[int]
                        ecio: str
                        error_rate: str
                        rscp: str
                        rssi: str
                        def __init__(self, ecio: _Optional[str] = ..., error_rate: _Optional[str] = ..., rscp: _Optional[str] = ..., rssi: _Optional[str] = ...) -> None: ...
                    class Signal(_message.Message):
                        __slots__ = ("five_g", "cdma1x", "evdo", "gsm", "lte_signal", "refresh", "threshold", "umts")
                        FIVE_G_FIELD_NUMBER: _ClassVar[int]
                        CDMA1X_FIELD_NUMBER: _ClassVar[int]
                        EVDO_FIELD_NUMBER: _ClassVar[int]
                        GSM_FIELD_NUMBER: _ClassVar[int]
                        LTE_SIGNAL_FIELD_NUMBER: _ClassVar[int]
                        REFRESH_FIELD_NUMBER: _ClassVar[int]
                        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
                        UMTS_FIELD_NUMBER: _ClassVar[int]
                        five_g: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Signal5g
                        cdma1x: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalCdma1x
                        evdo: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalEvdo
                        gsm: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalGsm
                        lte_signal: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalLte
                        refresh: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalRefresh
                        threshold: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalThreshold
                        umts: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalUmts
                        def __init__(self, five_g: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Signal5g, _Mapping]] = ..., cdma1x: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalCdma1x, _Mapping]] = ..., evdo: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalEvdo, _Mapping]] = ..., gsm: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalGsm, _Mapping]] = ..., lte_signal: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalLte, _Mapping]] = ..., refresh: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalRefresh, _Mapping]] = ..., threshold: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalThreshold, _Mapping]] = ..., umts: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SignalUmts, _Mapping]] = ...) -> None: ...
                    class SimStatus(_message.Message):
                        __slots__ = ("dbus_path", "active", "eid", "emergency_numbers", "esim_status", "gid1", "gid2", "iccid", "imsi", "operator_code", "operator_name", "removability", "sim_type")
                        DBUS_PATH_FIELD_NUMBER: _ClassVar[int]
                        ACTIVE_FIELD_NUMBER: _ClassVar[int]
                        EID_FIELD_NUMBER: _ClassVar[int]
                        EMERGENCY_NUMBERS_FIELD_NUMBER: _ClassVar[int]
                        ESIM_STATUS_FIELD_NUMBER: _ClassVar[int]
                        GID1_FIELD_NUMBER: _ClassVar[int]
                        GID2_FIELD_NUMBER: _ClassVar[int]
                        ICCID_FIELD_NUMBER: _ClassVar[int]
                        IMSI_FIELD_NUMBER: _ClassVar[int]
                        OPERATOR_CODE_FIELD_NUMBER: _ClassVar[int]
                        OPERATOR_NAME_FIELD_NUMBER: _ClassVar[int]
                        REMOVABILITY_FIELD_NUMBER: _ClassVar[int]
                        SIM_TYPE_FIELD_NUMBER: _ClassVar[int]
                        dbus_path: str
                        active: str
                        eid: str
                        emergency_numbers: _containers.RepeatedScalarFieldContainer[str]
                        esim_status: str
                        gid1: str
                        gid2: str
                        iccid: str
                        imsi: str
                        operator_code: str
                        operator_name: str
                        removability: str
                        sim_type: str
                        def __init__(self, dbus_path: _Optional[str] = ..., active: _Optional[str] = ..., eid: _Optional[str] = ..., emergency_numbers: _Optional[_Iterable[str]] = ..., esim_status: _Optional[str] = ..., gid1: _Optional[str] = ..., gid2: _Optional[str] = ..., iccid: _Optional[str] = ..., imsi: _Optional[str] = ..., operator_code: _Optional[str] = ..., operator_name: _Optional[str] = ..., removability: _Optional[str] = ..., sim_type: _Optional[str] = ...) -> None: ...
                    class Modem(_message.Message):
                        __slots__ = ("three_g_pp", "cdma", "dbus_path", "generic", "signal", "sim_status")
                        class SimStatusEntry(_message.Message):
                            __slots__ = ("key", "value")
                            KEY_FIELD_NUMBER: _ClassVar[int]
                            VALUE_FIELD_NUMBER: _ClassVar[int]
                            key: str
                            value: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SimStatus
                            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SimStatus, _Mapping]] = ...) -> None: ...
                        THREE_G_PP_FIELD_NUMBER: _ClassVar[int]
                        CDMA_FIELD_NUMBER: _ClassVar[int]
                        DBUS_PATH_FIELD_NUMBER: _ClassVar[int]
                        GENERIC_FIELD_NUMBER: _ClassVar[int]
                        SIGNAL_FIELD_NUMBER: _ClassVar[int]
                        SIM_STATUS_FIELD_NUMBER: _ClassVar[int]
                        three_g_pp: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.ThreeGpp
                        cdma: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Cdma
                        dbus_path: str
                        generic: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Generic
                        signal: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Signal
                        sim_status: _containers.MessageMap[str, Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SimStatus]
                        def __init__(self, three_g_pp: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.ThreeGpp, _Mapping]] = ..., cdma: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Cdma, _Mapping]] = ..., dbus_path: _Optional[str] = ..., generic: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Generic, _Mapping]] = ..., signal: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Signal, _Mapping]] = ..., sim_status: _Optional[_Mapping[str, Device.Status.DeviceInfo.HardwareInformation.ModemStatus.SimStatus]] = ...) -> None: ...
                    MODEM_FIELD_NUMBER: _ClassVar[int]
                    modem: Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Modem
                    def __init__(self, modem: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus.Modem, _Mapping]] = ...) -> None: ...
                OS_FIELD_NUMBER: _ClassVar[int]
                BIOS_FIELD_NUMBER: _ClassVar[int]
                SYSTEM_FIELD_NUMBER: _ClassVar[int]
                CPU_FIELD_NUMBER: _ClassVar[int]
                BLOCK_FIELD_NUMBER: _ClassVar[int]
                NETWORK_FIELD_NUMBER: _ClassVar[int]
                GPU_FIELD_NUMBER: _ClassVar[int]
                MEMORY_INFO_FIELD_NUMBER: _ClassVar[int]
                HAILO_INFO_FIELD_NUMBER: _ClassVar[int]
                NVIDIA_INFO_FIELD_NUMBER: _ClassVar[int]
                MODEM_STATUS_FIELD_NUMBER: _ClassVar[int]
                os: Device.Status.DeviceInfo.HardwareInformation.OS
                bios: Device.Status.DeviceInfo.HardwareInformation.BIOS
                system: Device.Status.DeviceInfo.HardwareInformation.System
                cpu: Device.Status.DeviceInfo.HardwareInformation.CPU
                block: Device.Status.DeviceInfo.HardwareInformation.Block
                network: Device.Status.DeviceInfo.HardwareInformation.Network
                gpu: Device.Status.DeviceInfo.HardwareInformation.GPU
                memory_info: Device.Status.DeviceInfo.HardwareInformation.MemoryInfo
                hailo_info: Device.Status.DeviceInfo.HardwareInformation.HailoInfo
                nvidia_info: Device.Status.DeviceInfo.HardwareInformation.NvidiaInfo
                modem_status: _containers.RepeatedCompositeFieldContainer[Device.Status.DeviceInfo.HardwareInformation.ModemStatus]
                def __init__(self, os: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.OS, _Mapping]] = ..., bios: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.BIOS, _Mapping]] = ..., system: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.System, _Mapping]] = ..., cpu: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.CPU, _Mapping]] = ..., block: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.Block, _Mapping]] = ..., network: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.Network, _Mapping]] = ..., gpu: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.GPU, _Mapping]] = ..., memory_info: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.MemoryInfo, _Mapping]] = ..., hailo_info: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.HailoInfo, _Mapping]] = ..., nvidia_info: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation.NvidiaInfo, _Mapping]] = ..., modem_status: _Optional[_Iterable[_Union[Device.Status.DeviceInfo.HardwareInformation.ModemStatus, _Mapping]]] = ...) -> None: ...
            class NetworkInterface(_message.Message):
                __slots__ = ("interface_name", "ip_address_v4", "external_ip_address_v4", "ip_address_v6", "external_ip_address_v6", "as_info", "carrier")
                class ASInfo(_message.Message):
                    __slots__ = ("asn", "name", "domain", "routes", "asn_type")
                    ASN_FIELD_NUMBER: _ClassVar[int]
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    DOMAIN_FIELD_NUMBER: _ClassVar[int]
                    ROUTES_FIELD_NUMBER: _ClassVar[int]
                    ASN_TYPE_FIELD_NUMBER: _ClassVar[int]
                    asn: str
                    name: str
                    domain: str
                    routes: _containers.RepeatedScalarFieldContainer[str]
                    asn_type: str
                    def __init__(self, asn: _Optional[str] = ..., name: _Optional[str] = ..., domain: _Optional[str] = ..., routes: _Optional[_Iterable[str]] = ..., asn_type: _Optional[str] = ...) -> None: ...
                class Carrier(_message.Message):
                    __slots__ = ("name", "mobile_country_code", "mobile_network_code", "location_area_code")
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    MOBILE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
                    MOBILE_NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
                    LOCATION_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
                    name: str
                    mobile_country_code: str
                    mobile_network_code: str
                    location_area_code: str
                    def __init__(self, name: _Optional[str] = ..., mobile_country_code: _Optional[str] = ..., mobile_network_code: _Optional[str] = ..., location_area_code: _Optional[str] = ...) -> None: ...
                INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
                IP_ADDRESS_V4_FIELD_NUMBER: _ClassVar[int]
                EXTERNAL_IP_ADDRESS_V4_FIELD_NUMBER: _ClassVar[int]
                IP_ADDRESS_V6_FIELD_NUMBER: _ClassVar[int]
                EXTERNAL_IP_ADDRESS_V6_FIELD_NUMBER: _ClassVar[int]
                AS_INFO_FIELD_NUMBER: _ClassVar[int]
                CARRIER_FIELD_NUMBER: _ClassVar[int]
                interface_name: str
                ip_address_v4: _containers.RepeatedScalarFieldContainer[str]
                external_ip_address_v4: _containers.RepeatedScalarFieldContainer[str]
                ip_address_v6: _containers.RepeatedScalarFieldContainer[str]
                external_ip_address_v6: _containers.RepeatedScalarFieldContainer[str]
                as_info: Device.Status.DeviceInfo.NetworkInterface.ASInfo
                carrier: Device.Status.DeviceInfo.NetworkInterface.Carrier
                def __init__(self, interface_name: _Optional[str] = ..., ip_address_v4: _Optional[_Iterable[str]] = ..., external_ip_address_v4: _Optional[_Iterable[str]] = ..., ip_address_v6: _Optional[_Iterable[str]] = ..., external_ip_address_v6: _Optional[_Iterable[str]] = ..., as_info: _Optional[_Union[Device.Status.DeviceInfo.NetworkInterface.ASInfo, _Mapping]] = ..., carrier: _Optional[_Union[Device.Status.DeviceInfo.NetworkInterface.Carrier, _Mapping]] = ...) -> None: ...
            class ControlPlaneInterfaceInfo(_message.Message):
                __slots__ = ("active_control_plane_interface", "usesProxy", "is_fallback")
                ACTIVE_CONTROL_PLANE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
                USESPROXY_FIELD_NUMBER: _ClassVar[int]
                IS_FALLBACK_FIELD_NUMBER: _ClassVar[int]
                active_control_plane_interface: str
                usesProxy: bool
                is_fallback: bool
                def __init__(self, active_control_plane_interface: _Optional[str] = ..., usesProxy: bool = ..., is_fallback: bool = ...) -> None: ...
            ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
            OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
            KERNEL_VERSION_FIELD_NUMBER: _ClassVar[int]
            OS_IMAGE_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
            OS_VERSION_FIELD_NUMBER: _ClassVar[int]
            DRIVER_FIELD_NUMBER: _ClassVar[int]
            HARDWARE_INFORMATION_FIELD_NUMBER: _ClassVar[int]
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            CONTROL_PLANE_INTERFACE_INFO_FIELD_NUMBER: _ClassVar[int]
            architecture: str
            operating_system: str
            kernel_version: str
            os_image: str
            container_runtime_version: str
            os_version: str
            driver: str
            hardware_information: Device.Status.DeviceInfo.HardwareInformation
            network_interfaces: _containers.MessageMap[str, Device.Status.DeviceInfo.NetworkInterface]
            control_plane_interface_info: Device.Status.DeviceInfo.ControlPlaneInterfaceInfo
            def __init__(self, architecture: _Optional[str] = ..., operating_system: _Optional[str] = ..., kernel_version: _Optional[str] = ..., os_image: _Optional[str] = ..., container_runtime_version: _Optional[str] = ..., os_version: _Optional[str] = ..., driver: _Optional[str] = ..., hardware_information: _Optional[_Union[Device.Status.DeviceInfo.HardwareInformation, _Mapping]] = ..., network_interfaces: _Optional[_Mapping[str, Device.Status.DeviceInfo.NetworkInterface]] = ..., control_plane_interface_info: _Optional[_Union[Device.Status.DeviceInfo.ControlPlaneInterfaceInfo, _Mapping]] = ...) -> None: ...
        class NormalizedAddress(_message.Message):
            __slots__ = ("postal_code", "country_code", "continent", "continent_id", "country", "country_id", "admin_area1", "admin_area1_id", "admin_area2", "admin_area2_id", "admin_area3", "admin_area3_id", "admin_area4", "admin_area4_id", "address", "coordinates", "accuracy")
            POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
            COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
            CONTINENT_FIELD_NUMBER: _ClassVar[int]
            CONTINENT_ID_FIELD_NUMBER: _ClassVar[int]
            COUNTRY_FIELD_NUMBER: _ClassVar[int]
            COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA1_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA1_ID_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA2_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA2_ID_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA3_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA3_ID_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA4_FIELD_NUMBER: _ClassVar[int]
            ADMIN_AREA4_ID_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            COORDINATES_FIELD_NUMBER: _ClassVar[int]
            ACCURACY_FIELD_NUMBER: _ClassVar[int]
            postal_code: str
            country_code: str
            continent: str
            continent_id: str
            country: str
            country_id: str
            admin_area1: str
            admin_area1_id: str
            admin_area2: str
            admin_area2_id: str
            admin_area3: str
            admin_area3_id: str
            admin_area4: str
            admin_area4_id: str
            address: str
            coordinates: _latlng_pb2.LatLng
            accuracy: float
            def __init__(self, postal_code: _Optional[str] = ..., country_code: _Optional[str] = ..., continent: _Optional[str] = ..., continent_id: _Optional[str] = ..., country: _Optional[str] = ..., country_id: _Optional[str] = ..., admin_area1: _Optional[str] = ..., admin_area1_id: _Optional[str] = ..., admin_area2: _Optional[str] = ..., admin_area2_id: _Optional[str] = ..., admin_area3: _Optional[str] = ..., admin_area3_id: _Optional[str] = ..., admin_area4: _Optional[str] = ..., admin_area4_id: _Optional[str] = ..., address: _Optional[str] = ..., coordinates: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., accuracy: _Optional[float] = ...) -> None: ...
        ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        NETWORK_CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
        PROXY_CONFIG_STATUS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
        ATTESTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        addresses: _containers.RepeatedCompositeFieldContainer[Device.Status.Address]
        conditions: _containers.RepeatedCompositeFieldContainer[Device.Status.Condition]
        network_config_state: Device.Status.NetworkConfigState
        proxy_config_status: Device.Status.ProxyConfigStatus
        device_info: Device.Status.DeviceInfo
        attestation_status: _containers.RepeatedCompositeFieldContainer[_common_pb2.PCR]
        normalized_address: Device.Status.NormalizedAddress
        def __init__(self, addresses: _Optional[_Iterable[_Union[Device.Status.Address, _Mapping]]] = ..., conditions: _Optional[_Iterable[_Union[Device.Status.Condition, _Mapping]]] = ..., network_config_state: _Optional[_Union[Device.Status.NetworkConfigState, _Mapping]] = ..., proxy_config_status: _Optional[_Union[Device.Status.ProxyConfigStatus, _Mapping]] = ..., device_info: _Optional[_Union[Device.Status.DeviceInfo, _Mapping]] = ..., attestation_status: _Optional[_Iterable[_Union[_common_pb2.PCR, _Mapping]]] = ..., normalized_address: _Optional[_Union[Device.Status.NormalizedAddress, _Mapping]] = ...) -> None: ...
    class PublicListingSpec(_message.Message):
        __slots__ = ("enabled", "field_mask")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, enabled: bool = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_LISTING_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _meta_pb2.Meta
    spec: Device.Spec
    status: Device.Status
    public_listing_spec: Device.PublicListingSpec
    display_name: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ..., spec: _Optional[_Union[Device.Spec, _Mapping]] = ..., status: _Optional[_Union[Device.Status, _Mapping]] = ..., public_listing_spec: _Optional[_Union[Device.PublicListingSpec, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...
