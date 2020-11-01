FROM python:3.8

LABEL org.opencontainers.image.source https://github.com/lost-stats/docker-images

ENV POETRY_VERSION=1.1.4

# Install geo dependencies
RUN apt-get update \
    && apt-get install -y libspatialindex-dev libproj-dev libgeos++-dev \
    && rm -rf /var/lib/apt/lists/*

# Install user yogi
RUN yes | adduser yogi --disabled-password --quiet \
    && usermod -aG sudo yogi \
    && echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "Set disable_coredump false" >> /etc/sudo.conf

USER yogi
WORKDIR /home/yogi
ENV PATH="/home/yogi/.local/bin:${PATH}"

RUN python3 -m venv .poetryvenv \
    && /home/yogi/.poetryvenv/bin/pip install "poetry==$POETRY_VERSION" \
    && mkdir -p /home/yogi/lost-stats-docker-image/
COPY poetry.lock pyproject.toml /home/yogi/lost-stats-docker-image/

# NOTE(khw): The grep's here are to do with econml's current odd dependency situation. To be removed in future
WORKDIR /home/yogi/lost-stats-docker-image
RUN bash -c "/home/yogi/.poetryvenv/bin/poetry config virtualenvs.in-project true" \
    && bash -c "/home/yogi/.poetryvenv/bin/poetry install" \
    && rm -rf /home/yogi/.cache

ENTRYPOINT ["/home/yogi/.poetryvenv/bin/poetry", "run"]