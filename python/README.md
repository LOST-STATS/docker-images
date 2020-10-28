# Adding dependencies to the Python image

We use `poetry` to manage our Python dependencies. To update the dependencies you should:
  * Run the following command to launch the current docker image:
    `docker run --rm -it -v "$(pwd)/poetry.lock:/home/yogi/poetry.lock" -v "$(pwd)/pyproject.toml:/home/yogi/pyproject.toml" ghcr.io/khwilson/tester-python:latest bash`
  * Once the terminal starts up, run `poetry add NAME_OF_DEPENDENCY`
  * Exit the terminal, and commit the resulting `pyproject.toml` and `poetry.lock` files in this folder
