#!/usr/bin/env python
import vtk
from vtk.test import Testing
from vtk.util.misc import vtkGetDataRoot
VTK_DATA_ROOT = vtkGetDataRoot()

# Performs a correlation in frequency domain.
s1 = vtk.vtkImageCanvasSource2D()
s1.SetScalarTypeToFloat()
s1.SetExtent(0,255,0,255,0,0)
s1.SetDrawColor(0)
s1.FillBox(0,255,0,255)
s1.SetDrawColor(2.0)
s1.FillTriangle(10,100,190,150,40,250)
s2 = vtk.vtkImageCanvasSource2D()
s2.SetScalarTypeToFloat()
s2.SetExtent(0,31,0,31,0,0)
s2.SetDrawColor(0.0)
s2.FillBox(0,31,0,31)
s2.SetDrawColor(2.0)
s2.FillTriangle(10,1,25,10,1,5)
fft1 = vtk.vtkImageFFT()
fft1.SetDimensionality(2)
fft1.SetInputConnection(s1.GetOutputPort())
fft1.ReleaseDataFlagOff()
fft1.Update()
# Pad kernel out to same size as image.
pad2 = vtk.vtkImageConstantPad()
pad2.SetInputConnection(s2.GetOutputPort())
pad2.SetOutputWholeExtent(0,255,0,255,0,0)
fft2 = vtk.vtkImageFFT()
fft2.SetDimensionality(2)
fft2.SetInputConnection(pad2.GetOutputPort())
fft2.ReleaseDataFlagOff()
fft2.Update()
# conjugate is necessary for correlation (not convolution)
conj = vtk.vtkImageMathematics()
conj.SetOperationToConjugate()
conj.SetInput1Data(fft2.GetOutput())
conj.Update()
# Corrleation is multiplication in frequencey space.
mult = vtk.vtkImageMathematics()
mult.SetOperationToComplexMultiply()
mult.SetInput1Data(fft1.GetOutput())
mult.SetInput2Data(conj.GetOutput())
rfft = vtk.vtkImageRFFT()
rfft.SetDimensionality(2)
rfft.SetInputConnection(mult.GetOutputPort())
real = vtk.vtkImageExtractComponents()
real.SetInputConnection(rfft.GetOutputPort())
real.SetComponents(0)
viewer = vtk.vtkImageViewer()
viewer.SetInputConnection(real.GetOutputPort())
viewer.SetColorWindow(256)
viewer.SetColorLevel(127.5)
# make interface
#skipping source
# --- end of script --
