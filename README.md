## Installation 
```
git clone https://github.com/kamakirito/ubuntu_server_utilization.git
cd ubuntu_server_utilization
pip install -r requirements.txt
```

# Discord

* Create new server in discord
* Navigate to Discord server settings >> Integrations >> create new webhook
* Copy the webhook url
* Paste in the Discord_URL in python-montering.py file

#To run this in every X mintues.. 

#make sure you are ubuntu_server_utilization directory 
```
chmod +x python-montering.py
cron -l
```
# if notthing shows up 
```
cron -e
```
#Keep these things handy
 * full path of python3
 * full path of python-montering.py file

```
# You can use these commands to locate the full path of python3

```
which python3
realpath python-montering.py
```

#Add this in the file 

*/10 * * * * <full_path_of_python/python3> <full_path_of_python_script/python-montering.py>
