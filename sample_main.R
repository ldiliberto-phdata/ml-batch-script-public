library(jsonlite)
# source from root of git repository
source('from/root/of/repo/extlib.R')

main <- function(...) {
  args = list(...)
  print("Here are the named arguments")
  print(args)
}

args <- commandArgs(trailingOnly = TRUE)
error = "Must specify keyword arguments only."
if(length(args) > 1){stop(error)}
kargs = jsonlite::fromJSON(args)
if(is.null(names(kargs))){stop(error)}
do.call(main, kargs)
