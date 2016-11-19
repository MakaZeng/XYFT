import mechanize
import cookielib
import urllib2

def maka_simplegetcontent(url):
    try:
        wp = urllib2.urlopen(url)
        content = wp.read()
        return content
    except Exception,e:
        print Exception,":",e

def maka_getcontent(url):
    try:

        br = mechanize.Browser()

        # Cookie Jar

        cj = cookielib.LWPCookieJar()

        br.set_cookiejar(cj)

        # Browser options

        br.set_handle_equiv(True)

        br.set_handle_gzip(False)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?

        # br.set_debug_http(True)

        # br.set_debug_redirects(True)

        # br.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)

        br.addheaders = [('User-agent',
                          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        r = br.open(url)

        html = r.read()

        return html

    except Exception, e:

        print Exception, ":", e

        content = ""

        return content