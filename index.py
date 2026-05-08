import numpy as np

file_path = '300_merged_300_utt082_300_utt086.npy'
data = np.load(file_path)

print(f"Data loaded from {file_path}. Shape: {data.shape}")
from google.colab import drive
drive.mount('/content/drive')
floc1='/content/drive/MyDrive/desp/'

import numpy as np
from scipy.stats import entropy, kurtosis

def calculate_descriptive_statistics(data_array):
    """
    Calculates a minimum of 10 descriptive statistics for a given NumPy array.

    Args:
        data_array (np.ndarray): The input NumPy array.

    Returns:
        dict: A dictionary containing the descriptive statistics.
    """
    stats=np.zeros((11))
    stats[0]=np.mean(data_array)
    stats[1]=np.median(data_array)
    stats[2]=np.std(data_array)
    stats[3]=np.var(data_array)
    stats[4]=np.min(data_array)
    stats[5]=np.max(data_array)
    stats[6]=np.max(data_array)-np.min(data_array)
    stats[7]=np.percentile(data_array,25)
    stats[8]=np.percentile(data_array,75)
    stats[9]=entropy(data_array-np.min(data_array))
    stats[10]=kurtosis(data_array)
    return stats

import glob

npy_files = glob.glob(floc1+'dep/'+'*.npy')
print("Found .npy files:")
for f in npy_files:
    print(f)
import re

# Group files by their numerical prefix
grouped_files = {}
for file_name in npy_files:
    match = re.match(floc1+r'(\d+)_.*', file_name)
    if match:
        prefix = match.group(1)
        if prefix not in grouped_files:
            grouped_files[prefix] = []
        grouped_files[prefix].append(file_name)

print("Files grouped by prefix:")
for prefix, files in grouped_files.items():
    print(f"Prefix {prefix}: {len(files)} files")
import numpy as np

loaded_data_by_prefix = {}
for prefix, files in grouped_files.items():
    loaded_data_by_prefix[prefix] = []
    for file_name in files:
        try:
            data_array = np.load(file_name)
            loaded_data_by_prefix[prefix].append(data_array)
        except Exception as e:
            print(f"Error loading {file_name}: {e}")

print("\nStructure of organized data:")
for prefix, data_arrays in loaded_data_by_prefix.items():
    if data_arrays:
        print(f"Prefix: {prefix}, Number of arrays: {len(data_arrays)}, Example array shape: {data_arrays[0].shape}")
    else:
        print(f"Prefix: {prefix}, No data arrays loaded.")
import pandas as pd
datan=pd.read_csv('train_split_Depression_AVEC2017.csv')
def split_ds(x):
  dsv=np.zeros((8*11))
  for i in range(0,8):
    dsv[11*i:11*(i+1)]=calculate_descriptive_statistics(x[256*i:256*(i+1)])
featv=[]
for i in range(0,6):
  feat=np.zeros((datan.shape[0],2048))
  for j in range(0,datan.shape[0]):
    try:
      d=loaded_data_by_prefix[str(datan['Participant_ID'][j])]
      feat[j,:]=np.mean(d,axis=0)
    except:
      print('not found',str(datan['Participant_ID'][j]))
    #k=0
    #while k<5+5*i and k<len(d):
     # feat[j,k*11:k*11+11]=calculate_descriptive_statistics(d[k])
     # k=k+1
  featv.append(feat)
featv1=[]
for i in range(0,6):
  #feat=np.zeros((datan1.shape[0],11*(5+5*i)))
  feat=np.zeros((datan1.shape[0],2048))
  for j in range(0,datan1.shape[0]):
    try:
      d=loaded_data_by_prefix[str(datan1['Participant_ID'][j])]
      feat[j,:]=np.mean(d,axis=0)
    except:
      print('not found',str(datan1['Participant_ID'][j]))

    #k=0
    #while k<5+5*i and k<len(d):
      #feat[j,k*11:k*11+11]=calculate_descriptive_statistics(d[k])
      #k=k+1
  featv1.append(feat)
from sklearn.utils import all_estimators
model=all_estimators(type_filter='classifier')
fmodel=[]
for name,mod in model:
  try:
    fmodel.append(mod())
  except:
    pass
from copy import copy
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,confusion_matrix
bacc=0
baccc=[]
bmestc=[]
s1=[]
for i in range(0,6):
  trdata=featv[i]
  tsdata=featv1[i]
  s=MinMaxScaler()
  trdatan=s.fit_transform(copy(trdata))
  tsdatan=s.transform(copy(tsdata))
  for j in range(0,len(fmodel)):
    try:
      m=copy(fmodel[j])

      m.fit(trdatan,tract)
      ypred=m.predict(tsdatan)
      print(m)
      print('accuracy',accuracy_score(tsact,ypred)*100)
      print('precision',precision_score(tsact,ypred))
      print('recall',recall_score(tsact,ypred))
      print('f1',f1_score(tsact,ypred))
      if bacc<accuracy_score(tsact,ypred)*100:
        bacc=accuracy_score(tsact,ypred)*100
        bestmodel=m
    except:
      pass
  baccc.append(bacc)
  bmestc.append(bestmodel)
  bacc=0
  s1.append(s)

