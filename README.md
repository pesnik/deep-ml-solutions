# Deep-ML Solutions

This repository contains my solutions to problems from [deep-ml.com](https://www.deep-ml.com/), a platform for practicing machine learning and data science. The solutions are organized by topic and implemented using [marimo.io](https://marimo.io/), a reactive Python notebook that’s great for version control and reproducibility.

---

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Topics](#topics)
- [Running Solutions Locally](#running-solutions-locally)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation

To set up this project, you’ll need Python installed. We use [Poetry](https://python-poetry.org/) for dependency management to keep things consistent and easy to replicate.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pesnik/deep-ml-solutions.git
   cd deep-ml-solutions
   ```

2. **Install Poetry:**
   ```bash
   pip install poetry
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

5. **Install marimo (if not already in dependencies):**
   ```bash
   poetry add marimo
   ```

---

## Project Structure

Here’s the directory layout of the repository:

```
deep-ml-solutions/
├── Linear_Algebra/
│   ├── Problem_1/
│   │   ├── data/           # Input data for the problem (if needed)
│   │   ├── solution.py     # Marimo notebook with the solution
│   │   └── README.md       # Problem description and run instructions
│   └── Problem_2/
│       ├── data/
│       ├── solution.py
│       └── README.md
├── Machine_Learning_Fundamentals/
│   ├── Problem_1/
│   │   ├── data/
│   │   ├── solution.py
│   │   └── README.md
│   └── Problem_2/
│       ├── data/
│       ├── solution.py
│       └── README.md
├── Deep_Neural_Networks/
│   └── ...                 # Similar structure for each problem
├── Computer_Vision/
│   └── ...                 # Similar structure for each problem
├── Natural_Language_Processing/
│   └── ...                 # Similar structure for each problem
├── utils/                  # Shared utilities or helper functions (optional)
│   └── helpers.py
├── .gitignore              # Git ignore file
├── LICENSE                 # MIT License file
├── pyproject.toml          # Poetry config for dependencies
├── poetry.lock             # Locked dependency versions
└── README.md               # This file
```

- **Topic Directories**: Each top-level folder (e.g., `Linear_Algebra`) corresponds to a deep-ml.com category.
- **Problem Subdirectories**: Within each topic, problems are numbered (e.g., `Problem_1`), each with its own `solution.py`, `data/` folder, and `README.md`.
- **Utils**: An optional folder for shared code across solutions.

---

## Usage

Solutions are grouped by topic, matching the categories on deep-ml.com. Each topic has its own directory, with subdirectories for individual problems.

- To find a solution:
  1. Go to a topic folder, e.g., `Linear_Algebra/`.
  2. Open the problem folder, e.g., `Problem_1/`.
  3. Check out `solution.py`—a marimo notebook saved as a Python file.

---

## Topics

Here are the main topics covered in this repository, with links to their respective directories:

- **[Linear Algebra](Linear_Algebra/)**  
  Problems related to vectors, matrices, eigenvalues, and other foundational concepts.
- **[Machine Learning Fundamentals](Machine_Learning_Fundamentals/)**  
  Covers basics like regression, classification, and optimization techniques.
- **[Deep Neural Networks](Deep_Neural_Networks/)**  
  Solutions for neural network architectures, backpropagation, and training methods.
- **[Computer Vision](Computer_Vision/)**  
  Tasks involving image processing, convolutional networks, and object detection.
- **[Natural Language Processing](Natural_Language_Processing/)**  
  Problems on text analysis, tokenization, and language models.

Each topic directory contains problem subdirectories (e.g., `Problem_1/`, `Problem_2/`), with solutions implemented as marimo notebooks.

---

## Running Solutions Locally

To run a solution:
1. Navigate to the problem directory.
2. Launch the marimo notebook:
   ```bash
   marimo new
   ```
   This opens the notebook in your browser for interactive use.

- **Note on Data**: Some solutions need data files, stored in a `data/` folder within each problem directory. If a dataset is missing, check the problem’s `README.md` for download instructions.

---

## Contributing

Want to help out? Here’s how:
1. Fork this repository.
2. Create a branch for your changes.
3. Make your edits and commit them.
4. Push to your fork and submit a pull request.

Keep the code style consistent and add tests if possible.

---

## License

This project is under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Got questions or ideas? Email me at [hasanrakibul.masum@gmail.com](mailto:hasanrakibul.masum@gmail.com).
