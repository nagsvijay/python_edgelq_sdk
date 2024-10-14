# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.applications.proto.v1 import distribution_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2
from edgelq_sdk.applications.proto.v1 import distribution_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2
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
        + f' but the generated code in edgelq_sdk/applications/proto/v1/distribution_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DistributionServiceStub(object):
    """Distribution service API for Applications
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDistribution = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/GetDistribution',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.GetDistributionRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
                _registered_method=True)
        self.BatchGetDistributions = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/BatchGetDistributions',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsResponse.FromString,
                _registered_method=True)
        self.ListDistributions = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/ListDistributions',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsResponse.FromString,
                _registered_method=True)
        self.WatchDistribution = channel.unary_stream(
                '/ntt.applications.v1.DistributionService/WatchDistribution',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionResponse.FromString,
                _registered_method=True)
        self.WatchDistributions = channel.unary_stream(
                '/ntt.applications.v1.DistributionService/WatchDistributions',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsResponse.FromString,
                _registered_method=True)
        self.CreateDistribution = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/CreateDistribution',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.CreateDistributionRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
                _registered_method=True)
        self.UpdateDistribution = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/UpdateDistribution',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.UpdateDistributionRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
                _registered_method=True)
        self.DeleteDistribution = channel.unary_unary(
                '/ntt.applications.v1.DistributionService/DeleteDistribution',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.DeleteDistributionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class DistributionServiceServicer(object):
    """Distribution service API for Applications
    """

    def GetDistribution(self, request, context):
        """GetDistribution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetDistributions(self, request, context):
        """BatchGetDistributions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDistributions(self, request, context):
        """ListDistributions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchDistribution(self, request, context):
        """WatchDistribution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchDistributions(self, request, context):
        """WatchDistributions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDistribution(self, request, context):
        """CreateDistribution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDistribution(self, request, context):
        """UpdateDistribution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDistribution(self, request, context):
        """DeleteDistribution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DistributionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDistribution,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.GetDistributionRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.SerializeToString,
            ),
            'BatchGetDistributions': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetDistributions,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsResponse.SerializeToString,
            ),
            'ListDistributions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDistributions,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsResponse.SerializeToString,
            ),
            'WatchDistribution': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchDistribution,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionResponse.SerializeToString,
            ),
            'WatchDistributions': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchDistributions,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsResponse.SerializeToString,
            ),
            'CreateDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDistribution,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.CreateDistributionRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.SerializeToString,
            ),
            'UpdateDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDistribution,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.UpdateDistributionRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.SerializeToString,
            ),
            'DeleteDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDistribution,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.DeleteDistributionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.applications.v1.DistributionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.applications.v1.DistributionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DistributionService(object):
    """Distribution service API for Applications
    """

    @staticmethod
    def GetDistribution(request,
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
            '/ntt.applications.v1.DistributionService/GetDistribution',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.GetDistributionRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
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
    def BatchGetDistributions(request,
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
            '/ntt.applications.v1.DistributionService/BatchGetDistributions',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.BatchGetDistributionsResponse.FromString,
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
    def ListDistributions(request,
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
            '/ntt.applications.v1.DistributionService/ListDistributions',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.ListDistributionsResponse.FromString,
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
    def WatchDistribution(request,
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
            '/ntt.applications.v1.DistributionService/WatchDistribution',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionResponse.FromString,
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
    def WatchDistributions(request,
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
            '/ntt.applications.v1.DistributionService/WatchDistributions',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.WatchDistributionsResponse.FromString,
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
    def CreateDistribution(request,
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
            '/ntt.applications.v1.DistributionService/CreateDistribution',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.CreateDistributionRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
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
    def UpdateDistribution(request,
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
            '/ntt.applications.v1.DistributionService/UpdateDistribution',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.UpdateDistributionRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__pb2.Distribution.FromString,
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
    def DeleteDistribution(request,
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
            '/ntt.applications.v1.DistributionService/DeleteDistribution',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_distribution__service__pb2.DeleteDistributionRequest.SerializeToString,
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