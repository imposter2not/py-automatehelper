#! python3

#python by default doesn't load up packages in a path, this loads a path
import sys
sys.path.insert(0, './lib')
import i2n_image as i2img
import i2n_key as i2key
import i2n_window as i2win

#put these in the lib packages
i2img.testload()
i2key.testload()
i2win.testload()

#i2n_window test
i2win.getcurrentwindow()


