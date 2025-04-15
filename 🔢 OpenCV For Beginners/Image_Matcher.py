import cv2
import os

def display_image(image):
    cv2.imshow("Grey Scale Images", image)
    cv2.waitKey(0)

def feature_detection_and_matching(image1_path):

    # Load the image
    image1 = cv2.imread(image1_path)

    # Select the ROI (Regoin Of Interest) by drawing a bounding box
    roi = cv2.selectROI("Select ROI Tea-Cup", image1, False, False)

    # Crop the selected ROI from the image
    x,y,w,h = roi
    cropped = image1[y:y+h, x:x+w]
    
    # Convert to greyscale
    grey1 = cv2.cvtColor(cropped, cv2.COLOR_BGR2GREY)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    _, descriptors1, = sift.detectAndCompute(grey1, None)

    # Draw matches
    # matched_image = cv2.drawMatchesKnn(image1, keypoints1, image2, keypoints2, good_matches, None, flags=2)

    return descriptors1

def feature_matching(image):

    # Convert target image to grayscale
    grey_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    _, descriptors2, = sift.detectAndCompute(grey_image2, None)

    # Use BFMatcher to match descriptors
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    # Apply Lowe's ratio test to filter out weak matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            # Wrap into a list
            good_matches.append([m])

    # Define a minimal number of good matches
    MIN_MATCH_COUNT = 7

    return len(good_matches) >= MIN_MATCH_COUNT

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if filepath.lower().endswith(('.jpg', '.jpeg', '.png')):

            # If true, read the image
            image = cv2.imread(filepath)

            # Check if current image matches the template image
            is_match = feature_matching(image)

            # Write the result on the image
            result_text = "Match found" if is_match else "No match"
            cv2.putText(image, result_text, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

            # Show the image
            display_image(image)

image1_path = "images/tea-cup.jpeg"
folder_path = "images" 

descriptors1 = feature_detection_and_matching(image1_path)

display_image(matched_image)

process_folder(folder_path)