package com.example.demo;

import com.example.grpc.HelloProto;
import com.example.grpc.HelloServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class GrpcClient {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 9090)
            .usePlaintext()
            .build();

        HelloServiceGrpc.HelloServiceBlockingStub stub = HelloServiceGrpc.newBlockingStub(channel);

        HelloProto.HelloRequest request = HelloProto.HelloRequest.newBuilder()
            .setName("World")
            .build();

        HelloProto.HelloResponse response = stub.sayHello(request);
        System.out.println("Response: " + response.getMessage());

        channel.shutdown();
    }
}