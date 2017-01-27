import sublime, sublime_plugin, re
from os.path import basename, splitext

class IndentUnifaMlsCommand(sublime_plugin.TextCommand):

   def run(self, edit):
      view = self.view
      regions = view.sel()

      # if there are more than 1 region or region one and it's not empty
      if len(regions) > 1 or not regions[0].empty():
         for region in view.sel():
            if not region.empty():
               s = view.substr(region)
               s = re.sub('(((?<=\n)|(^))\ {6})', '', s)     # remove leading 6 spaces
               s = s.replace('\n', '')                       # remove newlines
               s = re.sub('(?<=[\(\[\{\)\]\}\,])\s+', '', s) # remove all whitespace between elements
               s = self.indent(s)                            # finally indent
               view.replace(edit, region, s)
      # else format all text
      else:
         alltextreg = sublime.Region(0, view.size())
         s = view.substr(alltextreg)
         s = re.sub('(((?<=\n)|(^))\ {6})', '', s)     # remove leading 6 spaces
         s = s.replace('\n', '')                       # remove newlines
         s = re.sub('(?<=[\(\[\{\)\]\}\,])\s+', '', s) # remove all whitespace between elements
         s = self.indent(s)                            # finally indent
         view.replace(edit, alltextreg, s)


   def indent(self, s):
      string = ""
      counter = 0

      for i, c in enumerate(s):
         string += c
         cMin = ""
         if i < len(s)-1:
            cPlus = s[i+1]
         if i > 1:
            cMin = s[i-1]

         if c == "{" and cPlus == "}":
            pass
         elif cMin == "{" and c == "}":
            pass
         else:
            if c == "{" or c == "(" or c == "[":
               counter += 1
            if c == "}" or c == ")" or c == "]":
               counter -= 1
            if c == "(" or c == ")" or c == "{" or c == "}" or c == ",":
               string += "\n"
               string += self.getIndentation(counter)

      return string


   def is_enabled(self):
      return True


   def getIndentation(self, total):
      tabSize, useSpaces = self.getIndentationSettings()
      string = ""
      if useSpaces:
         i = 0
         while (i < total * tabSize):
            string += " "
            i += 1
      else:
         i = 0
         while (i < total):
            string += "\t"
            i += 1

      return string


   def getIndentationSettings(self):
      global settings
      settings = sublime.load_settings('Preferences.sublime-settings')
      return [
         settings.get('tab_size', 3),
         settings.get('translate_tabs_to_spaces', True)
      ]
