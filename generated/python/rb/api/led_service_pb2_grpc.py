# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from rb.api import led_pb2 as rb_dot_api_dot_led__pb2

GRPC_GENERATED_VERSION = '1.65.2'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in rb/api/led_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class LEDServiceStub(object):
    """Service for controlling LED behavior
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetLEDColor = channel.unary_unary(
                '/rb.api.LEDService/SetLEDColor',
                request_serializer=rb_dot_api_dot_led__pb2.SetLEDColorRequest.SerializeToString,
                response_deserializer=rb_dot_api_dot_led__pb2.SetLEDColorResponse.FromString,
                _registered_method=True)


class LEDServiceServicer(object):
    """Service for controlling LED behavior
    """

    def SetLEDColor(self, request, context):
        """Sets the LED color and (optionally) its blinking behavior.
        If blinking is true, the LED blinks at 'blinking_freq' for 'duration'.
        Otherwise, the LED remains in the requested color for 'duration'.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LEDServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetLEDColor': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLEDColor,
                    request_deserializer=rb_dot_api_dot_led__pb2.SetLEDColorRequest.FromString,
                    response_serializer=rb_dot_api_dot_led__pb2.SetLEDColorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rb.api.LEDService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('rb.api.LEDService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LEDService(object):
    """Service for controlling LED behavior
    """

    @staticmethod
    def SetLEDColor(request,
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
            '/rb.api.LEDService/SetLEDColor',
            rb_dot_api_dot_led__pb2.SetLEDColorRequest.SerializeToString,
            rb_dot_api_dot_led__pb2.SetLEDColorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
