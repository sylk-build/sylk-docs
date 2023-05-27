# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Plugin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Readme_pb2 as Readme__pb2
import Docusaurus_pb2 as Docusaurus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cPlugin.proto\x12\x0esylk.Plugin.v1\x1a\x0cReadme.proto\x1a\x10\x44ocusaurus.proto\"i\n\x06Plugin\x12(\n\x06readme\x18\x01 \x03(\x0b\x32\x18.sylk.Readme.v1.Markdown\x12\x35\n\ndocusaurus\x18\x03 \x01(\x0b\x32!.sylk.Docusaurus.v1.PresetOptionsb\x06proto3')



_PLUGIN = DESCRIPTOR.message_types_by_name['Plugin']

@overload
class Plugin(_message.Message):
	"""sylk.build generated message [sylk.Plugin.v1.Plugin]
	A class respresent a Plugin type
	
	"""
	readme = List[Readme__pb2.Markdown] # type: List[Readme__pb2.Markdown]
	docusaurus = Docusaurus__pb2.PresetOptions # type: Docusaurus__pb2.PresetOptions

	def __init__(self, readme=List[Readme__pb2.Markdown], docusaurus=Docusaurus__pb2.PresetOptions):
		"""
		

		Attributes:
		----------
		readme : List[Readme__pb2.Markdown]
			
		docusaurus : Docusaurus__pb2.PresetOptions
			
		"""
		pass
Plugin = _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), {
  'DESCRIPTOR' : _PLUGIN,
  '__module__' : 'Plugin_pb2'
  # @@protoc_insertion_point(class_scope:sylk.Plugin.v1.Plugin)
  })
_sym_db.RegisterMessage(Plugin)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLUGIN._serialized_start=64
  _PLUGIN._serialized_end=169
# @@protoc_insertion_point(module_scope)
