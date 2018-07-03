
#!/usr/bin/python
import tensorflow as tf
import random

tf.InteractiveSession()
a = tf.fill((2,2),random.randint(1,5))
b = tf.fill((2,2),random.randint(1,5))
c = tf.fill((2,2),random.randint(1,5))
print("matrix a",a.eval())
print("matrix b",b.eval())
print("matrix c",c.eval())
d = tf.matmul(a,a)
print("a*a",d.eval())
e = tf.add(d,b)
print("+b",e.eval())
f = tf.matmul(e,c)
print("final",f.eval())