# Microservice gRPC Example

Dự án này trình bày cách xây dựng một hệ thống microservice sử dụng gRPC với **Spring Boot (Java)** làm máy chủ và **FastAPI (Python)** làm máy khách.

## 🏗 Cấu trúc dự án

```
.
├── java-server/     # Dịch vụ gRPC máy chủ (Spring Boot)
└── python-client/   # Dịch vụ gRPC máy khách (Python)
```

## 🔧 Yêu cầu hệ thống

Trước khi bắt đầu, đảm bảo rằng bạn đã cài đặt các công cụ sau:

- **Java 21** hoặc mới hơn  
- **Maven** để biên dịch và chạy server  
- **Python 3.7+** để chạy client  
- **gRPC & protobuf** để tạo các file giao tiếp  

## 🚀 Hướng dẫn sử dụng

### 1️⃣ Cài đặt và chạy dịch vụ gRPC Server (Java)

1. **Di chuyển vào thư mục `java-server`**

   ```bash
   cd java-server
   ```

2. **Biên dịch và chạy server**
  
   ```bash
   ./mvnw clean install
   ./mvnw spring-boot:run
   ```

   - Nếu thành công, server sẽ chạy trên cổng `9090`.

### 2️⃣ Cài đặt và chạy dịch vụ gRPC Client (Python)

1. **Di chuyển vào thư mục `python-client`**

   ```bash
   cd ../python-client
   ```

2. **Cài đặt các thư viện gRPC cần thiết**

   ```bash
   pip install grpcio grpcio-tools
   ```

3. **Chạy client để gửi yêu cầu đến server**

   ```bash
   python client.py
   ```

   - Nếu kết nối thành công, bạn sẽ thấy thông điệp phản hồi từ server.

## 🛠 Các lỗi thường gặp và cách khắc phục

| Lỗi | Nguyên nhân | Cách khắc phục |
|------|------------|---------------|
| `Connection refused` | Server chưa chạy | Đảm bảo server Java đang chạy trên cổng `9090` |
| `ModuleNotFoundError: No module named 'grpc'` | Chưa cài đặt gRPC Python | Chạy `pip install grpcio grpcio-tools` |

## 📌 Ghi chú bổ sung

- Nếu bạn muốn thay đổi giao diện gRPC (`hello.proto`), cần **biên dịch lại** file `.proto` trước khi chạy ứng dụng.
- Cổng server mặc định là **9090**, có thể thay đổi trong file cấu hình Java nếu cần.

---

📜 **License**: MIT  
🚀 **Author**: Bạn 🚀
