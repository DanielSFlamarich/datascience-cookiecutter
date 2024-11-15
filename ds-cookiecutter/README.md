<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
  </a>

<h3 align="center">Data Science Cookiecutter</h3>

  <p align="center">
    This repo will help you create new repositories already with all the tools needed to do data analysis. This template should be used by the data teams to build software that has the same consistent architecture through all projects.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Starting a new project</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Python >= 3.5 

[cookiecutter Python package](https://pypi.org/project/cookiecutter/) >= 1.4.0: 
`pip install cookiecutter`

### Starting a new project

You should be in the folder you want to create the new repo when starting a new project. 

#### Step 1 : Run this command line, answer a few questions (all are optional, if you really feel lazy and don't want to answer any of them, just title the repo when `repo name` appears), and cookiecutter will automatically create the directory.

`cookiecutter https://github.com/danielsflamarich-sns/ds-cookiecutter.git`

#### Step 2: After that, go to the newly created folder and create a new environment (in the example below, the environment name is `env`. The template has a gitignore file already created that'll ignore the environment folder in commits, so you should call your environment like this):

`python3 -m venv env`

##### If, for some reason you don't like this name and come up with another one, you'll have to change the gitignore file to make it ignore the environment with your fancy name.

#### Step 3: Activate newly created environment (again, called `env` in this example):

`source env/bin/activate`

#### Step 4: Install basic requirements (listed in requirements.txt)

`pip install -r requirements.txt`

#### Step 5: This one's optional, but it'll make your life easier so why not also create the kernel so it's available in the notebook/lab:

`python -m ipykernel install --user --name=my_new_kernel`

#### Step 6: There you go, you're all set! Go build something amazing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Project Organization

The main architecture is as follows:

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for data scientists using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── processed      <- The final data. Clean/engineered/canonical data sets for modeling
    │   ├── queries        <- SQL statements for connections.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number with a zero on the left (for ordering),
    │                         the creator's initials, underscore plus delimited description, e.g.
    │                         `01_dsf_exploratory_data_analysis`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── plots          <- Generated graphics/plots/figures to be used in reporting/slides
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── util               <- Python functions used in the notebooks
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── connections    <- Redshift connections
    │   ├── data           <- Scripts to download/generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are great and an amazing way to learn and make our team better. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please clone the repo and create a pull request.

1. Clone the repo.
2. Create your Feature Branch (`git checkout -b feature/CreatingAmazingFeature`)
3. Commit your Changes (`git commit -m 'Added some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/CreatingAmazingFeature`)
5. Open a Pull Request

It's that simple! :smile:

<p align="right">(<a href="#readme-top">back to top</a>)</p>
