import string
import random
import webapp2
import cgi
from google.appengine.ext import db


form = """
<form method="post">
    What URL would you like to shorten?
    <br><br>
    <label>
        Input URL
        <input type="text" name="url_in" value="%(url_in)s">
    </label>

    <div style="color: red">%(error)s</div>

    <br>
    <br>
    <input type="submit">
</form>
"""


## model for url db
class Url(db.Model):
    url_long = db.StringProperty(required=True)
    url_short = db.StringProperty(required=True)
    use_count = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


def escape_html(s):
    return cgi.escape(s, quote=True)


def add_http(url_long):
    if not (url_long.startswith('http://')):
        url_long = "http://" + url_long
    return url_long


def return_short_url(url_long):
    url_long = add_http(url_long)
    urldata = check_for_url_long(url_long)
    if not urldata:
        return make_url_short(url_long)
    else:
        return urldata


def pull_urldata_from_db(url_long='', url_short=''):
    if url_long:
        urldata = db.GqlQuery("SELECT * FROM Url WHERE url_long=:1 limit 1",
                              url_long).get()
        return urldata
    elif url_short:
        urldata = db.GqlQuery("SELECT * FROM Url WHERE url_short=:1 limit 1",
                              url_short).get()
        return urldata
    else:
        return


def add_url_to_db(url_long, url_short):
    Url(url_long=url_long, url_short=url_short, use_count=1).put()


def check_for_url_long(url_long):
    urldata = pull_urldata_from_db(url_long)
    if urldata:
        urldata.use_count = urldata.use_count + 1
        urldata.put()
        return urldata.url_short
    else:
        return


def check_for_url_short(url_short):
    urldata = pull_urldata_from_db(url_short)
    if not urldata:
        return True
    else:
        return False


def make_url_short(url_long):
    url_short = ''.join(random.choice(string.letters) for x in xrange(6))
    if check_for_url_short(url_short):
        add_url_to_db(url_long, url_short)
        return url_short
    else:
        make_url_short(url_long)


class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", url_in=""):
        self.response.out.write(form % {"error": error,
                                        "url_in": escape_html(url_in)})

    def get(self):
        self.write_form()

    def post(self):
        user_url_in = self.request.get('url_in')

        if user_url_in == '':
            self.write_form("Please enter a valid URL into the input box",
                            user_url_in)

        else:
            url_short = return_short_url(user_url_in)
            self.redirect('/done?' + url_short)


class URLHandler(webapp2.RequestHandler):
    def get(self):

        url_out = "http://localhost:9080/" + self.request.query_string
        self.response.out.write("Here is your shortened URL:  "
                                + url_out)


class Redirector(webapp2.RequestHandler):
    def get(self, url_in=''):
        urldata = pull_urldata_from_db(url_short=url_in)
        display_url = urldata.url_long

        if not display_url:
            self.error(404)
            return

        self.redirect(str(display_url))


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/done', URLHandler),
                               ('/(\w+)', Redirector)],
                              debug=True)
