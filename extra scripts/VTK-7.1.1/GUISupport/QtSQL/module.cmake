vtk_module(vtkGUISupportQtSQL
  GROUPS
    Qt
  TEST_DEPENDS
    vtkTestingCore
    vtkGUISupportQt
  EXCLUDE_FROM_WRAPPING
  DEPENDS
    vtkCommonCore
    vtkIOSQL
  PRIVATE_DEPENDS
    vtksys
  )