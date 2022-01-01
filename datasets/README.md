Download the dataset from https://grouplens.org/datasets/movielens/. Extract the `.zip` into this file.

The directory shoud look like `/datasets/ml-<size>` for each separate dataset. Example:

```
datasets/
├── ml-20m
│   ├── genome-scores.csv
│   ├── genome-tags.csv
│   ├── links.csv
│   ├── movies.csv
│   ├── ratings.csv
│   ├── README.txt
│   ├── tags.csv
│   ├── training.pickle [after preprocessing]
│   ├── testing.pickle [after preprocessing]
│   └── validation.pickle [after preprocessing]
└── README.md
```

# TODO:
- Load movieset data
- Create a csv with item info, in the format of movie_id, feature, value
- Create a pivoted version by movie_id