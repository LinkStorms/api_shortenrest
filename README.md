# Base Repository
Dear employees, this is a base repo created for you to use it in the different
services you develop. The structure is simple, there is a `.gitignore` file to
avoid adding local files to the repositories, the GPLv3 License in the LICENSE
file and `requirements.txt` which contains only `flask` and its dependencies.
The `app` folder is where all of the source codes will be placed. Do not write
any code outside this folder.

## Managing the Environment and Dependencies
To start working, first install `virtualenv` with pip.
```bash
pip install virtualenv
```

Then create an empty virtual environment.
```bash
virtualenv .venv
```
Note that `.venv` is the name of the virtual environment directory, this
directory is omitted in the `.gitignore` file.

After creating the virtual environment, activate it.

UNIX based Operating Systems (GNU/Linux, macOS, etc.)
```bash
source .venv/bin/activate
```

Windows
```batch
.\venv\Scripts\activate
```

Now you can install the required python packages in the clean environment you
just created.
```bash
pip install -r requirements.txt
```

This will only install `flask` and its dependencies. If you need other
packages, you need to install them with `pip install` first, and then update
the `requirements.txt` file with this command.
```bash
pip freeze > requirements.txt
```
Be careful not to update `requirements.txt` outside the virtual environment,
since every python package you have installed on your computer will be added
to the requirements of the project.

## Running the Service

After installing `flask` and its dependencies from `requirements.txt` file,
you can go to the `app` folder and run the simple **Hello, World!** app with
this command.
```
flask --app main --debug run
```

There is also a `config.py.sample` file in the `app` directory. This is
a template for `config.py` file which should be created by the user who runs
the service. Any local or secret variables that cannot be shared on the GitHub
repo will be stored in this file. Be aware that `config.py` is ignored by the
`.gitignore` file. Whatever that is written or added in this file should be
also reflected in the `config.py.sample` so it is crystal clear what should be
added to `config.py` to run the service.

## Further Questions?
If you have questions regarding how to create a new service, feel free to send
an email to your manager [smmousavisp@gmail.com](smmousavisp@gmail.com). I
will do my best to respond in time.

Please understand that violating these rules and conditions will result in
disciplinary punishments. 
