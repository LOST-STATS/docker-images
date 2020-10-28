FROM python:3.8

ENV POETRY_VERSION=1.1.4

# Install user yogi
RUN yes | adduser yogi --disabled-password
RUN usermod -aG sudo yogi
RUN echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Set disable_coredump false" >> /etc/sudo.conf

USER yogi
WORKDIR /home/yogi
ENV PATH="/home/yogi/.local/bin:${PATH}"

RUN python3 -m venv .poetryvenv \
    && /home/yogi/.poetryvenv/bin/pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /home/yogi/
RUN bash -c "/home/yogi/.poetryvenv/bin/poetry export -f requirements.txt > requirements.txt" \
    &&  pip install -r requirements.txt