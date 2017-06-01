vtk_module(vtkRenderingVolumeOpenGL2
  TCL_NAME
    vtkRenderingVolumeOpenGLII
  IMPLEMENTS
    vtkRenderingVolume
  BACKEND
    OpenGL2
  IMPLEMENTATION_REQUIRED_BY_BACKEND
  TEST_DEPENDS
    vtkTestingCore
    vtkTestingRendering
    vtkRenderingFreeType
    vtkImagingSources
    vtkImagingGeneral
    vtkInteractionStyle
  KIT
    vtkOpenGL
  DEPENDS
    vtkCommonCore
    vtkCommonDataModel
    vtkImagingCore
    vtkImagingMath
    vtkRenderingCore
    vtkRenderingOpenGL2
    vtkRenderingVolume
    vtkglew
  PRIVATE_DEPENDS
    vtkCommonMath
    vtkCommonSystem
    vtkCommonTransforms
    vtkFiltersCore
    vtkFiltersGeneral
    vtkFiltersSources
    vtksys
  )