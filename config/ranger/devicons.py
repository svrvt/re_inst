#!/usr/bin/python
# coding=UTF-8
import re;
import os;

file_node_extensions = {
    '7z'       : '',
    'ai'       : '',
    'apk'      : '',
    'avi'      : '',
    'bat'      : '',
    'bmp'      : '',
    'bz2'      : '',
    'c'        : '',
    'c++'      : '',
    'cab'      : '',
    'cc'       : '',
    'clj'      : '',
    'cljc'     : '',
    'cljs'     : '',
    'coffee'   : '',
    'conf'     : '',
    'cp'       : '',
    'cpio'     : '',
    'cpp'      : '',
    'css'      : '',
    'cxx'      : '',
    'd'        : '',
    'dart'     : '',
    'db'       : '',
    'deb'      : '',
    'diff'     : '',
    'dump'     : '',
    'edn'      : '',
    'ejs'      : '',
    'epub'     : '',
    'erl'      : '',
    'f#'       : '',
    'fish'     : '',
    'flac'     : '',
    'flv'      : '',
    'fs'       : '',
    'fsi'      : '',
    'fsscript' : '',
    'fsx'      : '',
    'gem'      : '',
    'gif'      : '',
    'go'       : '',
    'gz'       : '',
    'gzip'     : '',
    'hbs'      : '',
    'hrl'      : '',
    'hs'       : '',
    'htm'      : '',
    'html'     : '',
    'ico'      : '',
    'ini'      : '',
    'java'     : '',
    'jl'       : '',
    'jpeg'     : '',
    'jpg'      : '',
    'js'       : '',
    'json'     : '',
    'jsx'      : '',
    'less'     : '',
    'lha'      : '',
    'lhs'      : '',
    'log'      : '',
    'lua'      : '',
    'lzh'      : '',
    'lzma'     : '',
    'markdown' : '',
    'md'       : '',
    'mkv'      : '',
    'ml'       : 'λ',
    'mli'      : 'λ',
    'mov'      : '',
    'mp3'      : '',
    'mp4'      : '',
    'mpeg'     : '',
    'mpg'      : '',
    'mustache' : '',
    'ogg'      : '',
    'pdf'      : '',
    'php'      : '',
    'pl'       : '',
    'pm'       : '',
    'png'      : '',
    'psb'      : '',
    'psd'      : '',
    'py'       : '',
    'pyc'      : '',
    'pyd'      : '',
    'pyo'      : '',
    'rar'      : '',
    'rb'       : '',
    'rc'       : '',
    'rlib'     : '',
    'rpm'      : '',
    'rs'       : '',
    'rss'      : '',
    'scala'    : '',
    'scss'     : '',
    'sh'       : '',
    'slim'     : '',
    'sln'      : '',
    'sql'      : '',
    'styl'     : '',
    'suo'      : '',
    't'        : '',
    'tar'      : '',
    'tgz'      : '',
    'ts'       : '',
    'twig'     : '',
    'vim'      : '',
    'vimrc'    : '',
    'wav'      : '',
    'xml'      : '',
    'xul'      : '',
    'xz'       : '',
    'yml'      : '',
    'zip'      : '',
}

dir_node_exact_matches = {
# English
    '.git'                             : '',
    'Desktop'                          : '',
    'Documents'                        : '',
    'Downloads'                        : '',
    'Dropbox'                          : '',
    'Music'                            : '',
    'Pictures'                         : '',
    'Public'                           : '',
    'Templates'                        : '',
    'Videos'                           : '',
# French
    'Bureau'                           : '',
    'Documents'                        : '',
    'Images'                           : '',
    'Musique'                          : '',
    'Publique'                         : '',
    'Téléchargements'                  : '',
    'Vidéos'                           : '',
# Portuguese
    'Documentos'                       : '',
    'Imagens'                          : '',
    'Modelos'                          : '',
    'Música'                           : '',
    'Público'                          : '',
    'Vídeos'                           : '',
    'Área de trabalho'                 : '',
# Italian
    'Documenti'                        : '',
    'Immagini'                         : '',
    'Modelli'                          : '',
    'Musica'                           : '',
    'Pubblici'                         : '',
    'Scaricati'                        : '',
    'Scrivania'                        : '',
    'Video'                            : '',
# German
    'Bilder'                           : '',
    'Dokumente'                        : '',
    'Musik'                            : '',
    'Schreibtisch'                     : '',
    'Vorlagen'                         : '',
    'Öffentlich'                       : '',
}

file_node_exact_matches = {
    '.Xdefaults'                       : '',
    '.Xresources'                      : '',
    '.bashprofile'                     : '',
    '.bashrc'                          : '',
    '.dmrc'                            : '',
    '.ds_store'                        : '',
    '.fasd'                            : '',
    '.gitconfig'                       : '',
    '.gitignore'                       : '',
    '.jack-settings'                   : '',
    '.mime.types'                      : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.vimrc'                           : '',
    '.xinputrc'                        : '',
    'config'                           : '',
    'dropbox'                          : '',
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'favicon.ico'                      : '',
    'gruntfile.coffee'                 : '',
    'gruntfile.js'                     : '',
    'gruntfile.ls'                     : '',
    'gulpfile.coffee'                  : '',
    'gulpfile.js'                      : '',
    'gulpfile.ls'                      : '',
    'ini'                              : '',
    'ledger'                           : '',
    'license'                          : '',
    'mimeapps.list'                    : '',
    'node_modules'                     : '',
    'procfile'                         : '',
    'react.jsx'                        : '',
    'user-dirs.dirs'                   : '',
}

def devicon(file):
  if file.is_directory: return dir_node_exact_matches.get(file.relative_path, '')
  return file_node_exact_matches.get(file.relative_path, file_node_extensions.get(file.extension, ''))
