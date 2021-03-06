vtk_module(vtkCommonExecutionModel
  GROUPS
    StandAlone
  COMPILE_DEPENDS
    vtkCommonMisc
  TEST_DEPENDS
    vtkTestingCore
    vtkFiltersCore
    vtkFiltersSources
    vtkIOCore
    vtkIOLegacy
  KIT
    vtkCommon
  DEPENDS
    vtkCommonCore
    vtkCommonDataModel
  PRIVATE_DEPENDS
    vtkCommonMisc
    vtkCommonSystem
  )