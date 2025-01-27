# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.limits.proto.v1 import accepted_plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2
from edgelq_sdk.limits.proto.v1 import accepted_plan_service_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2
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
        + f' but the generated code in edgelq_sdk/limits/proto/v1/accepted_plan_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AcceptedPlanServiceStub(object):
    """AcceptedPlan service API for Limits
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAcceptedPlan = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/GetAcceptedPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.GetAcceptedPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
                _registered_method=True)
        self.BatchGetAcceptedPlans = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/BatchGetAcceptedPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansResponse.FromString,
                _registered_method=True)
        self.ListAcceptedPlans = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/ListAcceptedPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansResponse.FromString,
                _registered_method=True)
        self.WatchAcceptedPlan = channel.unary_stream(
                '/ntt.limits.v1.AcceptedPlanService/WatchAcceptedPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanResponse.FromString,
                _registered_method=True)
        self.WatchAcceptedPlans = channel.unary_stream(
                '/ntt.limits.v1.AcceptedPlanService/WatchAcceptedPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansResponse.FromString,
                _registered_method=True)
        self.CreateAcceptedPlan = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/CreateAcceptedPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.CreateAcceptedPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
                _registered_method=True)
        self.UpdateAcceptedPlan = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/UpdateAcceptedPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.UpdateAcceptedPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
                _registered_method=True)
        self.DeleteAcceptedPlan = channel.unary_unary(
                '/ntt.limits.v1.AcceptedPlanService/DeleteAcceptedPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.DeleteAcceptedPlanRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class AcceptedPlanServiceServicer(object):
    """AcceptedPlan service API for Limits
    """

    def GetAcceptedPlan(self, request, context):
        """GetAcceptedPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetAcceptedPlans(self, request, context):
        """BatchGetAcceptedPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAcceptedPlans(self, request, context):
        """ListAcceptedPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAcceptedPlan(self, request, context):
        """WatchAcceptedPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAcceptedPlans(self, request, context):
        """WatchAcceptedPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAcceptedPlan(self, request, context):
        """CreateAcceptedPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAcceptedPlan(self, request, context):
        """UpdateAcceptedPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAcceptedPlan(self, request, context):
        """DeleteAcceptedPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AcceptedPlanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAcceptedPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAcceptedPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.GetAcceptedPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.SerializeToString,
            ),
            'BatchGetAcceptedPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetAcceptedPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansResponse.SerializeToString,
            ),
            'ListAcceptedPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAcceptedPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansResponse.SerializeToString,
            ),
            'WatchAcceptedPlan': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAcceptedPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanResponse.SerializeToString,
            ),
            'WatchAcceptedPlans': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAcceptedPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansResponse.SerializeToString,
            ),
            'CreateAcceptedPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAcceptedPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.CreateAcceptedPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.SerializeToString,
            ),
            'UpdateAcceptedPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAcceptedPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.UpdateAcceptedPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.SerializeToString,
            ),
            'DeleteAcceptedPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAcceptedPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.DeleteAcceptedPlanRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.limits.v1.AcceptedPlanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.limits.v1.AcceptedPlanService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AcceptedPlanService(object):
    """AcceptedPlan service API for Limits
    """

    @staticmethod
    def GetAcceptedPlan(request,
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
            '/ntt.limits.v1.AcceptedPlanService/GetAcceptedPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.GetAcceptedPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
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
    def BatchGetAcceptedPlans(request,
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
            '/ntt.limits.v1.AcceptedPlanService/BatchGetAcceptedPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.BatchGetAcceptedPlansResponse.FromString,
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
    def ListAcceptedPlans(request,
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
            '/ntt.limits.v1.AcceptedPlanService/ListAcceptedPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.ListAcceptedPlansResponse.FromString,
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
    def WatchAcceptedPlan(request,
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
            '/ntt.limits.v1.AcceptedPlanService/WatchAcceptedPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlanResponse.FromString,
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
    def WatchAcceptedPlans(request,
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
            '/ntt.limits.v1.AcceptedPlanService/WatchAcceptedPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.WatchAcceptedPlansResponse.FromString,
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
    def CreateAcceptedPlan(request,
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
            '/ntt.limits.v1.AcceptedPlanService/CreateAcceptedPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.CreateAcceptedPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
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
    def UpdateAcceptedPlan(request,
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
            '/ntt.limits.v1.AcceptedPlanService/UpdateAcceptedPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.UpdateAcceptedPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__pb2.AcceptedPlan.FromString,
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
    def DeleteAcceptedPlan(request,
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
            '/ntt.limits.v1.AcceptedPlanService/DeleteAcceptedPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_accepted__plan__service__pb2.DeleteAcceptedPlanRequest.SerializeToString,
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
