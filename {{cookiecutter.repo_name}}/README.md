{{cookiecutter.project_name}}
==============================

{{cookiecutter.project_description}}

Use
----
After setting up the environment with requirements.txt, run from the directory root with `python train/code/train_models.py` or  `python predict/code/generate_predictions.py`. 


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

{{cookiecutter.author_name}}
--------
