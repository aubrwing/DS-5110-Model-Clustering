# DS 5110 Model Clustering
This repository contains data and the code that was used in the project titled "Utilizing Statistical Methods to Analyze Pretrained Machine Learning Models" for the DS 5110 course.

Aubrey Winger, Rory Black, Tatev Kyosababyan


## The Data
The data was extracted from a data set provided to us containing information on over 700 different pre-trained models. In total, the 700+ models amounted to roughly *1 TB*. Since this was far too large of a data set for any of our local devices, we analyzed a subset of the data to only evaluate *105 different pre-trained models*. We were provided with information on each pre-trained model's weights.

### Additional Features
From the model name and weights given, we chose to extract further information from [huggingface.co](huggingface.co). The features we manually extracted are listed below.
* Domain
* Learning Rate
* Train Batch Size
* Eval Batch Size
* Num Epochs
* Num Layers
* Num Weights -- Layer 1
* Num Weights -- Layer 2
* ...
* Num Weights -- Layer 25

The reduced data set can be seen in the [model data](https://github.com/roryblakc/DS-5110-Model-Clustering/blob/main/model_data.csv) file in this repository.


## Contents
* [Model Download .py file](https://github.com/roryblakc/DS-5110-Model-Clustering/blob/main/model_download.py)
