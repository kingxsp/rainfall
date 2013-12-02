import asyncio

from hurricane.web import Application, HTTPHandler


class HelloHandler(HTTPHandler):
    @asyncio.coroutine
    def handle(self, request):
        return self.render("Hello World!!")


app = Application({
    '/': HelloHandler(),
})
app.run()