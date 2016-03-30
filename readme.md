Gestion Badminton
===========
Install
-------
* `git clone git@github.com:Eirika/Gestion-Badminton-Casir.git` : retrieve the repo
* `cd Gestion-Badminton-Casir`
* `virtualenv -p python3 --no-site-packages .venv` : create a virtual-env for python code  
* Windows :
  * `.\.venv\Scripts\activate.bat` : activate the venv
* Linux :
  * `source .venv/bin/activate` : activate the venv
* `pip install -r requirement.txt` : install all requirements


How to use
----------
#### Populate database
```
>>> import.py
```
> Will create an populate the database with all the data in the "donnees" folder

#### Use the application
```
>>> start.py
```
> Will start the application and open the first menu
