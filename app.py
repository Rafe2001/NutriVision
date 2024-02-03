from flask import Flask, render_template, request
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

def gemini_response(input_prompt, image):
    model = genai.GenerativeModel(model_name='gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text 

def input_image_setup(file_uploaded):
    if file_uploaded is not None:
        # Read the file into bytes
        bytes_data = file_uploaded.read()
        
        image_parts = [{"mime_type": file_uploaded.mimetype, "data": bytes_data}]
        
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        input_prompt = """
        As a nutrition expert, your task is to analyze the nutritional content of the food items captured in the image. 
        Please provide the following details for each food item:
        1. Item Name - Number of Calories
        2. Item Name - Number of Calories
        3. ...

        Additionally, assess whether the food is considered healthy based on its nutritional profile. 
        Provide insights on portion sizes, serving recommendations, and the overall nutritional value of the meal or snack.
        Evaluate the balance of essential nutrients and micronutrients in the food items, including carbohydrates, fats, proteins, fibers, sugars, vitamins, and minerals. 
        Offer suggestions for dietary modifications or healthier alternatives based on the nutritional analysis.
        Consider including information on allergens, dietary restrictions, or special considerations for specific dietary patterns (e.g., vegan, gluten-free, low-carb).

        Encourage users to make informed food choices by understanding the nutritional content of their meals and the potential impact 
        on energy levels, weight management, and overall health and well-being.
"""
        image_data = input_image_setup(uploaded_file)
        response = gemini_response(input_prompt, image_data)                                                                                                    
        return render_template('result.html', response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
