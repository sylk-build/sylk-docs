"""sylk.build Generated Server Code"""
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
from concurrent import futures
import time
import grpc
import docs_pb2_grpc
import docs

def serve(host="0.0.0.0:44880"):
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	docs_pb2_grpc.add_docsServicer_to_server(docs.docs(),server)
	server.add_insecure_port(host)
	server.start()
	print("[*] Started sylk.build server at -> %s" % (host))
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == "__main__":
	serve()