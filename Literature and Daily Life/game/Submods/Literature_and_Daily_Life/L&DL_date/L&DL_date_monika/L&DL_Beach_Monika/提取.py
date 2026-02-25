import os
import datetime

# 你的目标文件夹路径
folder_path = r"E:\L&DL_date\L&DL_date_monika\L&DL_Beach_Monika"

# 输出文件路径
output_file = r"E:\文件列表.txt"

# 获取所有文件和文件夹名
all_items = os.listdir(folder_path)

# 只获取文件（排除文件夹）
files_only = []
for item in all_items:
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        files_only.append(item)

# 保存到文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"文件夹路径：{folder_path}\n")
    f.write(f"文件总数：{len(files_only)}\n")
    f.write("="*50 + "\n")
    
    # 按字母顺序排序
    files_only.sort()
    
    for i, filename in enumerate(files_only, 1):
        f.write(f"{i:3d}. {filename}\n")
    
    f.write("\n生成时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(f"已生成文件列表，保存至：{output_file}")
print(f"找到 {len(files_only)} 个文件")