import h5py
import numpy as np

def find_nearest_vector(array, value):
   #idx = np.array([np.linalg.norm(x-value) for x in array]).argmin()
   #id30 = np.where(array[:,2]>-30e3)
   #array = array[id30]
   idx = np.array([np.linalg.norm(x[0:3]-value[0:3]) for x in array]).argmin()
   return array[idx]

# Parsing python arguments
import argparse
parser = argparse.ArgumentParser(description='find closest surface triangle center from receiver')
parser.add_argument('--surface',nargs=1, help='surface hdf5 filename')
parser.add_argument('--receiver',nargs=1, help='receiver ascii filename')
args = parser.parse_args()

# Read Hdf5
from pythonXdmfReader import *
xdmfFilename = args.fault[0]
faultxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)

centers = (faultxyz[connect[:,0]] + faultxyz[connect[:,1]] + 
faultxyz[connect[:,2]])/3.

FidReceivers = args.receivers[0]
FidReceiversnew = args.receivers[0]+'2'
Receivers = np.loadtxt(FidReceivers)
FidReceiversnew = FidReceivers+'2'
fout = open(FidReceiversnew,'w')

for rec in Receivers:
    print(rec)
    newrec = find_nearest_vector(centers, rec)
    fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
fout.close()
