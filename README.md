# Image Search By an Artistic Style

This Streamlit web application allows users to search for images based on their artistic style. The primary use case for this application is for an eCommerce website that enables users to find posters or images similar in terms of artistic style to a query image they upload.

## Features

- **Style Transfer Model:** The application uses a TensorFlow model for style transfer, which is based on the principles outlined in the paper "A Neural Algorithm of Artistic Style" by Gatys et al. [2].

- **Visualization:** Users can see a scatter plot of image embeddings in a 2D space, providing a visual representation of the similarity between images based on their artistic style.

- **Top Similar Images:** After selecting a query image, the application displays the top 5 images that are most similar in terms of artistic style to the selected image.

## How to Use

To run this Streamlit application, follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have the required dependencies installed, including TensorFlow, NumPy, OpenCV, Scikit-learn, and Streamlit. You can install them using pip or conda.

3. Download and prepare your image dataset. Make sure the images are located in a directory, and you have the file paths to the images.

4. Replace the `image_paths` variable with the file paths to your images in the code.

5. Run the Streamlit app by executing the following command in your terminal: `streamlit run your_app_name.py`

6. Access the Streamlit app in your web browser. You can interact with the application to search for images by artistic style.

## References

- TensorFlow Tutorial on Neural Style Transfer: [Link](https://www.tensorflow.org/tutorials/generative/style_transfer)

- Gatys, L., Ecker, A., Bethge, M. (2015). "A Neural Algorithm of Artistic Style." [Link to Paper](https://arxiv.org/abs/1508.06576)



