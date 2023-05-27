"""sylk.build service implemantation for -> docs"""
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
from typing import Iterator
import docs_pb2_grpc
import Docusaurus_pb2
import protobuf_pb2

class docs(docs_pb2_grpc.docsServicer):

	# @rpc @@sylk - DO NOT REMOVE
	def build(self, request: Docusaurus_pb2.PresetOptions, context) -> protobuf_pb2.Empty:
		# response = protobuf_pb2.Empty()
		# return response

		super().build(request, context)

