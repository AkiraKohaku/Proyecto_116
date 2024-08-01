import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercurio",
            (115,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Tierra",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Marte",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (580,390),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturno",
            (780,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Urano",
            (975,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptuno",
            (1110,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("Output",img)
cv2.waitKey(0)
