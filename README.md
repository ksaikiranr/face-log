# Face-Log

## Introduction
The  objective  is  to  develop  an application which increases the security of mobile and laptops by adding facial authentication system.
 
The proposed system enhances the security of mobiles and laptops. In mobiles and laptops the login consists of either a pattern lock or alphanumeric string both of which can be exploited/forged easily.

The facial recognition process involves three steps:
* Training Data Gathering: Gather face data (face images in this case) of the users.
* Training of Recognizer: Feed that face data (and respective names of each face) to the face recognizer so that it can learn.
* Recognition: Feed new faces of the persons.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites
Python 3:
```
$ dnf install python3
```
Numpy and opencv modules:
```
$ dnf install numpy opencv*
```
### Running
```python3 faceRecWeb.py```
