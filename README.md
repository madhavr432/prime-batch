# 🐍 Python Journey

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data%20Science-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Git Automation](https://img.shields.io/badge/Automation-prime__push.bat-success.svg?logo=git&logoColor=white)](#-automation-tool-prime_pushbat)
[![Author](https://img.shields.io/badge/Author-Madhav%20Raj-purple.svg)](#-author--attribution)

> A comprehensive, hands-on repository tracking my learning journey through **Python Programming**, **Data Structures**, **Object-Oriented Programming (OOP)**, **File I/O & Exception Handling**, **Numerical Computing with NumPy**, and **Data Analysis with Pandas**.

---

## 📑 Table of Contents
- [📌 Overview](#-overview)
- [✨ Key Highlights](#-key-highlights)
- [📂 Repository Structure](#-repository-structure)
- [📚 Detailed Curriculum & Modules](#-detailed-curriculum--modules)
  - [Day 2: Core Python & Datatypes](#day-2-core-python--datatypes)
  - [Day 3: Control Flow, Functions & Lambdas](#day-3-control-flow-functions--lambdas)
  - [Day 4: Deep Dive into Data Structures](#day-4-deep-dive-into-data-structures)
  - [Day 5: Object-Oriented Programming (OOP)](#day-5-object-oriented-programming-oop)
  - [Day 6: File Handling, Exceptions & JSON](#day-6-file-handling-exceptions--json)
  - [NumPy: High-Performance Vector Computations](#numpy-high-performance-vector-computations)
  - [Pandas: Data Analysis & Feature Engineering](#pandas-data-analysis--feature-engineering)
- [⚙️ Automation Tool (`prime_push.bat`)](#-automation-tool-prime_pushbat)
- [🚀 Getting Started](#-getting-started)
- [🛠️ Prerequisites & Setup](#️-prerequisites--setup)
- [🎯 Learning Goals](#-learning-goals)
- [🧑‍💻 Author & Attribution](#-author--attribution)

---

## 📌 Overview

**Python Journey** serves as a structured collection of daily Python exercises, modular problem sets, real-world case studies, and Jupyter Notebooks focusing on Data Science and Machine Learning prerequisites. 

Whether it's mastering fundamental syntax, implementing complex inheritance models, performing tensor/array operations in NumPy, or aggregating large datasets with Pandas, this repository documents continuous skill progression with runnable code snippets and organized topic assignments.

---

## ✨ Key Highlights

- 🧩 **Modular Daily Learning Path**: Incrementally structured from basic datatypes to advanced data analysis.
- 📝 **100+ Practice Assignments**: Hands-on problem sets (`assignment_q1.py` ... `q10.py`) after every major concept.
- ⚡ **NumPy & Data Math**: In-depth notebooks covering vectorization, sigmoid activations, Mean Squared Error (MSE), axes manipulation, and broadcasting.
- 📊 **Pandas Data Analysis**: Exploratory Data Analysis (EDA) on datasets like `Countries.csv` and `anime.csv`, featuring Pivot Tables, Aggregations, and Feature Extraction.
- 🤖 **Automated Workflow**: Custom Windows batch script ([`prime_push.bat`](./prime_push.bat)) to seamlessly stage, commit with timestamping, pull-rebase, and push to GitHub.

---

## 📂 Repository Structure

```text
python-journey/
│
├── day2/                  # Core Python, variables, basic arithmetic & assignments
├── day3/                  # Loops, conditionals, match-case, functions & lambdas
├── day4/                  # Data structures (Strings, Lists, Tuples, Sets, Dicts)
├── day5/                  # Object-Oriented Programming (Classes, Inheritance, Polymorphism)
├── day6/                  # File I/O (txt, json), exception handling, comprehensions
│   └── assignment/        # File I/O & exception assignments with data assets
├── numpy/                 # 20+ Jupyter notebooks on numerical computing & math
├── pandas/                # Data analysis, DataFrames, EDA, Pivot Tables & CSVs
├── anaconda_projects/     # Anaconda environment configs & databases
├── prime_push.bat         # Automated Git push & sync batch tool
└── README.md              # Project documentation
```

---

## 📚 Detailed Curriculum & Modules

### Day 2: Core Python & Datatypes
* **Core Concepts**: Variable declaration, dynamic typing, input/output operations, and basic arithmetic calculations.
* **Featured Scripts**:
  - [`datatype.py`](./day2/datatype.py): Python type checking and casting.
  - [`average.py`](./day2/average.py) & [`sum_2.py`](./day2/sum_2.py): Basic mathematical computations.
  - `assignment_q1.py` to `assignment_q10.py`: Daily practice exercises covering elementary logic.

### Day 3: Control Flow, Functions & Lambdas
* **Core Concepts**: Conditional branching (`if-elif-else`), `match-case` statements, `for` & `while` loops, loop jump statements (`break`/`continue`), positional/default arguments, and anonymous `lambda` expressions.
* **Featured Scripts**:
  - [`matchcase.py`](./day3/matchcase.py), [`break.py`](./day3/break.py), [`continue.py`](./day3/continue.py), [`range.py`](./day3/range.py)
  - [`function.py`](./day3/function.py), [`lambda.py`](./day3/lambda.py), [`default.py`](./day3/default.py)
  - [`FactOfN.py`](./day3/FactOfN.py), [`sumofn.py`](./day3/sumofn.py), [`vowel.py`](./day3/vowel.py), [`numberofi.py`](./day3/numberofi.py)
  - `Assignment_q1.py` to `Assignment_q10.py`: Algorithmic assignments (factorials, summation, filtering).

### Day 4: Deep Dive into Data Structures
* **Core Concepts**: String operations & slicing, f-strings, Mutable vs Immutable types, List methods, Tuple operations, Set theory (unions, intersections), and Dictionary key-value manipulations.
* **Featured Scripts**:
  - [`stringslicing.py`](./day4/stringslicing.py), [`fstrings.py`](./day4/fstrings.py), [`stringformating.py`](./day4/stringformating.py)
  - [`listslicing.py`](./day4/listslicing.py), [`methods_in_lists.py`](./day4/methods_in_lists.py), [`loops_for_lists.py`](./day4/loops_for_lists.py)
  - [`inter_union.py`](./day4/inter_union.py), [`methods_in_sets.py`](./day4/methods_in_sets.py)
  - [`method_in_dictionary.py`](./day4/method_in_dictionary.py)
  - `Assignment_q1.py` to `Assignment_q10.py` & `q1.py`: Complex data structure manipulation tasks.

### Day 5: Object-Oriented Programming (OOP)
* **Core Concepts**: Classes & Instantiation, Constructors (`__init__`), Instance vs Class attributes, Encapsulation, Data Abstraction, Inheritance models (Single, Multilevel, Multiple), Polymorphism, and Duck Typing.
* **Featured Scripts & Projects**:
  - [`class_objects.py`](./day5/class_objects.py), [`constructor.py`](./day5/constructor.py), [`attributes.py`](./day5/attributes.py), [`methods.py`](./day5/methods.py)
  - [`Encapsulation_in_oops.py`](./day5/Encapsulation_in_oops.py), [`abstraction.py`](./day5/abstraction.py)
  - [`inheritence_in_oops.py`](./day5/inheritence_in_oops.py), [`multilevel_inheritance.py`](./day5/multilevel_inheritance.py), [`multiple_inheritance.py`](./day5/multiple_inheritance.py)
  - [`polymorphism.py`](./day5/polymorphism.py), [`poly_ducktyping.py`](./day5/poly_ducktyping.py)
  - [`productstore.py`](./day5/productstore.py): Real-world OOP simulation for product management.
  - `Assignment_q1.py` to `Assignment_q10.py`: OOP problem-solving exercises.

### Day 6: File Handling, Exceptions & JSON
* **Core Concepts**: Reading, writing, and appending files using context managers (`with`), JSON serialization/deserialization, robust error handling (`try-except-finally`), List Comprehensions, and file-based word searching.
* **Featured Scripts**:
  - [`read.py`](./day6/read.py), [`write.py`](./day6/write.py), [`append.py`](./day6/append.py), [`with.py`](./day6/with.py)
  - [`exception_handling.py`](./day6/exception_handling.py)
  - [`jsn.py`](./day6/jsn.py), `data.json`, `data1.json`
  - [`LIst_Comprehensions.py`](./day6/LIst_Comprehensions.py), [`word_search1.py`](./day6/word_search1.py), [`word_seatch2.py`](./day6/word_seatch2.py)
  - [`assignment/`](./day6/assignment/): Practicing file handling with `names.txt`, `log.txt`, and `cities.json`.

### NumPy: High-Performance Vector Computations
* **Core Concepts**: Multi-dimensional array operations, vectorization vs loops, broadcasting rules, matrix reshaping, axes reduction, mathematical loss functions, and dataset generation.
* **Featured Notebooks**:
  - [`creating_arrays.ipynb`](./numpy/creating_arrays.ipynb), [`data_types.ipynb`](./numpy/data_types.ipynb), [`indexing.ipynb`](./numpy/indexing.ipynb), [`slicing.ipynb`](./numpy/slicing.ipynb)
  - [`reshaping.ipynb`](./numpy/reshaping.ipynb), [`expand_dims.ipynb`](./numpy/expand_dims.ipynb), [`axes.ipynb`](./numpy/axes.ipynb)
  - [`mathematical_fns.ipynb`](./numpy/mathematical_fns.ipynb), [`mean_square_error.ipynb`](./numpy/mean_square_error.ipynb), [`sigmoid.ipynb`](./numpy/sigmoid.ipynb), [`vector_normalisation.ipynb`](./numpy/vector_normalisation.ipynb)
  - [`vectorisation_and_broadcasting.ipynb`](./numpy/vectorisation_and_broadcasting.ipynb), [`speed.ipynb`](./numpy/speed.ipynb), [`graphs.ipynb`](./numpy/graphs.ipynb)

### Pandas: Data Analysis & Feature Engineering
* **Core Concepts**: DataFrames & Series creation, handling missing data (`dropna`/`fillna`), GroupBy aggregation, multi-table merging/joining, Pivot Tables, and feature extraction from raw tabular data.
* **Featured Notebooks & Datasets**:
  - [`dataframe.ipynb`](./pandas/dataframe.ipynb), [`operations.ipynb`](./pandas/operations.ipynb), [`missing_data.ipynb`](./pandas/missing_data.ipynb)
  - [`group_by_aggregation.ipynb`](./pandas/group_by_aggregation.ipynb), [`merging_joining_concatenation.ipynb`](./pandas/merging_joining_concatenation.ipynb)
  - [`PivotTables.ipynb`](./pandas/PivotTables.ipynb), [`FeatureExtraction.ipynb`](./pandas/FeatureExtraction.ipynb), [`Countries.ipynb`](./pandas/Countries.ipynb)
  - Datasets: [`Countries.csv`](./pandas/Countries.csv), [`anime.csv`](./pandas/anime.csv)

---

## ⚙️ Automation Tool (`prime_push.bat`)

To maintain a frictionless learning workflow, this repository includes a custom Windows Batch automation script [`prime_push.bat`](./prime_push.bat).

### Script Capabilities:
1. **UTF-8 Support**: Enforces UTF-8 character encoding to handle special characters cleanly.
2. **Git Environment Check**: Verifies Git installation and repository initialization.
3. **Dynamic Branching**: Automatically detects the currently checked-out Git branch.
4. **Auto-Pull/Rebase**: Pulls remote changes before pushing to avoid non-fast-forward merge conflicts.
5. **Flexible Commit Messages**: Prompts for a custom commit message or auto-generates a timestamped message (e.g., `Auto-upload on 2026-08-18 10:00:00`).
6. **Error Handling**: Outputs errors cleanly to `git_error.log` if a push fails.

---

## 🚀 Getting Started

### 🛠️ Prerequisites & Setup

1. **Python Installation**: Ensure Python 3.9+ is installed.
   ```bash
   python --version
   ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/madhavr432/python-journey.git
   cd python-journey
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install Required Packages**:
   ```bash
   pip install numpy pandas matplotlib jupyter
   ```

5. **Launch Jupyter Notebooks**:
   ```bash
   jupyter notebook
   ```

---

## 🎯 Learning Goals

- 🐍 Build rock-solid fundamentals in core Python syntax and algorithmic logic.
- 🏗️ Master Object-Oriented design patterns for scalable code architecture.
- 📂 Gain proficiency in file operations, JSON data exchange, and robust exception handling.
- 📐 Leverage NumPy for high-performance numerical operations and ML math (Sigmoid, MSE, Vectorization).
- 📊 Master Pandas for real-world Data Cleaning, Exploratory Data Analysis (EDA), and Feature Engineering.

---

## 🧑‍💻 Author & Attribution

**Madhav Raj**  
🎓 B.Tech Computer Science & Engineering (CSE) Student  
🏫 Lakshmi Narain College of Technology (LNCT), Bhopal  
🔗 GitHub Profile: [@madhavr432](https://github.com/madhavr432)  
📁 Repository: [https://github.com/madhavr432/python-journey](https://github.com/madhavr432/python-journey)

---
*Happy Coding! 🚀 Keep building and learning every day.*
