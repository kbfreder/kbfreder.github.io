#!/usr/bin/env python
# coding: utf-8

# # Image Classification: How to run inference on the endpoint you have created?

# ### Download example images. 

# In[1]:


import boto3
from IPython.core.display import HTML


# In[26]:


# import sagemaker

# sagemaker_session = sagemaker.Session()
# role = sagemaker.get_execution_role()
# role


# In[2]:


region = boto3.Session().region_name
s3 = boto3.client("s3")


# In[3]:


s3_bucket = "pepsico-potato-chip-dataset"
key_prefix = "Test"


# In[4]:


response = s3.list_objects_v2(Bucket=s3_bucket,
                                       Prefix=f"{key_prefix}/Defective")

defective_objects = [x['Key'] for x in response['Contents']]

defective_objects[:5]


# In[5]:


response = s3.list_objects_v2(Bucket=s3_bucket,
                                       Prefix=f"{key_prefix}/Non-Defective")
non_defective_objects = [x['Key'] for x in response['Contents']]

non_defective_objects[:5]


# In[6]:


import random


# In[9]:


def_obj_ex = random.choice(defective_objects)
non_obj_ex = random.choice(non_defective_objects)

def_ex = def_obj_ex.split('/')[-1]
non_def_ex = non_obj_ex.split('/')[-1]


# In[10]:


s3.download_file(
    Bucket="pepsico-potato-chip-dataset",
    Key=def_obj_ex,
    Filename=def_ex
)


# In[12]:


s3.download_file(
    Bucket="pepsico-potato-chip-dataset",
    Key=non_obj_ex,
    Filename=non_def_ex
)


# ### Open the downloaded images and load in memory.

# In[13]:


images = {}
with open(def_ex, 'rb') as file: images[def_ex] = file.read()
with open(non_def_ex, 'rb') as file: images[non_def_ex] = file.read()


# In[14]:


HTML(f'<table><tr><td> <img src="{def_ex}" alt="def" style="height: 250px;"/> <figcaption>def.jpg</figcaption>'
     f'</td><td> <img src="{non_def_ex}" alt="non-def" style="height: 250px;"/> <figcaption>non_def.jpg</figcaption>'
     '</td></tr></table>')


# ### Query endpoint that you have created with the opened images and parse predictions
# 
# Note: Backend scripts and the notebooks have been updated in Jan '22. This notebook will not work with the previously 
# launched endpoints. If experiencing an error, please launch the endpoint again. 

# In[15]:


import json

def query_endpoint(img):
    endpoint_name = 'jumpstart-ftc-tf-ic-imagenet-inception-v3-classificati'
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-image', Body=img, Accept='application/json;verbose')
    return response
    

def parse_prediction(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    predicted_label = model_predictions['predicted_label']
    labels = model_predictions['labels']
    probabilities = model_predictions['probabilities']
    return predicted_label, probabilities, labels 

for filename, img in images.items():
    query_response = query_endpoint(img)
    predicted_label, probabilities, labels = parse_prediction(query_response)
    display(HTML(f'<img src={filename} alt={filename} align="left" style="width: 250px;"/>' 
                 f'<figcaption>Predicted Label is : {predicted_label}</figcaption>'))


# In[16]:


import os


# In[18]:


os.remove(def_ex)


# In[20]:


images.keys()


# In[22]:


probabilities


# In[25]:


# n = 10

# def_obj_test_list = random.choices(defective_objects, n)
# def_file_test_list = [x.split('/')[-1] for x in def_obj_test_list]

# nondef_obj_test_list = random.choices(non_defective_objects, n)
# nondef_file_test_list = [x.split('/')[-1] for x in nondef_obj_test_list]


def_preds = {}
non_def_preds = {}
problem_files = {}

def fetch_and_predict(obj):
    file_name = obj.split('/')[-1]
    s3.download_file(
        Bucket="pepsico-potato-chip-dataset",
        Key=obj,
        Filename=file_name
    )
    with open(file_name, 'rb') as file: img = file.read()
    query_response = query_endpoint(img)
    predicted_label, probabilities, labels = parse_prediction(query_response)
    os.remove(file_name)
    return predicted_label, probabilities

for i, obj in enumerate(defective_objects):
    file_name = obj.split('/')[-1]
    pred, probas = fetch_and_predict(obj)
    def_preds[file_name] = [pred, probas]


# In[ ]:





# In[27]:



for i, obj in enumerate(non_defective_objects):
    file_name = obj.split('/')[-1]
    try:
        pred, probas = fetch_and_predict(obj)
        non_def_preds[file_name] = [pred, probas]
    except Exception as e:
        problem_files[file_name] = e
        


# In[26]:


len(def_preds)


# In[28]:


len(non_def_preds)


# In[31]:


list(def_preds.values())[:5]


# In[35]:


d_correct = len(list(filter(lambda x: x[0] == 'Defective', list(def_preds.values()))))
d_total = len(def_preds)

nd_correct = len(list(filter(lambda x: x[0] == 'Non-Defective', list(non_def_preds.values()))))
nd_total = len(non_def_preds)


# In[36]:


d_correct, nd_correct


# In[37]:


accuracy = (d_correct + nd_correct) / (d_total + nd_total)
accuracy


# In[38]:


# Categorical accuracy
print(d_correct / d_total)
print(nd_correct / nd_total)


# 
