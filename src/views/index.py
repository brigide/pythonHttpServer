def displayPage():
    return ("""
    <html>
    <head>
        <title>AAAA</title>
    </head>
    <body>
        <form method="POST" action="/test">
            <label>Name:</label>
            <input type="text" id="name" name="name" /><br />
        
            <label>Email:</label>
            <input type="text" id="email" name="email" /><br />
        

            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """)

