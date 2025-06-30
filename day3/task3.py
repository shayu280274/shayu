import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ScholarBibtexCrawler:
    def __init__(self, headless=False):
        """
        初始化爬虫

        :param headless: 是否使用无头模式 (默认显示浏览器)
        """
        # 配置浏览器选项
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,720')

        # 随机选择用户代理
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        ]
        options.add_argument(f'user-agent={random.choice(user_agents)}')

        # 初始化浏览器
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)
        self.results = {}

        # 模拟人类行为参数
        self.min_delay = 1.5
        self.max_delay = 4.0
        self.scroll_delay = 0.5

    def human_delay(self):
        """模拟人类操作延迟"""
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)

    def human_scroll(self):
        """模拟人类滚动行为"""
        for _ in range(random.randint(1, 3)):
            scroll_amount = random.randint(200, 600)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(self.scroll_delay)

    def human_mouse_movement(self, element):
        """模拟人类鼠标移动到元素上的行为"""
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(random.uniform(0.5, 1.2))
        except Exception:
            pass

    def search_article(self, title):
        """搜索文章"""
        try:
            # 访问Google Scholar
            self.driver.get('https://scholar.google.com')
            self.human_delay()

            # 定位搜索框
            search_box = self.wait.until(
                EC.presence_of_element_located((By.NAME, 'q'))
            )

            # 模拟人类输入
            for char in title:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))

            # 模拟人类提交搜索
            search_box.send_keys(Keys.RETURN)
            self.human_delay()
            self.human_scroll()

            return True
        except TimeoutException:
            print(f"超时: 无法找到搜索框 - {title}")
            return False
        except Exception as e:
            print(f"搜索错误: {e}")
            return False

    def get_first_result(self, title):
        """获取第一个搜索结果"""
        try:
            # 定位第一个结果
            first_result = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.gs_ri h3 a'))
            )

            # 模拟人类鼠标移动
            self.human_mouse_movement(first_result)

            # 点击结果
            first_result.click()
            self.human_delay()
            self.human_scroll()

            return True
        except TimeoutException:
            print(f"超时: 未找到搜索结果 - {title}")
            return False
        except Exception as e:
            print(f"点击结果错误: {e}")
            return False

    def get_bibtex_citation(self, title):
        """获取BibTeX引用"""
        try:
            # 定位"引用"按钮
            cite_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.gs_citi'))
            )

            # 模拟人类鼠标移动
            self.human_mouse_movement(cite_button)

            # 点击"引用"按钮
            cite_button.click()
            self.human_delay()

            # 定位BibTeX选项
            bibtex_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'BibTeX')]"))
            )

            # 模拟人类鼠标移动
            self.human_mouse_movement(bibtex_option)

            # 点击BibTeX选项
            bibtex_option.click()
            self.human_delay()

            # 获取BibTeX内容
            bibtex_content = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, 'pre'))
            ).text

            return bibtex_content.strip()
        except TimeoutException:
            print(f"超时: 未找到引用选项 - {title}")
            return None
        except NoSuchElementException:
            print(f"元素未找到: 无法定位引用元素 - {title}")
            return None
        except Exception as e:
            print(f"获取引用错误: {e}")
            return None

    def crawl_article(self, title):
        """爬取单个文章的BibTeX引用"""
        print(f"\n开始处理: '{title}'")

        # 步骤1: 搜索文章
        if not self.search_article(title):
            self.results[title] = "搜索失败"
            return

        # 步骤2: 获取第一个结果
        if not self.get_first_result(title):
            self.results[title] = "未找到搜索结果"
            return

        # 步骤3: 获取BibTeX引用
        bibtex = self.get_bibtex_citation(title)

        if bibtex:
            self.results[title] = bibtex
            print(f"成功获取BibTeX引用")
        else:
            self.results[title] = "获取引用失败"

    def crawl_articles(self, articles):
        """爬取多个文章"""
        print("=" * 70)
        print("Google Scholar BibTeX 爬虫启动")
        print("模拟人类操作中...")
        print("=" * 70)

        for i, title in enumerate(articles, 1):
            print(f"\n处理进度: {i}/{len(articles)}")
            self.crawl_article(title)

            # 随机等待时间，避免请求过于频繁
            if i < len(articles):
                wait_time = random.uniform(8, 15)
                print(f"等待 {wait_time:.1f} 秒后继续...")
                time.sleep(wait_time)

        print("\n" + "=" * 70)
        print("所有文献处理完成!")
        print("=" * 70)

        # 保存结果到文件
        self.save_results()

        return self.results

    def save_results(self):
        """保存结果到文件"""
        # 保存为JSON
        with open('scholar_bibtex_results.json', 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        # 保存为BibTeX文件
        with open('references.bib', 'w', encoding='utf-8') as f:
            for bibtex in self.results.values():
                if isinstance(bibtex, str) and bibtex.startswith('@'):
                    f.write(bibtex + '\n\n')

        print("结果已保存到: scholar_bibtex_results.json 和 references.bib")

    def close(self):
        """关闭浏览器"""
        self.driver.quit()


if __name__ == "__main__":
    # 需要爬取的文献列表
    articles = [
        "Automatic crater detection and age estimation for mare regions on the lunar surface",
        "The origin of planetary impactors in the inner solar system",
        "Deep learning based systems for crater detection: A review",
        "A preliminary study of classification method on lunar topography and landforms",
        "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution",
        "Fast r-cnn",
        "You only look once: Unified, real-time object detection",
        "Attention is all you need",
        "End-to-end object detection with transformers"
    ]

    # 创建爬虫实例 (设置 headless=True 在后台运行)
    crawler = ScholarBibtexCrawler(headless=False)

    try:
        # 开始爬取
        results = crawler.crawl_articles(articles)

        # 打印结果
        print("\n最终结果:")
        print("=" * 70)
        for title, bibtex in results.items():
            print(f"\n文献标题: {title}")
            print("BibTeX引用:")
            print("-" * 60)
            if isinstance(bibtex, str) and bibtex.startswith('@'):
                print(bibtex)
            else:
                print(f"错误: {bibtex}")
            print("-" * 60)

    except Exception as e:
        print(f"主程序错误: {e}")
    finally:
        # 确保关闭浏览器
        crawler.close()