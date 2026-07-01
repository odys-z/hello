# About

  The HelloWorld of SurrealismUI.

# Walk Through

1. Start from Sources

    See SurrealismUI/tests for latest version.

    Download code zip, extract to, say, surrealism-ui-nightly.

    Config .vscode/settings.json & CMakeLists.txt.

    ```
      {
        "slint.libraryPaths": {
            // "surrealism": "../Discord_SurrealismUI-main/ui/index.slint"
            "surrealism": "../surrealism-ui-nightly"
        }
      }
    ```
    ```
      get_filename_component(SURREALISM_UI_DIR 
        "${CMAKE_CURRENT_SOURCE_DIR}/../surrealism-ui-nightly" 
        ABSOLUTE
      )
    ```

1. Compile with MinGW + GCC 16.1.0

    ```
      export PATH="/c/Qt-6.10/Tools/CMake_64/bin:$PATH"
      export PATH="/c/Qt-6.10/mingw64-gcc16.1.0/bin:$PATH"
      rustup target add --toolchain stable-x86_64-pc-windows-msvc x86_64-pc-windows-gnu
      # WIN32 for the first time or any fetch contents updata
      cmake -G "MinGW Makefiles" -B build -DFETCHCONTENT_BASE_DIR="C:/CMakeCache" -DFETCHCONTENT_FULLY_DISCONNECTED=FALSE
      # to avoid github downloading
      cmake -G "MinGW Makefiles" -B build -DFETCHCONTENT_BASE_DIR="C:/CMakeCache" -DFETCHCONTENT_FULLY_DISCONNECTED=ON
      cmake --build build
      build/my_application.exe
    ```

1. Switching Function Pages

    ```
      menu:=SMenu {
        change(index, data) => {
          debug(index, data);
          router-index = index;
          menu-changed(index, data.id, data.name);
        }
      }

      right-wrapper:=Rectangle {
        if router-index==0: index-page:= Rectangle {
        }
        if router-index==1: index-page:= Rectangle {
        }
      }
    ```

1. Embed a WebView

    Currently Slint cannot embed a product ready webview window. That's not released.

    To popup a separate window,

    ```
      webview::webview w(true, nullptr);
      w.set_title("Popup Webview");
      w.set_size(600, 500, WEBVIEW_HINT_NONE);
      
      // The script run at onload().
      w.init("window.addEventListener('DOMContentLoaded', () => { if(typeof foo === 'function') foo(); });");

      w.navigate("https://github.com/webview/webview");
    ```

1. Implement a Filesystem Explorer

