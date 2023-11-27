from .models import Product, Category

def load_categories(data):
    lines = data.strip().split('\n')
    categories = {}

    for line in lines:
        id, title, parent_id = line.split(':')
        category = Category(id=int(id), title=title)
        category.save()
        categories[id] = category

    for line in lines:
        id, title, parent_id = line.split(':')
        if parent_id != 'None':
            category = categories[id]
            if parent_id in categories:
                category.parent = categories[parent_id]
                category.save()



def load_products(data):
    lines = data.strip().split('\n')
    for line in lines:
        id, title, category_id, quantity, price = line.split(':')
        category = Category.objects.get(id=int(category_id))
        Product(id=int(id), title=title, category=category, quantity=int(quantity), price=float(price)).save()
