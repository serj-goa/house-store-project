# House store project
 
Displays a list of real estate objects.

<p align="center">
      <img src="https://github.com/serj-goa/house-store-project/blob/main/site_example/homepage.png" alt="Homepage" width="400">
</p>

Provides the opportunity to select an object of interest and leave a request for it.

<p align="center">
      <img src="https://github.com/serj-goa/house-store-project/blob/main/site_example/house_detail.png" alt="House detail" width="400">
</p>

---

### Built with:

[<img src="https://img.shields.io/badge/python-3.11-blue?style=for-the-badge&logo=Python">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Django-3.0-blue?style=for-the-badge&logo=Django">](https://docs.djangoproject.com/en/4.1/)
[<img src="https://img.shields.io/badge/SQLite3-grey?style=for-the-badge&logo=SQLite3">](https://www.postgresql.org/)
---

### Local launch:

1. Clone the repository.

    While in the code folder, create a virtual environment 

    ```python
    python -m venv venv
    ```

2. Activate it:

    `venv\scripts\activate.bat` - Windows

    `source venv/bin/activate`  - Linux/Mac

3. Install dependencies 
    ```python
    python -m pip install -r requirements.txt
   ```

4. To run it locally, while in the project directory, execute the commands:

    ```python
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
