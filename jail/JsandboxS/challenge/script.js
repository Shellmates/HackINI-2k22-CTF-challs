#!/usr/bin/env node
var fs = require('fs');

const black_list = "0123456789!\"#$%&'()*+-/;<>?@\\^|~\t\n\r\x0b\x0c "

function * func(){
    fs.readFile('./.passwd', 'utf8', function(err, data){
        console.log(data);
    });
}

const readline = require("readline");
const interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

interface.question(
    "Welcome to JsandboxS, I gave you a secret phone, you have use it to escape \n",
    function (input) {
        interface.close();
        if ( !black_list.split("").some(x => input.includes(x)) )
        {
            try 
            {
                eval(input)
            }
            catch(e)
            {
                    console.log('you can\'t break the walls :(')
            }
        }
        else
        {
            console.log('you still in jail...you can\'t escape like that')
        }
    }

);
