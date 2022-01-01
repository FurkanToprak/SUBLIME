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
│   ├── item_features.csv [after preprocessing]
│   ├── training.csv [after preprocessing]
│   ├── testing.csv [after preprocessing]
│   └── validation.csv [after preprocessing]
└── README.md
```

# TODO:
- load dataset into a Dataset()  (data_utils.py)
- refactor model.py
- train + pickle FM model (train_rec.py) 
- generate predictions (predict.py)
- evaluate model (evaluate_model.py)
- refactor lime_rs.py
- generate LIMERS (run_lime_rs.py)
- generate bias as a feature
- generate bias explanations
- evalutate bias explanations