
import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

import sys


# pip install --upgrade streamlit


import sys
sys.exit()

col1,col2=st.columns(2)
with col1:
    st.image('raccoon.jpg',width=300)
with col2:
    st.write('안녕 나는 라쿤이야!')
    '전화번호(📞) : 010-xxxx-xxxx'
    '이메일(📧) : 19683011@konyang.ac.kr'
    '주소(🏠) : 충북 청주시 xxx xxx'

'## : orange["자기소개"]'

col=st.columns(4)
with col[0]:
    st.link_button("google(🌐)", "https://google.com")
with col[1]:
    st.link_button("naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("daum(🇩)", "https://daum.com")
with col[3]:
    st.link_button("facebook(ⓕ)","https://facebook.com")





fig,ax = plt.subplots()

x=[]
y=[]
for i in range(-10,11,2):
    x.append(i)
    y.append(3*i**3-5*i**2+3*i-7)

col1,col2,col3= st.columns(3)

with col1:
    cc=st.radio('선의 색을 선택하시오',['red','green','blue','orange'])
with col2:
    ma=st.radio('마커의 형태를 선택하시오',['o','^','s'])
with col3:
    ls=st.radio('선의 형태를 선택하시오',['-','-.',':'])

plt.plot(x,y,color=cc,linestyle=ls,marker=ma)
st.pyplot(fig)


fig,ax = plt.subplots()


x =[]
y =[]
for i in range(-100,101,45):
    x.append(i)
    y.append(2*i**3-5*i**2+3*i-7)

# 대안1
col1,col2,col3=st.columns(3)
with col1:
    color=st.radio('색을 선택하시오.',('red','green','blue'))
with col2:
    linestyle=st.radio('선의 스타일을 선택하시오.',('-','-.',':'))
with col3:
    marker=st.radio('마커의 스타일을 선택하시오.',('s','^','o'))


# 대안2
plt.plot(x,y,color= color, marker=marker, linestyle=linestyle)

st.pyplot(fig)

import sys
sys.exit()
st.write('Hello, *World!* **tt** ***yy*** :red[red] :green[green] :blue[blue] :white_check_mark:')
# 이뒤의 실행문은 읽지 않겠다


# 터미널창 깨끗하게 함
import os
os.system('cls')

# 1차원 배열
# li=[1,2,3,4]
# n=np.array(li)
# p= pd.Series(li,index=['a','b','c','d'])
# li
# n
# p
# 2차원배열

list1=list([['한빛','남자','20','180'],
            ['한결','남자','21','177'],
            ['한라','여자','20','160'],
            ['한정','여자','220','150']])
n=np.array(list1)
col_names=['이름','성별','나이','키']
df=pd.DataFrame(list1,columns=col_names,index=['1','2','3','4'])

genre = st.radio(
    "선택하시오",
    ["오름차순", "내림차순", "기타","요약"],
horizontal=True,index=2)
# 가로로 만들기, 기본몇번째 선택할것인지
number = st.number_input('Insert a number',value=20,step=1)
df.iloc[3,2]=number


if '오름'in genre:
    st.dataframe(df.sort_values(by=['키']))
if '내림'in genre:
    st.dataframe(df.sort_values(by=['키'],ascending=False))
if '기타'in genre:
    st.dataframe(df)
if '요약'in genre:
    st.dataframe(df.describe())

# 배열
# li=np.array([7,2,5,4])
# li
# li_sort= np.sort(li)[::-1]
# li_sort

# 임의의 수 각자 더하기
# li=np.array([1,2,3,4])
# li+3


# for i in range(6):
#     r= random.randint(1,45)
#     r


# a=np.array([1,10,5,2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(np.square(a))

# a=np.arange(8)
# a
# a.shape=(2,4)
# a
# b=a.flatten()
# b
# b.resize((2,4))
# b

# list1 = [[1,2,3,4],[1,2,3,4]]
# a=np.array(list1)
# a

# list1 = [[10,10,10,10],[10,10,10,10],[10,10,10,10],[10,10,10,10],[10,10,10,10]]
# a=np.array(list1)
# a

# a.shape
# s=a.sum(axis=0)
# s
# mn=a.min(axis=1)
# mn
# max=a.max(axis=1)
# max

# def find_numbers_with_mod(n):
#     for i in range(1, n + 1):
#         if i % 7 == 3:
#             print(i)
# n=100

# e=np.eye(3)
# ('5',e)
# 시험문제 eye대각선 반대로
# def user_eye(n):
#     arr=np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i ==j or i ==n-j-1:
#                         arr[i,j]=1
#     return arr

# arr=user_eye(10)
# arr

# 교수님꺼
# n=5
# arr=np.full((n,n),'나머지')
# arr

# for i in range(n):
#         for j in range(n):
#             # arr[i,j]='나머지'
#             if i ==j or i+j==n-1:
#                 arr[i,j]='대'

# arr



# n2 = []
# n2.append(10)
# n2
# np.append(n2,15)
# n2

# arr=np.array([1,2,3])
# s=arr.sum()
# s
# s1=np.sum(arr)
# s1

# n=np.ndim
# np.size(a)
# a.T



# def sta(arr):
#     sum=0 #초기값
#     mx=-1e10
#     mn=1e10
#     for i in arr:
#         s = s+ i
#         if mx<1:
#             mx=i
#         if mn>1:
#             mn=i
#     arr
#     'sum=',sum,'min=',mn,'max=',mx
#     return s,mx,mn

# list_1=[5,13,7,4,11]
# [s1,mx1,mn1]=sta(list_1)
# s1,mx1,mn1

# list_1=[1,2,7,4,50,33]
# s=sum(list_1)
# mx=max(list_1)
# mn=min(list_1)
# s,mx,mn






# '덧셈결과',a+b
# '뺄셈결과',a-b
# '곱셈결과',a*b
# '나눗셈결과',a/b
# '나눗셈 정수 몫',a//b
# '나눗셈 나머지',a%b
# '거듭제곱 결과',a**b

# grade=80

# if grade>=90:
#     'A'
# elif grade>=80:
#     'B'
# elif grade>=70:
#     'C'
# elif grade>=60:
#     'D'
# else:
#     'F'


# for a in range(1,10,1):
#     a,'단'
#     for i in range(1,10,1):
#         b=str(a) + 'X' +str(i)+'='+str(a*i)
#         b

# li=[1,2,3,4,5,1,3,4,1,2,2,2,3,4,2,3,2,5,2,3,4]
# li.append(50)
# li
# c=li.count(2)
# c

# li.sort(reverse=True)
# li



# dict={'name':'신수인','weight':69,'height':172,'addreess':'논산시 대학로 121'}
# dict

# for k in dict.keys():
#     k
# for v in dict.values():
#     v
# '============================='
# for k,v in dict.items():
#     k   
#     v
# ty=type(dict)
# ty


# dict_1={'name':'길동이','birth':1990,'addr':'kr'}
# (dict_1)
# dict_1['birth']

# dict_1['weight']=60.5
# dict_1['family']=['아빠','엄마','여동생']
# (dict_1)

# dict_1.update({'weight':67.8,'hobby':['게임','독서']})
# (dict_1)

# dict_1['hobby']=['축구','등산']
# (dict_1)

# t=turtle.Turtle()
# t.shape('turtle')

# t.circle(50)
# t.penup()
# t.goto(70,90)
# t.pendown()
# t.right(90)
# t.forward(100)
# t.penup()
# t.goto(0,-70)
# t.pendown()
# t.circle(50)
# turtle.done()


# 여기부터 1학기꺼

# 1번문제
# for i in range(1,101,4):
#     st.write(i, end="")


# 2번문제
# im=np.full((500,500,3),255,dtype=np.uint8)

# c1=250
# c2=250
# r=120
# for row in range(500):
#     for column in range(500):
#         if (row-c1)**2 + (column-c2)**2 <=r**2:
#             im[row,column,0]=255
#             im[row,column,1]=255
#             im[row,column,0]=255
#         else:
#             im[row,column,0]=255
#             im[row,column,1]=255
#             im[row,column,1]=0

# st.image(im)


# 3번문제
# src=cv2.imread('enhan1.png')
# s=src.shape
# st.image(src)





# 히스토그램 예제
# src=np.array ([ [0,0,0,0],
#                 [1,2,3,4],
#                 [3,4,4,1],
#                 [2,5,5,3],
#                 ],dtype=np.uint8)
# src
# src=cv2.imread('enhan1.png')
# s=src.shape
# st.image(src)

# c=np.zeros(6)
# for row in range(s[0]):
#     for col in range(s[1]):
#         for k in range(6):
#             if src[row,col]==k:
#                 c[k]=c[k]+1
# src=cv2.imread('bright.jpg')

# hist1=cv2.calcHist(images=[src], channels=[0],mask=None, histSize=[256], ranges=[0,256])
# hist1

# y=histflatten=hist1.flatten()
# x=binx=np.arange(256)

# fig,ax=plt.subplots()
# plt.plot(x,y,color='r')
# plt.bar(x,y,width=1,color='b')
# plt.plot(binx,histflatten,color='r')
# plt.bar(binx,histflatten,width=8,color='b')

# col1,col2=st.columns(2)
# with col1:
#     st.image(src)
# with col2:
#     st.pyplot(fig)


# c=np.zeros(6)
# for i in range(4):
#     for j in range(4):
#         for k in range(6):
#             if src [i,j]==k:
#                 c[k] = c[k] + 1

# c

# # 시험문제
# # full은 임의의 숫자 가능
# im=np.full((500,500,3),255,dtype=np.uint8)

# c1=250
# c2=250
# r=120
# for row in range(500):
#     for column in range(500):
#         if (row-c1)**2 + (column-c2)**2 <=r**2:
#             im[row,column,0]=255
#             im[row,column,1]=255
#             im[row,column,0]=255
#         else:
#             im[row,column,0]=255
#             im[row,column,1]=255
#             im[row,column,1]=0
# # # line 선그리기
# color=(0,0,255)  
# start=(50,20)
# end=(200,20)    
# cv2.line(im,start,end,color,thickness=10)
# cv2.line(im,(50,100),(200,100),(0,255,0),thickness=3)

# 사각형 그리기
# color=(0,0,255)
# cv2.rectangle(im,(50,10),(200,50),color,thickness=-1)

# 원 그리기
# center=(125,110)
# radius=(30)
# cv2.circle(im,center,radius,(255,0,0),thickness=-1)

# 타원형 그리기
# center=(125,200)
# axes=(70,50)
# angle=0
# startangle=0
# endangle=360
# color=(255,255,0)

# cv2.ellipse(im,center,axes,angle,startangle,endangle,color,thickness=-1)

# 다각형 그리기
# points=np.array([[60,60],[100,10],[200,0],[150,100],[100,100]])
# points
# cv2.polylines(im,[points],True,thickness=-1)

# st.image(im)




#open cv는 R,B가 반전되있음
# im=cv2.imread('twins.jpg')
# rgb_img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
# gray_img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# # add=더하기
# add=cv2.add(gray_img,100)
# # subtract=빼기
# sub=cv2.subtract(gray_img,100)

# add1=gray_img+255
# sub1=gray_img-255

# col1, col2, col3 = st.columns(3)

# # with는 묶는다는 뜻
# with col1:
#     # st.header("original image")
#     st.image(gray_img)
#     # st.write('초기사진')

# with col2:
#     # st.header("bgr2rgb")
#     st.image(add)
#     # st.image(add1)
#     # st.write('컬러사진')

# with col3:
#     # st.header("gray_image")
#     st.image(sub)
    # st.image(sub1)
    # st.write('흑백사진')




# im_bgr=im
# im_bgr[:,:,0]=im[:,:,2]
# im_bgr[:,:,2]=im[:,:,0]

# st.image(im)
# st.image(rgb_img)
# st.image(gray_img)


# im=cv2.imread('cameraman.jpg')
# im1=im+200
# im1[:,:,1]   

# st.image(im)
# st.image(im1)




# 영상타입,픽셀크기,3차원,정수int8비트
# im=np.zeros((50,310,3),np.uint8)

# im[:,0:64]=0
# im[:,64:128]=64
# im[:,128:192]=128
# im[:,192:256]=192
# im[:,256:310]=255



# : 은 0에서255까지 쓰겠다는 표시
# im[:,:,:]=[0,0,0]  
# im[50:60,150:250,1]=255

# im[50:150,240:250,1]=255

# im[50:150,150:160,1]=255

# im[150:160,150:250,1]=255

# st.image(im)


#  matplotlib사용하기위한 코딩
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()

# # 그릴데이터 생성
# x=np.arange(0,10,0.1)
# y=np.sin(x)
# yc=np.cos(x)
# # 데이터 시각화
# plt.plot(x,y,marker='^',color='k',linestyle='--',label='sin')
# # 밑에거로 축약해서 사용가능
# plt.plot(x,y,'^k--',label='sin')
# plt.plot(x,yc,marker='o',color='r',linestyle='-',label='cos')
# ax.set_xlabel('xxxxxx')
# ax.set_ylabel('yyyyyy')
# ax.set_title('a')
# ax.legend(loc='lower left')
# st.pyplot(fig)



# t=turtle.Turtle()

# color_list=['yellow','blue','red','orange','green','purple','black','magenta']
# color_list=color_list*5
# t.pendown()
# t.width(5)

# n=20
# ang= 360/n
# for i in range(n):
#     col = color_list[i]
#     t.color(col)
#     for j in range(n):
#         t.right(ang)
#         t.forward(100)
        
#     t.left(ang)

# turtle.done()

# t=turtle.Turtle()
# t.shape('turtle')

# def f(x,opt):
#     if opt =='sin':
#         y= 100*np.sin(x/20)
#     if opt =='cos': 
#         y= 100*np.sin(x/20)
#         return y

# t.width(2)
# t.color('black')

# s=300
# t.goto(s,0)
# t.goto(0,0)
# t.goto(0,s)
# t.goto(0,0)

# t.width(5)
# t.color('blue')
# for x in range(s):
#     t.goto(x, f(x, 'sin'))

# t.penup()
# t.goto(0,100)
# t.pendown()

# # t.width(5)
# t.color('red')
# for x in range(s):
#     t.width(5)
#     t.goto(x,f(x,'sin'))

# turtle.done()


