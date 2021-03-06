vtk_module(vtkInteractionWidgets
  GROUPS
    Rendering
  TEST_DEPENDS
    vtkIOLegacy
    vtkIOXML
    vtkIOParallel
    vtkRenderingVolume${VTK_RENDERING_BACKEND}
    vtkTestingRendering
    vtkInteractionImage
    vtkInteractionStyle
    vtkFiltersModeling
    vtkFiltersFlowPaths
    vtkFiltersSelection
    vtkFiltersProgrammable
    vtkRenderingLOD
    vtkImagingStencil
  KIT
    vtkInteraction
  DEPENDS
    vtkCommonCore
    vtkCommonExecutionModel
    vtkFiltersGeneral
    vtkFiltersSources
    vtkRenderingCore
  PRIVATE_DEPENDS
    vtkCommonComputationalGeometry
    vtkCommonDataModel
    vtkCommonMath
    vtkCommonSystem
    vtkCommonTransforms
    vtkFiltersCore
    vtkFiltersHybrid
    vtkFiltersModeling
    vtkImagingColor
    vtkImagingCore
    vtkImagingGeneral
    vtkImagingHybrid
    vtkInteractionStyle
    vtkRenderingAnnotation
    vtkRenderingFreeType
    vtkRenderingVolume
  )