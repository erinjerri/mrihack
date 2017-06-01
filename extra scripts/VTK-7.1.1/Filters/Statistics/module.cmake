vtk_module(vtkFiltersStatistics
  GROUPS
    StandAlone
  TEST_DEPENDS
    vtkTestingCore
  KIT
    vtkFilters
  DEPENDS
    vtkCommonCore
    vtkCommonExecutionModel
    vtkalglib
  PRIVATE_DEPENDS
    vtkCommonDataModel
    vtkCommonMisc
    vtkImagingFourier
  )