from copy import copy
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,confusion_matrix
bacc=0
baccc=[]
bmestc=[]
s1=[]
for i in range(0,6):
  trdata=featv[i]
  tsdata=featv1[i]
  s=MinMaxScaler()
  trdatan=s.fit_transform(copy(trdata))
  tsdatan=s.transform(copy(tsdata))
  for j in range(0,len(fmodel)):
    try:
      m=copy(fmodel[j])

      m.fit(trdatan,tract)
      ypred=m.predict(tsdatan)
      print(m)
      print('accuracy',accuracy_score(tsact,ypred)*100)
      print('precision',precision_score(tsact,ypred))
      print('recall',recall_score(tsact,ypred))
      print('f1',f1_score(tsact,ypred))
      if bacc<accuracy_score(tsact,ypred)*100:
        bacc=accuracy_score(tsact,ypred)*100
        bestmodel=m
    except:
      pass
  baccc.append(bacc)
  bmestc.append(bestmodel)
  bacc=0
  s1.append(s)

fmodev=[]
for k1 in range(0,6):
  fmodn=[]
  for mod in fmodel:
      fmodn.append(make_pipeline(SelectKBest(f_classif,k=20+20*k1),mod))
  fmodev.append(fmodn)
from copy import copy
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,confusion_matrix
bacc=0
baccc=[]
bmestc=[]
for i in range(0,6):
  trdata=copy(trdatan)
  tsdata=copy(tsdatan)
  fmodel=copy(fmodev[i])
  for j in range(0,len(fmodel)):
    try:
      m=copy(fmodel[j])
      m.fit(trdata,tract)
      ypred=m.predict(tsdata)
      print(m)
      print('accuracy',accuracy_score(tsact,ypred)*100)
      print('precision',precision_score(tsact,ypred))
      print('recall',recall_score(tsact,ypred))
      print('f1',f1_score(tsact,ypred))
      if bacc<accuracy_score(tsact,ypred)*100:
        bacc=accuracy_score(tsact,ypred)*100
        bestmodel=m
    except:
      pass
  baccc.append(bacc)
  bmestc.append(bestmodel)
  bacc=0

from sklearn.preprocessing import MinMaxScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
def normalizedata(X_train):
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    return X_train
from sklearn.tree import DecisionTreeClassifier,ExtraTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
kf=KFold(n_splits=5,shuffle=True)
def model_per1(trdata,tract,tsdata,tsact):
  model=GradientBoostingClassifier()
  #np.random.shuffle(data)
  #scaler = MinMaxScaler()
  #trdata=scaler.fit_transform(trdata)
  #tsdata=scaler.transform(tsdata)
  acc=accuracy_score(tsact,model.fit(trdata,tract).predict(tsdata))
  return acc,model
from copy import copy
def fitness(chr,trdata,tsdata,tract,tsact):
  noc=np.shape(chr)[0]
  fit=np.zeros((noc,3))
  modelf=[]
  for i in range(0,noc):
    in1=np.where(chr[i,:]==1)
    trdatan=trdata[:,in1[0]]
    tsdatan=tsdata[:,in1[0]]
    fit[i,0]=len(in1[0])
    fit[i,1],m=model_per1(copy(trdatan),tract,copy(tsdatan),tsact)
    modelf.append(m)
    fit[i,2]=0.99*fit[i,1]+0.01*(np.shape(chr)[1]-len(in1[0]))/np.shape(chr)[1]
  return fit,modelf
def crossover(chr):
  noc=np.shape(chr)[0]
  nchr=np.zeros((int(noc/2),np.shape(chr)[1]))
  np.random.shuffle(chr)
  mid=int(np.shape(chr)[1]/2)
  for i in range(0,int(noc/2)):
    nchr[i,0:mid]=chr[2*i,0:mid]
    nchr[i,mid:]=chr[2*i+1,mid:]
  return nchr
def mutaion(chr):
  nor=np.random.randint(0,np.shape(chr)[1],[np.shape(chr)[0],10])
  for i in range(0,np.shape(chr)[0]):
    for j in range(0,10):
      chr[i,nor[i,j]]=1-chr[i,nor[i,j]]
  return chr
def gafs(trdata,tract,tsdata,tsact):
  noc=100
  print("ALL Features",model_per1(copy(trdata),tract,copy(tsdata),tsact))
  chr=np.random.randint(0,2,[noc,np.shape(trdata)[1]])
  gen=0
  bfit=0
  while gen<200:
    fit,modelf=fitness(chr,trdata,tsdata,tract,tsact)
    in1=np.argmax(fit[:,2])
    cfit=np.max(fit[:,2])
    if cfit>bfit:
      bfit=cfit
      bchr=copy(chr[in1,:])
      bnof=fit[in1,0]
      bacc=fit[in1,1]
      bmodel=copy(modelf[in1])
    chr[0:int(noc/2),:]=crossover(chr)
    chr[0:int(noc/2),:]=mutaion(chr[0:int(noc/2),:])
    chr[int(noc/2):,:]=np.random.randint(0,2,[int(noc/2),np.shape(trdata)[1]])
    gen=gen+1
    print('gen=',gen,'nof=',bnof,'bacc=',bacc,'bfit=',bfit)
  return bchr,bmodel
trdata=copy(fvn[1])
tsdata=copy(fvn1[1])
bchr,bmodel=gafs(trdata,tract,tsdata,tsact)
dsvtn=['me','med','std','var','min','max','ran','Q1','Q3','en','kt']
dctnf=[]
for i in range(0,6):
  for j in range(0,11):
    dctnf.append(dsvtn[j])
!pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Convert the list of important features to a single string
word_string = " ".join(impf)

# Generate the word cloud
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(word_string)

# Display the generated image:
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()

