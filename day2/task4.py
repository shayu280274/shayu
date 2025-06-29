import os
import re


def windows_natural_sort_key(s):
    """
    为Windows自然排序生成排序键
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def rename_files():
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 配置路径（使用绝对路径）
    image_folder = os.path.join(script_dir, "tupian")
    name_file = os.path.join(script_dir, "xm.txt")

    # 检查文件是否存在
    if not os.path.exists(name_file):
        print(f"错误: 找不到姓名文件 '{name_file}'")
        print("请确保xm.txt与脚本在同一目录")
        return

    if not os.path.exists(image_folder):
        print(f"错误: 找不到图片文件夹 '{image_folder}'")
        return

    # 读取姓名列表
    try:
        with open(name_file, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f.readlines() if line.strip()]
            names = [name + ".png" for name in names]  # 添加扩展名
    except Exception as e:
        print(f"读取姓名文件失败: {e}")
        return

    # 获取图片文件列表并按Windows自然排序
    try:
        image_files = [f for f in os.listdir(image_folder)
                       if f.lower().endswith(".png")]

        # 使用Windows自然排序
        image_files.sort(key=windows_natural_sort_key)
    except Exception as e:
        print(f"读取图片文件夹失败: {e}")
        return

    # 验证数量匹配
    if len(image_files) != len(names):
        print(f"错误: 图片数量({len(image_files)})与姓名数量({len(names)})不匹配!")
        print(f"图片文件: {len(image_files)}个, 姓名: {len(names)}个")
        return

    # 打印预览
    print("序号 | 原文件名 -> 新文件名")
    print("-" * 50)
    for i, (old_name, new_name) in enumerate(zip(image_files, names)):
        print(f"{i + 1:2d}. {old_name} -> {new_name}")

    # 确认操作
    confirm = input("\n确认重命名? (y/n): ").strip().lower()
    if confirm != "y":
        print("操作已取消")
        return

    # 执行重命名
    success_count = 0
    for i, (old_name, new_name) in enumerate(zip(image_files, names)):
        try:
            old_path = os.path.join(image_folder, old_name)
            new_path = os.path.join(image_folder, new_name)

            # 处理重名冲突
            counter = 1
            original_new_name = new_name
            while os.path.exists(new_path):
                name_part, ext = os.path.splitext(original_new_name)
                new_name = f"{name_part}_{counter}{ext}"
                new_path = os.path.join(image_folder, new_name)
                counter += 1

            os.rename(old_path, new_path)
            print(f"重命名成功: {old_name} -> {os.path.basename(new_path)}")
            success_count += 1
        except Exception as e:
            print(f"重命名失败 [{old_name}]: {e}")

    print(f"\n操作完成! 成功重命名 {success_count}/{len(names)} 个文件")


if __name__ == "__main__":
    rename_files()