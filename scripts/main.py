# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:21:08 2020

@author: Fazlur Rahman
"""

from preprocessing import get_grayscale, get_binary, invert_area, draw_text, detect
from ROI_selection import detect_lines, get_ROI
import cv2 as cv

def main(display = True, print_text = True, write = True):
    filename = '../images/karbon.png'
    
    src = cv.imread(cv.samples.findFile(filename))
    
    horizontal, vertical = detect_lines(src, minLinLength=350, display=True, write = True)
    
    gray = get_grayscale(src)
    bw = get_binary(gray)
    cv.imshow("bw", bw)
    cv.imwrite("bw.png", bw)
    #bw = erode(bw, kernel_size=2)
    
    cv.waitKey(0)
    
    ## set counter for image indexing
    counter = 0
    
    ## set line index
    first_line_index = 1
    last_line_index = 5

    table_cells = {}
    
    ## read text
    print("Start detecting text...")
    for i in range(0, 45):
        for j in range(0, 5):

            left_line_index = j
            right_line_index = j+1
            top_line_index = i
            bottom_line_index = i+1
            
            cropped_image, (x,y,w,h) = get_ROI(bw, horizontal, vertical, left_line_index,
                         right_line_index, top_line_index, bottom_line_index)
            
            text = detect(cropped_image)
            table_cells[str(i) + ' ' + str(j)] = text


            if (display or write):
                    image_with_text = draw_text(src, x, y, w, h, text)
                    
            if (display):
                cv.imshow("detect", image_with_text)
                cv.waitKey(0)
                cv.destroyAllWindows()

            if (write):
                cv.imwrite("../Images/"+ str(counter) + ".png", image_with_text);
            
    
    print(table_cells)
    return 0
    
if __name__ == "__main__":
    main()