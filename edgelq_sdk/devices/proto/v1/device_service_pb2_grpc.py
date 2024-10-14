# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.devices.proto.v1 import device_custom_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2
from edgelq_sdk.devices.proto.v1 import device_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2
from edgelq_sdk.devices.proto.v1 import device_service_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2
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
        + f' but the generated code in edgelq_sdk/devices/proto/v1/device_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DeviceServiceStub(object):
    """Device service API for Devices
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/GetDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.GetDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
                _registered_method=True)
        self.BatchGetDevices = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/BatchGetDevices',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesResponse.FromString,
                _registered_method=True)
        self.ListDevices = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/ListDevices',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesResponse.FromString,
                _registered_method=True)
        self.WatchDevice = channel.unary_stream(
                '/ntt.devices.v1.DeviceService/WatchDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceResponse.FromString,
                _registered_method=True)
        self.WatchDevices = channel.unary_stream(
                '/ntt.devices.v1.DeviceService/WatchDevices',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesResponse.FromString,
                _registered_method=True)
        self.CreateDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/CreateDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.CreateDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
                _registered_method=True)
        self.UpdateDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/UpdateDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
                _registered_method=True)
        self.DeleteDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/DeleteDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.ProvisionServiceAccountToDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/ProvisionServiceAccountToDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceResponse.FromString,
                _registered_method=True)
        self.RemoveServiceAccountFromDevice = channel.unary_unary(
                '/ntt.devices.v1.DeviceService/RemoveServiceAccountFromDevice',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceResponse.FromString,
                _registered_method=True)
        self.Heartbeat = channel.stream_stream(
                '/ntt.devices.v1.DeviceService/Heartbeat',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatMsg.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatResponse.FromString,
                _registered_method=True)


class DeviceServiceServicer(object):
    """Device service API for Devices
    """

    def GetDevice(self, request, context):
        """GetDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetDevices(self, request, context):
        """BatchGetDevices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDevices(self, request, context):
        """ListDevices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchDevice(self, request, context):
        """WatchDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchDevices(self, request, context):
        """WatchDevices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDevice(self, request, context):
        """CreateDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDevice(self, request, context):
        """UpdateDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDevice(self, request, context):
        """DeleteDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvisionServiceAccountToDevice(self, request, context):
        """ProvisionServiceAccountToDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveServiceAccountFromDevice(self, request, context):
        """RemoveServiceAccountFromDevice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Heartbeat(self, request_iterator, context):
        """Heartbeat
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.GetDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.SerializeToString,
            ),
            'BatchGetDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetDevices,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesResponse.SerializeToString,
            ),
            'ListDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevices,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesResponse.SerializeToString,
            ),
            'WatchDevice': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceResponse.SerializeToString,
            ),
            'WatchDevices': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchDevices,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesResponse.SerializeToString,
            ),
            'CreateDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.CreateDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.SerializeToString,
            ),
            'UpdateDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.SerializeToString,
            ),
            'DeleteDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ProvisionServiceAccountToDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvisionServiceAccountToDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceResponse.SerializeToString,
            ),
            'RemoveServiceAccountFromDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveServiceAccountFromDevice,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceResponse.SerializeToString,
            ),
            'Heartbeat': grpc.stream_stream_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatMsg.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.devices.v1.DeviceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.devices.v1.DeviceService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DeviceService(object):
    """Device service API for Devices
    """

    @staticmethod
    def GetDevice(request,
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
            '/ntt.devices.v1.DeviceService/GetDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.GetDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
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
    def BatchGetDevices(request,
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
            '/ntt.devices.v1.DeviceService/BatchGetDevices',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.BatchGetDevicesResponse.FromString,
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
    def ListDevices(request,
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
            '/ntt.devices.v1.DeviceService/ListDevices',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.ListDevicesResponse.FromString,
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
    def WatchDevice(request,
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
            '/ntt.devices.v1.DeviceService/WatchDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDeviceResponse.FromString,
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
    def WatchDevices(request,
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
            '/ntt.devices.v1.DeviceService/WatchDevices',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.WatchDevicesResponse.FromString,
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
    def CreateDevice(request,
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
            '/ntt.devices.v1.DeviceService/CreateDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.CreateDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
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
    def UpdateDevice(request,
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
            '/ntt.devices.v1.DeviceService/UpdateDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__pb2.Device.FromString,
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
    def DeleteDevice(request,
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
            '/ntt.devices.v1.DeviceService/DeleteDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.SerializeToString,
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
    def ProvisionServiceAccountToDevice(request,
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
            '/ntt.devices.v1.DeviceService/ProvisionServiceAccountToDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.ProvisionServiceAccountToDeviceResponse.FromString,
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
    def RemoveServiceAccountFromDevice(request,
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
            '/ntt.devices.v1.DeviceService/RemoveServiceAccountFromDevice',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.RemoveServiceAccountFromDeviceResponse.FromString,
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
    def Heartbeat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/ntt.devices.v1.DeviceService/Heartbeat',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatMsg.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_device__custom__pb2.HeartbeatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
