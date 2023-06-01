import webpage
class mainpage(webapp2.RequestHandler):
def get(self):
self.response.write("hello world")
app=webapp2.WSGIApplication([{'/',mainpage}],debug=true)
