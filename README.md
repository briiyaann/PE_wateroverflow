# The Wateroverflow Practical exam
A Simple app that compute the amount of water poured at specific glass built on Django

# Setup
1. Clone this repo in your projects folder.

```
git clone https://github.com/briiyaann/PE_wateroverflow.git
```

2. Create a virtual environment and install the dependencies.

```
# create and activate the virtual env
virtualenv -p python3.7 env
source env/bin/activate

# install dependencies
pip install -r requirements.txt
```
3. Run the tests to ensure everything is in working order.

```
python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.028s

OK
Destroying test database for alias 'default'...
```

4. Access the water overflow app via [http://127.0.0.1:8000](http://127.0.0.1:8000)
