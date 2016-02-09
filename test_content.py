from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

src = blocks.file_source(gr.sizeof_gr_complex*1, "/home/furonics/GNURadio/test", False)
snk = blocks.vector_sink_c()
tb = gr.top_block()
tb.connect(src,snk)
tb.run()
data=snk.data()
print data