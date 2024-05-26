import random
import math
import time



def neuralNetwork(speed,blob,to_food,i,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,b1,b2,b3,b4,b5,b6,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36):
    print("meow")
    h1=to_food.x*w1[i]+to_food.y*w2[i]+b1[i]
    h2=to_food.x*w3[i]+to_food.y*w4[i]+b2[i]
    h3=to_food.x*w5[i]+to_food.y*w6[i]+b3[i]
    h4=to_food.x*w7[i]+to_food.y*w8[i]+b4[i]
    h5=to_food.x*w9[i]+to_food.y*w10[i]+b5[i]
    h6=to_food.x*w11[i]+to_food.y*w12[i]+b6[i]

    if h1 < 0:
        h1=0
    if h2 < 0:
        h2=0
    if h3 < 0:
        h3=0
    if h4 < 0:
        h4=0
    if h5 < 0:
        h5=0
    if h6 < 0:
        h6=0

    lh1=h1*w13[i]+h2*w14[i]+h3*w15[i]+h4*w16[i]+h5*w17[i]+h6*w18[i]
    lh2=h1*w19[i]+h2*w20[i]+h3*w21[i]+h4*w22[i]+h5*w23[i]+h6*w24[i]
    lh3=h1*w25[i]+h2*w26[i]+h3*w27[i]+h4*w28[i]+h5*w29[i]+h6*w30[i]
    lh4=h1*w31[i]+h2*w32[i]+h3*w33[i]+h4*w34[i]+h5*w35[i]+h6*w36[i]
    print(blob[i])
    print(lh1,lh2,lh3,lh4)
    if lh1>lh2 and lh1>lh3 and lh1>lh4:
        print(i, "up")
        blob[i].y = blob[i].y - speed
        return blob[i]
    elif lh2>lh1 and lh2>lh3 and lh2>lh4:
        print(i, "down")
        blob[i].y = blob[i].y + speed
        return blob[i]
    elif lh3>lh2 and lh3>lh1 and lh3>lh4:
        print(i, "left")
        blob[i].x = blob[i].x + speed
        return blob[i]
    elif lh4>lh1 and lh4>lh3 and lh4>lh2:
        print(i, "right")
        blob[i].x = blob[i].x - speed
        return blob[i]
    elif lh1==lh2 and lh1==lh3 and lh1==lh4:
        print("stay")
        return blob[i]
