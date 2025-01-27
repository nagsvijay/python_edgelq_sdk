# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.ztp.proto.v1 import tpm_attestation_cert_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2
from edgelq_sdk.ztp.proto.v1 import tpm_attestation_cert_service_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2
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
        + f' but the generated code in edgelq_sdk/ztp/proto/v1/tpm_attestation_cert_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TpmAttestationCertServiceStub(object):
    """TpmAttestationCert service API for Ztp
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTpmAttestationCert = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/GetTpmAttestationCert',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.GetTpmAttestationCertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
                _registered_method=True)
        self.BatchGetTpmAttestationCerts = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/BatchGetTpmAttestationCerts',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsResponse.FromString,
                _registered_method=True)
        self.ListTpmAttestationCerts = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/ListTpmAttestationCerts',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsResponse.FromString,
                _registered_method=True)
        self.WatchTpmAttestationCert = channel.unary_stream(
                '/ntt.ztp.v1.TpmAttestationCertService/WatchTpmAttestationCert',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertResponse.FromString,
                _registered_method=True)
        self.WatchTpmAttestationCerts = channel.unary_stream(
                '/ntt.ztp.v1.TpmAttestationCertService/WatchTpmAttestationCerts',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsResponse.FromString,
                _registered_method=True)
        self.CreateTpmAttestationCert = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/CreateTpmAttestationCert',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.CreateTpmAttestationCertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
                _registered_method=True)
        self.UpdateTpmAttestationCert = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/UpdateTpmAttestationCert',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.UpdateTpmAttestationCertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
                _registered_method=True)
        self.DeleteTpmAttestationCert = channel.unary_unary(
                '/ntt.ztp.v1.TpmAttestationCertService/DeleteTpmAttestationCert',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.DeleteTpmAttestationCertRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class TpmAttestationCertServiceServicer(object):
    """TpmAttestationCert service API for Ztp
    """

    def GetTpmAttestationCert(self, request, context):
        """GetTpmAttestationCert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetTpmAttestationCerts(self, request, context):
        """BatchGetTpmAttestationCerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTpmAttestationCerts(self, request, context):
        """ListTpmAttestationCerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchTpmAttestationCert(self, request, context):
        """WatchTpmAttestationCert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchTpmAttestationCerts(self, request, context):
        """WatchTpmAttestationCerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTpmAttestationCert(self, request, context):
        """CreateTpmAttestationCert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTpmAttestationCert(self, request, context):
        """UpdateTpmAttestationCert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTpmAttestationCert(self, request, context):
        """DeleteTpmAttestationCert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TpmAttestationCertServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTpmAttestationCert': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTpmAttestationCert,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.GetTpmAttestationCertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.SerializeToString,
            ),
            'BatchGetTpmAttestationCerts': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetTpmAttestationCerts,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsResponse.SerializeToString,
            ),
            'ListTpmAttestationCerts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTpmAttestationCerts,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsResponse.SerializeToString,
            ),
            'WatchTpmAttestationCert': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchTpmAttestationCert,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertResponse.SerializeToString,
            ),
            'WatchTpmAttestationCerts': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchTpmAttestationCerts,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsResponse.SerializeToString,
            ),
            'CreateTpmAttestationCert': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTpmAttestationCert,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.CreateTpmAttestationCertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.SerializeToString,
            ),
            'UpdateTpmAttestationCert': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTpmAttestationCert,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.UpdateTpmAttestationCertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.SerializeToString,
            ),
            'DeleteTpmAttestationCert': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTpmAttestationCert,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.DeleteTpmAttestationCertRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.ztp.v1.TpmAttestationCertService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.ztp.v1.TpmAttestationCertService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TpmAttestationCertService(object):
    """TpmAttestationCert service API for Ztp
    """

    @staticmethod
    def GetTpmAttestationCert(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/GetTpmAttestationCert',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.GetTpmAttestationCertRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
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
    def BatchGetTpmAttestationCerts(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/BatchGetTpmAttestationCerts',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.BatchGetTpmAttestationCertsResponse.FromString,
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
    def ListTpmAttestationCerts(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/ListTpmAttestationCerts',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.ListTpmAttestationCertsResponse.FromString,
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
    def WatchTpmAttestationCert(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/WatchTpmAttestationCert',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertResponse.FromString,
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
    def WatchTpmAttestationCerts(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/WatchTpmAttestationCerts',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.WatchTpmAttestationCertsResponse.FromString,
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
    def CreateTpmAttestationCert(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/CreateTpmAttestationCert',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.CreateTpmAttestationCertRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
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
    def UpdateTpmAttestationCert(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/UpdateTpmAttestationCert',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.UpdateTpmAttestationCertRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__pb2.TpmAttestationCert.FromString,
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
    def DeleteTpmAttestationCert(request,
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
            '/ntt.ztp.v1.TpmAttestationCertService/DeleteTpmAttestationCert',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_tpm__attestation__cert__service__pb2.DeleteTpmAttestationCertRequest.SerializeToString,
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
