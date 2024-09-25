# base image
FROM python:3.12

# setup working directory in container
WORKDIR /app

# copy all files to app directory
COPY . /app/

# command to run on container start
# CMD ["python", "Assig#2Report_card.py","Reportcard.py"]
CMD ["sh", "-c", "python Assig#2Report_card.py && python Reportcard.py"]
