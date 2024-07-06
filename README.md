# Label Utils

`label-utils` is a Python utility for validating and correcting label files in datasets used for machine learning tasks. This repository contains two scripts: `validate_labels.py` and `correct_labels.py`. These scripts help ensure that the label files in your dataset are valid and correct, preventing issues during model training and evaluation.

## Features

- **Validate Labels**: Check if label files contain valid class indices and are within the expected range.
- **Correct Labels**: Automatically correct invalid class indices in label files.

## Getting Started

### Prerequisites

- Python 3.x
- `os`, `re`, `argparse` modules (These are standard Python modules, no need to install them separately)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Reza-Rezvan/label-utils.git
cd label-utils
