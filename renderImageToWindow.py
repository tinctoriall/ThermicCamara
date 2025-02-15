import cv2
import numpy as np

# Get screen resolution dynamically
screen_width = cv2.getWindowImageRect("Temperature Visualization")[2] if cv2.getWindowImageRect(
    "Temperature Visualization") else 1920
screen_height = cv2.getWindowImageRect("Temperature Visualization")[3] if cv2.getWindowImageRect(
    "Temperature Visualization") else 1080


def generate_temperature_matrix():
    """Generate a random 100x100 matrix of temperature values (Replace with actual data)."""
    return np.random.uniform(20, 80, (100, 100))  # Simulated temperature range (20°C to 80°C)


def normalize_temperature(data):
    """Normalize temperature values to range 0-255 for grayscale mapping."""
    min_temp, max_temp = data.min(), data.max()
    normalized = 255 * (1 - (data - min_temp) / (max_temp - min_temp))  # Invert: white = low temp, black = high temp
    return normalized.astype(np.uint8)


def upscale_image(image, target_width, target_height):
    """Upscale the image smoothly to fit the screen."""
    return cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_CUBIC)


# Create window for display
cv2.namedWindow("Temperature Visualization", cv2.WINDOW_NORMAL)

while True:
    # Generate new temperature data
    temperature_data = generate_temperature_matrix()

    # Convert temperature matrix to grayscale image
    gray_image = normalize_temperature(temperature_data)

    # Upscale the image to screen resolution
    upscaled_image = upscale_image(gray_image, screen_width, screen_height)

    # Show the updated image
    cv2.imshow("Temperature Visualization", upscaled_image)

    # Wait for 1 second, exit if 'q' is pressed
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# Close the window when done
cv2.destroyAllWindows()
