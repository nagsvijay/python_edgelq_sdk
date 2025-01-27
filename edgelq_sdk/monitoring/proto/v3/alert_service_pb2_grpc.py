# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.monitoring.proto.v3 import alert_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2
from edgelq_sdk.monitoring.proto.v3 import alert_service_pb2 as edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2
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
        + f' but the generated code in edgelq_sdk/monitoring/proto/v3/alert_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AlertServiceStub(object):
    """Alert service API for Monitoring
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAlert = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/GetAlert',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.GetAlertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
                _registered_method=True)
        self.BatchGetAlerts = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/BatchGetAlerts',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsResponse.FromString,
                _registered_method=True)
        self.ListAlerts = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/ListAlerts',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsResponse.FromString,
                _registered_method=True)
        self.WatchAlert = channel.unary_stream(
                '/ntt.monitoring.v3.AlertService/WatchAlert',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertResponse.FromString,
                _registered_method=True)
        self.WatchAlerts = channel.unary_stream(
                '/ntt.monitoring.v3.AlertService/WatchAlerts',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsResponse.FromString,
                _registered_method=True)
        self.CreateAlert = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/CreateAlert',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.CreateAlertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
                _registered_method=True)
        self.UpdateAlert = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/UpdateAlert',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.UpdateAlertRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
                _registered_method=True)
        self.DeleteAlert = channel.unary_unary(
                '/ntt.monitoring.v3.AlertService/DeleteAlert',
                request_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.DeleteAlertRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class AlertServiceServicer(object):
    """Alert service API for Monitoring
    """

    def GetAlert(self, request, context):
        """GetAlert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetAlerts(self, request, context):
        """BatchGetAlerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAlerts(self, request, context):
        """ListAlerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAlert(self, request, context):
        """WatchAlert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchAlerts(self, request, context):
        """WatchAlerts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAlert(self, request, context):
        """CreateAlert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAlert(self, request, context):
        """UpdateAlert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAlert(self, request, context):
        """DeleteAlert
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAlert': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAlert,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.GetAlertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.SerializeToString,
            ),
            'BatchGetAlerts': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetAlerts,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsResponse.SerializeToString,
            ),
            'ListAlerts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAlerts,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsResponse.SerializeToString,
            ),
            'WatchAlert': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAlert,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertResponse.SerializeToString,
            ),
            'WatchAlerts': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAlerts,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsResponse.SerializeToString,
            ),
            'CreateAlert': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAlert,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.CreateAlertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.SerializeToString,
            ),
            'UpdateAlert': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAlert,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.UpdateAlertRequest.FromString,
                    response_serializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.SerializeToString,
            ),
            'DeleteAlert': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAlert,
                    request_deserializer=edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.DeleteAlertRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.monitoring.v3.AlertService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.monitoring.v3.AlertService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AlertService(object):
    """Alert service API for Monitoring
    """

    @staticmethod
    def GetAlert(request,
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
            '/ntt.monitoring.v3.AlertService/GetAlert',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.GetAlertRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
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
    def BatchGetAlerts(request,
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
            '/ntt.monitoring.v3.AlertService/BatchGetAlerts',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.BatchGetAlertsResponse.FromString,
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
    def ListAlerts(request,
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
            '/ntt.monitoring.v3.AlertService/ListAlerts',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.ListAlertsResponse.FromString,
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
    def WatchAlert(request,
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
            '/ntt.monitoring.v3.AlertService/WatchAlert',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertResponse.FromString,
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
    def WatchAlerts(request,
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
            '/ntt.monitoring.v3.AlertService/WatchAlerts',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.WatchAlertsResponse.FromString,
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
    def CreateAlert(request,
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
            '/ntt.monitoring.v3.AlertService/CreateAlert',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.CreateAlertRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
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
    def UpdateAlert(request,
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
            '/ntt.monitoring.v3.AlertService/UpdateAlert',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.UpdateAlertRequest.SerializeToString,
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__pb2.Alert.FromString,
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
    def DeleteAlert(request,
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
            '/ntt.monitoring.v3.AlertService/DeleteAlert',
            edgelq__sdk_dot_monitoring_dot_proto_dot_v3_dot_alert__service__pb2.DeleteAlertRequest.SerializeToString,
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
