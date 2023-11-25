This project is ment to work with THE LINKS,LINKS2,ELINKS Text browser,
In conjuction with the FABGL VGA32 ANSI Color Terminal.

You will have to setup one of the browsers above, I recommend ELINKS, on a Raspberry PI.

set terminal to max resolution 512x384,64 colors

set your telnet terminal 
LINES to 45-48
and 
COLUMNS to 80-83 
depending on your monitor.

When using any of the browsers above know they are extremely buggy
they can crash and start to generate a tmp file that will fill your
harddrive until system crash. I would isolate things.
 
for Elinks
i would setup a alias
alias elinks="elinks -no-connect -touch-files 1"

DO NOT use the bookmarks function in these browsers as it tends to make them go crazy.

here is my elinks.conf file which setups up the file associations.
you can use cat to output to the serial terminal
or use a small shell program:

#!/bin/bash
echo "$(<$1)"

that will pipe to the stdout.

the configuration file below sets the browser to automatically download and run cat which will send the escape codes to your terminal
i named the escape character files BMP because Elinks got confused with using VT file extensions.


------- configuration
## ELinks 0.13.GIT configuration file

## This is ELinks configuration file. You can edit it manually,
## if you wish so; this file is edited by ELinks when you save
## options through UI, however only option values will be altered
## and missing options will be added at the end of file; if option
## is not written in this file, but in some file included from it,
## it is NOT counted as missing. Note that all your formatting,
## own comments and so on will be kept as-is.
##
## Obviously, if you don't like what ELinks is going to do with
## this file, you can change it by altering the config.saving_style
## option. Come on, aren't we friendly guys after all?



##############################
# Automatically saved options
#

## config 
#  Configuration handling options.

  ## config.saving_style_w [0|1]
  #  This is internal option used when displaying a warning about obsolete
  #  config.saving_style. You shouldn't touch it.
  set config.saving_style_w = 1


## terminal 
#  Terminal options.

  ## terminal.vt100 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.vt100.colors <num>
    set terminal.vt100.colors = 2


## ui 
#  User interface options.

  ## ui.language <language>
  #  Language of user interface. 'System' means that the language will be
  #  extracted from the environment dynamically.
  set ui.language = "English"





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.xterm-color 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.xterm-color.m11_hack [0|1]
    set terminal.xterm-color.m11_hack = 1





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.vt100 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.vt100.m11_hack [0|1]
    set terminal.vt100.m11_hack = 1





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.xterm-color 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.xterm-color.type <num>
    set terminal.xterm-color.type = 1





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.vt100 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.vt100.utf_8_io [0|1]
    set terminal.vt100.utf_8_io = 0
    ## terminal.vt100.type <num>
    set terminal.vt100.type = 2





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.xterm-color 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.xterm-color.charset <codepage>
    set terminal.xterm-color.charset = "VISCII"





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.vt100 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.vt100.charset <codepage>
    set terminal.vt100.charset = "utf-8"
    ## terminal.vt100.underline [0|1]
    set terminal.vt100.underline = 1





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.xterm-color 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.xterm-color.italic [0|1]
    set terminal.xterm-color.italic = 1
    ## terminal.xterm-color.utf_8_io [0|1]
    set terminal.xterm-color.utf_8_io = 0





##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.extension 
  #  Extension <-> MIME type association.
 
    ## mime.extension.vt,VT,vT,Vt <str>
    #  MIME-type matching this file extension ('*' is used here in place of
    #  '.').
    
    set mime.extension.jpg="image/jpeg"
    set mime.extension.jpeg="image/jpeg"
    set mime.extension.png="image/png"
    set mime.extension.gif="image/gif"
    set mime.extension.bmp="image/bmp"
    set mime.extension.vt="image/vt"

    set mime.extension.vt="image/vt"

    set mime.handler.image_viewer.unix.ask = 0
    set mime.handler.image_viewer.unix-xwin.ask = 0

    set mime.handler.image_viewer.unix.block = 0
    set mime.handler.image_viewer.unix-xwin.block = 0

    set mime.handler.image_viewer.unix.program = "cat %"
    set mime.handler.image_viewer.unix-xwin.program = "cat %"
    
    
    set mime.type.image.jpg = "image_viewer"
    set mime.type.image.jpeg = "image_viewer"
    set mime.type.image.png = "image_viewer"
    set mime.type.image.gif = "image_viewer"
    set mime.type.image.bmp = "image_viewer"
    set mime.type.image.vt = "image_viewer"
    set mime.type.application.vt="image_viewer"


