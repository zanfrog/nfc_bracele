import os

folder_path = r"C:\python_project\Python traning\nfc_bracele\background"
files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# 先將所有檔案重新命名為暫存名稱，避免直接衝突
for i, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    temp_path = os.path.join(folder_path, f"temp_{i}.png")
    os.rename(old_path, temp_path)

# 再將暫存名稱改為目標名稱
for i in range(len(files)):
    temp_path = os.path.join(folder_path, f"temp_{i}.png")
    new_path = os.path.join(folder_path, f"bg{i+1}.png")
    os.rename(temp_path, new_path)

print("批次重新命名完成！")