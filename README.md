# Semantically Understanding Bias with LIME
Currently an ongoing rewrite of coionobrega's [explaining-recommendations](https://github.com/caionobrega/explaining-recommendations) repository, which is an implementation of LIME-RS, as discussed in [this paper](https://dl.acm.org/doi/10.1145/3297280.3297443).

Will hopefully be used to understand the effect of popularity bias in any given recommendation.
## Disclaimer
I am not the author of the novel LIME algorithm or the implementation for Recommender Systems (LIME-RS). I merely wrote this to use in my own research, as the [original codebase](https://github.com/caionobrega/explaining-recommendations) was not usable. 

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
Use `data_preprocessing.ipynb` to produce preprocessed training, testing, and validation splits for whichever dataset you choose.

# TODO:
- generate predictions (predict.py)
- evaluate model (evaluate_model.py)
- refactor lime_rs.py
- generate LIMERS (run_lime_rs.py)
- generate bias as a feature
- generate bias explanations
- evalutate bias explanations
- validation
- add logging
