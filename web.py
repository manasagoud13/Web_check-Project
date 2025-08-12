# Import the required libraries
import urllib.request
from tkinter import *
import tkinter as tk
# Create an instance of tkinter frame or windowdow
window=Tk()

# Set the size of the tkinter windowdow
window.geometry("700x350")
window.title("PythonGeeks")#give title to the window
head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))# a lable
head.pack(pady=20)
#fucntion to check
def check():
    web= (url.get())
    status_code = urllib.request.urlopen(web).getcode()
    website_is_up = status_code == 200
    if website_is_up==TRUE:
        Label(window, text="Website Available", font=('Calibri 15')).place(x=260,y=200)
    else:
        Label(window, text="Website Not Available", font=('Calibri 15')).place(x=260,y=200)

url=tk.StringVar()# url is of string type
Entry(window, textvariable=url).place(x=200,y=80,height=30,width=280)# enter a website url
#create a button
Button(window, text="Check",command=check).place(x=320,y=160)
window.mainloop()#main command




# In this article, we are going to create a simple python project to monitor whether a website is available or not. We will be making this project using urllib library and tkinter library. It is a mediocre-level project where we will learn a little about http codes. Let’s start with Python Website Connectivity Checker Project development.
# What is a Site Connectivity Checker?
# A site connectivity checker is an application that helps us to monitor whether a website is available or not. There are many times when we open a url and the site isn’t available. To avoid such troubles we can use a website connectivity checker. The user just needs to input the url and it will be checked and availability will be visible.
# Python Website Connectivity Checker Project Details
# The objective is to create a GUI based project which will have an input field where we have to enter the url. If the url is available “Available” will be displayed else “Not Available” will be displayed. To build this project we need a basic understanding of Python and Tkinter Module.
# Prerequisites
# To build this project we need to install the following libraries:
# 1. Tkinter Module – This module is for creating an easy GUI in Python. To install Tkinter, use the following command:
# pip install tk
# 2. Urllib Module – This module is used while working with URLs. To install urllib Module, use the following command:
# pip install urllib
# Download the Source Code.
# Before proceeding with the Python Website Connectivity Checker Project, click here to download the source code for this project: Python Websiteite Connectivity Project
# Steps to Create Python Website Connectivity Checker Project
# The following are the steps to create the site connectivity checker project-
# * 		Importing the required libraries.
# * 		Making the GUI.
# * 		Function to check the URL.
# Let’s look at the steps in detail.
# 1. Importing the Required Libraries:
# # Import the required libraries
# import urllib.request
# from tkinter import *
# import tkinter as tk
# a. Tkinter Module – Tkinter Module is for creating an easy GUI in python. We will be using built methods in this library.
# b. Urllib Library – Urllib library is used to do operations with urls in python. In this project, we will be using urllib.request to monitor what is the http code of the url.
# 2. Creating GUI for Python Website Connectivity Checker Project:
# window=Tk()
# * 		This command uses the Tk() method to create a GUI window named window.
# # Set the size of the tkinter window
# window.geometry("700x350")
# window.title("PythonGeeks")#give title to the window
# head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))# a label
# head.pack(pady=20)
# * 		Now that we have created a window, we will be specifying some attributes to it. To give a specific size to the window, we use the geometry() method. We give a title to the window using the title() method.
# * 		Now we want to add a heading to our window. For this we create a label named head using the Label() method. While using a Label() method, we can specify the text, font, background color, foreground color, etc. To display this Label on the window, we use the pack() method.
# Entry(window, textvariable=url).place(x=200,y=80,height=30,width=280)# enter a website url
# #create a button
# Button(window, text="Check",command=check).place(x=320,y=160)
# window.mainloop()#main command
# * 		Now we create a text area using the Entry() method in the tkinter library. This will be the area on the window where the user can put in the urls that are to be tested. Textvariable is an attribute that specifies that whatever input is given will be saved in a variable named url. To display this input area, we use the place() method. Inside a place method, x and y coordinates need to be specified.
# * 		We create a button using the Button() method. command=check ensures that when the button is clicked the check function is evoked. To place the button we use place() method and specify the x and y coordinates within.
# 3. Creating Check Function to check URL:
# url=tk.StringVar()# url is of string type
# * 		Whatever url is entered in the Entry field was saved in the variable url. Now we need to make sure that the url variable is String Type. StringVar() method helps you to manage strings and get its value when needed.
# def check():
# web= (url.get())
# status_code = urllib.request.urlopen(web).getcode()
# website_is_up = status_code == 200
# if website_is_up==TRUE:
# Label(window, text="Website Available", font=('Calibri 15')).place(x=260,y=200)
# else:
# Label(window, text="Website Not Available", font=('Calibri 15')).place(x=260,y=200)
# * 		We create a check() function which will perform a url checking for us. Whenever the button will be clicked this function will be evoked.
# * 		We create a variable named web. Using the get() method we extract the value of the url and save the value on the web.
# * 		Urllib.request helps us to use the urlopen which will open that url for us. Once the url is open we check the status code for that url by using the getcode() method. We saved this status code of the web in a variable status_code.
# * 		As we want to check if the website is working or not, we want the source code to be 200. (Status Code 200 means OK. It specifies that a website is working). Now we check if status_code is equal to 200 or not. A boolean value ( true or false ) is saved in a variable website_is_up.
# * 		Now using the if-else loop, we check if the website_is_up is true then we make a label to display “Website Available”. If it is false then we display a label “Website Not Available”.
# Hurray! We have successfully completed our project. Now let us have a look at the output.
