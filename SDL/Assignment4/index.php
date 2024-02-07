<?php
session_start();

// Initialize array to store product names
if (!isset($_SESSION['products'])) {
    $_SESSION['products'] = array();
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve product name from form
    $productName = $_POST['product'];

    // Check if product name is present in the array
    if (in_array($productName, $_SESSION['products'])) {
        $message = "Product is already present.";
    } else {
        // Add product to the array
        array_push($_SESSION['products'], $productName);
        $message = "Product added successfully.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Management</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Add or Check Product</h2>
        <form method="post" action="index.php">
            <input type="text" name="product" placeholder="Enter product name">
            <button type="submit" name="submit">Submit</button>
        </form>
        <?php if(isset($message)): ?>
            <p><?php echo $message; ?></p>
        <?php endif; ?>
    </div>
</body>
</html>
