# tf_rnn_model_load_testing

### How it works?

create virtual environment using:

```shell
virtualenv <env_name>
```
Change the directory.
```shell
cd <env_name>
```
Clone this repository.
```shell
git clone https://github.com/chaturvediabhay24/tf_rnn_model_load_testing.git
```
Change the directory.
```shell
cd tf_rnn_model_load_testing
```
Install dependencies.
```shell
pip install -r requirements.txt
```

To start the server run the following command.
```shell
gunicorn app:app -b localhost:5000 &
```
To start the testing environment run the following command
```shell
locust
```

## View
* For viewing api open http://127.0.0.1:5000
* For viewing locust ui open http://localhost:8089
* Enter the number of users, hatch rate and host(http://127.0.0.1:5000) to start the test.
