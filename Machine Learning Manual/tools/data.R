library(dplyr)

iris = datasets::iris
min_max_norm <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

#apply Min-Max normalization to first four columns in iris dataset
iris_norm <- as.data.frame(lapply(iris[1:4], min_max_norm))

iris_norm['Species'] <- c(rev(iris)[1])
print(iris_norm)

write.csv(iris_norm, './tools/data/douglas.csv')

