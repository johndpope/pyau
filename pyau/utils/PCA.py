import numpy as np


def PCA(dataMatrix, NDIMS) :
    """
    Performs PCA on data.
    Reduces the dimensionality to NDIMS
    Returns dataMatrix,eigVectors,eigValues,dataMean
    """
    if dataMatrix.shape[1]<NDIMS:
        NDIMS=dataMatrix.shape[1]
        print 'Cannot reduce from %i to %i dimensions'%(dataMatrix.shape[1],NDIMS)
        return dataMatrix,None,None,None
    
    print 'Performing PCA from %i to %i dimensions'%(dataMatrix.shape[1],NDIMS)
    
    # taking out the mean
    dataMean=dataMatrix.mean(axis=0)
    dataMatrix= dataMatrix-dataMean

    (eigValues,eigVectors)=np.linalg.eig(np.cov(dataMatrix.T))
    perm=np.argsort(-eigValues)
    eigVectors=eigVectors[:,perm[0:NDIMS]]
    dataMatrix=np.dot(dataMatrix,eigVectors)
#    print dataMatrix.shape
    return dataMatrix,eigVectors,eigValues,dataMean

def invPCA(reducedMatrix, eigVectors, dataMean):
    if eigVectors is not None:
        return np.dot(reducedMatrix,np.linalg.pinv(eigVectors))+dataMean
    else:
        return reducedMatrix

def pcaSpace(dataMatrix,eigVectors,dataMean):
    """
    reduce the data using an already computed PCA
    """
    dataMatrix-=dataMean
    dataMatrix=np.dot(dataMatrix,eigVectors)
    return dataMatrix
    
#TODO
#def savePCA(reducedMatrix, eigVectors, dataMean, fileName='PCA'):
#    np.save(fileName+'_PCAdata')
