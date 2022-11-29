# livMathsQuiz

Quiz platform for Liverpool Maths Group

## Installation

The installation process for this webapp is pretty involved, but a full script for setup containing the below instructions can be found in `setup.sh` (asuming ubuntu!)

1. Install Python, Pip, Postgresql if not installed already:

```apt install python3 python3-pip postgresql systemctl```

2. Install prerequisites from `requirements.txt`

```pip install -r requirements.txt```

3. Set up the database:

```sh
systemctl start postgresql
pg_ctlcluster 12 main start # Note - the 12 here corresponds to the version of postgresql installed. Mine is 12, so it's 12. Latest is 14!
sudo -u postgres psql -c "CREATE USER samball WITH PASSWORD 'MathsIsCool'"
sudo -u postgres psql -c "CREATE DATABASE mathsquiz WITH OWNER samball"
```

4. Write `django` database to `postgresql`:
```sh
python3 manage.py migrate
```

5. Generate a secret key:
```sh
echo SECRET_KEY=`openssl rand -base64 32` > .env
```

6. Create a superuser for adding questions (and adding users for adding questions!)
```
python3 manage.py createsuperuser
```

7. Run the server!
```sh
python3 manage.py runserver
```

8. BONUS: If the server is running on an external domain - turn `DEBUG` to `False` in `mathsQuiz/settings.py` and add the domain to `ALLOWED_HOSTS` in the same file. 
