FROM pytorch/pytorch:latest

RUN pip install nnunetv2 

COPY example_code.py .

COPY ./Model ./Model

