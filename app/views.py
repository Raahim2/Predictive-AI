from django.shortcuts import render
from joblib import load
# from PIL import Image
# import tensorflow as tf
import numpy as np
# from tensorflow.keras.models import load_model


def index(request):
    return render(request,'index.html')


def HPP(request):
    if request.method == "POST":

        bhk = int(request.POST.get('bhk'))
        area = int(request.POST.get('area'))

        model = load("app/ML/mumbai.pkl")
        white = model.predict([[bhk,area]])[0]
        black=white/2
        total=black+white

        total=int(total/10000)
        total=total*10000

        if(total<10000000):
            total=total/100000
            total=round(total,2)
            new=f"{total}L"
        else:
            total=total/10000000
            total=round(total,2)
            new=f"{total}Cr"

        return render(request, 'HPP.html', {'predicted_price': new})

    return render(request, 'HPP.html')

def CR(request):
    if request.method == "POST":

        cources = int(request.POST.get('cources'))
        lowest = int(request.POST.get('lp'))
        highest = int(request.POST.get('hp'))
        area = int(request.POST.get('area'))
        fees = int(request.POST.get('fees'))
        placement = int(request.POST.get('placement'))
        avg = (highest+lowest)/2

    

        model = load("app/ML/CR.pkl")
        rating = model.predict([[cources , lowest , highest , fees , avg , area , placement]])[0]

        return render(request, 'CR.html', {'predicted_price': round(rating,1)})

    return render(request, 'CR.html')


def FPP(request):
    if request.method == "POST":

        time = int(request.POST.get('time'))
        time=time*60
        distance = int(request.POST.get('dist'))
        passengers = int(request.POST.get('num'))

        model = load("app//ML/FPP.pkl")
        fair = model.predict([[time , distance , passengers , 0]])[0]

        return render(request, 'FPP.html', {'predicted_price': fair })

    return render(request, 'FPP.html')



    
#Function HDC and PCD uses tensorflow that could not be imported in vercel for time being code is commented out
    
# def HDC(request):
#     if request.method == 'POST':
#         uploaded_image = request.FILES['image']
#         if uploaded_image:
            
#             model = load_model("app/ML/HDC.h5")

#             image = Image.open(uploaded_image)
#             image_array = np.array(image)
#             if(image_array.ndim==2):
#                 image_array = tf.image.grayscale_to_rgb(tf.expand_dims(image_array, axis=-1))
            
#             prediction = model.predict(tf.expand_dims(image_array, axis=0))

#             prediction=np.argmax(prediction)

#         return render(request, 'HDC.html', {'predicted_price': prediction})

#     return render(request, 'HDC.html')

def HDC(request):
    return render(request, 'HDC.html', {'predicted_price': 7})

    
# def PDC(request):
#     CLASSES=["Healthy","Powdery","Rust"]
#     if request.method == 'POST':
#         uploaded_image = request.FILES['image']
#         if uploaded_image:
            
#             model = load_model("app/ML/PDC.h5")

#             image = Image.open(uploaded_image)
#             image_array = np.array(image)

#             image_array.resize(256,256)

#             if(image_array.ndim==2):
#                 image_array = tf.image.grayscale_to_rgb(tf.expand_dims(image_array, axis=-1))
            
#             prediction = model.predict(tf.expand_dims(image_array, axis=0))

#             prediction=np.argmax(prediction)

#         return render(request, 'PDC.html', {'predicted_price': CLASSES[prediction]})

#     return render(request, 'PDC.html')

def PDC(request):
    return render(request, 'PDC.html', {'predicted_price':"Healthy"})
