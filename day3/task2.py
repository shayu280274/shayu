import requests
from lxml import etree
import os
from urllib.parse import urljoin


def download_images():
    url = "http://pic.netbian.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 创建保存图片的目录
        save_dir = 'd:\\images'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 获取网页内容
        response = requests.get(url, headers=headers)
        response.encoding = 'gbk'

        # 解析HTML
        html = etree.HTML(response.text)

        # 获取所有图片的相对路径
        img_relative_paths = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")

        if not img_relative_paths:
            print("未找到任何图片")
            return

        print(f"找到 {len(img_relative_paths)} 张图片")

        # 下载每张图片
        for i, relative_path in enumerate(img_relative_paths):
            # 拼接完整的图片URL
            img_url = urljoin(url, relative_path)

            # 获取图片文件名和扩展名
            img_name = os.path.basename(img_url)
            img_ext = os.path.splitext(img_name)[1] or '.jpg'  # 如果没有扩展名默认用.jpg

            try:
                # 下载图片
                img_response = requests.get(img_url, headers=headers, timeout=10)
                img_response.raise_for_status()

                # 保存路径
                save_path = os.path.join(save_dir, f'image_{i}{img_ext}')

                # 保存图片
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"已下载: {save_path}")

            except Exception as e:
                print(f"下载图片失败: {img_url}, 错误: {str(e)}")

        print("所有图片下载完毕")

    except Exception as e:
        print(f"发生错误: {str(e)}")


if __name__ == "__main__":
    download_images()