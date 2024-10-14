# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.secrets.proto.v1 import crypto_key_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__pb2
from edgelq_sdk.secrets.proto.v1 import crypto_key_service_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2
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
        + f' but the generated code in edgelq_sdk/secrets/proto/v1/crypto_key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CryptoKeyServiceStub(object):
    """CryptoKey service API for Secrets
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCryptoKey = channel.unary_unary(
                '/ntt.secrets.v1.CryptoKeyService/GetCryptoKey',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.GetCryptoKeyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__pb2.CryptoKey.FromString,
                _registered_method=True)
        self.BatchGetCryptoKeys = channel.unary_unary(
                '/ntt.secrets.v1.CryptoKeyService/BatchGetCryptoKeys',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysResponse.FromString,
                _registered_method=True)
        self.ListCryptoKeys = channel.unary_unary(
                '/ntt.secrets.v1.CryptoKeyService/ListCryptoKeys',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysResponse.FromString,
                _registered_method=True)
        self.WatchCryptoKey = channel.unary_stream(
                '/ntt.secrets.v1.CryptoKeyService/WatchCryptoKey',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyResponse.FromString,
                _registered_method=True)
        self.WatchCryptoKeys = channel.unary_stream(
                '/ntt.secrets.v1.CryptoKeyService/WatchCryptoKeys',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysResponse.FromString,
                _registered_method=True)
        self.DeleteCryptoKey = channel.unary_unary(
                '/ntt.secrets.v1.CryptoKeyService/DeleteCryptoKey',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.DeleteCryptoKeyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class CryptoKeyServiceServicer(object):
    """CryptoKey service API for Secrets
    """

    def GetCryptoKey(self, request, context):
        """GetCryptoKey
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetCryptoKeys(self, request, context):
        """BatchGetCryptoKeys
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCryptoKeys(self, request, context):
        """ListCryptoKeys
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchCryptoKey(self, request, context):
        """WatchCryptoKey
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchCryptoKeys(self, request, context):
        """WatchCryptoKeys
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCryptoKey(self, request, context):
        """DeleteCryptoKey
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CryptoKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCryptoKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCryptoKey,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.GetCryptoKeyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__pb2.CryptoKey.SerializeToString,
            ),
            'BatchGetCryptoKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetCryptoKeys,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysResponse.SerializeToString,
            ),
            'ListCryptoKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCryptoKeys,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysResponse.SerializeToString,
            ),
            'WatchCryptoKey': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchCryptoKey,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyResponse.SerializeToString,
            ),
            'WatchCryptoKeys': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchCryptoKeys,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysResponse.SerializeToString,
            ),
            'DeleteCryptoKey': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCryptoKey,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.DeleteCryptoKeyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.secrets.v1.CryptoKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.secrets.v1.CryptoKeyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CryptoKeyService(object):
    """CryptoKey service API for Secrets
    """

    @staticmethod
    def GetCryptoKey(request,
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
            '/ntt.secrets.v1.CryptoKeyService/GetCryptoKey',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.GetCryptoKeyRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__pb2.CryptoKey.FromString,
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
    def BatchGetCryptoKeys(request,
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
            '/ntt.secrets.v1.CryptoKeyService/BatchGetCryptoKeys',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.BatchGetCryptoKeysResponse.FromString,
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
    def ListCryptoKeys(request,
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
            '/ntt.secrets.v1.CryptoKeyService/ListCryptoKeys',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.ListCryptoKeysResponse.FromString,
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
    def WatchCryptoKey(request,
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
            '/ntt.secrets.v1.CryptoKeyService/WatchCryptoKey',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeyResponse.FromString,
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
    def WatchCryptoKeys(request,
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
            '/ntt.secrets.v1.CryptoKeyService/WatchCryptoKeys',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.WatchCryptoKeysResponse.FromString,
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
    def DeleteCryptoKey(request,
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
            '/ntt.secrets.v1.CryptoKeyService/DeleteCryptoKey',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_crypto__key__service__pb2.DeleteCryptoKeyRequest.SerializeToString,
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