# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_request_custom_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_request_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2
from edgelq_sdk.limits.proto.v1alpha2 import plan_assignment_request_service_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2
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
        + f' but the generated code in edgelq_sdk/limits/proto/v1alpha2/plan_assignment_request_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PlanAssignmentRequestServiceStub(object):
    """PlanAssignmentRequest service API for Limits
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlanAssignmentRequest = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/GetPlanAssignmentRequest',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.GetPlanAssignmentRequestRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
                _registered_method=True)
        self.BatchGetPlanAssignmentRequests = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/BatchGetPlanAssignmentRequests',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsResponse.FromString,
                _registered_method=True)
        self.ListPlanAssignmentRequests = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/ListPlanAssignmentRequests',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.FromString,
                _registered_method=True)
        self.WatchPlanAssignmentRequest = channel.unary_stream(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/WatchPlanAssignmentRequest',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestResponse.FromString,
                _registered_method=True)
        self.WatchPlanAssignmentRequests = channel.unary_stream(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/WatchPlanAssignmentRequests',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsResponse.FromString,
                _registered_method=True)
        self.CreatePlanAssignmentRequest = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/CreatePlanAssignmentRequest',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.CreatePlanAssignmentRequestRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
                _registered_method=True)
        self.UpdatePlanAssignmentRequest = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/UpdatePlanAssignmentRequest',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.UpdatePlanAssignmentRequestRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
                _registered_method=True)
        self.DeletePlanAssignmentRequest = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/DeletePlanAssignmentRequest',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.DeletePlanAssignmentRequestRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.AcceptPlanAssignment = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/AcceptPlanAssignment',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentResponse.FromString,
                _registered_method=True)
        self.DeclinePlanAssignment = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/DeclinePlanAssignment',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentResponse.FromString,
                _registered_method=True)
        self.ListApproverPlanAssignmentRequests = channel.unary_unary(
                '/ntt.limits.v1alpha2.PlanAssignmentRequestService/ListApproverPlanAssignmentRequests',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.ListApproverPlanAssignmentRequestsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.FromString,
                _registered_method=True)


class PlanAssignmentRequestServiceServicer(object):
    """PlanAssignmentRequest service API for Limits
    """

    def GetPlanAssignmentRequest(self, request, context):
        """GetPlanAssignmentRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetPlanAssignmentRequests(self, request, context):
        """BatchGetPlanAssignmentRequests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlanAssignmentRequests(self, request, context):
        """ListPlanAssignmentRequests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPlanAssignmentRequest(self, request, context):
        """WatchPlanAssignmentRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPlanAssignmentRequests(self, request, context):
        """WatchPlanAssignmentRequests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePlanAssignmentRequest(self, request, context):
        """CreatePlanAssignmentRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePlanAssignmentRequest(self, request, context):
        """UpdatePlanAssignmentRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePlanAssignmentRequest(self, request, context):
        """DeletePlanAssignmentRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptPlanAssignment(self, request, context):
        """AcceptPlanAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeclinePlanAssignment(self, request, context):
        """DeclinePlanAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListApproverPlanAssignmentRequests(self, request, context):
        """ListApproverPlanAssignmentRequests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlanAssignmentRequestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlanAssignmentRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlanAssignmentRequest,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.GetPlanAssignmentRequestRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.SerializeToString,
            ),
            'BatchGetPlanAssignmentRequests': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetPlanAssignmentRequests,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsResponse.SerializeToString,
            ),
            'ListPlanAssignmentRequests': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlanAssignmentRequests,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.SerializeToString,
            ),
            'WatchPlanAssignmentRequest': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPlanAssignmentRequest,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestResponse.SerializeToString,
            ),
            'WatchPlanAssignmentRequests': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPlanAssignmentRequests,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsResponse.SerializeToString,
            ),
            'CreatePlanAssignmentRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePlanAssignmentRequest,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.CreatePlanAssignmentRequestRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.SerializeToString,
            ),
            'UpdatePlanAssignmentRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePlanAssignmentRequest,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.UpdatePlanAssignmentRequestRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.SerializeToString,
            ),
            'DeletePlanAssignmentRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePlanAssignmentRequest,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.DeletePlanAssignmentRequestRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AcceptPlanAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptPlanAssignment,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentResponse.SerializeToString,
            ),
            'DeclinePlanAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeclinePlanAssignment,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentResponse.SerializeToString,
            ),
            'ListApproverPlanAssignmentRequests': grpc.unary_unary_rpc_method_handler(
                    servicer.ListApproverPlanAssignmentRequests,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.ListApproverPlanAssignmentRequestsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.limits.v1alpha2.PlanAssignmentRequestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.limits.v1alpha2.PlanAssignmentRequestService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PlanAssignmentRequestService(object):
    """PlanAssignmentRequest service API for Limits
    """

    @staticmethod
    def GetPlanAssignmentRequest(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/GetPlanAssignmentRequest',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.GetPlanAssignmentRequestRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
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
    def BatchGetPlanAssignmentRequests(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/BatchGetPlanAssignmentRequests',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.BatchGetPlanAssignmentRequestsResponse.FromString,
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
    def ListPlanAssignmentRequests(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/ListPlanAssignmentRequests',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.FromString,
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
    def WatchPlanAssignmentRequest(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/WatchPlanAssignmentRequest',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestResponse.FromString,
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
    def WatchPlanAssignmentRequests(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/WatchPlanAssignmentRequests',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.WatchPlanAssignmentRequestsResponse.FromString,
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
    def CreatePlanAssignmentRequest(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/CreatePlanAssignmentRequest',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.CreatePlanAssignmentRequestRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
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
    def UpdatePlanAssignmentRequest(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/UpdatePlanAssignmentRequest',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.UpdatePlanAssignmentRequestRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__pb2.PlanAssignmentRequest.FromString,
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
    def DeletePlanAssignmentRequest(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/DeletePlanAssignmentRequest',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.DeletePlanAssignmentRequestRequest.SerializeToString,
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
    def AcceptPlanAssignment(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/AcceptPlanAssignment',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.AcceptPlanAssignmentResponse.FromString,
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
    def DeclinePlanAssignment(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/DeclinePlanAssignment',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.DeclinePlanAssignmentResponse.FromString,
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
    def ListApproverPlanAssignmentRequests(request,
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
            '/ntt.limits.v1alpha2.PlanAssignmentRequestService/ListApproverPlanAssignmentRequests',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__custom__pb2.ListApproverPlanAssignmentRequestsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_plan__assignment__request__service__pb2.ListPlanAssignmentRequestsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
