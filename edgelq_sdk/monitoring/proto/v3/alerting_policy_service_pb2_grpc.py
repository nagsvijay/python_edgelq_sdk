# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.monitoring.proto.v3 import alerting_policy_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2
from edgelq_sdk.monitoring.proto.v3 import alerting_policy_service_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2
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
        + f' but the generated code in edgelq_sdk/monitoring/proto/v3/alerting_policy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AlertingPolicyServiceStub(object):
    """AlertingPolicy service API for Monitoring
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAlertingPolicy = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/GetAlertingPolicy',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.GetAlertingPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
                _registered_method=True)
        self.BatchGetAlertingPolicies = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/BatchGetAlertingPolicies',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesResponse.FromString,
                _registered_method=True)
        self.ListAlertingPolicies = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/ListAlertingPolicies',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesResponse.FromString,
                _registered_method=True)
        self.WatchAlertingPolicy = channel.unary_stream(
                '/ntt.monitoring.v3.AlertingPolicyService/WatchAlertingPolicy',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyResponse.FromString,
                _registered_method=True)
        self.WatchAlertingPolicies = channel.unary_stream(
                '/ntt.monitoring.v3.AlertingPolicyService/WatchAlertingPolicies',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesResponse.FromString,
                _registered_method=True)
        self.CreateAlertingPolicy = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/CreateAlertingPolicy',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.CreateAlertingPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
                _registered_method=True)
        self.UpdateAlertingPolicy = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/UpdateAlertingPolicy',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.UpdateAlertingPolicyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
                _registered_method=True)
        self.DeleteAlertingPolicy = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/DeleteAlertingPolicy',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.DeleteAlertingPolicyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SearchAlertingPolicies = channel.unary_unary(
                '/ntt.monitoring.v3.AlertingPolicyService/SearchAlertingPolicies',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesResponse.FromString,
                _registered_method=True)


class AlertingPolicyServiceServicer(object):
    """AlertingPolicy service API for Monitoring
    """

    def GetAlertingPolicy(self, request, context):
        """GetAlertingPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetAlertingPolicies(self, request, context):
        """BatchGetAlertingPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAlertingPolicies(self, request, context):
        """ListAlertingPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAlertingPolicy(self, request, context):
        """WatchAlertingPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAlertingPolicies(self, request, context):
        """WatchAlertingPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAlertingPolicy(self, request, context):
        """CreateAlertingPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAlertingPolicy(self, request, context):
        """UpdateAlertingPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAlertingPolicy(self, request, context):
        """DeleteAlertingPolicy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchAlertingPolicies(self, request, context):
        """SearchAlertingPolicies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertingPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAlertingPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAlertingPolicy,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.GetAlertingPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.SerializeToString,
            ),
            'BatchGetAlertingPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetAlertingPolicies,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesResponse.SerializeToString,
            ),
            'ListAlertingPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAlertingPolicies,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesResponse.SerializeToString,
            ),
            'WatchAlertingPolicy': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAlertingPolicy,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyResponse.SerializeToString,
            ),
            'WatchAlertingPolicies': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAlertingPolicies,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesResponse.SerializeToString,
            ),
            'CreateAlertingPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAlertingPolicy,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.CreateAlertingPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.SerializeToString,
            ),
            'UpdateAlertingPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAlertingPolicy,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.UpdateAlertingPolicyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.SerializeToString,
            ),
            'DeleteAlertingPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAlertingPolicy,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.DeleteAlertingPolicyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SearchAlertingPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchAlertingPolicies,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.monitoring.v3.AlertingPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.monitoring.v3.AlertingPolicyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AlertingPolicyService(object):
    """AlertingPolicy service API for Monitoring
    """

    @staticmethod
    def GetAlertingPolicy(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/GetAlertingPolicy',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.GetAlertingPolicyRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
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
    def BatchGetAlertingPolicies(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/BatchGetAlertingPolicies',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.BatchGetAlertingPoliciesResponse.FromString,
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
    def ListAlertingPolicies(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/ListAlertingPolicies',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.ListAlertingPoliciesResponse.FromString,
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
    def WatchAlertingPolicy(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/WatchAlertingPolicy',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPolicyResponse.FromString,
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
    def WatchAlertingPolicies(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/WatchAlertingPolicies',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.WatchAlertingPoliciesResponse.FromString,
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
    def CreateAlertingPolicy(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/CreateAlertingPolicy',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.CreateAlertingPolicyRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
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
    def UpdateAlertingPolicy(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/UpdateAlertingPolicy',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.UpdateAlertingPolicyRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__pb2.AlertingPolicy.FromString,
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
    def DeleteAlertingPolicy(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/DeleteAlertingPolicy',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.DeleteAlertingPolicyRequest.SerializeToString,
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
    def SearchAlertingPolicies(request,
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
            '/ntt.monitoring.v3.AlertingPolicyService/SearchAlertingPolicies',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alerting__policy__service__pb2.SearchAlertingPoliciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
