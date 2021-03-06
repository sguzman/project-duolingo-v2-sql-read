# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sql_read.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sql_read.proto',
  package='sql_read',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0esql_read.proto\x12\x08sql_read\"\x12\n\x03\x41\x63k\x12\x0b\n\x03msg\x18\x01 \x01(\x08\"\x14\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t25\n\x07SQLRead\x12*\n\x07GetUser\x12\r.sql_read.Ack\x1a\x0e.sql_read.User\"\x00\x62\x06proto3'
)




_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='sql_read.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='sql_read.Ack.msg', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=46,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='sql_read.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sql_read.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'sql_read_pb2'
  # @@protoc_insertion_point(class_scope:sql_read.Ack)
  })
_sym_db.RegisterMessage(Ack)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'sql_read_pb2'
  # @@protoc_insertion_point(class_scope:sql_read.User)
  })
_sym_db.RegisterMessage(User)



_SQLREAD = _descriptor.ServiceDescriptor(
  name='SQLRead',
  full_name='sql_read.SQLRead',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=70,
  serialized_end=123,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='sql_read.SQLRead.GetUser',
    index=0,
    containing_service=None,
    input_type=_ACK,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SQLREAD)

DESCRIPTOR.services_by_name['SQLRead'] = _SQLREAD

# @@protoc_insertion_point(module_scope)
