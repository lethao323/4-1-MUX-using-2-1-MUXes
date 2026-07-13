# MUX 4-to-1 Hierarchical Design

Đây là dự án thiết kế mạch dồn kênh (Multiplexer) 4-sang-1 sử dụng cấu trúc phân cấp  (hierarchical design). Dự án được triển khai trên nền tảng TinyTapeout để học tập về thiết kế logic số và quy trình tapeout chip SKY130.

## Cấu trúc thiết kế
Thiết kế sử dụng 3 khối MUX 2-sang-1 (`mux2to1`) được kết nối theo mô hình phân cấp:
- **Tầng 1:** 2 khối MUX 2-sang-1 chọn giữa (I0, I1) và (I2, I3) dựa trên tín hiệu chọn S0.
- **Tầng 2:** 1 khối MUX 2-sang-1 chọn giữa kết quả của Tầng 1 dựa trên tín hiệu chọn S1.



[Image of 4 to 1 multiplexer circuit diagram]


## Pin Mapping (Gán chân)
Dự án sử dụng các cổng I/O của TinyTapeout như sau:

| Tín hiệu | Cổng I/O | Mô tả |
| :--- | :--- | :--- |
| **I0** | `ui_in[0]` | Đầu vào dữ liệu 0 |
| **I1** | `ui_in[1]` | Đầu vào dữ liệu 1 |
| **I2** | `ui_in[2]` | Đầu vào dữ liệu 2 |
| **I3** | `ui_in[3]` | Đầu vào dữ liệu 3 |
| **S0** | `ui_in[4]` | Tín hiệu chọn LSB |
| **S1** | `ui_in[5]` | Tín hiệu chọn MSB |
| **Y** | `uo_out[0]` | Đầu ra kết quả |

## Cách mô phỏng (Simulation)
Để kiểm tra thiết kế trước khi đưa vào sản xuất, hãy vào thư mục `test/` và chạy lệnh sau (yêu cầu đã cài đặt Icarus Verilog và Cocotb):

```bash
make -B
