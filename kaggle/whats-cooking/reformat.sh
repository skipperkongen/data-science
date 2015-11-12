#!/bin/sh

jq --compact-output '.[] | {id: .id, ingredients: .ingredients}' test.json > test-spark.json
jq --compact-output '.[] | {id: .id, cuisine: .cuisine, ingredients: .ingredients}' train.json > train-spark.json