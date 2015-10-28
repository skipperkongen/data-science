# Analyze JSON data with Spark

In this section, we use Spark to analyze Twitter data. 

## Read JSON data into DataFrame

Reading JSON data into Spark is dead easy (just set basepath below to your data-science folder):

```scala
val basepath = "/path/to/data-science"
val df = sqlContext.read.json(s"$basepath/data/twitter-sample/sample.json")
```

## Inspect the data

Count the number of tweets that lack a text:

```scala
df.select($"text".isNotNull.as("hasText")).groupBy("hasText").count.show
```

## Reshape the data

The Twitter JSON schema is a little verbose, so we will reduce the data to the bare essensials. Also, we will remove tweets with data missing and lowercase the text with a function from the useful [sql functions package](https://spark.apache.org/docs/1.4.0/api/scala/index.html#org.apache.spark.sql.functions$).

First, we will import the set of useful functions in the sql package:

```scala
import org.apache.spark.sql.{functions => func}
```

Next, we will filter, project and lowercase the data:

```scala
val projected = df.select($"created_at", $"user.id", $"user.screen_name", $"text", $"entities.hashtags.text".as("hashtags"), $"entities.user_mentions")

val filtered = projected.filter($"created_at".isNotNull && $"id".isNotNull && $"text".isNotNull)

val lowered = filtered.select($"*", func.lower($"text").as("lowerText")).drop("text").withColumnRenamed("lowerText", "text")
```
