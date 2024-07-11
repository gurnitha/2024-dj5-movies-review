# Membuat Aplikasi Reviews Movie Menggunakan Django versi 5.0


#### 1. Inisial commit - membuat proyek django dan mengupload filenya ke Github

        new file:   .gitignore
        new file:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Create movie app

        modified:   README.md
        new file:   movie/__init__.py
        new file:   movie/admin.py
        new file:   movie/apps.py
        new file:   movie/migrations/__init__.py
        new file:   movie/models.py
        new file:   movie/tests.py
        new file:   movie/views.py


#### 3. Register movie app to config/settings.py

        modified:   README.md
        modified:   config/settings.py


#### 4. Hello World!

        modified:   README.md
        modified:   config/urls.py
        modified:   movie/views.py

        Tested :)


#### 5. Membuat Home page

        modified:   README.md
        new file:   movie/templates/home.html
        modified:   movie/views.py

        :)


#### 6. Membuat About page

        modified:   README.md
        modified:   config/urls.py
        new file:   movie/templates/about.html
        modified:   movie/views.py

        :)


#### 7. Menampilkan data statis pada Home page

        modified:   README.md
        modified:   movie/templates/home.html
        modified:   movie/views.py

        :)


#### 8. Menambahkan Bootstrap pada Home page

        modified:   README.md
        modified:   movie/templates/home.html

        :)


#### 8. Restrukturisasi proyek part 1: Urls dan Views

        modified:   README.md
        modified:   config/urls.py
        new file:   movie/urls.py
        modified:   movie/views.py


#### 9. Restrukturisasi proyek part 2: Templates

        modified:   README.md
        modified:   config/settings.py
        modified:   movie/views.py
        renamed:    movie/templates/about.html -> templates/movie/about.html
        renamed:    movie/templates/home.html -> templates/movie/home.html


#### 10. Membuat form pencarian (search)

        modified:   README.md
        modified:   templates/movie/home.html