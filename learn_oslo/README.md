## learn_oslo
examples of oslo libarly.

### 1 install reqirements
`pip install -r reqirements.txt`

recommand using virtual environment.

### 2 log examples
`python /learn_oslo/log_examples/*.py`

###  3 config examples
####3.1 run examples
`python /learn_oslo/cmd/demo.py`
you can see config options define in /learn_oslo/cmd/api.py

#### 3.2 create directory under `/etc` and change owner of the created folder as follow:

```
$mkdir /etc/learn_oslo
$chown your_os_username:root /etc/learn_oslo
```

#### 3.3 crete config file `learn_oslo.conf` under `/etc/learn_oslo/`:

```
[DEFAULT]
log_dir = /var/log/learn_oslo
logging_exception_prefix = %(color)s%(asctime)s.%(msecs)03d TRACE %(name)s %(instance)s
logging_debug_format_suffix = from (pid=%(process)d) %(funcName)s %(pathname)s:%(lineno)d
logging_default_format_string = %(asctime)s.%(msecs)03d %(color)s%(levelname)s %(name)s [-%(color)s] %(instance)s%(color)s%(message)s
logging_context_format_string = %(asctime)s.%(msecs)03d %(color)s%(levelname)s %(name)s [%(request_id)s %(user_name)s %(project_name)s%(color)s] %(instance)s%(color)s%(message)s

#log_file=learn_oslo.log
api_config = api.ini
client_socket_timeout = 600

a=[aaa]
aa=aaaa
[api]
a=[a,a]
b=[b,b]
c=cc

[mongo]
db = rm
username = rm
password = RM_DBPASS
host = mongodb://30.161.221.245
port = 27017
```

#### 3.4 run examples again, you can see the value of each option read from
learn_oslo.conf created above.
`python /learn_oslo/cmd/demo.py`

#### 3.5 generate config file automatically
auto generator will find entry point of each python project in  python
 lib path, so we need to install this project before auto generate it's config
 file as follow in develop mode:
 ```
$python setup.py develop
 ```
have a look in `setup.cfg`, in sector `entry_points`, `learn_oslo/opts.py`
and `etc/learn_oslo/learn_oslo-config-generator.conf`, this 3 files are in this
code folder.
run the following listing to generate config:
```
oslo-config-generator --config-file etc/learn_oslo/learn_oslo-config-generator.conf
```
a new file will be create in folder `etc/learn_oslo/` with name `learn_oslo.conf.sample`.
you can delete this file and use command above to generate again.

#### 4 oslo service
execute `python /learn_oslo/cmd/demo_service.py` to start service with 2 workers.
pay attention to the output and log file `/var/log/learn_oslo/demo_service.py.log`