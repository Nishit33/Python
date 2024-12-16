# Assignment For Python 


'''
1) Why Django should be used for web-development? Explain how you can create a project in Django?

--> Django is a powerful web framework for building robust, secure, and scalable websites. 

Ease of Use: Django simplifies the development process with pre-built tools for common tasks like authentication, form handling, and database management.

Secure: It comes with built-in protections against common security threats like SQL injection and cross-site scripting (XSS).

Scalability: Django can handle high traffic and large applications, making it ideal for projects of all sizes.

Rapid Development: With Django, developers can create prototypes or full-fledged applications quickly.

Versatile: From small blogs to large e-commerce sites, Django supports a variety of projects.


How to Create a Project in Django:

Install Django   pip install django

Start a Django Project  django-admin startproject project_name

Navigate to the Project Folder   cd project_name

Run the Development Server  python manage.py runserver

Create a Django App  python manage.py startapp app_name


Add the App to the Project  INSTALLED_APPS = [
    ...,
    'app_name',
]

Start Building
 

'''





'''
2) How to check installed version of django?

--> To check versoin of django using the terminal command prompt

1) django-admin --versoin
2) using python interpreter by typing in terminal 
   import django
   print(django.get_versoin())

   so yeah this is 2 type to check django versoin 

'''



'''
3) Explain what does django-admin.py make messages command is used for?

--> The django-admin.py makemessages command is used for localization (i18n) in Django. 
    It helps create message files to translate text into different languages for your application.

    Key Purpose:
    It extracts all the translatable text (marked with translation functions like _() or gettext()) from your Django project files and generates language-specific files. 
    These files can then be used to provide translations for your app in various languages.

    django-admin.py makemessages -l <language_code>

    django-admin makemessages -l es
    |
    This will generate a django.po file inside the locale/es/LC_MESSAGES folder. 
    The file contains all the text marked for translation in your project.

    When to Use This Command?
    -You're preparing your app for multiple languages.
     You've added new translatable text to your project and need to update the message files.

'''




'''

4) What is Django URLs?make program to create django urls

-> What Are Django URLs?
    In Django, URLs (Uniform Resource Locators) are used to define the paths that map to specific views (functions or classes) in your application. 
    The urls.py file is where you organize these mappings, enabling users to access different pages of your website by visiting specific routes.

    ->(Create Django URLs)

    django-admin startproject myproject
    cd myproject
    python manage.py startapp myapp


    (create view )

    def home(request):
        return render(request,'home.html')


    (define Urls)   

    urlpatterns = [
        path('',views.home , name='home'),
        path('abour/' , views.about , name='about'),
    ]

    
    (Run the server)

    python manage.py runserver


'''




'''
5) What is a QuerySet? Write program to create a new Post object in database:

--> What is Queryset?
    A QuerySet in Django represents a collection of database queries. 
    It is used to retrieve, filter, and manipulate data from the database in an efficient and structured way.

    Common Operations with QuerySets:

    Retrieve All Objects = Post.objects.all()
    Filter Records  = Post.objects.filter(title="Django Tutorial")
    Retrieve a Single Object = Post.objects.get(id=1)


    (Program to Create a New Post Object in the Database)

    {Define the Post Model}

    from django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title


            
    (Apply Migrations)

    python manage.py makemigrations
    python manage.py migrate

    

    (Create a New Post Object)
    python manage.py shell

    from myapp.models import Post

    # Create a new Post object
    post = Post.objects.create(title="My First Post", content="This is the content of my first post!")
    print(post.id)  # Check the ID of the new post
            
    

    (Using a View (views.py))

    from django.http import HttpResponse
    from .models import Post

    def create_post(request):
        post = Post.objects.create(title="My First Post", content="This is the content of my first post!")
        return HttpResponse(f"Post '{post.title}' created with ID {post.id}")


    (Add a URL for the View)

    from django.urls import path
    from . import views

    urlpatterns = [
        path('create-post/', views.create_post, name='create_post'),
    ]


    (python manage.py runserver)

    This will save the new Post object in your database. 
    You can verify it using the Django admin panel or by querying the database.

'''



'''
6) Mention what command line can be used to load data into Django?

--> To load data into Django application you can use loaddata command. 
    This command imports data from files (like json , xml , yaml) into database 

    python manage.py loaddata <filename>


    -The data file must be formatted correctly and typically contains information about models and their fields.
    -Make sure the database structure (tables) is ready by running migrations before loading data.
    -This command is commonly used for initial data setup or restoring backups.
'''





'''
7) Explain what does django-admin.py make messages command is used for?

--> The django-admin.py makemessages command is used for localization (i18n) in Django. 
    It helps create message files to translate text into different languages for your application.

    Key Purpose:
    It extracts all the translatable text (marked with translation functions like _() or gettext()) from your Django project files and generates language-specific files. 
    These files can then be used to provide translations for your app in various languages.

    django-admin.py makemessages -l <language_code>

    django-admin makemessages -l es
    |
    This will generate a django.po file inside the locale/es/LC_MESSAGES folder. 
    The file contains all the text marked for translation in your project.

    When to Use This Command?
    -You're preparing your app for multiple languages.
     You've added new translatable text to your project and need to update the message files.

     

'''



'''
8) Make Django application to demonstrate following things o There will
be 2 modules(Admin,Product manager) o Admin can add product name
(ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc.


--> here's how you can create simple Django application with two modules.  Admin and Product Manager ,
    where the admin can add product , Product ID and Product Name .

    create Django project and app 

    django-admin startproject myproject
    cd myproject
    python manage.py startapp myapp




    (Define the product Model)

    from django.db import models
    class Product(models.Model):
        product_id = models.AutoField(primary_key=True)
        product_name = models.CharField(max_length=100)

        def __str__(self):
            return self.product_name


            

    (Register the Model in Admin Panel)

    from django.contrib import admin
    from .models import Product

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('product_id', 'product_name')





    (Set Up URLs)

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('products/', include('products.urls')),
    ]

    

    
    (Create Views for Product Manager)

    from django.shortcuts import render, redirect
    from .models import Product

    # View to add a new product
    def add_product(request):
        if request.method == 'POST':
            product_name = request.POST.get('product_name')
            if product_name:
                Product.objects.create(product_name=product_name)
                return redirect('list_products')
        return render(request, 'products/add_product.html')

    # View to list all products
    def list_products(request):
        products = Product.objects.all()
        return render(request, 'products/list_products.html', {'products': products})



    
    (Create Templates)

    Template to Add Products

    <h1>Add Product</h1>
    <form method="POST">
        {% csrf_token %}
        <label for="product_name">Product Name:</label>
        <input type="text" name="product_name" id="product_name" required>
        <button type="submit">Add Product</button>
    </form>
    <a href="{% url 'list_products' %}">View Products</a>

    

    
    Template to List Products

    <h1>Product List</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.product_id }} - {{ product.product_name }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add_product' %}">Add Product</a>




    (Apply Migrations)

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


    So basically Admin Module
    - Admin can add product via the admin interface
    - Admin can view the product list in the admin panel 

    And Product manager Module
    - Product Manager can add product through the Add product page.
    - Product Manager can view all product on the product list page.



'''