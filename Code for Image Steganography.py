#importing libraries
import cv2
import string
import os
p={}
q={}

for i in range(255):
    p[chr(i)]=i
    q[i]=chr(i)

x=cv2.imread(r"C:\Users\chitr\OneDrive\Desktop\New folder\flower.jfif")

i=x.shape[0]
j=x.shape[1]
print(i,j)

#Input security key and secret message
key=input("Enter key to edit(security key):")  #password
text=input("Enter text to hide:")  #secret message

kl=0
tln=len(text)
z,n,m=0,0,0


l=len(text)

#Encoding text into a image
for i in range(l):
    x[n,m,z]=p[text[i]]^p[key[kl]]
    n=n+1
    m=m+1
    m=(m+1)%3
    kl=(kl+1)%len(key)

#saves the encryted image
cv2.imwrite("encryptimage.jpg",x)
os.startfile("encryptimage.jpg")
print("Text hiding in image completed successfully")

kl=0
tln=len(text)
z,n,m=0,0,0

#unhide text from image
ch=int(input("\n Enter 0 to extract data from image:"))

if ch==0:
    key1=input("\n\n Re enter the key to extract text:")
    decrypt=""

    if key==key1:
        for i in range(l):
            decrypt+=q[x[n,m,z]^p[key[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key)
        print("encrpted text was:", decrypt)
    else:
        print("key doesnot matched")

else:
    print("thank you ! Existing")
