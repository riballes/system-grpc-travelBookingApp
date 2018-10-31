# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='car_app.proto',
  package='car_app',
  syntax='proto3',
  serialized_pb=_b('\n\rcar_app.proto\x12\x07\x63\x61r_app\"\x1a\n\tSelection\x12\r\n\x05value\x18\x01 \x01(\t\"\x1d\n\nSysMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb7\x01\n\x0e\x43\x61rApplication\x12\x34\n\x07\x43\x61rList\x12\x12.car_app.Selection\x1a\x13.car_app.SysMessage\"\x00\x12\x36\n\tCarReserv\x12\x12.car_app.Selection\x1a\x13.car_app.SysMessage\"\x00\x12\x37\n\nCarDisplay\x12\x12.car_app.Selection\x1a\x13.car_app.SysMessage\"\x00\x42/\n\x18io.grpc.examples.car_appB\x0b\x43\x61rAppProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_SELECTION = _descriptor.Descriptor(
  name='Selection',
  full_name='car_app.Selection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='car_app.Selection.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=52,
)


_SYSMESSAGE = _descriptor.Descriptor(
  name='SysMessage',
  full_name='car_app.SysMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='car_app.SysMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['Selection'] = _SELECTION
DESCRIPTOR.message_types_by_name['SysMessage'] = _SYSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Selection = _reflection.GeneratedProtocolMessageType('Selection', (_message.Message,), dict(
  DESCRIPTOR = _SELECTION,
  __module__ = 'car_app_pb2'
  # @@protoc_insertion_point(class_scope:car_app.Selection)
  ))
_sym_db.RegisterMessage(Selection)

SysMessage = _reflection.GeneratedProtocolMessageType('SysMessage', (_message.Message,), dict(
  DESCRIPTOR = _SYSMESSAGE,
  __module__ = 'car_app_pb2'
  # @@protoc_insertion_point(class_scope:car_app.SysMessage)
  ))
_sym_db.RegisterMessage(SysMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030io.grpc.examples.car_appB\013CarAppProtoP\001\242\002\003HLW'))

_CARAPPLICATION = _descriptor.ServiceDescriptor(
  name='CarApplication',
  full_name='car_app.CarApplication',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=86,
  serialized_end=269,
  methods=[
  _descriptor.MethodDescriptor(
    name='CarList',
    full_name='car_app.CarApplication.CarList',
    index=0,
    containing_service=None,
    input_type=_SELECTION,
    output_type=_SYSMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CarReserv',
    full_name='car_app.CarApplication.CarReserv',
    index=1,
    containing_service=None,
    input_type=_SELECTION,
    output_type=_SYSMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CarDisplay',
    full_name='car_app.CarApplication.CarDisplay',
    index=2,
    containing_service=None,
    input_type=_SELECTION,
    output_type=_SYSMESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CARAPPLICATION)

DESCRIPTOR.services_by_name['CarApplication'] = _CARAPPLICATION

# @@protoc_insertion_point(module_scope)