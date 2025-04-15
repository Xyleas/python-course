import cv2

def display_image(image):
    cv2.imshow("Grey Scale Images", image)
    cv2.waitKey(0)

def feature_detection_and_matching(image1_path, image2_path):

    # Load the image
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert to greyscale
    grey1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GREY)
    grey2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GREY)

    # display_image(grey1)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    keypoints1, descriptors1, = sift.detectAndCompute(grey1, None)
    keypoints2, descriptors2, = sift.detectAndCompute(grey2, None)

    # Use BFMatcher to match descriptors
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    # Apply Lowe's ratio test to filter out weak matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            # Wrap into a list
            good_matches.append([m])

    # Draw matches
    matched_image = cv2.drawMatchesKnn(image1, keypoints1, image2, keypoints2, good_matches, None, flags=2)

    return matched_image

image1_path = "images/tea-cup.jpeg"
image2_path = "images/tea-cup-2.jpeg" 

matched_image = feature_detection_and_matching(image1_path, image2_path)

display_image(matched_image)