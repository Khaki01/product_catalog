import random

from django.core.management.base import BaseCommand

from catalog.models import Category, Product, Tag

# from faker import Faker


# Could use faker, but the results are not to my liking
# fake = Faker()

class Command(BaseCommand):
    help = 'Create data instead of manual addition in adminpage'

    def handle(self, *args, **kwargs):
        self.create_categories()
        self.create_tags()
        self.create_products()

    def create_categories(self):
        categories = ['Electronics', 'Books', 'Clothing', 'Home & Garden', 'Sports', 'Fashion', 'Kitchen']
        for name in categories:
            Category.objects.get_or_create(name=name)

    def create_tags(self):
        tags = ['New', 'Trendy', 'Eco-Friendly', 'Limited Edition', 'Sale',
                'Wireless', 'Organic', 'Bestseller', 'Gift', 'Premium', 'Remarcable']
        for name in tags:
            Tag.objects.get_or_create(name=name)

    def create_products(self):
        product_data = [
            {'name': 'Smartphone XSuperNewUltra', 'description': 'Latest high-end smartphone in collaboration between apple, samsung, huawei, nokia, kaspi with OLED display and 5G.', 'category': 'Electronics', 'tags': ['New', 'Wireless', 'Premium']},
            {'name': 'Noise Adding Headphones', 'description': 'Experience immersive sound with active noise cancellation.', 'category': 'Electronics', 'tags': ['Trendy', 'Wireless', 'Premium']},
            {'name': 'E-Reader Newbie', 'description': 'Lightweight e-reader with high-resolution display.', 'category': 'Books', 'tags': ['Bestseller', 'New', 'Gift']},
            {'name': 'Vintage Leather Jacket', 'description': 'A stylish leather jacket that never goes out of fashion.', 'category': 'Clothing', 'tags': ['Trendy', 'Limited Edition', 'Sale']},
            {'name': 'Smart Garden Kit', 'description': 'Grow fresh herbs indoors with automated watering.', 'category': 'Home & Garden', 'tags': ['Eco-Friendly', 'New', 'Remarcable']},
            {'name': 'Nike Shoes Ultra', 'description': 'Lightweight and comfortable running shoes for athletes.', 'category': 'Sports', 'tags': ['New', 'Sale']},
            {'name': 'Designer Dolchegabanna Handbag', 'description': 'Luxury handbag crafted with premium materials.', 'category': 'Fashion', 'tags': ['Limited Edition', 'Premium', 'Gift']},
            {'name': 'Organic Bamboo Cutting Board', 'description': 'Eco-friendly cutting board made from sustainable bamboo.', 'category': 'Kitchen', 'tags': ['Eco-Friendly', 'Organic']},
            {'name': 'Berserk Manga Set', 'description': 'A collection of timeless literary classics. Best manga in the world', 'category': 'Books', 'tags': ['Bestseller', 'Remarcable']},
            {'name': 'Wireless Gaming Mouse', 'description': 'Precision gaming mouse with ergonomic design.', 'category': 'Electronics', 'tags': ['Wireless', 'Premium']},
            {'name': 'Luxury Silk Scarf', 'description': 'Elegant silk scarf for any occasion.', 'category': 'Fashion', 'tags': ['Premium', 'Trendy']},
            {'name': 'Yoga Mat Pro', 'description': 'Non-slip, high-density yoga mat for ultimate comfort.', 'category': 'Sports', 'tags': ['Sale', 'New']},
            {'name': 'Handmade Ceramic Mug', 'description': 'Beautifully crafted ceramic mug, perfect for coffee lovers.', 'category': 'Kitchen', 'tags': ['Organic', 'Remarcable']},
            {'name': 'Smart Home Security Camera', 'description': 'Monitor your home with real-time HD video and AI detection.', 'category': 'Electronics', 'tags': ['New', 'Premium']},
            {'name': 'Limited Edition Sneakers', 'description': 'Exclusive sneakers designed for ultimate comfort and style.', 'category': 'Fashion', 'tags': ['Limited Edition', 'Trendy']},
            {'name': 'Portable Blender', 'description': 'Blend smoothies on the go with this USB rechargeable blender.', 'category': 'Kitchen', 'tags': ['Eco-Friendly', 'New']},
            {'name': 'Wireless Charging Station', 'description': 'Charge multiple devices wirelessly with fast-charging support.', 'category': 'Electronics', 'tags': ['Wireless', 'New']},
            {'name': 'Comfy Bed Sheets', 'description': 'Soft and breathable bed sheets made from premium cotton.', 'category': 'Home & Garden', 'tags': ['Premium', 'Remarcable']},
            {'name': 'Cookbook: Recipes to become like Baki', 'description': 'A collection of Gordon Ramsey approved and delicious recipes.', 'category': 'Books', 'tags': ['Bestseller', 'Gift']},
            {'name': 'Foldable Electric Bike', 'description': 'Eco-friendly and portable electric bike with long battery life.', 'category': 'Sports', 'tags': ['New', 'Eco-Friendly']},
            {'name': 'Smart Mirror Pro', 'description': 'A futuristic mirror with AI fitness tracking and virtual assistant.', 'category': 'Home & Garden', 'tags': ['New', 'Premium', 'Remarcable']},
            {'name': 'Ergonomic Office Chair', 'description': 'Designed for maximum comfort and productivity during long hours.', 'category': 'Home & Garden', 'tags': ['Premium', 'Sale']},
            {'name': 'Solar-Powered Power Bank', 'description': 'Charge your devices anywhere with renewable solar energy.', 'category': 'Electronics', 'tags': ['Eco-Friendly', 'New', 'Wireless']},
            {'name': 'Titanium Camping Cookware Set', 'description': 'Ultra-light and durable cookware set for outdoor adventures.', 'category': 'Kitchen', 'tags': ['Eco-Friendly', 'Limited Edition']},
            {'name': 'Smart AI Pet Feeder', 'description': 'Automatic pet feeder with portion control and scheduling.', 'category': 'Home & Garden', 'tags': ['New', 'Trendy']},
        ]

        categories = {c.name: c for c in Category.objects.all()}
        tags = {t.name: t for t in Tag.objects.all()}

        for product in product_data:
            category = categories.get(product['category'])
            product_obj, created = Product.objects.get_or_create(
                name=product['name'],
                defaults={
                    'description': product['description'],
                    'category': category
                }
            )
            if created:
                product_obj.tags.set([tags[tag] for tag in product['tags'] if tag in tags])