#!/usr/bin/env python
import vtk
from vtk.test import Testing

# create a test dataset
#
math = vtk.vtkMath()

# Note: the bigger the data the better vtkStaticPointLocator performs
#testSize = "large"
testSize = "medium"
#testSize = "small"

if testSize == "large":
    numPts = 100000000
    numProbes = 1000000
elif testSize == "medium":
    numPts = 2000000
    numProbes = 50000
else:
    numPts = 20000
    numProbes = 5000

# Create an initial set of points and asssociated datatset
points = vtk.vtkPoints()
points.SetDataTypeToDouble()
points.SetNumberOfPoints(numPts)
for i in range(0,numPts):
    points.SetPoint(i,math.Random(-1,1),math.Random(-1,1),math.Random(-1,1))

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
points.ComputeBounds()

# Create points array which are positions to probe data with
# FindClosestPoint(), We also create an array to hold the results of this
# probe operation.
probePoints = vtk.vtkPoints()
probePoints.SetDataTypeToDouble()
probePoints.SetNumberOfPoints(numProbes)
math.RandomSeed(314159)
for i in range (0,numProbes):
    probePoints.SetPoint(i,math.Random(-1,1),math.Random(-1,1),math.Random(-1,1))
closest = vtk.vtkIdList()
closest.SetNumberOfIds(numProbes)
staticClosest = vtk.vtkIdList()
staticClosest.SetNumberOfIds(numProbes)

# Print initial statistics
print("Processing NumPts: {0}".format(numPts))
print("\n")

# Time the creation and building of the incremental point locator
locator = vtk.vtkPointLocator()
locator.SetDataSet(polydata)
locator.SetNumberOfPointsPerBucket(5)
locator.AutomaticOn()

timer = vtk.vtkTimerLog()
timer.StartTimer()
locator.BuildLocator()
timer.StopTimer()
time = timer.GetElapsedTime()
print("Build Point Locator: {0}".format(time))

# Probe the dataset with FindClosestPoint() and time it
timer.StartTimer()
for i in range (0,numProbes):
    closest.SetId(i, locator.FindClosestPoint(probePoints.GetPoint(i)))
timer.StopTimer()
opTime = timer.GetElapsedTime()
print("    Closest point probing: {0}".format(opTime))

# Poke other methods before deleting locator class
closestN = vtk.vtkIdList()
locator.FindClosestNPoints(10, probePoints.GetPoint(0), closestN)

# Time the deletion of the locator. The incremental locator is quite slow due
# to fragmented memory.
timer.StartTimer()
del locator
timer.StopTimer()
time2 = timer.GetElapsedTime()
print("    Delete Point Locator: {0}".format(time2))
print("    Point Locator (Total): {0}".format(time+time2))
print("\n")

# StaticPointLocator
# Time the creation of static point locator
staticLocator = vtk.vtkStaticPointLocator()
staticLocator.SetDataSet(polydata)
staticLocator.SetNumberOfPointsPerBucket(5)
staticLocator.AutomaticOn()

staticTimer = vtk.vtkTimerLog()
staticTimer.StartTimer()
staticLocator.BuildLocator()
staticTimer.StopTimer()
StaticTime = staticTimer.GetElapsedTime()
print("Build Static Point Locator: {0}".format(StaticTime))

# Now probe the dataset with FindClosestPoint()
math.RandomSeed(314159)
staticTimer.StartTimer()
for i in range (0,numProbes):
    staticClosest.SetId(i, staticLocator.FindClosestPoint(probePoints.GetPoint(i)))
staticTimer.StopTimer()
staticOpTime = staticTimer.GetElapsedTime()
print("    Static Closest point probing: {0}".format(staticOpTime))

# Check that closest point operation gives the same answer and the
# incremental point locator. Note that it is possible to realize different
# results because buckets (and hence points) are processed in a different
# order, and if the distance apart is the same then the order decides which
# point is selected (from FindClosestPoint()). For small random datasets this
# is unlikely to happen.
error = 0
for i in range (0,numProbes):
    if closest.GetId(i) != staticClosest.GetId(i):
        error = 1

# Poke other methods before deleting static locator class
staticClosestN = vtk.vtkIdList()
staticLocator.FindClosestNPoints(10, probePoints.GetPoint(0), staticClosestN)
for i in range (0,10):
    if staticClosestN.GetId(i) != closestN.GetId(i):
        error = 1

# Okay now delete class
staticTimer.StartTimer()
del staticLocator
staticTimer.StopTimer()
StaticTime2 = staticTimer.GetElapsedTime()
print("    Delete Point Locator: {0}".format(StaticTime2))
print("    Static Point Locator (Total): {0}".format(StaticTime+StaticTime2))
print("\n")

# Print out the speedups
print("Speed ups:")
print("    Build: {0}".format(time/StaticTime))
if StaticTime2 > 0.0:
    print("    Delete: {0}".format(time2/StaticTime2))
else:
    print("    Delete: (really big)")
print("    Total: {0}".format((time+time2)/(StaticTime+StaticTime2)) )


# Return test results. If the assert is not true, then different results were
# generated by vtkStaticPointLocator and vtkPointLocator.
assert error == 0
