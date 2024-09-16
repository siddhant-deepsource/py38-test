import gettext
import locale


lang = locale.getdefaultlocale()[0]
trans = gettext.translation("qmm", localedir=None, languages=[lang], fallback=True)
trans.install()

print(_("hrray"))

builtinss = dir(__builtins__)
print('_' in builtinss)

print(__("hurray!"))
