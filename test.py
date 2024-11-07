from generators.text_gen import PostGenerator
from generators.image_gen import ImageGenerator
from social_publishers.vk_publisher import VKPublisher
import config as conf
import os

# Установка прокси перед инициализацией классов
os.environ["http_proxy"] = conf.http_proxy
os.environ["https_proxy"] = conf.https_proxy

post_gen = PostGenerator(conf.openai_key, tone="солидный и доверительный", topic="Новая коллекция ювелирных украшений от компании ЗлатоМаркет")
content = post_gen.generate_post()
img_desc = post_gen.generate_post_image_description()

img_gen = ImageGenerator(conf.openai_key)
image_url = img_gen.generate_image(img_desc)

print(content)
print(image_url)

vk_pub = VKPublisher(conf.vk_api_key, conf.vk_group_id)
vk_pub.publish_post(content, image_url)

