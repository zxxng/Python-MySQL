import matplotlib.pyplot as plt 
 
x = [x for x in range(20)]     
y = [x**2 for x in range(20)]  
z = [x**3 for x in range(20)]  
 
plt.plot(x, x, label='linear')   
plt.plot(x, y, label='quadratic') 
plt.plot(x, z, label='qubic') 
 
plt.xlabel('x label')      
plt.ylabel('y label')     
plt.title("My Plot") 
plt.legend()              
plt.show()
