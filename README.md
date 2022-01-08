# AIML_template

Consice explaination of what this package do.

A `template base-line project` to act as initial empty repo for AIML team packages


# Notice

Something important that you think the reader must know.

## Setup

### Using docker

```bash
# Explain how to build the docker

docker build -f dockerfile_deploy -t aiml_sample_deploy .
```

### Without docker

```bash
# Explain how to install the package

pip install git+[repo_git_url]
```


## Usage

### How to run?

```python
# Implement the simplest and most basic usage of the package

from aiml_template import SampleClass


sample_class = SampleClass()
sample_class.sample_method()
```

### Sample response

```json
# Sample output of SampleClass.sample_method
[
    {
        "bounding_box": {
            "top_left_x": .1,
            "top_left_y": .2,
            "bottom_right_x": .3,
            "bottom_right_y": .4,
        },
        "confidence": .9,
        "tag": "cat"
    },
    {
        "bounding_box": {
            "top_left_x": .1,
            "top_left_y": .2,
            "bottom_right_x": .3,
            "bottom_right_y": .4,
        },
        "confidence": .8,
        "tag": "dog"
    }
]
```


## Unittest

```bash
# Run all tests all python versions
tox

# Run all tests on a single python version
tox -e py36

# Run a single test
tox -e py36 tests tests/test_script.py::ClassTest::method_test
```


## Benchmark

### Accuracy

| **Property** | **Value** |
|--------------|-----------|
| Property 1   | Value 1   |

### Performance

| **Property** | **Value** |
|--------------|-----------|
| Property 1   | Value 1   |


## Urgent issues and future work
1. *Nothing so far* <-- use when list is empty


## Issues and future work
1. *Nothing so far* <-- use when list is empty
2. Feature: a new feature
3. Bug: an existing bug
4. Refactor: refactor something
5. Idea: an idea to improve the package
6. TODO: something to be done
7. ~~Feature: sample done task~~


## Contributors
1. Hamid Mohammadi: <sandstormeatwo@gmail.com>
