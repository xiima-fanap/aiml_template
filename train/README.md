# Train

Concise description of model, method, and dataset being trained


## Notice

Anything that user must take into account when using the train script


## Setup

### Build docker image

```bash
# Instructions to build train dockerfile
docker build -f ../dockerfile_train aiml_template_train .
```

### Install requirements

```bash
pip install -r ../requirements/requirements_base.txt
pip install -r ../requirements/requirements_train.txt
```


## Train

```bash
# Start the train container
docker run -it --rm --gpus all -v $(pwd):/workdir aiml_template_train bash

# Start training
python3 train.py -c config.yaml
```

### Config description

| Property | Type | Recommended value | Description |
|----------|------|-------------------|-------------|
| hdf5_dataset_path | str | N/A | Path to the HDF5 file containing the dataset |
| saved_model_path | str | ./saved_models | Path to save the model checkpoints |
| train_iterations | int | 50 | Number for iterations to train the model |


## Urgent issues and future work
1. *Nothing so far*


## Issues and future work
1. *Nothing so far*


## Contributors
1. \[Name Surname\]: <name@domain.com>
