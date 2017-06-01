vtk_module(vtkFiltersAMR
  GROUPS
    StandAlone
  TEST_DEPENDS
    vtkImagingCore
    vtkIOAMR
    vtkTestingCore
    vtkTestingRendering
  KIT
    vtkParallel
  DEPENDS
    vtkCommonDataModel
    vtkCommonExecutionModel
  PRIVATE_DEPENDS
    vtkCommonCore
    vtkCommonMath
    vtkCommonSystem
    vtkFiltersCore
    vtkIOXML
    vtkParallelCore
  )