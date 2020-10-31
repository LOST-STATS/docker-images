# Adding dependencies to the R image

We use `renv` to manage our R dependencies. To update the dependencies you should:
  * Add them to `requirements.R` in the `renv::install` section
  * Run the following: `docker run --rm -it -v "$(pwd)/renv.lock:/home/yogi/renv.lock" -v "$(pwd)/requirements.R:/home/yogi/requirements.R" ghcr.io/lost-stats/docker-images/tester-r:latest R -e "source('requirements.R')"`
  * Then commit the updated `renv.lock` and `requirements.R` files in this folder
