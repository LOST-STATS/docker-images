FROM buildpack-deps:buster

LABEL org.opencontainers.image.source https://github.com/lost-stats/docker-images

# Install base packages
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y sudo gnupg wget

RUN apt-get update && apt-get install -y \
	vim \
	software-properties-common \
	libssl-dev \
	libcurl4-openssl-dev \
	libxml2-dev

# Install base R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 'E19F5F87128899B192B1A2C2AD5F960A256A04AF' \
    && add-apt-repository 'deb http://cloud.r-project.org/bin/linux/debian buster-cran40/' \
    && apt-get update \
    && apt-get install -y r-base

# Install user yogi
RUN adduser yogi --disabled-password
RUN yes | usermod -aG sudo yogi
RUN echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Set disable_coredump false" >> /etc/sudo.conf

USER yogi

WORKDIR /home/yogi
RUN mkdir -p /home/yogi/.R/lib
ENV R_LIBS="/home/yogi/.R/lib"

# Install renv
RUN mkdir -p /home/yogi/.local/share/renv \
    && R -e 'install.packages("remotes", repos = "https://cloud.r-project.org")' \
    && R -e 'remotes::install_github("rstudio/renv@0.12.0-30")'

COPY renv.lock /home/yogi/renv.lock
RUN R -e 'renv::restore()'