# Data wrangling with jq

In this section we will show how to use [jq](https://stedolan.github.io/jq/) to wrangle JSON data.

## Example: Twitter JSON

In this example, we'll work with a sample of JSON data downloaded from twitter. We will primarily use [jq](https://stedolan.github.io/jq/) to process the JSON data.

Prerequisites:

* Linux shell
* [jq](https://stedolan.github.io/jq/) for processing JSON
* A [sample](https://dev.twitter.com/streaming/reference/get/statuses/sample) Twitter JSON file, `sample.json`.

### Filtering

Here we show how to filter tweets on a condition.

For example, to extract only tweets that have a valid coordinate, i.e. the 'geo' attribute is not null, use a selection:

```
jq 'select(.geo != null) sample.json
```

### Projection

Here we will show how to project JSON data to an alternative structure.

For example, to retain a subset of the original tweet attributes including some nested structure, we can use a combination of pipes and list comprehensions.

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
}' sample.json
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