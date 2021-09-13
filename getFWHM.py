from ij.io import OpenDialog
from ij import IJ
from ij.gui import Roi, Overlay, WaitForUserDialog, ProfilePlot
from ij.measure import CurveFitter
import jarray

# open a file
op = OpenDialog("Choose Track Data...","")	# select manually
path = op.getDirectory() + op.getFileName()	# define path
#print path							# check path
IJ.open(path)						# open image window

# select a plotprofile (ref: https://note.com/kdgn/n/n503c77913ea1)
IJ.setTool("line")
myWait = WaitForUserDialog("Message","Drow a line, then click OK.")
myWait.show()
imp = IJ.getImage()

roi = imp.getRoi()
#print roi.getType()
#if roi.getType() == Roi.LINE():	# somehow "Roi.LINE" doesn't work 
if roi.getType() == 5:			# use "5" instead of "Roi.LINE"
	profile = roi.getPixels()	# get plotprofile
	#print profile			# check plotprofile (debug)
	#print len(profile)		# check length of plotprofile (debug)
xa = range(len(profile) - 1)
ya = profile
jxa = jarray.array(xa,"d")		# convert java.array to avoid error
#jya = jarray.array(ya,"d")
jya = ya

cf = CurveFitter(jxa,jya)		# define instance of CurveFitter

cf.doFit(CurveFitter.GAUSSIAN)	# do Gaussian fitting (see https://imagej.nih.gov/ij/developer/api/ij/ij/measure/CurveFitter.html#getParams())
print "FWHM = ", 2.355 * cf.getParams()[3]
plot = cf.getPlot()
plot.show()
