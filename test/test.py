import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_4to1(dut):
    test_cases = [
        (0, 0, 0, 0, 0, 1, 1), # Chọn I0
        (0, 1, 0, 0, 1, 0, 1), # Chọn I1
        (1, 0, 0, 1, 0, 0, 1), # Chọn I2
        (1, 1, 1, 0, 0, 0, 1), # Chọn I3
    ]

    for s1, s0, i3, i2, i1, i0, expected in test_cases:
        # Cấp giá trị đầu vào
        dut.ui_in.value = (s1 << 5) | (s0 << 4) | (i3 << 3) | (i2 << 2) | (i1 << 1) | i0
        await Timer(1, unit="us") # Đã sửa units thành unit
        
        # Đọc toàn bộ giá trị số nguyên của cổng ra rồi dùng phép AND để lấy bit đầu tiên
        output_val = int(dut.uo_out.value) & 1
        
        assert output_val == expected, f"Lỗi logic tại S1={s1}, S0={s0}"
    
    print("Test passed!")
