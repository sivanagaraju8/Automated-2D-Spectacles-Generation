'''
--------------------------
@ Author: Gamidi Siva NAgaraju

--------------------------
'''
#!/usr/bin/python3

#import necessary Python modules
import numpy as np
import cv2
from PIL import Image
height =256 #height of the image
width = 512	#width of the image

print("**** Enter Details for 2D View of Spectacles (in cm)****")
lens= input("Enter type of lens (round/rectangle): ") 
if lens=="round":
	diameter=int(float(input("Enter diameter: "))*100)
elif lens=="rectangle":
	 len_height=int(float(input("Enter height of glass: ")))*100	#Lens height
	 len_width=int(float(input("Enter Width of glass: ")))*100		#Lens width
else:
	print("Error: please enter the availiable lens type")
	exit(0)

b_w=int(float(input("Enter bridge width: "))*100)		
b_h=int(float(input("Enter bridge height: "))	*100)	
t_h=int(float(input("Enter temple holder height : "))*100 -5) 
t_w=int(float(input("Enter temple holder width: "))*100)	
t=input("Enter frame color (prefer hex): ").lstrip('#')
l= input("Enter Lens color (prefer hex): ").lstrip('#')

t_color=tuple(int(t[i:i+2], 16) for i in (0, 2, 4))	#conversion of hex color to RGB
l_color=tuple(int(l[i:i+2], 16) for i in (0, 2, 4)) #conversion of hex color to RGB	
t_color=t_color[::-1]	#reversimg the color in BGR format
l_color=l_color[::-1]	#reversing the color in BGR format
#img1=cv2.imread("../specs.png",1)

img=np.ones((height,width,3),np.uint8)*255 #create an empty image 
if lens=='round':
	radius=int(diameter/2)		#radius of the glass
	centre=int(height/2)		#centre point of height 
	ref=centre-20				#some reference in height (Y)
	bcx1=(width//2)-(b_w//2)	#brdge X coordinate1
	bcx2=(width//2)+(b_w//2)	#brdge X coordinate2
	bcy1=ref-(b_h//2)-8			#brdge Y coordinate1
	bcy2=ref+(b_h//2)-8			#brdge Y coordinate2
	ecx1=bcx1-radius			#elipse1 X cordinate
	ecy1=centre-15				#elipse1 Y coordinate
	ecx2=bcx2+radius            #elipse2 X Coordinate 
	ecy2=centre-15				#elipse2 Y Coordinate 
	tempx1= ecx1-5-(radius+8)   #Left Temple holder coordiante's Distance
	tempx2= ecx2+5+(radius+8)   #Right Temple holder coordinate's Distance 

	temp1 = np.array([[[0,ref-int(t_h/2)],[tempx1,ref-int(t_h/2)-5],		# temple holder cordinates
	 			[tempx1,ref+int(t_h/2)+5],[0,ref+int(t_h/2)]]], np.int32) 

	temp2 = np.array([[[width-1,ref-int(t_h/2)],[tempx2,ref-int(t_h/2)-5], 	# temple holder cordinates
			[tempx2,ref+int(t_h/2)+5],[width-1,ref+int(t_h/2)]]], np.int32)

	img = cv2.fillPoly(img, [temp1], t_color)		#draw temple holder1
	img = cv2.fillPoly(img, [temp2], t_color)		#draw temple  holder2

	img = cv2.ellipse(img, (ecx1-10,ecy1), (radius+8,radius+4), #frame of the glass
	 40, 0, 360, t_color, 12) 
	img=cv2.circle(img,(ecx1-10,ecy1),radius+1,l_color,-1)  #glass

	img=cv2.rectangle(img,(bcx1-5,bcy1),(bcx2+5,bcy2),t_color,-1) #bridge

	img = cv2.ellipse(img, (ecx2+10,ecy1), (radius+8,radius+4), #frame of glass
	 -40, 0, 360, t_color, 12) 
	img=cv2.circle(img,(ecx2+10,ecy1),radius+1,l_color,-1)		#glass

	cv2.imwrite("final_2d_out.png",img)				#save image
else:

	centre=int(height/2) 		#centre point of height
	ref=centre-10		 		#some reference point
	bcx1=(width//2)-(b_w//2)	#bridge X cordinate1
	bcx2=(width//2)+(b_w//2)	#bridge X Coordinate2 
	bcy1=ref-(b_h//2)			#bridge Y Coordinate1
	bcy2=ref+(b_h//2)			#bridge Y Coordinate2 

	img=cv2.rectangle(img,(bcx1-5,bcy1-15),(bcx2+5,bcy2-15),t_color,-1) #bridge

	#left side glass with frame
	img=cv2.rectangle(img,(bcx1,bcy1-(len_height//2)),(bcx1-len_width,bcy1+(len_height//2)),l_color,-1)
	img=cv2.rectangle(img,(bcx1,bcy1-(len_height//2)),(bcx1-len_width-3,bcy1+(len_height//2)),t_color,5)

	#right side glass with frame
	img=cv2.rectangle(img,(bcx2,bcy1-(len_height//2)),(bcx2+len_width,bcy1+(len_height//2)),l_color,-1)
	img=cv2.rectangle(img,(bcx2,bcy1-(len_height//2)),(bcx2+len_width+3,bcy1+(len_height//2)),t_color,5)

	#Temple Holder parameters
	tempx1= bcx1-len_width
	tempx2= bcx2+len_width

	temp1 = np.array([[[0,ref-int(t_h/2-10)],[tempx1,ref-int(t_h/2)-15],	#left side Temple holder
	 			[tempx1,ref+int(t_h/2)-5],[0,ref+int(t_h/2-10)]]], np.int32)

	temp2 = np.array([[[width-1,ref-int(t_h/2-10)],[tempx2,ref-int(t_h/2)-15],	#right side temple holder
			[tempx2,ref+int(t_h/2)-5],[width-1,ref+int(t_h/2-10)]]], np.int32)

	img = cv2.fillPoly(img, [temp1], t_color)	#draw polygon of Left temp holder
	img = cv2.fillPoly(img, [temp2], t_color)	#deraw polygon of Right temp holder
	
	cv2.imwrite("final_2d_out.png",img)			#write/save final output image
	
img2 = Image.open('final_2d_out.png')			#open 3 channel  generated image to make 4 channels 
img2 = img2.convert("RGBA")						#RGBA coversion
datas = img2.getdata()							#get all info from converted image

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:	#adding alpha channel and
        newData.append((255, 255, 255, 0))						#making it transparent

    #reducing the alpha value of glass's color 
    elif item[0] ==l_color[2] and item[1]==l_color[1] and item[2]==l_color[0]:
    	newData.append((l_color[2],l_color[1],l_color[0],155))
    else:
        newData.append(item)
    #print(item)
img2.putdata(newData)
img2.save("final_2d_out.png", "PNG")	#save final 4 channeled PNG Image
img2.show()
