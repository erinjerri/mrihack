vtk_module(vtkFiltersParallelStatistics
  TEST_DEPENDS
    vtkParallelMPI
    vtkTestingCore
  KIT
    vtkParallel
  DEPENDS
    vtkFiltersStatistics
    vtkalglib
  PRIVATE_DEPENDS
    vtkCommonCore
    vtkCommonDataModel
    vtkCommonSystem
    vtkParallelCore
  )