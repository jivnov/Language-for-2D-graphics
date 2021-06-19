# Language-for-2D-graphics

A language for creating 2D graphics using relational operations, implemented for Compilers course at AGH UST.

## Setup

To install TwoDim compiler run ```pip install -i https://test.pypi.org/simple/ Language-for-2D-graphics```.

## Usage
To compile file ```example.code``` and save output to ```example_output.svg``` run: 
```twodim example.code example_output.svg```
### How to write code ?
* __Viewport__: each program starts with a viewport clause, declaring the final image size. Example: ```#viewport 100 100;```
* __Declaring a shape__: ```rect A [10%, 50%] <255, 0, 0>;``` creates a red rectangle of width 10% and height 50% of the parent shape sizes (viewport or shape using a function). The numbers provided in square brackets are width and height, and the RGB color is typed in the angle brackets. If no color is provided, the shape will be black. Also you can omit zero values in the end of the color code (e.g. <255> stand for red, <255, 255> for yellow).
* __Relations between shapes__: there are the following types of relations available:
    * *left, right, top, bottom* - centering on shape at the chosen side of another shape(outside the object).
    * *atleft, atright, attop, atbottom* - sticking the shapes corresponding sides at the same line (e.g. ```A attop B``` means that A and B upper edge will be on the same line, so A will be inside B sticked to the top(provided A is smaller than B).)
  
* __Functions__: ```func Foo(rect Arg1, rect Arg2) { ... };``` Use functions to create and reuse complex shapes.
* __Assignmnent__: you can assign a function result to a *shape* variable calling ```shape S = Foo(Arg1, Arg2);```
* __Draw__: When finished creating your layout, call `draw S;` on the variable you want to start drawing from to export the image you created into svg file. Attention: calling draw on different objects might produce different output.

Functions' and variables' names should start with capital letter: ```func MyFunction1(), shape S, rect Banner```. End every line with a semicolon.

*Check the examples of correct code in example_code folder and get started!*
