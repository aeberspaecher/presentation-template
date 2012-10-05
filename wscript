#!/usr/bin/env python

top = '.'
out = "build"

def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal("Could not find pdflatex")

def build(ctx):
    ctx(
            features = 'tex',
            type     = 'pdflatex', # pdflatex or xelatex
            source   = 'talk.tex', # mandatory, the source
            outs     = 'pdf', # 'pdf' or 'ps pdf'
            #deps     = 'crossreferencing.lst', # to give dependencies directly
            prompt   = 0, # 0 for the batch mode
        )

    if ctx.cmd == 'build':
        if ctx.options.view:
            ctx.exec_command("xdg-open {0}/talk.pdf".format(out))

def options(ctx):
        ctx.add_option("--view", action="store_true", default=False,
                       help='view the PDf after it is built')
