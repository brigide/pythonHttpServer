def displayPage():

    return '''<html>
    <body>

    <h2>Create contact</h2>

    <form action="/contacts" method="post">
        
        <label for="name">First name:</label><br>
        <input name="name" type="text" id="name" class="form-control" placeholder="John Watson"><br><br>

        <label for="address">Address:</label><br>
        <input name="address" type="text" id="address" class="form-control" placeholder="221B Baker Street"><br><br>

        <label for="phone">Phone:</label><br>
        <input name="phone" type="text" id="phone" class="form-control" placeholder="12345-6789"><br><br>

        <button id="button_create" class="float-left submit-button" >Submit</button>

    </form> 

    <p>Press submit to create a contact.</p>

    </body>
    <script type="text/javascript">
            document.getElementById("button_create").onclick = function () {{location.href = "contacts";}};
    </script>
    </html>'''
