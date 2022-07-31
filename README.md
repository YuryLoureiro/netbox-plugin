# Netbox Bigipnetbox
[Netbox](https://github.com/netbox-community/netbox) Plugin description

## Compatibility

This plugin in compatible with [NetBox](https://netbox.readthedocs.org/) 3.2 and later.

## Instructions
### Donwload repositioriy
You can get this skeleton in two ways:
1. Create your own GitHub repository using that one as a template [HowTo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
2. Clone this repo or download it as an archive

```
pip install ...
```
Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['bigipnetbox']
```

### Helpfulness
Useful tools for developing the plugin you can find in the develop folder of this repo.
Use Makefile to run a new development environment with docker in 3 commands. (docker and docker-compose required).   

0. Set `PYTHON_VER` and `NETBOX_VER` in Makefile or environment
```
PYTHON_VER?=3.7
NETBOX_VER?=v2.10.3
```
1. Build netbox container
```
make cbuild
docker-compose -f ./develop/docker-compose.yml \
		-p my_new_plugin build \
		--build-arg netbox_ver=v2.10.3 \
		--build-arg python_ver=3.7
postgres uses an image, skipping
redis uses an image, skipping
Building netbox
[+] Building 1.7s (15/15) FINISHED                                                                                                              
...
Successfully built ec6e8aabbaddb7c4386aef8f779d9ae7e8562f521e9041b7c20a3233f4c3a6d9
Building worker
[+] Building 0.2s (15/15) FINISHED                                                                                                              
...
Successfully built ec6e8aabbaddb7c4386aef8f779d9ae7e8562f521e9041b7c20a3233f4c3a6d9
```
2. Run netbox container
```
make debug
```
3. Add django superuser
```
make adduser
docker-compose -f ./develop/docker-compose.yml -p my_new_plugin run netbox python manage.py createsuperuser
Creating my_new_plugin_netbox_run ... done
Username (leave blank to use 'root'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

## Quickstart

To get it up and running run the following commands.

```bash
git clone https://github.com/YuryLoureiro/netbox-plugin.git
cd netbox-plugin
make cbuild
make debug
```

The whole application will be available after a few minutes.
Open the URL `http://0.0.0.0:8000/` in a web-browser.
You should see the NetBox homepage.
In the top-right corner you can login.
The default credentials are:

* Username: **admin**
* Password: **admin**
