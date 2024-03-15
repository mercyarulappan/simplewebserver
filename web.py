from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>
Top Companies
</title>
</head>
 <table border="5" cellspacing="5"cellpadding="10"  height="100" width="800">
   <caption align="center"><strong>TOP COMPANIES IN REVENUE</strong></caption>
   <tr  align="center">
    <th>Rank</th>
    <th>Company</th>
    <th>Revenue</th>
    <th>FY</th>
    <th>Headquartus</th>
    <th>Market Cap</th>
    <th>Refs</th>
   </tr>
   <tr  align="center">
     <td>1</td>
     <td>Microsoft</td>
     <td>$86.8</td>
     <td>2014</td>
     <td>Redmond,Washington,USA</td>
     <td>$370.3</td>
     <td>[1][2]</td>
   </tr>
   <tr  align="center">
     <td>2</td>
     <td>Oracle</td>
     <td>$37.1</td>
     <td>2013</td>
     <td>Redwood City,CA,USA</td>
     <td>$79.4</td>
     <td>[3][4]</td>
   </tr>
   <tr  align="center">
     <td>3</td>
     <td>SAP</td>
     <td>$20.9</td>
     <td>2013</td>
     <td>Walldorf,Germany</td>
     <td>$35.5</td>
     <td>[5][6]</td>
   </tr>
   <tr  align="center">
     <td>4</td>
     <td>Symantec</td>
     <td>$6.8</td>
     <td>2013</td>
     <td>Mountain View,CA,USA</td>
     <td>$14</td>
     <td>[7][8]</td>
   </tr>
   <tr  align="center">
     <td>5</td>
     <td>VMware</td>
     <td>$5.2</td>
     <td>2013</td>
     <td>Palo Alto,CA,USA</td>
     <td>$41.03</td>
     <td>[9][10]</td>
   </tr>
   <tr  align="center">
     <td>6</td>
     <td>CA Technologies</td>
     <td>$4.7</td>
     <td>2013</td>
     <td>Islandia,NY,USA</td>
     <td>$11.6</td>
     <td>[11][12]</td>
   </tr>
   <tr  align="center">
     <td>7</td>
     <td>Adobe Systems</td>
     <td>$4.4</td>
     <td>2013</td>
     <td>San Jose,CA,USA</td>
     <td>$10.2</td>
     <td>[13][14]</td>
   </tr>
   <tr  align="center">
     <td>8</td>
     <td>Fiserve</td>
     <td>$4.5</td>
     <td>2013</td>
     <td>Brookfield,WI,USA</td>
     <td>$8.5</td>
     <td>[15][16]</td>
   </tr>
   <tr  align="center">
     <td>9</td>
     <td>Intuit</td>
     <td>$4.2</td>
     <td>2013</td>
     <td>Mountain View,CA,USA</td>
     <td>$5.1</td>
     <td>[17][18]</td>
   </tr>
   <tr  align="center">
     <td>10</td>
     <td>Amadeus IT Group</td>
     <td>$3.8</td>
     <td>2013</td>
     <td>Madrid,Spain</td>
     <td>$6.8</td>
     <td>[19][20]</td>
   </tr>
 </table>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()