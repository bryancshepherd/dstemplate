Data Science Project Template
==============================

This is a cookiecutter data science project template. This template helps get data science projects up to speed quickly and ensures a standard organization.

Instructions for using this template
----
**Step 1 - Getting the tools**
- Activate an environment with the cookiecutter package installed. If one doesn't exist, create one and install cookiecutter, e.g., `pip install cookiecutter`.

**Step 2 - Downloading the template**
- From a terminal in the root `Projects` folder, run `cookiecutter https://github.com/bryancshepherd/dstemplate.git`. 

**Step 3 - Making the cookies**
- Follow the prompts. This will create a project folder in the current directory.

**Step 4 - Environment Management**
- Run `pip install -r requirements.txt` to install current versions of basic dependencies like pandas and Flask.


Project Organization
------------
```
├── app                <- Dashboard for visualizing training model performance results
│   ├── static         <- CSS files and other static assets for the dashboard
│   ├── tables         <- Data tables that provide data for the dashboard
│   ├── templates      <- HTML templates for the dashboard
│   └── dashboard.py   <- The main dashboard application code
│
├── docs               <- Project documentation
│
├── libs               <- In-house libraries and scripts that are not installed via pip
│
├── logs               <- Log files
│
├── model_objects      <- Serialized model objects and crosswalks 
│   ├── current        <- Model objects from currently active runs; these are the models currently being used for predictions, etc.
│   ├── previous       <- Model objects from the previous run; these are kept for comparisons and evaluation
│   └── temp           <- Temporary versions of the model objects that do not need to be kept
│
├── predict            <- Prediction related code and data; used only if predictions are required
│   ├── code           <- Code to generate predictions on new data
│   │   └── generate_predictions.py <- The main prediction code; this should kick off the run
│   ├── data           <- Input data for new predictions
│   └── output         <- Output files for holding results; not used if results are written to the database
│
├── tests              <- Testing related code
│
├── train              <- Training related code and data
│   ├── code           <- Code to train models on training data
│   │   └── train_models.py <- The main training code; this should kickoff the run
│   └── data           <- Input training data
│
├── README.md          <- The top-level README for this project
│
└── requirements.txt   <- The requirements file for reproducing the environment, e.g.
                          generated with `pip freeze > requirements.txt`

```
--------