##############################
# Automatically saved options
#

## document 
#  Document options.

  ## document.cache 
  #  Cache options.

    ## document.cache.format 
    #  Format cache options.

      ## document.cache.format.size <num>
      #  Number of cached formatted pages. Do not get too generous here,
      #  'formatted' means that all the accompanying structures are kept in
      #  memory so that you get the cached document immediately, but these
      #  structures may take a lot - 2x the size of the HTML source is probably
      #  not unusual, but it can be even more if the document consists of a lot
      #  of short lines (padded right, if possible) and links and not much other
      #  markup. So if you set this to 256 and then you don't like your ELinks
      #  eating 90M, don't come complaining to us. ;-)
      #  
      #  Also note that the format cache itself is not counted to the memory
      #  cache size, but the HTML source of the formatted documents is always
      #  cached, even if it is over the memory cache size threshold. (Then of
      #  course no other documents can be cached.)
      set document.cache.format.size = 0







##############################
# Automatically saved options
#

## document 
#  Document options.

  ## document.cache 
  #  Cache options.

    ## document.cache.memory 
    #  Memory cache options.

      ## document.cache.memory.size <num>
      #  Memory cache size (in bytes).
      set document.cache.memory.size = 4k







##############################
# Automatically saved options
#

## document 
#  Document options.

  ## document.cache 
  #  Cache options.

    ## document.cache.revalidation_interval <num>
    #  Period in seconds that a cache entry is considered to be up-to-date. When
    #  a document is loaded and this interval has elapsed since the document was
    #  initially loaded or most recently revalidated with the server, the server
    #  will be checked in case there is a more up-to-date version of the
    #  document.
    #  
    #  A value of -1 disables automatic revalidation.
    set document.cache.revalidation_interval = -1






##############################
# Automatically saved options
#

## ui 
#  User interface options.

  ## ui.clock 
  #  Digital clock in the status bar.

    ## ui.clock.enable [0|1]
    #  Whether to display a digital clock in the status bar.
    set ui.clock.enable = 1






##############################
# Automatically saved options
#

## ui 
#  User interface options.

  ## ui.success_msgbox [0|1]
  #  When you pressed a [ Save ] button in some manager, this option will make
  #  sure that a box confirming success of the operation will pop up.
  set ui.success_msgbox = 0





##############################
# Automatically saved options
#

## terminal 
#  Terminal options.

  ## terminal.vt100 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.vt100.italic [0|1]
    set terminal.vt100.italic = 1





##############################
# Automatically saved options
#

## document 
#  Document options.

  ## document.download 
  #  Options regarding files downloading and handling.

    ## document.download.directory <str>
    #  Default download directory.
    set document.download.directory = "./"

    ## document.download.set_original_time [0|1]
    #  Set the timestamp of each downloaded file to the timestamp stored on the
    #  server.
    set document.download.set_original_time = 0

    ## document.download.overwrite <num>
    #  Prevent overwriting the local files:
    #  0 is files will silently be overwritten
    #  1 is add a suffix .{number} (for example '.1') to the name
    #  2 is ask the user
    set document.download.overwrite = 0


  ## document.history 
  #  History options.

    ## document.history.global 
    #  Global history options.

      ## document.history.global.enable [0|1]
      #  Enable global history ("history of all pages visited").
      set document.history.global.enable = 1







