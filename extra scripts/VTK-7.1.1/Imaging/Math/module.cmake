vtk_module(vtkImagingMath
  GROUPS
    Imaging
    StandAlone
  KIT
    vtkImaging
  DEPENDS
    vtkCommonExecutionModel
  PRIVATE_DEPENDS
    vtkCommonCore
    vtkCommonDataModel
  )