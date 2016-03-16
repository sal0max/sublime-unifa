# Sublime UNIFA
A collection of tools for [Sublime Text](http://www.sublimetext.com/) to ease working in the UNIFA Environment.

## Features

### Syntax highlighting for

* `trace.ufa` files
* `ufalistmsg` output
* `.bs2log` BS2000 access logs
* `.SQL.LOG` and `.SQL.WV.LOG` Maintain-DB logs

### Plugin: `trace.ufa`-indenter

`trace.ufa` files are hard-wrapped at 80 characters per line. The indenter removes those wraps without messing up pre-formatted blocks (like interface descriptions).

* It can be accessed
   * via the Command Palette and typing `UNIFA: Indent UNIFA-Trace`
   * or in the menu: `Selection > Format > Indent UNIFA-Trace`
* When no text is selected the entire file will get formatted.  
  If some text is selected, only that part will get indented.


## Screenshots
![Screenshot](https://raw.githubusercontent.com/msal/sublime-ufa/raw/screen02.png)


## Installation
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Install Package`
* Search for `UNIFA`


## License
**Copyright 2014-2016 MSal.**

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
