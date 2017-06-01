vtk_module(vtkIOXdmf3
  TCL_NAME vtkIOXdmfIII
  GROUPS
  TEST_DEPENDS
    vtkFiltersGeneral
    vtkTestingCore
    vtkTestingRendering
    vtkParallelMPI
  DEPENDS
    vtkCommonCore
    vtkCommonExecutionModel
    vtkIOLegacy
  PRIVATE_DEPENDS
    vtkCommonDataModel
    vtkCommonSystem
    vtkFiltersExtraction
    vtkParallelCore
    vtksys
    vtkxdmf3
  )