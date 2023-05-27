from typing import Tuple, Iterator, Any
import grpc
import sys
from functools import partial
from sylk.commons.interceptors import sylk_client_pre_rpc
import logging
from google.protobuf import empty_pb2
from . import docs_pb2_grpc as docsService
from . import Plugin_pb2 as Plugin
from . import Docusaurus_pb2 as Docusaurus
from . import Readme_pb2 as Readme

# For available channel options in python visit https://github.com/grpc/grpc/blob/v1.46.x/include/grpc/impl/codegen/grpc_types.h
_CHANNEL_OPTIONS = (("grpc.keepalive_permit_without_calls", 1),
	("grpc.keepalive_time_ms", 120000),
	("grpc.keepalive_timeout_ms", 20000),
	("grpc.http2.min_time_between_pings_ms", 120000),
	("grpc.http2.max_pings_without_data", 1),)

# Global metadata
_METADATA = (('sylk-version','0.0.7'),)

# Global auth key that will be verified by sylk client
_GLOBAL_AUTH_KEY = None

# Generated thanks to [sylk.build](https://www.sylk.build)
class sylkdocs:

	def __init__(self, host="localhost", port=44880, timeout=10, log_level='ERROR'):
		logging.root.setLevel(log_level)
		self._sylk_global_auth_key = _GLOBAL_AUTH_KEY
		channel = grpc.insecure_channel('{0}:{1}'.format(host, port),_CHANNEL_OPTIONS)
		try:
			grpc.channel_ready_future(channel).result(timeout=timeout)
		except grpc.FutureTimeoutError:
			logging.error('Timed out: Server seems to be offline. Verify your connection configs.')
			sys.exit(1)
		self.docsStub = docsService.docsStub(channel)

	
	def build_WithCall(self, request: empty_pb2.Empty, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Empty, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.docsStub.build.with_call(request,metadata=metadata)

	
	def build(self, request: empty_pb2.Empty, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Empty:
		"""sylk - """

		return self.docsStub.build(request,metadata=metadata)