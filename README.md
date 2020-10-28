# Garbage Segregation

Waste Segregation means to group Waste into different Categories. Each waste goes into its category at the point of dumping or collection. Under the Waste Regulations 2011, you must segregate cardboard, glass, metal, paper, plastic, trash and at source unless it is technically or economically unfeasible. Under the same regulations, you should implement the waste hierarchy; reduce, reuse, recycle, other recovery and disposal.  By law, you should implement this hierarchy and segregation helps with recycling in particular. Waste segregation is included in law because it is much easier to recycle. Effective segregation of wastes means that less waste goes to landfill which makes it cheaper and better for people and the environment. It is important to segregate for public health.  In particular, hazardous wastes can cause long term health problems, so it is very important that they are disposed of correctly and safely and not mixed in with the normal waste coming out of your home or office.

## Objective:

In this project, we have tried to classify garbage under the same categories as provided by the Waste Regulations 2011:
<br>

<img src="visualize/cardboard15.jpg" height = "90" > <img src="visualize/glass6.jpg" height = "90" > <img src="visualize/metal21.jpg" height = "90" > <img src="visualize/paper10.jpg" height = "90" > <img src="visualize/plastic25.jpg" height = "90" > <img src="visualize/trash91.jpg" height = "90" >
<br>

- Cardboard 
- Glass  
- Metal 
- Paper 
- Plastic 
- Trash

## Steps Involved:

- Viewing classes in Directory

- Visualizing Images in Dataset from each class

- Data Configuration

- Data Preparation and Loading

    - Creating a Generator for Training Set
    - Creating a Generator for Testing Set
    
- Writing the labels into a text file 'Labels.txt 

- Model Architecture

- Model Compilation

- Training the Model (batch_size = 32, epochs = 10)

- Testing Predictions

- Saving model as 'model.h5'

- Deploying the Model as a Web Application using Streamlit

<hr>

## Steps for using the Web Application
- Setting up the Python Environment with the dependencies:

        pip install -r Requirements.txt

- Cloning the Repository: 

        git clone https://github.com/srijarkoroy/Garbage_Segregation.git
- Entering The directory: 

        cd Garbage_Segregation
- Running the Web App:

        streamlit run app.py
- Stopping the web app from the terminal:

        Ctrl+C

## Demonstration
<br>

Here's a Demo on how the Web Application works 
<br>
<br>

![](Deployment/GarbageDemo.gif)
