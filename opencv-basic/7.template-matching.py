import cv2


def template_matching(base_source, template_source):
    img = cv2.imread(f"assets/{base_source}.jpg")
    img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
    H, W = img.shape[0], img.shape[1]

    template = cv2.imread(f"assets/{template_source}.jpg")
    template = cv2.resize(template, (0, 0), fx=0.75, fy=0.75)
    h, w = template.shape[0], template.shape[1]

    # Some methods for performing the template matching
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    methods_str = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
                   "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"]

    # Perform template matching for all possible methods
    for index, method in enumerate(methods):
        img2 = img.copy()

        # Dimension of result: (W - w + 1, H - h + 1)
        # Basically sliding the template image over the base image
        result = cv2.matchTemplate(image=img2, templ=template, method=method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print(min_loc, max_loc)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottom_right = (location[0] + w, location[1] + h)

        # Draw a rectangle around the locations
        cv2.rectangle(img2, location, bottom_right, (0, 255, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        img2 = cv2.putText(img2, text=methods_str[index],
                           org=(int(W / 3), 40),
                           fontFace=font,
                           color=(0, 0, 0),
                           thickness=2,
                           lineType=cv2.LINE_AA,
                           fontScale=1)

        cv2.imshow(methods_str[index], img2)
        cv2.imwrite(f"assets/{template_source}_{methods_str[index]}.jpg", img2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    template_matching(base_source="smh_rhb_1024px", template_source="smh_rhb_car_red")
