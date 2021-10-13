FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app.py ${LAMBDA_TASK_ROOT}
COPY trained_model/categories.txt ${LAMBDA_TASK_ROOT}/trained_model/
COPY trained_model/numerics_columns.txt ${LAMBDA_TASK_ROOT}/trained_model/
COPY trained_model/model.h5 ${LAMBDA_TASK_ROOT}/trained_model/

CMD [ "app.handler" ]