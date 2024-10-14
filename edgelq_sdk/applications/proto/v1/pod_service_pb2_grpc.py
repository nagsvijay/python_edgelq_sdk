# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.applications.proto.v1 import pod_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2
from edgelq_sdk.applications.proto.v1 import pod_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2
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
        + f' but the generated code in edgelq_sdk/applications/proto/v1/pod_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PodServiceStub(object):
    """Pod service API for Applications
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPod = channel.unary_unary(
                '/ntt.applications.v1.PodService/GetPod',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.GetPodRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
                _registered_method=True)
        self.BatchGetPods = channel.unary_unary(
                '/ntt.applications.v1.PodService/BatchGetPods',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsResponse.FromString,
                _registered_method=True)
        self.ListPods = channel.unary_unary(
                '/ntt.applications.v1.PodService/ListPods',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsResponse.FromString,
                _registered_method=True)
        self.WatchPod = channel.unary_stream(
                '/ntt.applications.v1.PodService/WatchPod',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodResponse.FromString,
                _registered_method=True)
        self.WatchPods = channel.unary_stream(
                '/ntt.applications.v1.PodService/WatchPods',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsResponse.FromString,
                _registered_method=True)
        self.CreatePod = channel.unary_unary(
                '/ntt.applications.v1.PodService/CreatePod',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.CreatePodRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
                _registered_method=True)
        self.UpdatePod = channel.unary_unary(
                '/ntt.applications.v1.PodService/UpdatePod',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.UpdatePodRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
                _registered_method=True)
        self.DeletePod = channel.unary_unary(
                '/ntt.applications.v1.PodService/DeletePod',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.DeletePodRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class PodServiceServicer(object):
    """Pod service API for Applications
    """

    def GetPod(self, request, context):
        """GetPod
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetPods(self, request, context):
        """BatchGetPods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPods(self, request, context):
        """ListPods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPod(self, request, context):
        """WatchPod
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchPods(self, request, context):
        """WatchPods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePod(self, request, context):
        """CreatePod
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePod(self, request, context):
        """UpdatePod
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePod(self, request, context):
        """DeletePod
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PodServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPod': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPod,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.GetPodRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.SerializeToString,
            ),
            'BatchGetPods': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetPods,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsResponse.SerializeToString,
            ),
            'ListPods': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPods,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsResponse.SerializeToString,
            ),
            'WatchPod': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPod,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodResponse.SerializeToString,
            ),
            'WatchPods': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchPods,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsResponse.SerializeToString,
            ),
            'CreatePod': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePod,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.CreatePodRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.SerializeToString,
            ),
            'UpdatePod': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePod,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.UpdatePodRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.SerializeToString,
            ),
            'DeletePod': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePod,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.DeletePodRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.applications.v1.PodService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.applications.v1.PodService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PodService(object):
    """Pod service API for Applications
    """

    @staticmethod
    def GetPod(request,
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
            '/ntt.applications.v1.PodService/GetPod',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.GetPodRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
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
    def BatchGetPods(request,
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
            '/ntt.applications.v1.PodService/BatchGetPods',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.BatchGetPodsResponse.FromString,
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
    def ListPods(request,
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
            '/ntt.applications.v1.PodService/ListPods',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.ListPodsResponse.FromString,
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
    def WatchPod(request,
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
            '/ntt.applications.v1.PodService/WatchPod',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodResponse.FromString,
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
    def WatchPods(request,
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
            '/ntt.applications.v1.PodService/WatchPods',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.WatchPodsResponse.FromString,
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
    def CreatePod(request,
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
            '/ntt.applications.v1.PodService/CreatePod',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.CreatePodRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
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
    def UpdatePod(request,
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
            '/ntt.applications.v1.PodService/UpdatePod',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.UpdatePodRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__pb2.Pod.FromString,
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
    def DeletePod(request,
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
            '/ntt.applications.v1.PodService/DeletePod',
            edgelq__sdk_dot_applications_dot_proto_dot_v1_dot_pod__service__pb2.DeletePodRequest.SerializeToString,
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
