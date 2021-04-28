def displayPage(contact):
    print(contact)
    return (f"""
            <html>
                <head>
                    <title>Contatos</title>
                </head>
                <body>
                    <button id="button_create" class="float-left submit-button" >Create new contact</button>
                    <button id="button_delete" class="float-left submit-button" >Delete contact</button>
                    <p> {contact} <p>
                </body>
            </html>
            <script type="text/javascript">
            document.getElementById("button_create").onclick = function () {{location.href = "error";}};
            document.getElementById("button_delete").onclick = function () {{location.href = "error";}};
            </script>
        """)