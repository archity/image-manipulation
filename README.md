# Image Manipulation
Repository for documenting about some of the image manipulation techniques using Python and other open-source libraries.

## 1. Instance Segmentation and Object Detection

* Make use of [pixellib](https://github.com/ayoolaolafenwa/PixelLib) library
* Use of a Mask R-CNN model
    * trained on coco dataset
* Python script [here](./segment.py)
  
---

## 2. Basic Image Manipulation using Pillow

Some basic `PIL` functions for image processing

* Merge two images
* Add/subtract two images
* Convert to grayscale
* Convert to Black-and-White
* Colour Inversion
* Rotation
* Gaussian Blur
* Edge Detection

Python notebook with the above implemented operations can be accessed [here](./basic-image-pillow.ipynb).

---

## 3. OpenCV based Basic Stuff

### 3.1 [Basic image loading](./opencv-basic/1.image-loading.py)

### 3.2 [Extracting snippet of an image](./opencv-basic/2.image-basics.py)

| <img width="200" alt="" src="./opencv-basic/assets/dragon_compresed.jpg"> | <img width="200" alt="" src="./opencv-basic/assets/copy-paste-dragonhead.jpg"> |
|:-:|:-:|

### 3.3 [Webcam based video capture](./opencv-basic/3.camera-videocapture.py)

* Capturing webcam feed
* Multiply, manipulate and fit to grid

| <img width="200" alt="" src="./opencv-basic/assets/webcam-screencapture-4frames.png"> |
|:-:|

### 3.4 [Drawing and Writing on Image](./opencv-basic/4.shape-drawing.py)

* Drawing overlay shapes and text on a webcam feed
* Can be generalized to any image or video

| <img width="200" alt="" src="./opencv-basic/assets/webcam-screencapture-shape-text.png"> |
|:-:|

### 3.5 [Colour Detection and Masking](./opencv-basic/5.colour-detection.py)

* Creating a masking image to detect a certain range of colour
* Applying mask to the video frame/image using `bitwise_and`

| <img width="400" alt="" src="./opencv-basic/assets/mask-colour-detection.png"> |
|:-:|

### 3.6 [Corner Detection](./opencv-basic/6.corner-detection.py)

* Shi-Tomasi Corner Detector

| <img width="200" alt="" src="./opencv-basic/assets/corners_chessboard.png"> | <img width="200" alt="" src="./opencv-basic/assets/corners_dragon.png"> |
|:-:|:-:|

### 3.7 [Template Matching](./opencv-basic/7.template-matching.py)

#### Input:

* Base input image:

    | <img width="400" alt="" src="./opencv-basic/assets/smh_rhb_1024px.jpg"> |
    |:-:|

* Template image(s), aka images to detect:

    | <img width="100" alt="" src="./opencv-basic/assets/smh_rhb_car_blue.jpg"> | <img width="100" alt="" src="./opencv-basic/assets/smh_rhb_car_red.jpg"> |
    |:-:|:-:|

We can make use of one or several methods for performing the template matching. Available methods are:

```py
methods = [cv2.TM_CCOEFF,
            cv2.TM_CCOEFF_NORMED,
            cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED,
            cv2.TM_SQDIFF,
            cv2.TM_SQDIFF_NORMED]
```

#### Output:

*  Blue car

    | <img width="400" alt="" src="./opencv-basic/assets/blue_car_detect_compresesd.jpg"> |
    |:-:|

* Red car

    | <img width="400" alt="" src="./opencv-basic/assets/red_car_detect_compressed.jpg"> |
    |:-:|

### 3.8 [Face and Eye Detection](./opencv-basic/8.face-eye-detection.py)

*
*

## 4. Image Stitching

* A simple Python script to stitch all the images in a specific directory to create a final collage.

* Pillow library utilized for image reading/writing

* Images are stitched in alphabetical order, from left to right, top to bottom

* Preserves the quality, as it stitches the images as it is, without compressing

* Python script [here](./image-stitching.py)

* Output *snapshot*:

| <img width="400" alt="" src="./img/maisiewilliams_digitalart_collage_snapshot.jpg"> |
|:-:|
