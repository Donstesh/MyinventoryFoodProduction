###A Simple Django project for inventory management system build with normal django

####how to Run this project

1. Create Virtual Enviorment
	```
	mkvirtualenv --python=`which python3` nameOfEnvironment
	```

2. Install dependencies
	```
	pip install -r requirements.txt
	```

3. Go To Project root `inventoryms/` and  Make migrations and migrate
	```
	./manage.py makemigrations && ./manage.py migrate
	```

4. Run the server
	```
	./manage.py runserver 0:9090
	```

