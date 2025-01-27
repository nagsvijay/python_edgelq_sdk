# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.limits.proto.v1 import plan_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2
from edgelq_sdk.limits.proto.v1 import plan_service_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2
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
        + f' but the generated code in edgelq_sdk/limits/proto/v1/plan_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PlanServiceStub(object):
    """Plan service API for Limits
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlan = channel.unary_unary(
                '/ntt.limits.v1.PlanService/GetPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.GetPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
                _registered_method=True)
        self.BatchGetPlans = channel.unary_unary(
                '/ntt.limits.v1.PlanService/BatchGetPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansResponse.FromString,
                _registered_method=True)
        self.ListPlans = channel.unary_unary(
                '/ntt.limits.v1.PlanService/ListPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansResponse.FromString,
                _registered_method=True)
        self.WatchPlan = channel.unary_stream(
                '/ntt.limits.v1.PlanService/WatchPlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanResponse.FromString,
                _registered_method=True)
        self.WatchPlans = channel.unary_stream(
                '/ntt.limits.v1.PlanService/WatchPlans',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansResponse.FromString,
                _registered_method=True)
        self.CreatePlan = channel.unary_unary(
                '/ntt.limits.v1.PlanService/CreatePlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.CreatePlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
                _registered_method=True)
        self.UpdatePlan = channel.unary_unary(
                '/ntt.limits.v1.PlanService/UpdatePlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.UpdatePlanRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
                _registered_method=True)
        self.DeletePlan = channel.unary_unary(
                '/ntt.limits.v1.PlanService/DeletePlan',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.DeletePlanRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class PlanServiceServicer(object):
    """Plan service API for Limits
    """

    def GetPlan(self, request, context):
        """GetPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetPlans(self, request, context):
        """BatchGetPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlans(self, request, context):
        """ListPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPlan(self, request, context):
        """WatchPlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPlans(self, request, context):
        """WatchPlans
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePlan(self, request, context):
        """CreatePlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePlan(self, request, context):
        """UpdatePlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePlan(self, request, context):
        """DeletePlan
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.GetPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.SerializeToString,
            ),
            'BatchGetPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansResponse.SerializeToString,
            ),
            'ListPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansResponse.SerializeToString,
            ),
            'WatchPlan': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanResponse.SerializeToString,
            ),
            'WatchPlans': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPlans,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansResponse.SerializeToString,
            ),
            'CreatePlan': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.CreatePlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.SerializeToString,
            ),
            'UpdatePlan': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.UpdatePlanRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.SerializeToString,
            ),
            'DeletePlan': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePlan,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.DeletePlanRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.limits.v1.PlanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.limits.v1.PlanService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PlanService(object):
    """Plan service API for Limits
    """

    @staticmethod
    def GetPlan(request,
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
            '/ntt.limits.v1.PlanService/GetPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.GetPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
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
    def BatchGetPlans(request,
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
            '/ntt.limits.v1.PlanService/BatchGetPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.BatchGetPlansResponse.FromString,
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
    def ListPlans(request,
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
            '/ntt.limits.v1.PlanService/ListPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.ListPlansResponse.FromString,
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
    def WatchPlan(request,
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
            '/ntt.limits.v1.PlanService/WatchPlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlanResponse.FromString,
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
    def WatchPlans(request,
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
            '/ntt.limits.v1.PlanService/WatchPlans',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.WatchPlansResponse.FromString,
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
    def CreatePlan(request,
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
            '/ntt.limits.v1.PlanService/CreatePlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.CreatePlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
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
    def UpdatePlan(request,
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
            '/ntt.limits.v1.PlanService/UpdatePlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.UpdatePlanRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__pb2.Plan.FromString,
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
    def DeletePlan(request,
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
            '/ntt.limits.v1.PlanService/DeletePlan',
            edgelq__sdk_dot_limits_dot_proto_dot_v1_dot_plan__service__pb2.DeletePlanRequest.SerializeToString,
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
