# Automated 2D Spectacles Generation
Designing spectacles using image processing libraries subjected to real world measurements in 2D.
An image must be generated from real-world spectales properties like eye size, bridge width and temple length plus the style like round, and square. 
Your code which will be considered as final output, this can be done using any programming language and image processing library of your choice.

# Getting started

## Prequisites
* [Python](http://python.org)
* [OpenCV](#) 
* [Numpy](#)
* [Pillow](#)

## Installing
* install [Python](http://python.org)
* install [OpenCV](#) 
* install [Numpy](#)
* install [Pillow](#)
## Built with 
* [Python](http://python.org)
### Design Procedure
  * Expect input parameters like type of glass, bridge width & height, Temple holder width, height & color,
            	and color of the lens to design a 2D view of spectacles from the user.
           
            	(a): all measurements are in cms except color
            	(b): color should be in Hex code
            	(c): lens type can be round or rectangle only
            	(d): inputs must not exceed the given image bounds
              
  * sample inputs are

              Lens type: round
              Lens diameter: 1.75cm (a round lens must only have diameter)
              Bridge width: 0.61cm
              Bridge height: 0.22cm
              Temple holder height: 0.48cm
              Temple holder width: 0.18cm
              Frame color: blue
              Glass color: green

  * Given image is 256x512x4 dimension (h x w x ch).

  * Start the design from the exact center of the image, draw bridge's half left side and half right side
               from this center point.

  * Draw the frame of the lens on the left side and right side, attaching with the bridge.

  * Draw the glass in the frame with a close attachment to it. 

  * finally, draw a temple holder starting and attaching from the lens frame to the end 
               and the starting point of the image on both sides, respectively.

  * The desired design will be displayed as PNG image file like below.
   ![Output Image](https://github.com/sivanagaraju8/Automated-2D-Spectacles-Generation-/blob/master/final_2d_out.png)

  #### Note: input is given in cms, it had mutiplied with 100 while performing on image with pixels.
       	  Further details will be in code, in the form of comments.
          
# Authors
* #### Gamidi Siva Nagaraju - [(https://www.linkedin.com/in/siva-nagaraju/)](https://www.linkedin.com/in/siva-nagaraju/)
