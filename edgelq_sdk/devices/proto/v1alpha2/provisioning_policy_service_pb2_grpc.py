# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_custom_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2
from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2
from edgelq_sdk.devices.proto.v1alpha2 import provisioning_policy_service_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in edgelq_sdk/devices/proto/v1alpha2/provisioning_policy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProvisioningPolicyServiceStub(object):
    """ProvisioningPolicy service API for Devices
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/GetProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.GetProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
                _registered_method=True)
        self.BatchGetProvisioningPolicies = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/BatchGetProvisioningPolicies',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesResponse.FromString,
                _registered_method=True)
        self.ListProvisioningPolicies = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/ListProvisioningPolicies',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesResponse.FromString,
                _registered_method=True)
        self.WatchProvisioningPolicy = channel.unary_stream(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/WatchProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyResponse.FromString,
                _registered_method=True)
        self.WatchProvisioningPolicies = channel.unary_stream(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/WatchProvisioningPolicies',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesResponse.FromString,
                _registered_method=True)
        self.CreateProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/CreateProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.CreateProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
                _registered_method=True)
        self.UpdateProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/UpdateProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.UpdateProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
                _registered_method=True)
        self.DeleteProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/DeleteProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.DeleteProvisioningPolicyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.ProvisionServiceAccountToProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/ProvisionServiceAccountToProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyResponse.FromString,
                _registered_method=True)
        self.RemoveServiceAccountFromProvisioningPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/RemoveServiceAccountFromProvisioningPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyResponse.FromString,
                _registered_method=True)
        self.ProvisionDeviceViaPolicy = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/ProvisionDeviceViaPolicy',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyResponse.FromString,
                _registered_method=True)
        self.RequestProvisioningApproval = channel.unary_unary(
                '/ntt.devices.v1alpha2.ProvisioningPolicyService/RequestProvisioningApproval',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalResponse.FromString,
                _registered_method=True)


class ProvisioningPolicyServiceServicer(object):
    """ProvisioningPolicy service API for Devices
    """

    def GetProvisioningPolicy(self, request, context):
        """GetProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetProvisioningPolicies(self, request, context):
        """BatchGetProvisioningPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProvisioningPolicies(self, request, context):
        """ListProvisioningPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchProvisioningPolicy(self, request, context):
        """WatchProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchProvisioningPolicies(self, request, context):
        """WatchProvisioningPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProvisioningPolicy(self, request, context):
        """CreateProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProvisioningPolicy(self, request, context):
        """UpdateProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProvisioningPolicy(self, request, context):
        """DeleteProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvisionServiceAccountToProvisioningPolicy(self, request, context):
        """ProvisionServiceAccountToProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveServiceAccountFromProvisioningPolicy(self, request, context):
        """RemoveServiceAccountFromProvisioningPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvisionDeviceViaPolicy(self, request, context):
        """ProvisionDeviceViaPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestProvisioningApproval(self, request, context):
        """RequestProvisioningApproval
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProvisioningPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.GetProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.SerializeToString,
            ),
            'BatchGetProvisioningPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetProvisioningPolicies,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesResponse.SerializeToString,
            ),
            'ListProvisioningPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProvisioningPolicies,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesResponse.SerializeToString,
            ),
            'WatchProvisioningPolicy': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyResponse.SerializeToString,
            ),
            'WatchProvisioningPolicies': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchProvisioningPolicies,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesResponse.SerializeToString,
            ),
            'CreateProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.CreateProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.SerializeToString,
            ),
            'UpdateProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.UpdateProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.SerializeToString,
            ),
            'DeleteProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.DeleteProvisioningPolicyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ProvisionServiceAccountToProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvisionServiceAccountToProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyResponse.SerializeToString,
            ),
            'RemoveServiceAccountFromProvisioningPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveServiceAccountFromProvisioningPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyResponse.SerializeToString,
            ),
            'ProvisionDeviceViaPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvisionDeviceViaPolicy,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyResponse.SerializeToString,
            ),
            'RequestProvisioningApproval': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestProvisioningApproval,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.devices.v1alpha2.ProvisioningPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.devices.v1alpha2.ProvisioningPolicyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProvisioningPolicyService(object):
    """ProvisioningPolicy service API for Devices
    """

    @staticmethod
    def GetProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/GetProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.GetProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchGetProvisioningPolicies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/BatchGetProvisioningPolicies',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.BatchGetProvisioningPoliciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListProvisioningPolicies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/ListProvisioningPolicies',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.ListProvisioningPoliciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WatchProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/WatchProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WatchProvisioningPolicies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/WatchProvisioningPolicies',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.WatchProvisioningPoliciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/CreateProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.CreateProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/UpdateProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.UpdateProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__pb2.ProvisioningPolicy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/DeleteProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__service__pb2.DeleteProvisioningPolicyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ProvisionServiceAccountToProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/ProvisionServiceAccountToProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionServiceAccountToProvisioningPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveServiceAccountFromProvisioningPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/RemoveServiceAccountFromProvisioningPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RemoveServiceAccountFromProvisioningPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ProvisionDeviceViaPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/ProvisionDeviceViaPolicy',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.ProvisionDeviceViaPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestProvisioningApproval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.devices.v1alpha2.ProvisioningPolicyService/RequestProvisioningApproval',
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1alpha2_dot_provisioning__policy__custom__pb2.RequestProvisioningApprovalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)