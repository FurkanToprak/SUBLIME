# Semantically Understanding Bias with LIME
Currently an ongoing rewrite of coionobrega's [explaining-recommendations](https://github.com/caionobrega/explaining-recommendations) repository, which is an implementation of LIME-RS, as discussed in [this paper](https://dl.acm.org/doi/10.1145/3297280.3297443).
Will hopefully be used to understand the gieven of popularity bias in any given recommendation.
## Disclaimer
I am not the author of the novel LIME algorithm or the implementation for Recommender Systems (LIME-RS). I merely wrote this to use in my own research, as the original codebase was not useable. 

## Instructions

### Installing Dependencies
Run `pipenv install`.

## Running Code
1) Run environment `pipenv shell`.
2) Run with `python3 main.py` 
3) Deactivate environment with `exit`.

## Configuring Dataset
see `datasets/README.md` and `experiment/config.py`.
### Data Preprocessing
Use `data_preprocessing.ipynb` to produce pickled training, testing, and validation matrices for whichever dataset you choose.
