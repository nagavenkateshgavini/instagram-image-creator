f = open('helloworld.html','wb')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
<h1>{}</h1>
</html>""".format("hai")

f.write(message)
f.close()
