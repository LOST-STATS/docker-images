FROM buildpack-deps:focal

LABEL org.opencontainers.image.source https://github.com/lost-stats/docker-images

# Install base packages
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get update && apt-get install -y \
	    vim-tiny \
	    software-properties-common \
	    libssl-dev \
	    libcurl4-openssl-dev \
	    libxml2-dev \
        locales \
        gnupg \
        wget \
        sudo \
    && rm -rf /var/lib/apt/lists/* \

    # Set locale
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8

# Set enivornment variables
ENV LC_ALL="en_US.UTF-8" \
    LANG="en_US.UTF-8" \
    DEBIAN_FRONTEND="noninteractive"

# Install base R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 'E298A3A825C0D65DFD57CBB651716619E084DAB9' \
    && add-apt-repository 'deb http://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' \
    && apt-get update \
    && apt-get install -y r-base r-base-dev r-recommended r-cran-littler \

    # Install common dependencies
    && apt-get install -y libgdal26 libgeos-3.8.0 libproj15 libudunits2-dev \

    # Install user yogi
    && adduser yogi --disabled-password --quiet \
    && yes | usermod -aG sudo yogi \
    && echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "Set disable_coredump false" >> /etc/sudo.conf \
    && rm -rf /var/lib/apt/lists/*

USER yogi

WORKDIR /home/yogi
RUN mkdir -p /home/yogi/.R/lib
ENV R_LIBS="/home/yogi/.R/lib"

# Install renv
RUN mkdir -p /home/yogi/.local/share/renv \
    && R -e 'install.packages("remotes", repos = "https://cloud.r-project.org")' \
    && R -e 'remotes::install_github("rstudio/renv@0.12.0-30")'

COPY Rprofile.site /etc/R

COPY renv.lock /home/yogi/renv.lock
RUN R -e 'renv::restore()'