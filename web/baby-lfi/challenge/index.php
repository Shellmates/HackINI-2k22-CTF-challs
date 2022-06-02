<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="main.css" />
    <title>Say Hello to our Gentelmen | LFI Warmups</title>
</head>
<body>
<br /><br />
    <div class="container">
        <h1 id="h1">LFI Warmups</h1>
        <hr />
        <h2 id="challenge">Hello I can speak 2 languages !</h2>
        <hr />
        <u><b>Rules</b></u>
        <ul>
        <li>include some critical file <code> why not /etc/passwd</code></li>
        </ul>
        <hr />
        <u><b>Challenge</b></u>
        <pre>Please Select a language of your choice : en/fr </pre>
        <p><b>HINT :</b> use the <code>language parameter </code> :)</p>
        <hr />
        <p>
            <?php
                error_reporting(0);
                ini_set('display_errors', 0);
                if (isset($_GET['language'])) {
                    echo "<u><b>Look Here !!!</b></u> <br />" ;

                    if ($_GET['language'] == "en"){
                        # include a file in place of the text !
                        include("en.php");   
                    }
                    elseif ($_GET['language'] == "fr"){
                        # include a file in place of the text !
                        include("fr.php");
                    }
                    else {
                        if ($_GET['language'] == "../../../etc/passwd"){
                            echo "&#127881; Hooray you made it ! &#127881;";
                            echo "<br />";

                        }  
                        include($_GET['language']);
                    }
                    
                }

            ?>
        </p>
    </div>
</body>
</html>