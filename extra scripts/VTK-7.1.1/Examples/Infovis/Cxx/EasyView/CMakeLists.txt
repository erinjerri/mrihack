cmake_minimum_required(VERSION 2.8.8)
if(POLICY CMP0020)
  cmake_policy(SET CMP0020 NEW)
endif()
if(POLICY CMP0025)
  cmake_policy(SET CMP0025 NEW) # CMake 3.0
endif()
if(POLICY CMP0043)
  cmake_policy(SET CMP0043 NEW) # CMake 3.0
endif()
if(POLICY CMP0053)
  cmake_policy(SET CMP0053 NEW) # CMake 3.1
endif()

project(EasyView)

find_package(VTK REQUIRED)
vtk_module_config(VTK
  vtkCommonCore
  vtkCommonDataModel
  vtkGUISupportQt
  vtkIOInfovis
  vtkInfovisCore
  vtkViewsCore
  vtkViewsInfovis
  vtkViewsQt
)
include(${VTK_USE_FILE})

if("${VTK_QT_VERSION}" STREQUAL "")
  message(FATAL_ERROR "VTK was not built with Qt")
endif()

# Use the include path and library for Qt that is used by VTK.
include_directories(
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
)

# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)

# Set your files and resources here
set(Srcs main.cxx EasyView.cxx)
set(UIs EasyView.ui)
set(Hdrs EasyView.h)
set(MOC_Hdrs EasyView.h)
set(Rcs Icons/icons.qrc)

# It is nice to have the ui in the windows project file.
# Right-click, choose Open With... press the Add button,
# and then find designer.exe and set as default.
# After this just click on it to bring it up in designer.
if(CMAKE_BUILD_TOOL MATCHES "(msdev|devenv)")
  set(Srcs ${Srcs} ${UIs})
endif(CMAKE_BUILD_TOOL MATCHES "(msdev|devenv)")

if(VTK_QT_VERSION VERSION_GREATER "4")
  # We have ui files, this will bring in the macro: qt5_wrap_ui
  find_package(Qt5 COMPONENTS Widgets REQUIRED QUIET)
  qt5_wrap_ui(UI_Srcs ${UIs})
  qt5_add_resources(Rcs_Srcs ${Rcs})

  source_group("Resources" FILES
    ${UIs}
    ${Rcs}
    ${EXE_ICON} # Not present
  )

  source_group("Generated" FILES
    ${UI_Srcs}
    ${MOC_Srcs}
    ${Rcs_Srcs}
  )

  #  set_source_files_PROPERTIES(${Srcs} PROPERTIES
  #                              OBJECT_DEPENDS "${UI_Srcs}")

  add_executable(EasyView
    MACOSX_BUNDLE  ${Srcs} ${Hdrs} ${UI_Srcs} ${MOC_Hdrs} ${Rcs_Srcs})

  qt5_use_modules(EasyView Core Gui Widgets)

  target_link_libraries(EasyView ${VTK_LIBRARIES})
else()
  find_package(Qt4 REQUIRED)

  include(${QT_USE_FILE})

  # Use what VTK built with
  set(QT_QMAKE_EXECUTABLE ${VTK_QT_QMAKE_EXECUTABLE} CACHE FILEPATH "")
  set(QT_MOC_EXECUTABLE ${VTK_QT_MOC_EXECUTABLE} CACHE FILEPATH "")
  set(QT_UIC_EXECUTABLE ${VTK_QT_UIC_EXECUTABLE} CACHE FILEPATH "")
  qt4_wrap_ui(UI_Srcs ${UIs})

  # Use the include path and library for Qt that is used by VTK.
  include_directories(
    ${QT_INCLUDE_DIR}
  )

  qt4_wrap_ui(UI_Srcs ${UIs})
  qt4_add_resources(Rcs_Srcs ${Rcs})

  add_definitions(-DQT_GUI_LIBS -DQT_CORE_LIB -DQT3_SUPPORT)
  set_source_files_PROPERTIES(${Srcs} PROPERTIES
                              OBJECT_DEPENDS "${UI_Srcs}")

  add_executable(EasyView
    MACOSX_BUNDLE ${Srcs} ${Hdrs} ${UI_Srcs} ${MOC_Hdrs} ${Rcs_Srcs})

  target_link_libraries(EasyView
    ${QT_LIBRARIES}
    ${VTK_LIBRARIES}
  )
endif()
