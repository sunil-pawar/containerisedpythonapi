#python imgae from hub

FROM python

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist

WORKDIR /restapi


# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it


EXPOSE 5000



# Install any needed packages specified in requirements.txt

copy requirement.txt /restapi
cOPY add.json /restapi

RUN pip install -r requirement.txt 

# Run main.py when the container launches

#copy ./pythonAPI/RestAPI2/src /restapi

CMD python main.py


