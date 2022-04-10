#GUI
from flexx import flx
from CIFA import lex

class UserInput(flx.Widget):

    def init(self):
        with flx.VBox():
            self.edit = flx.LineEdit(placeholder_text='Your name')
            flx.Widget(flex=1)

    @flx.reaction('edit.user_done')
    def update_user(self, *events):

        self.root.store.set_username(self.edit.text)
        l = lex()
        a = l.run(self.root.store.username)

class SomeInfoWidget(flx.Widget):

    def init(self):
        with flx.FormLayout():
            flx.Label(title='program:\n', text=lambda: self.root.store.username)
            flx.Widget(flex=1)

class Store(flx.JsComponent):

    username = flx.StringProp(settable=True)

class Example(flx.Widget):

    store = flx.ComponentProp()

    def init(self):

        # Create our store instance
        self._mutate_store(Store())

        # Imagine this being a large application with many sub-widgets,
        # and the UserInput and SomeInfoWidget being used somewhere inside it.
        with flx.HSplit():
            with flx.VBox(flex=1):
                UserInput(flex=1)
                SomeInfoWidget(flex=10)
            with flx.TabLayout(flex=3):
                SomeInfoWidget(title='LEX')
                flx.Widget(style='background:#eee;')


app = flx.App(Example)
app.launch('app')  # to run as a desktop app
# app.launch('browser')  # to open in the browser
flx.run()  # mainloop will exit when the app is closed