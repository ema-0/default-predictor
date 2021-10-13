# Default predictor

## 1. How to run the application
Make a POST request to the endpoint: 

```https://9rnn9xw0hd.execute-api.eu-west-1.amazonaws.com/default/default-predictor```

with a dictionary in the request body containing all the information about one account, for instance:

```json
{"uuid": "6f6e6c6a-2081-4e6b-8eb3-4fd89b54b2d7",
 "account_amount_added_12_24m": 0,
 "account_days_in_dc_12_24m": 0.0,
 "account_days_in_rem_12_24m": 0.0,
 "account_days_in_term_12_24m": 0.0,
 "account_incoming_debt_vs_paid_0_24m": 0.0091346153846153,
 "account_status": 1.0,
 "account_worst_status_0_3m": 1.0,
 "account_worst_status_12_24m": "nan",
 "account_worst_status_3_6m": 1.0,
 "account_worst_status_6_12m": 1.0,
 "age": 20,
 "avg_payment_span_0_12m": 6.4,
 "avg_payment_span_0_3m": 5.25,
 "merchant_category": "Youthful Shoes & Clothing",
 "merchant_group": "Clothing & Shoes",
 "has_paid": "True",
 "max_paid_inv_0_12m": 7225.0,
 "max_paid_inv_0_24m": 7225.0,
 "name_in_email": "F",
 "num_active_div_by_paid_inv_0_12m": 0.0,
 "num_active_inv": 0,
 "num_arch_dc_0_12m": 0,
 "num_arch_dc_12_24m": 0,
 "num_arch_ok_0_12m": 5,
 "num_arch_ok_12_24m": 0,
 "num_arch_rem_0_12m": 0,
 "num_arch_written_off_0_12m": 0.0,
 "num_arch_written_off_12_24m": 0.0,
 "num_unpaid_bills": 1,
 "status_last_archived_0_24m": 1,
 "status_2nd_last_archived_0_24m": 1,
 "status_3rd_last_archived_0_24m": 1,
 "status_max_archived_0_6_months": 1,
 "status_max_archived_0_12_months": 1,
 "status_max_archived_0_24_months": 1,
 "recovery_debt": 0,
 "sum_capital_paid_account_0_12m": 8815,
 "sum_capital_paid_account_12_24m": 0,
 "sum_paid_inv_0_12m": 27157,
 "time_hours": 19.8955555555556,
 "worst_status_active_inv": "nan"}
```

### AWS services
The model has been wrapped in a rest API, hosted by AWS. It triggers a Lambda function that
relies on a Docker image, compiled locally and then pushed in a registry.

So the AWS services involved are API Gateway, Lambda and Elastic Container Registry.


# 2. About the repo
The repo files are organized in 3 folders:
- `data`:
  - *dataset.csv* file used to train and validate the model. 
    For sake of simplicity and because its small size, I included in the repo.
    Ideally it should be downloaded directly by the user.
  - *predictions.csv* output of the model on the unlabelled data points given in input .
- `notebooks`: the prototype of the algorithm, with a short description of the
model and performance evaluation. It includes all the development parts, from data manipulation
to training and testing of the neural network. Finally, it saves the model and makes predictions.
- `lambda_default_predictor`: this folder cointains all the files
need to build a Docker image able to predict on new data:
  - *app.py*: the lambda handler
  - *Dockerfile*: the AWS dockerfile to create an image compatible with ECR
  - *trained_model*:  written by the notebook and read by the application. It contains the model and
  other data required:
    - *categories.txr*
    - *numerics_columns.txt*
    - *model.h5*

Finally, I included the conda environment file *klarna.yml* to recreate
my developing environment with conda.

For instance, with Linux and MacOs:
```console
conda env create -f klarna.yml
conda activate klarna 
```
