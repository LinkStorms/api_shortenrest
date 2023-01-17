# ShortenREST External API Adapter
This service will provide and API to create and manage short urls with
[ShortenREST](https://shorten.rest/). You should visit
[ShortenREST](https://shorten.rest/) website and create an account. After
that, get a token and use that to create or manage your short urls with this
service.


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

## Running the Service
After installing the dependencies, you can go to the `app` directory and then
run the service by executing the following command.
```bash
python main.py
```
If you want to change the port number, you can do so by changing the `PORT`
constant in the `settings.py` file.

## Further Questions?
Feel free to create an issue or contact us directly.
