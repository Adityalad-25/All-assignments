<?php
abstract class Shape {
    abstract public function calculateArea();
}

class Circle extends Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function calculateArea() {
        return pi() * $this->radius * $this->radius;
    }
}

class Square extends Shape {
    private $side;

    public function __construct($side) {
        $this->side = $side;
    }

    public function calculateArea() {
        return $this->side * $this->side;
    }
}

class Rectangle extends Shape {
    private $length;
    private $width;

    public function __construct($length, $width) {
        $this->length = $length;
        $this->width = $width;
    }

    public function calculateArea() {
        return $this->length * $this->width;
    }
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["shape"])) {
        $shapeType = $_POST["shape"];
        switch ($shapeType) {
            case "circle":
                $radius = 5; // Sample radius, you can get it from the form if needed
                $circle = new Circle($radius);
                $area = $circle->calculateArea();
                echo "The area of the circle is: $area";
                break;
            case "square":
                $side = 4; // Sample side length, you can get it from the form if needed
                $square = new Square($side);
                $area = $square->calculateArea();
                echo "The area of the square is: $area";
                break;
            case "rectangle":
                $length = 6; // Sample length, you can get it from the form if needed
                $width = 3; // Sample width, you can get it from the form if needed
                $rectangle = new Rectangle($length, $width);
                $area = $rectangle->calculateArea();
                echo "The area of the rectangle is: $area";
                break;
            default:
                echo "Invalid shape selected.";
        }
    } else {
        echo "No shape selected.";
    }
}
?>
