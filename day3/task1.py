import requests
from bs4 import BeautifulSoup

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://movie.douban.com/top250"

try:
    # 发送HTTP请求
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取前10个电影名称
    movies = []
    for item in soup.select('.item')[:10]:  # 只取前10个条目
        title_tag = item.select_one('.title')
        if title_tag:
            movies.append(title_tag.text.strip())

    # 打印结果
    print("豆瓣电影Top250排行榜前10名：")
    for i, title in enumerate(movies, 1):
        print(f"{i}. {title}")

except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")
except Exception as e:
    print(f"发生错误：{e}")