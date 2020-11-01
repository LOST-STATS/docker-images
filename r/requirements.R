#' This file sets up our renv environment. If you'd like to add
#' any extra dependencies, add them in the renv::install section below
#' After that run::
#'
#'  docker run --rm -v renv.lock:/home/yogi/renv.lock requirements.R:/home/yogi/requirements.R ghcr.io/khwilson/tester-r Rscript --vanilla -e 'source("requirements.R")''
#'
#' Note that this should _only_ be run when you want to update the
#' renv.lock file. Otherwise, you should use renv::restore()

# Save all the packages that are in our library
renv::settings$snapshot.type("simple")

renv::install(c(
    "tidyverse",
    "lubridate",
    "ggplot2",
    "corrplot",
    "tsibble",
    "lmtest",
    "fGarch",
    "ggpubr",
    "ggthemes",
    "viridis",
    "tseries",
    "caret",
    "glmnet",
    "janitor",
    "caTools",
    "naniar",
    "gbm",
    "e1071",
    "dummies",
    "sf"
))

renv::snapshot()