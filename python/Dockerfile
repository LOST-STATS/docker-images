FROM python:3.8

LABEL org.opencontainers.image.source https://github.com/lost-stats/docker-images

ENV POETRY_VERSION=1.1.4

# Install user yogi
RUN yes | adduser yogi --disabled-password --quiet \
    && usermod -aG sudo yogi \
    && echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "Set disable_coredump false" >> /etc/sudo.conf

USER yogi
WORKDIR /home/yogi
ENV PATH="/home/yogi/.local/bin:${PATH}"

RUN python3 -m venv .poetryvenv \
    && /home/yogi/.poetryvenv/bin/pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /home/yogi/

# NOTE(khw): The grep's here are to do with econml's current odd dependency situation. To be removed in future
RUN bash -c "/home/yogi/.poetryvenv/bin/poetry export -f requirements.txt | grep -v econml > requirements.txt" \
    &&  pip install -r requirements.txt \
    && bash -c "/home/yogi/.poetryvenv/bin/poetry export --without-hashes -f requirements.txt | egrep 'econml|llvmlite' > requirements.txt" \
    && pip install -r requirements.txt \
    && rm -rf /home/yogi/.cache /home/yogi/.poetryvenv
