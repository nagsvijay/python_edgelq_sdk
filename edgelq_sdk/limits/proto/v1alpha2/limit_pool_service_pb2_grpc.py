# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_custom_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__custom__pb2
from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2
from edgelq_sdk.limits.proto.v1alpha2 import limit_pool_service_pb2 as edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2
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
        + f' but the generated code in edgelq_sdk/limits/proto/v1alpha2/limit_pool_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LimitPoolServiceStub(object):
    """LimitPool service API for Limits
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLimitPool = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/GetLimitPool',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.GetLimitPoolRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
                _registered_method=True)
        self.BatchGetLimitPools = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/BatchGetLimitPools',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsResponse.FromString,
                _registered_method=True)
        self.ListLimitPools = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/ListLimitPools',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsResponse.FromString,
                _registered_method=True)
        self.WatchLimitPool = channel.unary_stream(
                '/ntt.limits.v1alpha2.LimitPoolService/WatchLimitPool',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolResponse.FromString,
                _registered_method=True)
        self.WatchLimitPools = channel.unary_stream(
                '/ntt.limits.v1alpha2.LimitPoolService/WatchLimitPools',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsResponse.FromString,
                _registered_method=True)
        self.UpdateLimitPool = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/UpdateLimitPool',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.UpdateLimitPoolRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
                _registered_method=True)
        self.DeleteLimitPool = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/DeleteLimitPool',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.DeleteLimitPoolRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.MigrateLimitPoolSource = channel.unary_unary(
                '/ntt.limits.v1alpha2.LimitPoolService/MigrateLimitPoolSource',
                request_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__custom__pb2.MigrateLimitPoolSourceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
                _registered_method=True)


class LimitPoolServiceServicer(object):
    """LimitPool service API for Limits
    """

    def GetLimitPool(self, request, context):
        """GetLimitPool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetLimitPools(self, request, context):
        """BatchGetLimitPools
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLimitPools(self, request, context):
        """ListLimitPools
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchLimitPool(self, request, context):
        """WatchLimitPool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchLimitPools(self, request, context):
        """WatchLimitPools
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLimitPool(self, request, context):
        """UpdateLimitPool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLimitPool(self, request, context):
        """DeleteLimitPool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MigrateLimitPoolSource(self, request, context):
        """MigrateLimitPoolSource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LimitPoolServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLimitPool': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLimitPool,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.GetLimitPoolRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.SerializeToString,
            ),
            'BatchGetLimitPools': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetLimitPools,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsResponse.SerializeToString,
            ),
            'ListLimitPools': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLimitPools,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsResponse.SerializeToString,
            ),
            'WatchLimitPool': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchLimitPool,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolResponse.SerializeToString,
            ),
            'WatchLimitPools': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchLimitPools,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsResponse.SerializeToString,
            ),
            'UpdateLimitPool': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateLimitPool,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.UpdateLimitPoolRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.SerializeToString,
            ),
            'DeleteLimitPool': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteLimitPool,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.DeleteLimitPoolRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'MigrateLimitPoolSource': grpc.unary_unary_rpc_method_handler(
                    servicer.MigrateLimitPoolSource,
                    request_deserializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__custom__pb2.MigrateLimitPoolSourceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.limits.v1alpha2.LimitPoolService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.limits.v1alpha2.LimitPoolService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LimitPoolService(object):
    """LimitPool service API for Limits
    """

    @staticmethod
    def GetLimitPool(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/GetLimitPool',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.GetLimitPoolRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
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
    def BatchGetLimitPools(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/BatchGetLimitPools',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.BatchGetLimitPoolsResponse.FromString,
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
    def ListLimitPools(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/ListLimitPools',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.ListLimitPoolsResponse.FromString,
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
    def WatchLimitPool(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/WatchLimitPool',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolResponse.FromString,
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
    def WatchLimitPools(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/WatchLimitPools',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.WatchLimitPoolsResponse.FromString,
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
    def UpdateLimitPool(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/UpdateLimitPool',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.UpdateLimitPoolRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
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
    def DeleteLimitPool(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/DeleteLimitPool',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__service__pb2.DeleteLimitPoolRequest.SerializeToString,
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
    def MigrateLimitPoolSource(request,
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
            '/ntt.limits.v1alpha2.LimitPoolService/MigrateLimitPoolSource',
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__custom__pb2.MigrateLimitPoolSourceRequest.SerializeToString,
            edgelq__sdk_dot_limits_dot_proto_dot_v1alpha2_dot_limit__pool__pb2.LimitPool.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
