#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(textarea_content):
    head = """
    <head>
<style>
body {
    background-color: linen;
}

h2 {
    color: maroon;
    font-size: 42px;
    text-align: center;
} 
label {
    display: block;
    text-align: center;
    font-size: 26px;
    color: maroon;
    font-weight: bold;
}
input {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
textarea {
    display: block;
    width: 400;
    height: 200;
    margin-left: auto;
    margin-right: auto;
    font-size:26px;
}
#rot {
    text-align: center;
    width: 80px;
    height: 40px;
    font-size: 26px;
}
#sub {
    width: 80px;
    height: 40px;
    font-size: 16px;
}
</style>
</head>"""

    foot = "</body></html>"
    rot_label = "<label>Rotate:</label>"
    rotation_input = "<input type='number' min='0' max='25' id='rot' name='rotation' value='0'/>"
    message_label ="<label>Enter a message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    submit = "<input type='submit' id='sub' value='Encrypt'/>"
    form = "<form method='post'>" + rot_label + rotation_input + "<br>" + message_label + textarea + "<br>" + submit + "</form>"
    header = head + "<h2>Web Caesar</h2>"
    return header + form + foot
	
class MainHandler(webapp2.RequestHandler):

    def get(self):
	content = build_page("")
        self.response.write(content)	

    def post(self):
        message = self.request.get("message")
        message = str(message)
        rotation = self.request.get("rotation")
        if rotation == "":
            rotation = 0
        rotation = int(rotation)
        encrypted_message = caesar.encrypt(message,rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        self.response.write(content)
    	
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
