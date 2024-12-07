import cv2

def analyze_progress_bar(image_path):
  """
  Analyzes a progress bar image and calculates the percentage of progress.

  Args:
    image_path: The path to the image file.

  Returns:
    The percentage of progress as a float.
  """
  # Load the image
  image = cv2.imread(image_path)

  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Assuming the progress bar is horizontal and has a distinct color 
  # (e.g., blue for filled, gray for unfilled), you might use thresholding 
  # to separate the bar from the background. You'll need to experiment 
  # with the threshold value to find what works best for your image.
  _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

  # Find the contours in the thresholded image
  contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Assuming the progress bar is the largest contour
  bar_contour = max(contours, key=cv2.contourArea)

  # Get the bounding rectangle of the bar
  x, y, w, h = cv2.boundingRect(bar_contour)

  # Count the number of filled (blue) pixels within the bar
  filled_pixels = cv2.countNonZero(thresholded[y:y+h, x:x+w]) 

  # Calculate the percentage
  total_pixels = w * h
  percentage = (filled_pixels / total_pixels) * 100

  return percentage

# Example usage:
image_path = 'D:\Downloads\\asdqw.png'  # Replace with the actual path
percentage = analyze_progress_bar(image_path)
print(f"Progress: {percentage:.2f}%")
