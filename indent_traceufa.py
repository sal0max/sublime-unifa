import sublime, sublime_plugin, re
from os.path import basename, splitext

class IndentUnifatraceCommand(sublime_plugin.TextCommand):

   def run(self, edit):
      view = self.view
      regions = view.sel()

      # if there are more than 1 region or region one and it's not empty
      if len(regions) > 1 or not regions[0].empty():
         for region in view.sel():
            if not region.empty():
               s = view.substr(region)
               s = self.indent(s)
               view.replace(edit, region, s)
      # format all text
      else:
         alltextreg = sublime.Region(0, view.size())
         s = view.substr(alltextreg).strip()
         s = self.indent(s)
         view.replace(edit, alltextreg, s)


   def indent(self, s):
        return re.sub(r"(?<=.{79}[^}])\n\ {6}", "", s)


   def is_enabled(self):
      """
      Enables or disables the 'indent' command. Command will be disabled if
      there are currently no text selections and current file is not 'traceufa'
      or 'Plain Text'. This helps clarify to the user about when the command can
      be executed, especially useful for UI controls.
      """
      if self.view is None:
         return False

      syntax = self.view.settings().get('syntax')
      language = splitext(basename(syntax))[0].lower() if syntax is not None else "plain text"
      return ((language == "traceufa") or (language == "plain text"))
