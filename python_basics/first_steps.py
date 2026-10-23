# first_steps.py 这是我的第一python 脚本： CAN ID 解码热身

can_id_str = "18fef100"  #一帧扩展帧OD (HEX 字符)

print(f"原始字符串：{can_id_str}")
print(f"长度：{len(can_id_str)}")
print(f"前三位：{can_id_str[0:3]}")
print(f"后三位：{can_id_str[-3:]}")

can_id_int = int(can_id_str,16)  # hex to int

print(f"转化成整数：{can_id_int}(十进制)")
print(f"十六进制显示:0x{can_id_int:08X}")
print(f"最低字节:0x{can_id_int & 0xff:02x}")