import grpc
import asyncio
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    async def SayHello(self, request, context):
        # Giả lập một tác vụ I/O-bound (ví dụ: gọi API khác, truy vấn cơ sở dữ liệu)
        await asyncio.sleep(1)  # Giả lập độ trễ 1 giây
        return hello_pb2.HelloReply(message=f'Hello, {request.name}!')

async def serve():
    # Tạo một gRPC server bất đồng bộ
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')  # Lắng nghe trên cổng 50051
    await server.start()
    print("Server is running on port 50051...")
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())