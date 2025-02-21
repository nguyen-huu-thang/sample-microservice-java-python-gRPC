import asyncio
import grpc, time
import hello_pb2
import hello_pb2_grpc

async def run():
    while True:
        async with grpc.aio.insecure_channel('localhost:9090') as channel:
            stub = hello_pb2_grpc.HelloServiceStub(channel)
            response = await stub.SayHello(hello_pb2.HelloRequest(name='World'))
            print("Greeting: " + response.message)
            await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(run())