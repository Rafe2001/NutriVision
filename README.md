# NutriVision

NutriVision is a web application that helps users analyze food items from images and calculate their nutritional content. The application provides details of each food item, including calorie intake, macronutrient breakdown, and whether the food is considered healthy based on nutritional guidelines.

## Features

- **Image Upload**: Users can upload images of food items to the application.
- **Nutritional Analysis**: NutriVision analyzes the uploaded images and provides details of each food item, including calorie intake and macronutrient breakdown.
- **Health Assessment**: The application assesses the nutritional content of food items and provides information on whether the food is considered healthy based on predefined nutritional guidelines.
- **User-Friendly Interface**: NutriVision offers a simple and intuitive interface for users to interact with the application.

## Technologies Used

- **Python**: Flask framework for building the backend API.
- **HTML/CSS**: Frontend design and layout.
- **Google Gemini**: Utilizing the google gemini-pro-vision for generating the response from image.
- **PIL (Python Imaging Library)**: Processing images uploaded by users.

## Usage

1. **Upload Image**: Choose an image of a food item using the upload button.
2. **Analysis**: NutriVision will analyze the image and provide detailed nutritional information.
3. **Health Assessment**: Based on the nutritional content, NutriVision will assess whether the food item is healthy.

## Installation

To run NutriVision locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rafe2001/nutri-vision.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Contributing

Contributions are welcome! If you'd like to contribute to NutriVision, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
