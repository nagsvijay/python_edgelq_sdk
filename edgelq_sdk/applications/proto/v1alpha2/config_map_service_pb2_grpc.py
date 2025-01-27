# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.applications.proto.v1alpha2 import config_map_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2
from edgelq_sdk.applications.proto.v1alpha2 import config_map_service_pb2 as edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2
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
        + f' but the generated code in edgelq_sdk/applications/proto/v1alpha2/config_map_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ConfigMapServiceStub(object):
    """ConfigMap service API for Applications
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfigMap = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/GetConfigMap',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.GetConfigMapRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
                _registered_method=True)
        self.BatchGetConfigMaps = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/BatchGetConfigMaps',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsResponse.FromString,
                _registered_method=True)
        self.ListConfigMaps = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/ListConfigMaps',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsResponse.FromString,
                _registered_method=True)
        self.WatchConfigMap = channel.unary_stream(
                '/ntt.applications.v1alpha2.ConfigMapService/WatchConfigMap',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapResponse.FromString,
                _registered_method=True)
        self.WatchConfigMaps = channel.unary_stream(
                '/ntt.applications.v1alpha2.ConfigMapService/WatchConfigMaps',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsResponse.FromString,
                _registered_method=True)
        self.CreateConfigMap = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/CreateConfigMap',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.CreateConfigMapRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
                _registered_method=True)
        self.UpdateConfigMap = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/UpdateConfigMap',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.UpdateConfigMapRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
                _registered_method=True)
        self.DeleteConfigMap = channel.unary_unary(
                '/ntt.applications.v1alpha2.ConfigMapService/DeleteConfigMap',
                request_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.DeleteConfigMapRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class ConfigMapServiceServicer(object):
    """ConfigMap service API for Applications
    """

    def GetConfigMap(self, request, context):
        """GetConfigMap
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetConfigMaps(self, request, context):
        """BatchGetConfigMaps
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConfigMaps(self, request, context):
        """ListConfigMaps
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchConfigMap(self, request, context):
        """WatchConfigMap
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchConfigMaps(self, request, context):
        """WatchConfigMaps
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConfigMap(self, request, context):
        """CreateConfigMap
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConfigMap(self, request, context):
        """UpdateConfigMap
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteConfigMap(self, request, context):
        """DeleteConfigMap
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConfigMapServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfigMap': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigMap,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.GetConfigMapRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.SerializeToString,
            ),
            'BatchGetConfigMaps': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetConfigMaps,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsResponse.SerializeToString,
            ),
            'ListConfigMaps': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConfigMaps,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsResponse.SerializeToString,
            ),
            'WatchConfigMap': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchConfigMap,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapResponse.SerializeToString,
            ),
            'WatchConfigMaps': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchConfigMaps,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsResponse.SerializeToString,
            ),
            'CreateConfigMap': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConfigMap,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.CreateConfigMapRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.SerializeToString,
            ),
            'UpdateConfigMap': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConfigMap,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.UpdateConfigMapRequest.FromString,
                    response_serializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.SerializeToString,
            ),
            'DeleteConfigMap': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteConfigMap,
                    request_deserializer=edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.DeleteConfigMapRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.applications.v1alpha2.ConfigMapService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.applications.v1alpha2.ConfigMapService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ConfigMapService(object):
    """ConfigMap service API for Applications
    """

    @staticmethod
    def GetConfigMap(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/GetConfigMap',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.GetConfigMapRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
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
    def BatchGetConfigMaps(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/BatchGetConfigMaps',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.BatchGetConfigMapsResponse.FromString,
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
    def ListConfigMaps(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/ListConfigMaps',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.ListConfigMapsResponse.FromString,
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
    def WatchConfigMap(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/WatchConfigMap',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapResponse.FromString,
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
    def WatchConfigMaps(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/WatchConfigMaps',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.WatchConfigMapsResponse.FromString,
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
    def CreateConfigMap(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/CreateConfigMap',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.CreateConfigMapRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
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
    def UpdateConfigMap(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/UpdateConfigMap',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.UpdateConfigMapRequest.SerializeToString,
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__pb2.ConfigMap.FromString,
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
    def DeleteConfigMap(request,
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
            '/ntt.applications.v1alpha2.ConfigMapService/DeleteConfigMap',
            edgelq__sdk_dot_applications_dot_proto_dot_v1alpha2_dot_config__map__service__pb2.DeleteConfigMapRequest.SerializeToString,
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
