# draw/__init__.py

import cv2
import numpy as np


def polygon(image, points, line_color=(0, 255, 0), fill_color=(0, 255, 0),
            line_thickness=3, line_opacity=0.8, fill_opacity=0.4):
    """
    Draw a polygon with different opacities for the outline and the fill on an image.

    Parameters:
    - image: The original image (NumPy array).
    - points: A list of points defining the polygon's vertices.
    - line_color: The color of the polygon outline (BGR tuple).
    - fill_color: The color of the polygon fill (BGR tuple).
    - line_thickness: The thickness of the polygon outline.
    - line_opacity: The opacity of the polygon outline (0.0 to 1.0).
    - fill_opacity: The opacity of the polygon fill (0.0 to 1.0).

    Returns:
    - The image with the polygon drawn with the specified opacities.
    """
    # Create two overlay images
    overlay_fill = image.copy()
    overlay_line = image.copy()

    # Convert points to the correct shape
    points = np.array(points, np.int32).reshape((-1, 1, 2))

    # Draw the filled polygon on the overlay_fill
    cv2.fillPoly(overlay_fill, [points], color=fill_color)

    # Draw the polygon outline on the overlay_line
    cv2.polylines(overlay_line, [points], isClosed=True, color=line_color, thickness=line_thickness)

    # Blend the filled polygon with the original image
    cv2.addWeighted(overlay_fill, fill_opacity, image, 1 - fill_opacity, 0, image)

    # Blend the polygon outline with the original image
    cv2.addWeighted(overlay_line, line_opacity, image, 1 - line_opacity, 0, image)

    return image


def rectangle(image, top_left, bottom_right, line_color=(0, 255, 0), fill_color=(0, 255, 0),
              line_thickness=3, line_opacity=0.8, fill_opacity=0.4):
    """
    Draw a rectangle with different opacities for the outline and the fill on an image.

    Parameters:
    - image: The original image (NumPy array).
    - top_left: The top-left corner of the rectangle (tuple of x, y).
    - bottom_right: The bottom-right corner of the rectangle (tuple of x, y).
    - line_color: The color of the rectangle outline (BGR tuple).
    - fill_color: The color of the rectangle fill (BGR tuple).
    - line_thickness: The thickness of the rectangle outline.
    - line_opacity: The opacity of the rectangle outline (0.0 to 1.0).
    - fill_opacity: The opacity of the rectangle fill (0.0 to 1.0).

    Returns:
    - The image with the rectangle drawn with the specified opacities.
    """
    # Create two overlay images
    overlay_fill = image.copy()
    overlay_line = image.copy()

    # Draw the filled rectangle on the overlay_fill
    cv2.rectangle(overlay_fill, top_left, bottom_right, color=fill_color, thickness=cv2.FILLED)

    # Draw the rectangle outline on the overlay_line
    cv2.rectangle(overlay_line, top_left, bottom_right, color=line_color, thickness=line_thickness)

    # Blend the filled rectangle with the original image
    cv2.addWeighted(overlay_fill, fill_opacity, image, 1 - fill_opacity, 0, image)

    # Blend the rectangle outline with the original image
    cv2.addWeighted(overlay_line, line_opacity, image, 1 - line_opacity, 0, image)

    return image


def line(image, start_point, end_point, line_color=(0, 255, 0),
         line_thickness=3, line_opacity=0.8):
    """
    Draw a line with specified opacity on an image.

    Parameters:
    - image: The original image (NumPy array).
    - start_point: The starting point of the line (tuple of x, y).
    - end_point: The ending point of the line (tuple of x, y).
    - line_color: The color of the line (BGR tuple).
    - line_thickness: The thickness of the line.
    - line_opacity: The opacity of the line (0.0 to 1.0).

    Returns:
    - The image with the line drawn with the specified opacity.
    """
    # Create an overlay image
    overlay_line = image.copy()

    # Draw the line on the overlay
    cv2.line(overlay_line, start_point, end_point, color=line_color, thickness=line_thickness)

    # Blend the line with the original image
    cv2.addWeighted(overlay_line, line_opacity, image, 1 - line_opacity, 0, image)

    return image


def circle(image, center, radius, line_color=(0, 255, 0), fill_color=(0, 255, 0),
           line_thickness=3, line_opacity=0.8, fill_opacity=0.4):
    """
    Draw a circle with different opacities for the outline and the fill on an image.

    Parameters:
    - image: The original image (NumPy array).
    - center: The center of the circle (tuple of x, y).
    - radius: The radius of the circle.
    - line_color: The color of the circle outline (BGR tuple).
    - fill_color: The color of the circle fill (BGR tuple).
    - line_thickness: The thickness of the circle outline.
    - line_opacity: The opacity of the circle outline (0.0 to 1.0).
    - fill_opacity: The opacity of the circle fill (0.0 to 1.0).

    Returns:
    - The image with the circle drawn with the specified opacities.
    """
    # Create two overlay images
    overlay_fill = image.copy()
    overlay_line = image.copy()

    # Draw the filled circle on the overlay_fill
    cv2.circle(overlay_fill, center, radius, color=fill_color, thickness=cv2.FILLED)

    # Draw the circle outline on the overlay_line
    cv2.circle(overlay_line, center, radius, color=line_color, thickness=line_thickness)

    # Blend the filled circle with the original image
    cv2.addWeighted(overlay_fill, fill_opacity, image, 1 - fill_opacity, 0, image)

    # Blend the circle outline with the original image
    cv2.addWeighted(overlay_line, line_opacity, image, 1 - line_opacity, 0, image)

    return image


def text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1,
              text_color=(0, 255, 0), text_opacity=0.8, thickness=2, background_color=None, background_opacity=0.4):
    """
    Draw text with specified opacity on an image. Optionally, draw a background behind the text.

    Parameters:
    - image: The original image (NumPy array).
    - text: The text string to be drawn.
    - position: Bottom-left corner of the text string in the image (tuple of x, y).
    - font: Font type (default is cv2.FONT_HERSHEY_SIMPLEX).
    - font_scale: Font scale factor that is multiplied by the font-specific base size.
    - text_color: The color of the text (BGR tuple).
    - text_opacity: The opacity of the text (0.0 to 1.0).
    - thickness: Thickness of the text strokes.
    - background_color: Optional background color (BGR tuple) behind the text.
    - background_opacity: Opacity of the background color (0.0 to 1.0).

    Returns:
    - The image with the text drawn with the specified opacity.
    """
    # Create an overlay image for the text
    overlay_text = image.copy()

    # If a background color is specified, calculate the size of the text and draw the background rectangle
    if background_color is not None:
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
        text_w, text_h = text_size
        top_left = (position[0], position[1] - text_h)
        bottom_right = (position[0] + text_w, position[1])
        cv2.rectangle(overlay_text, top_left, bottom_right, background_color, thickness=cv2.FILLED)
        # Blend the background with the original image
        cv2.addWeighted(overlay_text, background_opacity, image, 1 - background_opacity, 0, image)

    # Draw the text on the overlay
    cv2.putText(overlay_text, text, position, font, font_scale, text_color, thickness, cv2.LINE_AA)

    # Blend the text with the original image
    cv2.addWeighted(overlay_text, text_opacity, image, 1 - text_opacity, 0, image)

    return image