##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.handler 
  #  A file type handler is a set of information about how to use an external
  #  program to view a file. It is possible to refer to it for several MIME
  #  types -- e.g., you can define an 'image' handler to which
  #  mime.type.image.png, mime.type.image.jpeg, and so on will refer; or one
  #  might define a handler for a more specific type of file -- e.g., PDF files.
  #  Note you must define both a MIME handler and a MIME type association for it
  #  to work.

    ## mime.handler.application 

      ## mime.handler.application.unix 

        ## mime.handler.application.unix.ask [0|1]
        set mime.handler.application.unix.ask = 0
        ## mime.handler.application.unix.block [0|1]
        set mime.handler.application.unix.block = 0
        ## mime.handler.application.unix.program <str>
        set mime.handler.application.unix.program = "cat %"







##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.type 
  #  Handler <-> MIME type association. The first sub-tree is the MIME class
  #  while the second sub-tree is the MIME type (ie. image/gif handler will
  #  reside at mime.type.image.gif). Each MIME type option should contain
  #  (case-sensitive) name of the MIME handler (its properties are stored at
  #  mime.handler.<name>).

    ## mime.type.image 

      ## mime.type.image.vt <str>
      set mime.type.image.vt = "image_viewer"






##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.handler 
  #  A file type handler is a set of information about how to use an external
  #  program to view a file. It is possible to refer to it for several MIME
  #  types -- e.g., you can define an 'image' handler to which
  #  mime.type.image.png, mime.type.image.jpeg, and so on will refer; or one
  #  might define a handler for a more specific type of file -- e.g., PDF files.
  #  Note you must define both a MIME handler and a MIME type association for it
  #  to work.

    ## mime.handler.octet-stream 

      ## mime.handler.octet-stream.unix 

        ## mime.handler.octet-stream.unix.ask [0|1]
        set mime.handler.octet-stream.unix.ask = 0
        ## mime.handler.octet-stream.unix.block [0|1]
        set mime.handler.octet-stream.unix.block = 0
        ## mime.handler.octet-stream.unix.program <str>
        set mime.handler.octet-stream.unix.program = "cat %"



  ## mime.type 
  #  Handler <-> MIME type association. The first sub-tree is the MIME class
  #  while the second sub-tree is the MIME type (ie. image/gif handler will
  #  reside at mime.type.image.gif). Each MIME type option should contain
  #  (case-sensitive) name of the MIME handler (its properties are stored at
  #  mime.handler.<name>).

    ## mime.type.octet-stream 

      ## mime.type.octet-stream.vt <str>
      set mime.type.octet-stream.vt = "image_viewer"






##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.default_type <str>
  #  Document MIME-type to assume by default (when we are unable to guess it
  #  properly from known information about the document).
  set mime.default_type = "application/octet-stream"
         ## mime.handler.default_type.unix.ask [0|1]
        set mime.handler.default_type.unix.ask = 0
        ## mime.handler.default_type.unix.block [0|1]
        set mime.handler.default_type.unix.block = 0
        ## mime.handler.default_type.unix.program <str>
        set mime.handler.default_type.unix.program = "cat %"







##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.extension 
  #  Extension <-> MIME type association.

    ## mime.extension.VT <str>
    #  MIME-type matching this file extension ('*' is used here in place of
    #  '.').
    set mime.extension.VT = "image/VT"






##############################
# Automatically saved options
#

## mime 
#  MIME-related options (handlers of various MIME types).

  ## mime.type 
  #  Handler <-> MIME type association. The first sub-tree is the MIME class
  #  while the second sub-tree is the MIME type (ie. image/gif handler will
  #  reside at mime.type.image.gif). Each MIME type option should contain
  #  (case-sensitive) name of the MIME handler (its properties are stored at
  #  mime.handler.<name>).

    ## mime.type.image 

      ## mime.type.image.VT <str>
      set mime.type.image.VT = "image_viewer"




