def displayPage():

    return '''<html>
    <body>

    <h2>HTML Forms</h2>

    <form action="/contacts method="post">
    <label for="name">First name:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="phone">Phone:</label><br>
    <input type="text" id="phone" name="phone"><br><br>
    <label for="address">Address:</label><br>
    <input type="text" id="address" name="address"><br><br>
    <input type="submit" value="Submit">
    </form> 

    <p>Press submit to create user"/action_page.php".</p>

    </body>
    <script>

    var nameValue = document.getElementById("name").value;
    var phoneValue = document.getElementById("phone").value;
    var addressValue = document.getElementById("address").value;

    </script>
    </html>'''
