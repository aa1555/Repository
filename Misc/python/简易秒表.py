import time

print("按下回车开始计时，再次按下回车停止计时。")
input("准备好了吗？开始！")
start_time = time.time()
input()
end_time = time.time()
print(f"你用了{(end_time - start_time):.2f}秒。")