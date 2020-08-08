import numpy as np
eps = 0.00001 # A value to compare the error with
nos = 6 # Number of states
v = np.zeros([1000,nos])
c = 0 # Value of constant
r = np.array([0,0,0,0,0,10]) + c*np.ones(nos)
error = np.empty(v.shape[1])
gama = 0.9
for k in range(0,v.shape[0]):
	for s in range(0,nos):
		if(s==0):
			v[k+1,s] = np.max((r[s+1]+gama*v[k,s+1],r[s]+gama*v[k,s]))
		elif(s==5):
			v[k+1,s] = np.max((r[s]+gama*v[k,s]))
		else:
			v[k+1,s] = np.max((r[s+1]+gama*v[k,s+1],r[s-1]+gama*v[k,s-1]))
	error[:] = np.absolute(v[k+1][:]-v[k][:])
	if np.max(error)<eps:
		break;
	print("Epoch =",k, "Error = ",np.max(error))
print("Optimal Value Function = ",v[k+1])