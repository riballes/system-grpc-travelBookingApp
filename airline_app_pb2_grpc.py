# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import airline_app_pb2 as airline__app__pb2


class AirlineApplicationStub(object):
  """Services provided as List, Reserve and Display
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AirlineList = channel.unary_unary(
        '/airline_app.AirlineApplication/AirlineList',
        request_serializer=airline__app__pb2.Selection.SerializeToString,
        response_deserializer=airline__app__pb2.SysMessage.FromString,
        )
    self.AirlineReserv = channel.unary_unary(
        '/airline_app.AirlineApplication/AirlineReserv',
        request_serializer=airline__app__pb2.Selection.SerializeToString,
        response_deserializer=airline__app__pb2.SysMessage.FromString,
        )
    self.AirlineDisplay = channel.unary_unary(
        '/airline_app.AirlineApplication/AirlineDisplay',
        request_serializer=airline__app__pb2.Selection.SerializeToString,
        response_deserializer=airline__app__pb2.SysMessage.FromString,
        )


class AirlineApplicationServicer(object):
  """Services provided as List, Reserve and Display
  """

  def AirlineList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AirlineReserv(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AirlineDisplay(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AirlineApplicationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AirlineList': grpc.unary_unary_rpc_method_handler(
          servicer.AirlineList,
          request_deserializer=airline__app__pb2.Selection.FromString,
          response_serializer=airline__app__pb2.SysMessage.SerializeToString,
      ),
      'AirlineReserv': grpc.unary_unary_rpc_method_handler(
          servicer.AirlineReserv,
          request_deserializer=airline__app__pb2.Selection.FromString,
          response_serializer=airline__app__pb2.SysMessage.SerializeToString,
      ),
      'AirlineDisplay': grpc.unary_unary_rpc_method_handler(
          servicer.AirlineDisplay,
          request_deserializer=airline__app__pb2.Selection.FromString,
          response_serializer=airline__app__pb2.SysMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'airline_app.AirlineApplication', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))