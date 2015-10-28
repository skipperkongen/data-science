# Data wrangling with jq

In this section we will show how to use [jq](https://stedolan.github.io/jq/) to wrangle JSON data.

## Example: Twitter JSON wrangling

In this example, we'll work with a sample of JSON data downloaded from twitter. We will primarily use [jq](https://stedolan.github.io/jq/) to process the JSON data.

Prerequisites:

* Linux shell
* [jq](https://stedolan.github.io/jq/) for processing JSON
* A [sample](https://dev.twitter.com/streaming/reference/get/statuses/sample) Twitter JSON file, `sample.json`. This file is provided in the data/twitter-sample directory of this repository.

### Filtering

A JSON file can be filtered according to a condition.

For example, to extract only tweets that have a valid coordinate, i.e. the 'geo' attribute is not null, use a selection:

```
jq 'select(.geo != null)' data/twitter-sample/sample.json
```

### Projection

We can map over a JSON file to project each object into a new object, e.g. one that retains just a subset of the original attributes.

The simplest possible projection is to extract a single attribute from each tweet, which may include null values:

```
jq '.user.id'  data/twitter-sample/sample.json  # notice that this is not valid JSON
```

To remove the null values and create a valid JSON structure, we can use a filter and a pipe:

```
jq 'select(.user.id != null) | {user_id: .user.id}' data/twitter-sample/sample.json
```

In a more advanced example, we will keep six core attributes of each tweet with nested structures for user information, hashtags and user mentions. This example uses pipes for the overall projection and list comprehensions for the hashtags and user mentions attributes.

```
jq '. | {
  created_at: .created_at, 
  user: {
    id: .user.id, 
    screen_name: .user.screen_name
  }, 
  text: .text, 
  hashtags: [.entities.hashtags[].text], 
  user_mentions: [.entities.user_mentions[] | {id: .id, screen_name: .screen_name}]
}' data/twitter-sample/sample.json
```

Example output:

```json
{
  "created_at": "Wed Oct 28 19:50:10 +0000 2015",
  "user": {
    "id": 2220769794,
    "screen_name": "johnny_enn"
  },
  "text": "RT @BestOfMeech: more parenting a deaf child https://t.co/Bm86aLwI5V",
  "hashtags": [],
  "user_mentions": [
    {
      "id": 3221958337,
      "screen_name": "BestOfMeech"
    }
  ]
}
```

## Write new JSON files based on jq output

This is simple. Just redirect the output of jq to a file. It is probably a good idea to use the `--compact-output` flag to write each object to a single line by itself. Here is how to do that with one of the example queries from above:

```
jq --compact-output 'select(.user.id != null) | {user_id: .user.id}' data/twitter-sample/sample.json > user-ids.json
``` 