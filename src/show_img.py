import matplotlib.pyplot as plt

def show(image):
    """
    show image in a fixed size
    
    Arg: 
        image: The read-in image using OpenCV
        
    """
    # Figure size in inches
    plt.figure(figsize=(9, 9))
    
    # Show image, with nearest neighbour interpolation
    plt.imshow(image, interpolation='nearest')